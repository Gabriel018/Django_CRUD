from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Contatos
# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({},request))

def clientes(request):
    template = loader.get_template('clientes.html')
    client = Contatos.objects.all().values()

    context = {
        'client':client
    }

    return HttpResponse(template.render(context,request))

def delete(request,id):
    Client = Contatos.objects.get(id=id)
    Client.delete()

    return HttpResponseRedirect(reverse('home'))

