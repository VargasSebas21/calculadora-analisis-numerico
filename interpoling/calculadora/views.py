from django.shortcuts import render
from .scripts import interpolacionNewton, runge_kutta_4, get_plot
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
import json
import numpy as np
import math

phi = lambda x,y: 4*np.exp(0.8*x) - 0.5*y

def home(request):
    return render(request, 'index.html', context = {'polinomio': math.inf,'calculate': False, 'result': False})  
 
def interpolacion(request):
    tipo = request.GET['tipo']
    if tipo == 'interpolacion':
        valorAInterpolar = float(request.GET['valorAI'])
        grado = int(request.GET['grado'])
        valores = np.array(request.GET['valoresX'].split(sep=','))
        valoresArray = np.asarray(valores, dtype = float)
        fx = np.array(request.GET['fx'].split(sep=','))
        fxArray =np.asarray(fx, dtype = float)
        polinomio = interpolacionNewton(valorAInterpolar,grado,valoresArray,fxArray)
        chart = get_plot(valoresArray,fxArray, 'GRAFICA POLINOMIO DE NEWTON')
        return render(request,'index.html',context={'polinomio': polinomio,'calculate': True, 'result': False,'chart': chart})
    elif tipo == 'runga':
        equis = float(request.GET['equis'])
        ye = float(request.GET['ye'])
        ache = float(request.GET['ache'])
        equisInicial = float(request.GET['equisInicial'])
        equisFinal = float(request.GET['equisFinal'])
        valores1, valores2 = runge_kutta_4(equis , ye , phi,ache ,equisInicial, equisFinal)
        chart = get_plot(valores1,valores2, 'GRAFICA RUNGEKUTTA')
        print('hola',valores1)
        return render(request,'inter.html',context={'polinomio': math.inf,'calculate': False, 'result': True, 'runga': {'valores1':valores1, 'valores2': valores2}, 'chart': chart})
    else:
        return render(request, 'index.html', context = {'polinomio': math.inf,'calculate': False, 'result': False,})  