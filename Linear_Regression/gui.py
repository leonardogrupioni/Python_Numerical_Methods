from tkinter import scrolledtext
from tkinter import *
from tkinter.font import Font
import tkinter as tk
import regressao_linear
from numpy import double
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

x = []
y = []

class App:
    def __init__(self):
        
        cor_fundo = '#dfe8ef'
        
        # Criamos a janela principal
        self.janela_principal = Tk()
        self.janela_principal.config(padx=50,pady=20,bg=cor_fundo)
    
        fonte = Font(family="Roboto", size=12)
        fonte_Neg = Font(family="Roboto", size=12, weight='bold')

        # Criando os frames
        self.frame_x  = Frame(self.janela_principal,bg=cor_fundo) 
        self.frame_y  = Frame(self.janela_principal,bg=cor_fundo)
        self.frame_botao = Frame(self.janela_principal,bg=cor_fundo) 
        
        # Criando label e botões do frame de cima
        self.label = Label(self.frame_x, text='Digite a variavel independete (x):', anchor='w', width=30, font=fonte_Neg,bg=cor_fundo)
        self.label2 = Label(self.frame_y, text='Digite a variavel dependente (y):', anchor='w', width=30, font=fonte_Neg,bg=cor_fundo)
        
        
        # Criando o widget de entrada
        self.entradaX = Entry(self.frame_x, width=25)
        self.entradaY = Entry(self.frame_y, width=25)
        
        # Empacotando label e entrada no frame de cima

        self.label.pack(side='left', anchor='w', pady=10, padx=20)
        self.entradaX.pack(side='left')
        
        self.label2.pack(side='left', anchor='w', pady=10, padx=20)
        self.entradaY.pack(side='left')
        
        # Criando os botões, no frame de baixo 
        self.botao_acrescentar = Button(self.frame_botao, text = 'acrescentar', command = self.armazenar, bg = '#DAE3EB')
        self.botao = Button(self.frame_botao, text='finalizar', command=self.numDecimais_janela, bg='#DAE3EB')
        self.botao_sair = Button(self.frame_botao, text='Sair', command=self.janela_principal.destroy, bg='#DAE3EB')
        
        # Empacotando os botões no frame de baixo
        self.botao.pack(side='left',padx=200)
        self.botao_acrescentar.pack(side='left',padx=10)
        self.botao_sair.pack(side='right',padx=10)
        
        # Empacotando os botões janela principal
        self.botao.pack()
        self.botao_sair.pack()
        
        # Empacotando os frames na janela principal
        self.frame_x.pack()
        self.frame_y.pack()
        self.frame_botao.pack()
        
        # Rodando
        mainloop()

    def numDecimais_janela(self):

        self.janela_numDecimais = Tk()
        self.janela_numDecimais.config(padx=50,pady=20,bg='#dfe8ef')

        self.frame_botao = Frame(self.janela_numDecimais,bg='#dfe8ef') 
        self.frame_numDecimais  = Frame(self.janela_numDecimais,bg='#dfe8ef')

        self.label3 = Label(self.frame_numDecimais, text='Digite a qtd de numDecimais:', anchor='w', width=30, font=Font(family="Roboto", size=12, weight='bold'),bg='#dfe8ef')
        self.entradaNumDecimais = Entry(self.frame_numDecimais, width = 25)

        self.label3.pack(side='left', anchor='w', pady=10, padx=20)
        self.entradaNumDecimais.pack(side='left')

        self.botao = Button(self.frame_botao, text='calcular', command=self.exibe, bg='#DAE3EB')
        self.botao_sair = Button(self.frame_botao, text='Sair', command=self.janela_numDecimais.destroy, bg='#DAE3EB')

        self.botao.pack(side='left',padx=200)
        self.botao_sair.pack(side='right',padx=10)

        self.frame_numDecimais.pack()
        self.frame_botao.pack()

        mainloop()
    
    def armazenar(self):
        x.append(double(self.entradaX.get()))
        y.append(double(self.entradaY.get())) 

        self.entradaX.delete(0,END)
        self.entradaY.delete(0,END)

    def armazenarX(self):
        x.append(double(self.entradaValoresX.get()))

        self.entradaValoresX.delete(0,END)

    def x_janela(self):
        self.janela_x = Tk()
        self.janela_x.config(padx=50,pady=20,bg='#dfe8ef')

        self.frame_botao = Frame(self.janela_x,bg='#dfe8ef') 
        self.frame_x  = Frame(self.janela_x,bg='#dfe8ef')

        self.label3 = Label(self.frame_x, text='Digite o valor de x:', anchor='w', width=30, font=Font(family="Roboto", size=12, weight='bold'),bg='#dfe8ef')
        self.entradaValoresX = Entry(self.frame_x, width = 25)

        self.label3.pack(side='left', anchor='w', pady=10, padx=20)
        self.entradaValoresX.pack(side='left')

        self.botao = Button(self.frame_botao, text='acrescentar', command=self.armazenarX, bg='#DAE3EB')
        self.botao_calcular = Button(self.frame_botao, text='calcular', command=self.calcularValoresY, bg='#DAE3EB')
        self.botao_sair = Button(self.frame_botao, text='Sair', command=self.janela_x.destroy, bg='#DAE3EB')

        self.botao.pack(side='left',padx=200)
        self.botao_calcular.pack(side='left',padx=10)
        self.botao_sair.pack(side='right',padx=10)

        self.frame_x.pack()
        self.frame_botao.pack()

        mainloop()

    def calcularValoresY(self):
        self.janela_x.destroy()

        valor = []
        valor, resultado = regressao_linear.calcularY(x)

        x.clear()

        # Cria uma janela Tkinter
        root = tk.Tk()
        root.title("Gráfico Matplotlib no Tkinter")
        root.configure(bg='white')

        text_widget = tk.Text(root, height=4, width=50, font = {'Roboto', 13})
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        #Configura o widget Text para se comportar como um Label
        text_widget.insert(tk.END, resultado)
        text_widget.config(state="disabled", wrap="word", bg=root.cget("bg"), relief="flat", highlightthickness=0)
        text_widget.tag_configure('center', justify = 'center')
        text_widget.tag_add('center', '1.0', 'end')
        #Cria uma barra de rolagem
        scroll_bar = tk.Scrollbar(root, command=text_widget.yview)
        scroll_bar.pack(side=tk.LEFT, fill=tk.Y)

        #Configura a barra de rolagem para trabalhar com o widget Text
        text_widget.config(yscrollcommand=scroll_bar.set)

        # Botão para fechar a aplicação, empacotado por último para ficar na parte inferior
        button = tk.Button(master=root, text="Fechar", command=root.destroy,
                  font=('Roboto', 14),  # Aumenta o tamanho da fonte
                  padx=20,  # Adiciona espaço horizontal interno
                  pady=10,  # Adiciona espaço vertical interno
                  bg='#F9F8FF',  # Cor de fundo do botão
        )
        button.pack(side=tk.BOTTOM)

        tk.mainloop()

    def exibe(self):

        numDecimais = int(self.entradaNumDecimais.get())

        self.janela_numDecimais.destroy()

        resultado, fig = regressao_linear.calcular(x, y, numDecimais)

        x.clear()
        y.clear()
        
        # Cria uma janela Tkinter
        root = tk.Tk()
        root.title("Gráfico Matplotlib no Tkinter")
        root.configure(bg='white')

        text_widget = tk.Text(root, height=4, width=50, font = {'Roboto', 13})
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        #Configura o widget Text para se comportar como um Label
        text_widget.insert(tk.END, resultado)
        text_widget.config(state="disabled", wrap="word", bg=root.cget("bg"), relief="flat", highlightthickness=0)
        text_widget.tag_configure('center', justify = 'center')
        text_widget.tag_add('center', '1.0', 'end')
        #Cria uma barra de rolagem
        scroll_bar = tk.Scrollbar(root, command=text_widget.yview)
        scroll_bar.pack(side=tk.LEFT, fill=tk.Y)

        #Configura a barra de rolagem para trabalhar com o widget Text
        text_widget.config(yscrollcommand=scroll_bar.set)

        # Cria uma figura do Matplotlib

        # Adiciona a figura do Matplotlib à janela do Tkinter abaixo do label
        canvas = FigureCanvasTkAgg(fig, master=root)  # A 'master' é a janela do Tkinter
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Botão para fechar a aplicação, empacotado por último para ficar na parte inferior
        button = tk.Button(master=root, text="Fechar", command=root.destroy,
                  font=('Roboto', 14),  # Aumenta o tamanho da fonte
                  padx=20,  # Adiciona espaço horizontal interno
                  pady=10,  # Adiciona espaço vertical interno
                  bg='#F9F8FF',  # Cor de fundo do botão
        )
        button_X = tk.Button(master=root, text="Valor_X", command=self.x_janela,
                  font=('Roboto', 14),  # Aumenta o tamanho da fonte
                  padx=20,  # Adiciona espaço horizontal interno
                  pady=10,  # Adiciona espaço vertical interno
                  bg='#F9F8FF',  # Cor de fundo do botão
        )
        button.pack(side=tk.BOTTOM)
        button_X.pack(side=tk.BOTTOM)

        tk.mainloop()

gui = App()