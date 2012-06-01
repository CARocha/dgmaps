
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from lugares.models import Lugar
from forms import LugarForm
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
from django.contrib.auth.decorators import login_required

# Create your views here.

@csrf_exempt
@login_required
def guardar_mapa(request):
    if request.method == 'POST':
        form = LugarForm(request.POST)

        if form.is_valid():
            forms_uncommited = form.save(commit=False)
            forms_uncommited.user = request.user
            #forms_uncommited.nombre = request.POST['nombre'].escape('%20', ' ')
            forms_uncommited.lat = request.POST['latitud']
            forms_uncommited.lng = request.POST['longitud']
            forms_uncommited.save()

    else:
        form = LugarForm()
    return render_to_response('lugares/lugar.html', locals(),
    	                        context_instance=RequestContext(request))

@login_required
def mostrar_globo(request):
    globos = Lugar.objects.filter(user=request.user)
    if request.is_ajax():
        lista = []
        for objeto in Lugar.objects.filter(user=request.user):
            if objeto.lat and objeto.lng:
                dicc = dict(nombre=objeto.nombre, descripcion=objeto.descripcion,
                            lon=float(objeto.lng) , lat=float(objeto.lat))
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
        #print serializado
        return HttpResponse(serializado, mimetype='application/json')

    #return render_to_response('lugares/mostrar.html', locals(),
    #                            context_instance=RequestContext(request))
@login_required
def index(request):
    globos = Lugar.objects.filter(user=request.user)

    return render_to_response('index.html', locals(),
                            context_instance=RequestContext(request))

@login_required    
def eliminar(request, id):
    globos_delete = Lugar.objects.get(id=id)
    globos_delete.delete()
    return HttpResponse('Se ha eliminado con exito')