from tkinter import scrolledtext
from tkinter import *
from tkinter.font import Font
import tkinter as tk
import integral_modular
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
        self.frame_h  = Frame(self.janela_principal,bg=cor_fundo)
        self.frame_botao = Frame(self.janela_principal,bg=cor_fundo) 
        
        # Criando label e botões do frame de cima
        self.labelT = Label(self.frame_Titulo, text='Legenda para Entrada de dados:', anchor='n', width=30, font=fonte_Neg,bg=cor_fundo)
        self.label = Label(self.frame_Texto, text='√ -> sqrt()\n\nlog -> log()\n\nlog10 -> log10()\n\nseno -> sin()\n\ncos -> cos()\n\ntangente -> tg()\n\nbase^expoente -> b**e\n\nmultiplicacao -> *', anchor='n', width=30, font=fonte,bg=cor_fundo)
        self.label1 = Label(self.frame_funcao, text='Digite a funcao:', anchor='w', width=30, font=fonte_Neg,bg=cor_fundo)
        self.label2 = Label(self.frame_numDecimais, text='Digite o numero de casas decimais:', anchor='w', width=30, font=fonte_Neg,bg=cor_fundo)
        self.label3 = Label(self.frame_a, text='Digite o intervalo inicial (a):', anchor='w', width=30, font=fonte_Neg,bg=cor_fundo)
        self.label4 = Label(self.frame_b, text='Digite o intervalo final (b):', anchor='w', width=30, font=fonte_Neg,bg=cor_fundo)
        self.label5 = Label(self.frame_n, text='Digite o numero de trapezios:', anchor='w', width=30, font=fonte_Neg,bg=cor_fundo)
        self.label6 = Label(self.frame_h, text='Digite a altura/passo (h):', anchor='w', width=30, font=fonte_Neg,bg=cor_fundo)
        
        # Criando o widget de entrada
        self.entradaFuncao = Entry(self.frame_funcao, width=25)
        self.entradaNumDecimais = Entry(self.frame_numDecimais, width=25)
        self.entradaA = Entry(self.frame_a, width=25)
        self.entradaB = Entry(self.frame_b, width=25)
        self.entradaN = Entry(self.frame_n, width=25)
        self.entradaH = Entry(self.frame_h, width=25)
        
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
        
        self.label6.pack(side='left', anchor='w', pady=10, padx=20)
        self.entradaH.pack(side='left')
        
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
        self.frame_h.pack()
        self.frame_botao.pack()
        
        # Rodando
        mainloop()
  
    def exibe(self):

        funcao = str(self.entradaFuncao.get())
        numDecimais = int(self.entradaNumDecimais.get())
        a = double(self.entradaA.get())
        b = double(self.entradaB.get())
        n = int(self.entradaN.get())
        h = double(self.entradaH.get())
        
        resultado, fig = integral_modular.calcular(funcao, numDecimais, a, b, n, h)
        
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
        button.pack(side=tk.BOTTOM)

        self.entradaFuncao.delete(0,END)
        self.entradaNumDecimais.delete(0,END)
        self.entradaA.delete(0,END)
        self.entradaB.delete(0,END)
        self.entradaN.delete(0,END)
        self.entradaH.delete(0,END)

        tk.mainloop()


gui = App()