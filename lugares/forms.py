from django import forms
from django.db import models
from django.forms import ModelForm
from models import *

class LugarForm(ModelForm):
    class Meta:
        model = Lugar