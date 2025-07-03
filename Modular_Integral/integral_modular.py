from math import *
from numpy import double
from sympy import lambdify
from sympy.abc import x
from decimal import Decimal, ROUND_HALF_UP
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
from tabulate import tabulate

def calcular(funcao, numDecimais, a, b, n, h):

    #definicao da precisao
    p = precisao(numDecimais)

    #declaracao da funcao com o lambdify
    f = lambdify(x,funcao)
    resultado = str('\n\nFuncao F(x) = ' + funcao + '\n')

    #erro de arredondamento
    
    erro = erroA(numDecimais,n,h)

    resultado = resultado + '\n' + str('Calculo do Erro de Arredondamento:')
    resultado = resultado + '\n' + str('\nNumero de Trapezios = ' + str(n) + '\nNumero de Decimais = ' + str(numDecimais) + '\nPasso(h) = ' + str(h))
    resultado = resultado + '\n' + str('\nErro = NumTrapezios * (5 * 10^(-numDecimais+1) ) * h')
    resultado = resultado + '\n' + str('Erro = ' + str(n) + ' * ' + '(5 * 10^(-' + str(numDecimais+1) + ') ) * ' + str(h) )
    resultado = resultado + '\n' + str('Erro = ' + f"{erro:.{numDecimais+1}f}" + '\n')

    indice, valores = tabela(f, numDecimais, n, a, h)

    resultado = resultado + '\n' + str('Tabela de intervalo: \n')

    df = pd.DataFrame({'x      ': indice, 'f(x)': valores})
    resultado = resultado + df.to_string(index=False, col_space = 15, justify = 'center')

    resultado = resultado + '\n' + str('\nsoma da area dos trapezios: ')
    somaTotal, resultadoSoma = soma(numDecimais, valores, indice, n)
    resultado = resultado + '\n' + resultadoSoma

    areaTotal, resultadoArea = areaTrapezio(numDecimais, double(somaTotal), h)
    resultado = resultado + '\n' + resultadoArea

    resultado = resultado + '\n' + str('Erro arredondado = '+ f"{erro:.{numDecimais+1}f}")

    resultado = resultado + '\n' + str('\n\nIntervalo: ')
    resultado = resultado + '\n' + str('[ ' + str(round((areaTotal - erro), numDecimais)) + '; ' + str(round((areaTotal + erro), numDecimais)) + ' ]')
    resultado = resultado + '\n' + str('[ ' + str(round(areaTotal, numDecimais+1)) + ' +- ' + f"{erro:.{numDecimais+1}f}" + ' ]')

    resultado = resultado + '\n' + str('\n\nFIM')

    fig, ax = plt.subplots()

    # Agora, plota os dados no eixo criado
    ax.plot(indice, valores)

    # Adiciona título ao gráfico e labels aos eixos
    ax.set_title('Gráfico')
    ax.set_xlabel('x')
    ax.set_ylabel(funcao)
    ax.grid(True)

    return (resultado, fig)

def precisao(numDecimais):
    return Decimal('1.' + '0' * numDecimais)

def erroA(numDecimais,n,h):
    p = precisao((numDecimais+1))
    aux = Decimal(str(n*(5*10**-(numDecimais+1))*h))

    return (aux.quantize(p, rounding = ROUND_HALF_UP))

def tabela(f,numDecimais,n,a,h):
    #definindo listas indice e valores
    indice = []
    valores = []

    #loop que preenche as listas de indice e valores
    i = a
    p = precisao(numDecimais)
    for j in range(0, n+1):
        indice.append(i)
        aux = Decimal(str(f(i)))
        valores.append(aux.quantize(p, rounding = ROUND_HALF_UP))
        i += h
    return (indice, valores)

def soma(numDecimais, valores, indice, n):
    total = 0
    somaString = ''

    for j in range(0, n+1):
        i = indice[j]
        num = round(valores[j], numDecimais)

        if j == 0 or j == n:
            total += (num/2)
        else: 
            total += num 

        somaString = somaString + '\n' + str('soma [' + str(round(i ,numDecimais)) + '] = ' + str(round(total,numDecimais)))

    p = precisao(numDecimais) #coloca +1 para mostrar na tela com mais uma casa?
    auxTotal = Decimal(str(total))
    auxTotal = total.quantize(p, rounding = ROUND_HALF_UP)

    somaString = somaString + '\n' + str('\nSoma total da area dos trapezios = ' + str(auxTotal))

    return (total, somaString)

def areaTrapezio(numDecimais, somaTotal, h):
    areaString = ''
    p = precisao(numDecimais)       #coloca +1 para mostrar na tela com mais uma casa?
    area = Decimal(str(somaTotal * h))
    auxArea = area.quantize(p, rounding = ROUND_HALF_UP)

    areaString = areaString + '\n' + str('Area do trapezio = ' + str(auxArea))

    return (area, areaString)

#calcular('(x**2)*sin(1/x**2)',4, 1, 2, 5, 0.2)
#calcular('log10(x)',8,6,10,8,0.5)
#calcular('e**(-x**2/2) / sqrt(2*pi)',5, 1.5, 2.5, 10, 0.1)
#calcular('sqrt(x)',3,2,5,6,0.5)