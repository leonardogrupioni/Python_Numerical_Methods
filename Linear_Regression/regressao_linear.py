from math import *
import numpy as np
from numpy import double
from sympy import lambdify
from sympy.abc import t
from decimal import Decimal, ROUND_HALF_UP
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
from tabulate import tabulate

valor_A = 0
valor_b = 0

def calcular(x, y, numDecimais):
    global valor_A, valor_B

    print(x)
    print(y)

    
    somaX_Y, somaX, somaY, somaX_2 = soma(x, y)
    pearson = calcularPearson(x, y, somaX_Y, somaX, somaY)
    determinacao = calcularCoeficienteDeterminacao(pearson)
    valor_A, valor_B = calcularCoeficientes(x, somaX_Y, somaX, somaY, somaX_2)

    #Permitir que se atribua valores para x e o programa retorne o valor de y, conforme a equação
    #Na saída:
    #valor de Y , quando se escolhe um valor de X

    resultado = str("X: Independente \n" + "Y: Dependente\n\n")

    df = pd.DataFrame({'X': x, 'Y': y})
    resultado = resultado + df.to_string(index=False, col_space = 15, justify = 'center')

    resultado = resultado  + '\n' + str('coeficente de correlacao (r): ' + str(round(pearson, numDecimais)))
    resultado = resultado + '\n' + str('coeficente de determinacao (r^2): ' + str(round(determinacao, 4) * 100) + '%') 
    resultado = resultado + '\n' + str('\n Sistema: ')
    resultado = resultado + '\n' + str(f'({len(x)} * a) + ({str(round(somaX, numDecimais))} * b) = {str(round(somaY, numDecimais))}') #Obs: precisa arredondar?
    resultado = resultado + '\n' + str(f'({str(round(somaX, numDecimais))} * a) + ({str(round(somaX_2, numDecimais))} * b) = {str(round(somaX_Y, numDecimais))}')
    resultado = resultado + '\n' + str('\n Solucao do sitema: ')
    resultado = resultado + '\n' + str(f'\n a = {str(round(valor_A, numDecimais))} e b = {str(round(valor_B, numDecimais))}')
    resultado = resultado + '\n' + str(f'\n Equacao da reta: y = {str(round(valor_B, numDecimais))}*x + {str(round(valor_A, numDecimais))}')

    f = []
    f, string_funcao = calcularY(x)
    funcao = str(f'{str(round(valor_B, numDecimais))}* x + {str(round(valor_A, numDecimais))}')

    fig, ax = plt.subplots()

    # Agora, plota os dados no eixo criado
    ax.plot(x, f)
    ax.scatter(x, f, marker = '*', color = 'red', )
    ax.scatter(x, y, marker = '*', color = 'orange')

    # Adiciona título ao gráfico e labels aos eixos
    ax.set_title('Gráfico')
    ax.set_xlabel('x')
    ax.set_ylabel(funcao)
    ax.grid(True)

    return resultado, fig

def calcularPearson(x, y, somaX_Y, somaX, somaY):
    #soma de x*y, soma de x e soma de y
    n = len(x)

    convX_Y = (somaX_Y/n) - ((somaX/n) * (somaY/n))

    desvio_padraoX = np.std(x)

    desvio_padraoY = np.std(y)

    r = convX_Y/(desvio_padraoX * desvio_padraoY)

    return r

def calcularCoeficienteDeterminacao(r):
    return r**2

def soma(x, y):
    somaX = 0
    somaX_2 = 0
    somaX_Y = 0
    somaY = 0

    for i in range(0, len(x)):
        somaX = somaX + x[i]
        somaX_2 = somaX_2 + (x[i]**2)
        somaY = somaY + y[i]
        somaX_Y = somaX_Y + (x[i] * y[i])

    return (somaX_Y, somaX, somaY, somaX_2)

def calcularY(x):
    funcao = []
    string_funcao = " "
    
    for i in range(0, len(x)):
        funcao.append((valor_B * x[i]) + valor_A)

    df = pd.DataFrame({'X': x, 'Y': funcao})
    string_funcao = string_funcao + df.to_string(index=False, col_space = 15, justify = 'center')

    return (funcao, string_funcao)

def calcularCoeficientes(x, somaX_Y, somaX, somaY, somaX_2):
    n = len(x)

    sistemaEsq = np.array([[n, somaX], [somaX, somaX_2]])
    sistemaDir = np.array([somaY, somaX_Y])

    resultado = np.linalg.solve(sistemaEsq, sistemaDir)

    return (resultado[0], resultado[1])