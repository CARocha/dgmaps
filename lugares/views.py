
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from lugares.models import Lugar
from forms import LugarForm

# Create your views here.

def guardar_mapa(request):
    if request.method == 'POST':
        form = LugarForm(request.POST)
        print form

        if forms.is_valid():
            forms_uncommited = form.save(commit=False)
            forms_uncommited.user = request.user
            forms_uncommited.lat = request.POST['lat']
            forms_uncommited.lng = request.POST['lng']
            forms_uncommited.save()

    else:
        form = LugarForm()
    return render_to_response('lugares/lugar.html', locals(),
    	                        context_instance=RequestContext(request))