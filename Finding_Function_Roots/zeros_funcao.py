from math import *
from numpy import double
from sympy import lambdify
from sympy.abc import x
from decimal import Decimal, ROUND_HALF_UP
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd


def calcular(funcao, numDecimais, a, b, e):
    i = 0
    fim = False
    #definicao da precisao
    p = precisao(numDecimais)

    #declaracao da funcao com o lambdify
    f = lambdify(x, funcao)
    resultado = str('\nFuncao F(x) = ' + funcao + '\n')

    while fim == False:
        medio = (a+b)/2

        resultado = resultado + str('\nx' + str(i) + ' = ' + str(round(medio, numDecimais)))
        i += 1

        amplitude = (b-a)/2
        resultado = resultado + str('\n|e| <= ' + str(round(amplitude, numDecimais)))

        if(amplitude <= e): 
            resultado = resultado + '\n\nResultado:\n'
            resultado = resultado + str(f'[{round(medio - amplitude, numDecimais)}; {round(medio + amplitude, numDecimais)}]\n')
            resultado = resultado + str(f'x0 = {round(medio, numDecimais)}')
            resultado = resultado + str(f'   erro: {round(amplitude, numDecimais)}')
            fim = True
        else:
            novoA = medio
            novoB = b
            b = medio

            resultado = resultado + str(f'\n\nIntervalos: [{round(a, numDecimais)};{round(b, numDecimais)}] ou [{round(b, numDecimais)}, {round(novoB, numDecimais)}]\n')

            x_valorA = f(a)
            x_valorB = f(novoB)
            x_valorNovoB = f(b)

            resultado = resultado + str(f'\nf({round(a, numDecimais)}) = {round(x_valorA, numDecimais)}\n')
            resultado = resultado + str(f'f({round(novoB, numDecimais)}) = {round(x_valorB, numDecimais)}\n')
            resultado = resultado + str(f'f({round(b, numDecimais)}) = {round(x_valorNovoB, numDecimais)}\n')

            a = valorA(x_valorA, x_valorB, x_valorNovoB, a, b, novoB)
            b = valorB(x_valorA, x_valorB, x_valorNovoB, a, b, novoB)

            resultado = resultado + str(f'\nNovo intervalo: [{round(a, numDecimais)}, {round(b, numDecimais)}]')

    return resultado

def precisao(numDecimais):
    return Decimal('1.' + '0' * numDecimais)

def valorA(x_valorA, x_valorB, x_valorNovoB, a, b, novoB):
    valor_a = 0

    if(x_valorA < 0 and x_valorB < 0):
        if(x_valorA < x_valorB):
            valor_a = novoB
        else:
            valor_a = a
    elif(x_valorA < 0 and x_valorNovoB < 0):
        if(x_valorA < x_valorNovoB):
            valor_a = b
        else:
            valor_a = a
    elif(x_valorB < 0 and x_valorNovoB < 0):
        if(x_valorB < x_valorNovoB):
            valor_a = b
        else:
            valor_a = novoB
    elif(x_valorA < 0):
        valor_a = a
    elif(x_valorB < 0):
        valor_a = novoB
    else:
        valor_a = b

    return valor_a

def valorB(x_valorA, x_valorB, x_valorNovoB, a, b, novoB):
    valor_b = 0

    if((x_valorA > 0 and x_valorB > 0)):
        if(x_valorA < x_valorB):
            valor_b = a
        else:
            valor_b = novoB
    elif(x_valorA > 0 and x_valorNovoB > 0):
        if(x_valorA < x_valorNovoB):
            valor_b = a
        else:
            valor_b = b
    elif(x_valorB > 0 and x_valorNovoB > 0):
        if(x_valorB < x_valorNovoB):
            valor_b = novoB
        else:
            valor_b = b

    elif(x_valorA > 0):
        valor_b = a
    elif(x_valorB > 0):
        valor_b = novoB
    else:
        valor_b = b

    return valor_b