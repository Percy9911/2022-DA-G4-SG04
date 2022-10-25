from multiprocessing import context
from re import template
from django.shortcuts import HttpResponse
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Mascotas


# Create your views here.

def home(request):
    mypets = Mascotas.objects.all().values()
    template = loader.get_template('vet.html')
    context = {
        'mypets': mypets,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['nombre']
    y = request.POST['propietario']
    z = request.POST['especie']
    a = request.POST['raza']
    pet = Mascotas(nombre=x, propietario=y, especie=z, raza=a)
    pet.save()
    return HttpResponseRedirect(reverse('home'))


def delete(request, id):
    pet = Mascotas.objects.get(id=id)
    pet.delete()
    return HttpResponseRedirect(reverse('home'))


def update(request, id):
    pet = Mascotas.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'pet': pet,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    nombre = request.POST['nombre']
    propietario = request.POST['propietario']
    especie = request.POST['especie']
    raza = request.POST['raza']
    pet = Mascotas.objects.get(id=id)
    pet.nombre = nombre
    pet.propietario = propietario
    pet.especie = especie
    pet.raza = raza
    pet.save()
    return HttpResponseRedirect(reverse('home'))
