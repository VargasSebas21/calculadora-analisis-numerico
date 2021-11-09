# Interpolacion de newton

import numpy as np
### se trabaja con una función polinómica y depende del grado que el usuario ingrese
## Debe recibir el grado como parámetro y el valor a interpolar

def interpolacionNewton(valor, grado, valores_x, f_x):
    polinomio = f_x[0]
    cont = 1
    matrizDiferencias = diferenciaDividida(f_x, valores_x, grado, 1, [], 1)
    print(matrizDiferencias)
    for i in range(grado):
        productos = 1
        for j in range(cont):
            productos *= (valor - valores_x[j])
        polinomio += matrizDiferencias[cont-1][0]*productos
        #print(diferenciaDividida(f_x, valores_x, grado, 0, 2, 0, [])[cont-1][0])
        cont += 1
    return polinomio

def diferenciaDividida(f_x, valores_x, grado, columna, matriz, paso):
    if(len(matriz) == 0):
        matriz.append(valores_x)
        matriz.append(f_x)
    diferencias = []
    for i in range(len(matriz[columna])):
        if(len(matriz[columna])-i == 1):
            break
        f2 = matriz[columna][i+1]
        f1 = matriz[columna][i]
        x2 = matriz[0][i+paso]
        x1 = matriz[0][i]
        diferencia = dividirDiferencias(f2,f1,x2,x1)
        diferencias.append(diferencia)
    matriz.append(diferencias)
    if(len(matriz)-2 == grado):
        matrizTotal = matriz[2:]
        return matrizTotal
    else:
        return diferenciaDividida(f_x, valores_x, grado, columna+1, matriz, paso+1)
    
def dividirDiferencias(f2,f1,x2,x1):
    print("f2 ", f2, " f1 ", f1, " x2 ", x2, " x1 ", x1)
    return ((f2-f1)/(x2-x1))


# RUNG KUTTA
def runge_kutta_4(x, y, dydx, h, xi, xf):
    xsol = [x]
    ysol = [y]
    n = int((xf-xi)/h)
    for i in range(n):
        k1 = dydx(x,y)
        k2 = dydx(x+(1/2)*h,(y+(1/2)*k1*h))
        k3 = dydx(x+(1/2)*h,(y+(1/2)*k2*h))
        k4 = dydx(x+h,y+k3*h)
        yn = y + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*h
        ysol.append(yn)
        y = yn
        xn = x + h
        xsol.append(xn)
        x = xn
    return xsol, ysol

def 