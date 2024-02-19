from django.shortcuts import render
from .models import *

def inicio(request):
    return render(request,"inicio.html",{})

def almuerzo(request):
    sandwiches = Sandwiches.objects.all()
    hamburguesas = Hamburguesas.objects.all()
    tapeos= Tapeo.objects.all()
    return render(request, "menu-comidas/almuerzo.html", 
                  {"sandwiches": sandwiches,
                  "hamburguesas": hamburguesas,
                  "tapeos":  tapeos})

def bebibas(request):
    bebidas = Bedidas.objects.all()
    tragos = Tragos.objects.all()
    return render(request, "menu-comidas/bebidas.html", 
                  {"bebidas": bebidas, 
                   "tragos": tragos})

def cafeteria(request):
    cafeteria = Cafeteria.objects.all()
    return render(request, "menu-comidas/cafes.html", 
                  {"cafeteria": cafeteria})

def ensalada(request):
    ensaladas = Ensaladas.objects.all()
    return render(request, "menu-comidas/ensalada.html", 
                  {"ensaladas": ensaladas})

def postres(request):
    postres = Postres.objects.all()
    return render(request, "menu-comidas/postres.html", 
                  {"postres": postres})

def desayuno(request):
    desayuno = Desayuno.objects.all()
    merienda = Merienda.objects.all()
    brusquetas = Brusquetas.objects.all()
    return render(request, "menu-comidas/desayuno.html", 
                  {"desayunos": desayuno, 
                   "meriendas":merienda,
                   "brusquetas":brusquetas
                   })
   
