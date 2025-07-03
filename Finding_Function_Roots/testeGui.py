from tkinter import scrolledtext
from tkinter import *
from tkinter.font import Font
import tkinter as tk
import zeros_funcao # type: ignore
from numpy import double
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class App:
    def __init__(self):
        cor_fundo = '#dfe8ef'
        
        # Criamos a janela principal
        self.janela_principal = Tk()
        self.janela_principal.config(padx=50,pady=20,bg=cor_fundo)
        
        fonte_Neg = Font(family="Roboto", size=12, weight='bold')
        fonte = Font(family="Roboto", size=12)

        # Criando os frames
        self.frame_Titulo = Frame(self.janela_principal,bg=cor_fundo)
        self.frame_Texto  = Frame(self.janela_principal,bg=cor_fundo) 
        self.frame_funcao  = Frame(self.janela_principal,bg=cor_fundo) 
        self.frame_numDecimais  = Frame(self.janela_principal,bg=cor_fundo)
        self.frame_a  = Frame(self.janela_principal,bg=cor_fundo)
        self.frame_b  = Frame(self.janela_principal,bg=cor_fundo)
        self.frame_n  = Frame(self.janela_principal,bg=cor_fundo)
        self.frame_botao = Frame(self.janela_principal,bg=cor_fundo) 
        
        # Criando label e botões do frame de cima
        self.labelT = Label(self.frame_Titulo, text='Legenda para Entrada de dados:', anchor='n', width=30, font=fonte_Neg,bg=cor_fundo)
        self.label = Label(self.frame_Texto, text='√ -> sqrt()\n\nlog -> log()\n\nlog10 -> log10()\n\nseno -> sin()\n\ncos -> cos()\n\ntangente -> tg()\n\nbase^expoente -> b**e\n\nmultiplicacao -> *', anchor='n', width=30, font=fonte,bg=cor_fundo)
        self.label1 = Label(self.frame_funcao, text='Digite a Lei (funcao):', anchor='w', width=30, font=fonte_Neg,bg=cor_fundo)
        self.label2 = Label(self.frame_numDecimais, text='Digite o numero de casas decimais:', anchor='w', width=30, font=fonte_Neg,bg=cor_fundo)
        self.label3 = Label(self.frame_a, text='Digite o inicio do intervalo da reta A:', anchor='w', width=30, font=fonte_Neg,bg=cor_fundo)
        self.label4 = Label(self.frame_b, text='Digite o fim do intervalo da reta B:', anchor='w', width=30, font=fonte_Neg,bg=cor_fundo)
        self.label5 = Label(self.frame_n, text='Digite o limite para o erro |e|:', anchor='w', width=30, font=fonte_Neg,bg=cor_fundo)
        
        # Criando o widget de entrada
        self.entradaFuncao = Entry(self.frame_funcao, width=25)
        self.entradaNumDecimais = Entry(self.frame_numDecimais, width=25)
        self.entradaA = Entry(self.frame_a, width=25)
        self.entradaB = Entry(self.frame_b, width=25)
        self.entradaN = Entry(self.frame_n, width=25)
        
        # Empacotando label e entrada no frame de cima
        self.labelT.pack(side='left', anchor='w', pady=10, padx=20)

        self.label.pack(side='left', anchor='w', pady=10, padx=20)

        self.label1.pack(side='left', anchor='w', pady=10, padx=20)
        self.entradaFuncao.pack(side='left')
        
        self.label2.pack(side='left', anchor='w', pady=10, padx=20)
        self.entradaNumDecimais.pack(side='left')
        
        self.label3.pack(side='left', anchor='w', pady=10, padx=20)
        self.entradaA.pack(side='left')
        
        self.label4.pack(side='left', anchor='w', pady=10, padx=20)
        self.entradaB.pack(side='left')
        
        self.label5.pack(side='left', anchor='w', pady=10, padx=20)
        self.entradaN.pack(side='left')
        
        
        # Criando os botões, no frame de baixo 
        self.botao = Button(self.frame_botao, text='Calcular', command=self.exibe, bg='#DAE3EB')
        self.botao_sair = Button(self.frame_botao, text='Sair', command=self.janela_principal.destroy, bg='#DAE3EB')
        
        # Empacotando os botões no frame de baixo
        self.botao.pack(side='left',padx=200)
        self.botao_sair.pack(side='right',padx=10)
        
        # Empacotando os botões janela principal
        self.botao.pack()
        self.botao_sair.pack()
        
        # Empacotando os frames na janela principal
        self.frame_Titulo.pack()
        self.frame_Texto.pack()
        self.frame_funcao.pack()
        self.frame_numDecimais.pack()
        self.frame_a.pack()
        self.frame_b.pack()
        self.frame_n.pack()
        self.frame_botao.pack()
        
        # Rodando
        mainloop()

    def exibe(self):

        funcao = str(self.entradaFuncao.get())
        numDecimais = int(self.entradaNumDecimais.get())
        a = double(self.entradaA.get())
        b = double(self.entradaB.get())
        e = double(self.entradaN.get())
        
        resultado = zeros_funcao.calcular(funcao, numDecimais, a, b, e)

        # create root window
        root = Tk()
  
        # create a horizontal scrollbar by
        # setting orient to horizontal
        h = Scrollbar(root, orient = 'horizontal')
  
        # attach Scrollbar to root window at 
        # the bootom
        h.pack(side = BOTTOM, fill = X)
  
        # create a vertical scrollbar-no need
        # to write orient as it is by
        # default vertical
        v = Scrollbar(root)
  
        # attach Scrollbar to root window on 
        # the side
        v.pack(side = RIGHT, fill = Y)
          
  
        t = Text(root, width = 100, height = 35, wrap = NONE,
                 xscrollcommand = h.set, 
                 yscrollcommand = v.set)
  
        # insert some text into the text widget
        text_width = 100  # Width of the Text widget in characters
        lines = str(resultado).split('\n')
        centered_lines = []
        for line in lines:
            spaces_to_add = (text_width - len(line)) // 2
            centered_line = ' ' * spaces_to_add + line
            centered_lines.append(centered_line)
        centered_text = '\n'.join(centered_lines)
        t.insert(END, centered_text)
  
        # attach Text widget to root window at top
        t.pack(side=TOP, fill=X, expand = True)
  
        h.config(command=t.xview)
  
        v.config(command=t.yview)

        self.entradaFuncao.delete(0,END)
        self.entradaNumDecimais.delete(0,END)
        self.entradaA.delete(0,END)
        self.entradaB.delete(0,END)
        self.entradaN.delete(0,END)
  
        root.mainloop()

gui = App()