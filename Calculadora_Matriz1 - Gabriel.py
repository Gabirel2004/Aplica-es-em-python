from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from fractions import Fraction
import random
import numpy as np

class CalculadoradeMatrizes:
    # Atributos da classe CalculadoradeMatrizes
    def __init__(self):
        self.entrada_matriz_A = []
        self.entrada_matriz_B = []       
    # Faz uma matriz quadrado magico 
    def quadrado_magico(self):
        try:
            ordem = simpledialog.askinteger("Entrada","Ordem da matriz:")

            quadrado_magico = np.zeros((ordem,ordem),dtype = np.int16)
            
            if ordem % 2 == 0:
                raise ValueError("Não existe matriz quadrado magico de ordem par!!")

            if ordem % 2 == 1:
                quadrado_magico = np.zeros((ordem, ordem), dtype=int)
                n = 1
                i = 0
                j = ordem // 2
                aleatorio = random.randint(-50,50)

                while n <= ordem**2:
                    quadrado_magico[i, j] = n + aleatorio
                    n += 1
                    newi, newj = (i - 1) % ordem, (j + 1) % ordem
                    if quadrado_magico[newi, newj]:
                        i += 1
                    else:
                        i, j = newi, newj
                    
                janelas.janela_resultado(quadrado_magico)
                    
        except ValueError as e:
            messagebox.showerror("Erro", str(e))            
    # Seta as entradas da matriz 
    def set_entrada(self,string_fracao):
        try:
            fracao = Fraction(string_fracao)
            return float(fracao)
        except ZeroDivisionError:
            raise ValueError("Erro: Denominador igual a 0!!")
    # Obtem os valores da matriz
    def get_entradas(self,linhas,colunas):
        matriz_aux = []
        for i in range(linhas):
            lista_aux = []
            for j in range(colunas):
                valor = self.set_entrada(self.entrada_matriz_A[i][j].get())
                lista_aux.append(valor)
            matriz_aux.append(lista_aux)
        return matriz_aux
    # Cria os quadradinhos de entrada dos valores
    def criar_matriz_A(self):
        linhas = int(janelas.entrada_linhas_A.get())
        colunas = int(janelas.entrada_coluna_A.get())

        # Limpar entradas de matriz A anteriores
        for i in self.entrada_matriz_A:
            for entrada in i:
                entrada.destroy()
                
        self.entrada_matriz_A.clear()
        # Criar novas entradas de matriz A
        for i in range(linhas):
            lista_aux = []
            for j in range(colunas):
                entrada = Entry(janelas.frame_entradas_A, width=3, font=('Arial', 15))
                entrada.grid(row=i + 2, column=j, padx=5, pady=5)
                lista_aux.append(entrada)
            self.entrada_matriz_A.append(lista_aux)
    # Cria os quadradinhos de entrada dos valore               
    def criar_matriz_B(self):
        linhas = int(janelas.entrada_linhas_B.get())
        colunas = int(janelas.entrada_coluna_B.get())
        # Limpar entradas de matriz B anteriores
        for i in self.entrada_matriz_B:
            for entrada in i:
                entrada.destroy()
        # Criar novas entradas de matriz B
        self.entrada_matriz_B.clear()
        for i in range(linhas):
            lista_aux = []
            for j in range(colunas):
                entrada = Entry(janelas.frame_entradas_B, width=3,font=('Arial',15))
                entrada.grid(row=i + 2, column=j, padx=5, pady=5)
                lista_aux.append(entrada)
            self.entrada_matriz_B.append(lista_aux)        
    #Calcula a multiplicação
    def calcula_multiplicacao(self):
        try:
            linhas_A = int(janelas.entrada_linhas_A.get())#Variavel que recebe as linhas da matriz a
            colunas_A = int(janelas.entrada_coluna_A.get())#Variavel que recebe as colunas da matriz a

            linhas_B = int(janelas.entrada_linhas_B.get())#Variavel que recebe as linhas da matriz b
            colunas_B = int(janelas.entrada_coluna_B.get())#Variavel que recebe as colunas da matriz b
            #verifica se é possivel calcular a multiplicação das matrizes
            if colunas_A != linhas_B:
                raise ValueError("As colunas da matriz A devem ser iguais a linhas da matriz B")
            #criar uma nova matriz que vai receber o resultado da multiplicação
            matriz_resultante = []
            for i in range(linhas_A):
                lista_aux = []
                for j in range(colunas_B):
                    soma = 0
                    for k in range(colunas_A):
                        soma += self.set_entrada(self.entrada_matriz_A[i][k].get()) * self.set_entrada(self.entrada_matriz_B[k][j].get())
                    lista_aux.append(soma)    
                matriz_resultante.append(lista_aux)

            janelas.janela_resultado(matriz_resultante)
        
        except ValueError as e:
            messagebox.showerror("Erro",str(e))       
    #Calcula a soma    
    def calcula_soma(self):
        try:
            linhas_a = int(janelas.entrada_linhas_A.get())#Variavel que recebe as linhas da matriz a
            colunas_a = int(janelas.entrada_coluna_A.get())#Variavel que recebe as colunas da matriz a

            linhas_b = int(janelas.entrada_linhas_B.get())#Variavel que recebe as linhas da matriz b
            colunas_b = int(janelas.entrada_coluna_B.get())#Variavel que recebe as colunas da matriz b
            
            if linhas_a != linhas_b or colunas_a != colunas_b:
                raise ValueError("As matrizes devem ser de msm ordem!!")
            
            matriz = []
            for i in range(linhas_a):
                #criar uma lista auxiliar para amazenar as linhas da matriz
                lista_aux = []
                for j in range(colunas_a):
                    #faz o calculo da soma das matrizes
                    valor = self.set_entrada(self.entrada_matriz_A[i][j].get()) + self.set_entrada(self.entrada_matriz_B[i][j].get())
                    lista_aux.append(valor)
                matriz.append(lista_aux)
             
            janelas.janela_resultado(matriz)
        except ValueError as e:
            messagebox.showerror("Erro",str(e))       
    #Calcula a subtração
    def calcula_subtracao(self):
        try:
            linhas_a = int(janelas.entrada_linhas_A.get())#Variavel que recebe as linhas da matriz a
            colunas_a = int(janelas.entrada_coluna_A.get())#Variavel que recebe as colunas da matriz a

            linhas_b = int(janelas.entrada_linhas_B.get())#Variavel que recebe as linhas da matriz b
            colunas_b = int(janelas.entrada_coluna_B.get())#Variavel que recebe as colunas da matriz b
            
            if linhas_a != linhas_b or colunas_a != colunas_b:
                raise ValueError("As matrizes devem ser de msm ordem!!")
            
            matriz = []
            for i in range(linhas_a):
                #criar uma lista auxiliar para amazenar as linhas da matriz
                lista_aux = []
                for j in range(colunas_a):
                    #faz o calculo da soma das matrizes
                    valor = self.set_entrada(self.entrada_matriz_A[i][j].get()) - self.set_entrada(self.entrada_matriz_B[i][j].get())
                    lista_aux.append(valor)
                matriz.append(lista_aux)
                
            janelas.janela_resultado(matriz)
        except ValueError as e:
            messagebox.showerror("Erro",str(e))       
    #Calcula a transposta  
    def calcula_transposta(self):
        linhas = int(janelas.entrada_linhas_A.get())#Variavel que recebe as linhas da matriz a
        colunas = int(janelas.entrada_coluna_A.get())#Variavel que recebe as colunas da matriz a
        #criar uma matriz para receber o resutado da trasposta
        matriz = self.get_entradas(linhas,colunas)

        matriz_transposta = np.transpose(matriz)

        janelas.janela_resultado(matriz_transposta)   
    # Calcula o determinate da matriz de entrada
    def calcular_determinate(self):
        try:
            linhas = int(janelas.entrada_linhas_A.get())
            colunas = int(janelas.entrada_coluna_A.get())

            if(linhas != colunas):
                raise ValueError("Erro a matriz não é quadrada!!")
            
            matriz_aux = self.get_entradas(linhas,colunas)

            determinate = np.linalg.det(matriz_aux)
            
            janelas.resultado_det(determinate)
        
        except ValueError as e:
            messagebox.showerror("Erro",str(e))
    # Calcula a inversa da matriz   
    def calcula_inversa(self):
        try:
            linhas = int(janelas.entrada_linhas_A.get())
            colunas = int(janelas.entrada_coluna_A.get())

            if linhas !=  colunas:
                raise ValueError("Erro a matriz não é quadrada!!")
            
            matriz_aux = self.get_entradas(linhas,colunas)

            if(np.linalg.det(matriz_aux) == 0):
                raise ValueError("Erro a matriz é singular!!")

            matriz_inversa = np.linalg.inv(matriz_aux)
            janelas.janela_resultado(matriz_inversa)
            
        except ValueError as e:
            messagebox.showerror("Erro",str(e))    
        
class Janelas:
    # Atributos da Classe Janelas 
    def __init__(self):
        #Atributos relacionados a matriz a
        self.frame_entradas_A = None
        self.entrada_linhas_A = None
        self.entrada_coluna_A = None
        self.entrada_matriz_A = []
        #Atributos relacionados a matriz b
        self.frame_entradas_B = None
        self.entrada_linhas_B = None
        self.entrada_coluna_B = None
        self.entrada_matriz_B = [] 
        #Atributos relacionados a janelas
        self.root = None
        self.nova_janela = None        
    # Janela de reultado do determinante
    def resultado_det(self,det):
        # Caso exista uma janela com de resutado aberta execute
        if self.root != None:
            self.destrir_janela_resultado()   
        
        self.root = Tk()
        self.root.geometry("+250+350")
        self.root.protocol("WM_DELETE_WINDOW",self.destrir_janela_resultado)
        self.root.resizable(False,False)
        self.root.title("Resultado")

        frame = Frame(self.root, relief="groove", bd=2, bg="#FFA07A")
        frame.grid(row=0, column=0, padx=5, pady=5)
        
        fracao = Fraction(det)
        resultado = Label(frame, text=f"Determinate: {fracao.limit_denominator(1000000)}", font=("Arial", 15), bg="light yellow", padx=20, pady=20)
        resultado.grid(padx=5, pady=5)  
    # Janela de resultados de matrizes
    def janela_resultado(self ,matriz):
        
        # Caso exista uma janela com de resutado aberta execute
        if self.root != None:
            self.destrir_janela_resultado()
        
        self.root = Tk()
        self.root.title("Matriz Resultante")
        self.root.protocol("WM_DELETE_WINDOW",self.destrir_janela_resultado)
        self.root.geometry("+150+300")
        self.root.configure(bg="#F5F5DC")
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                # Usar valor_formatado ao invés de matriz[i][j]
                valor_formatado = Fraction(matriz[i][j])
                Label(self.root, text=valor_formatado.limit_denominator(1000000), bg="#F5F5DC", font=("Arial",15)).grid(row=i, column=j, padx=5, pady=5)
                # Criar um rótulo para exibir cada elemento da matriz
                grade = Label(self.root, text=valor_formatado.limit_denominator(100), width=8, height=2, relief="groove", bg="peachpuff", bd=4,font=("Arial",15))
                grade.grid(row=i, column=j, padx=5, pady=5)
        self.root.mainloop           
    # Destroi a janela de resultado caso esteja aberta
    def destrir_janela_resultado(self):
            self.root.destroy()
            self.root = None
    # Destroi as jalenas de interação
    def destruir_janela(self):
        # Caso exista uma janela com de resutado aberta execute
        if self.root != None:
            self.root.destroy()
            self.root = None
        op.entrada_matriz_A.clear()
        op.entrada_matriz_B.clear()
        self.nova_janela.destroy()
        janelas.janela_pincipal()  
    # Abre a janela principal o APP
    def janela_pincipal(self):
          
        def abri_janela_multiplicacao():
            janela.destroy()
            self.janela_multiplicacao()

        def abri_janela_soma():
            janela.destroy()
            self.janela_soma()
        
        def abri_janela_subtracao():
            janela.destroy()
            self.janela_subtracao()
        
        def abri_janela_transposta():
            janela.destroy()
            self.janela_transposta()
          
        def abri_janela_determinate():
            janela.destroy()
            self.janela_determinate()
            
        def abri_janela_inversa():
            janela.destroy()
            self.janela_inversa()        
        # Configurações da janela principal
        janela = Tk()
        janela.resizable(False,False)
        janela.geometry("+450+225")
        janela.title("Calculadora de Matrizes")
        # Frame principal
        frame = Frame(janela, relief="groove", bd=4, bg="peachpuff")
        frame.pack(padx=20, pady=20)
        # Frame para rótulos
        frame_label = Frame(frame, bg="peachpuff")
        frame_label.grid(row=0, columnspan=3)
        Label(frame_label, text="Calculadora de Matrizes", font=("Arial", 20, "bold"), bg="peachpuff").pack(pady=5)
        # Frame para os botões de ação
        frame_botoes = Frame(frame, bg="light yellow")
        frame_botoes.grid(row=1, columnspan=3, pady=5)
        # Botões de ação
        Button(frame_botoes, text="Multiplicação", font=("Arial", 15), bg="mintcream", relief="ridge", bd=2, width=15, command=abri_janela_multiplicacao).grid(row=0, column=0, padx=10, pady=10)
        Button(frame_botoes, text="Soma", font=("Arial", 15), bg="mintcream", relief="ridge", bd=2, width=15, command=abri_janela_soma).grid(row=0, column=1, padx=10, pady=10)
        Button(frame_botoes, text="Subtração", font=("Arial", 15), bg="mintcream", relief="ridge", bd=2, width=15, command=abri_janela_subtracao).grid(row=0, column=2, padx=10, pady=10)
        Button(frame_botoes, text="Transposta", font=("Arial", 15), bg="mintcream", relief="ridge", bd=2, width=15, command=abri_janela_transposta).grid(row=1, column=0, padx=10, pady=10)
        Button(frame_botoes, text="Quadrado Mágico", font=("Arial", 15), bg="mintcream", relief="ridge", bd=2, width=15, command=op.quadrado_magico).grid(row=1, column=1, padx=10, pady=10)
        Button(frame_botoes, text="Determinante", font=("Arial", 15), bg="mintcream", relief="ridge", bd=2, width=15, command=abri_janela_determinate).grid(row=1, column=2, padx=10, pady=10)
        Button(frame_botoes, text="Inversa", font=("Arial", 15), bg="mintcream", relief="ridge", bd=2, width=15, command=abri_janela_inversa).grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        janela.mainloop()
    # Abre a janela que faz da multiplicação
    def janela_multiplicacao(self):
            
        self.nova_janela = Tk()
        self.nova_janela.protocol("WM_DELETE_WINDOW",self.destruir_janela)
        self.nova_janela.resizable(False,False)
        self.nova_janela.geometry("+350+225")
        self.nova_janela.title("Multiplicação")
        # Frame Principal
        frame = Frame(self.nova_janela,bg='peachpuff',relief="groove",bd=2)
        frame.pack(padx=10,pady=10)
        # Frame para a Matriz A
        frame_matriz_A = Frame(frame, relief="groove", bd=2, bg="#FFA07A")
        frame_matriz_A.grid(row=0, column=0, padx=5, pady=5)
        # Frame para a entrada dos valores da matriz A
        self.frame_entradas_A = Frame(frame_matriz_A, bg="#FFA07A")
        self.frame_entradas_A.grid(row=2,columnspan=5,padx=5,pady=5)
        
        Label(frame_matriz_A, text="Matriz A", font=("Arial", 20, "bold"), bg="#FFA07A").grid(row=0, columnspan=5, padx=5, pady=5)
        Label(frame_matriz_A, text="Linhas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_linhas_A = Entry(frame_matriz_A, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_linhas_A.grid(row=1, column=1, padx=5, pady=5)
        Label(frame_matriz_A, text="Colunas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=2, padx=5, pady=5)
        self.entrada_coluna_A = Entry(frame_matriz_A, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_coluna_A.grid(row=1, column=3, padx=5, pady=5)
        Button(frame_matriz_A, text="Criar Matriz A", font=("Arial",12), bg="light gray", relief="sunken", bd=2, command=op.criar_matriz_A).grid(row=1, column=4, padx=5, pady=5)
        # Frame para a Matriz B
        frame_matriz_B = Frame(frame, relief="groove", bd=2, bg="#FFA07A")
        frame_matriz_B.grid(row=0, column=1, padx=5, pady=5)
        # Frame para a entrada dos valores da matriz A
        self.frame_entradas_B = Frame(frame_matriz_B, bg="#FFA07A")
        self.frame_entradas_B.grid(row=2,columnspan=5,padx=5,pady=5)
        
        Label(frame_matriz_B, text="Matriz B", font=("Arial", 20, "bold"), bg="#FFA07A").grid(row=0, columnspan=5, padx=5, pady=5)
        Label(frame_matriz_B, text="Linhas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_linhas_B = Entry(frame_matriz_B, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_linhas_B.grid(row=1, column=1, padx=5, pady=5)
        Label(frame_matriz_B, text="Colunas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=2, padx=5, pady=5)
        self.entrada_coluna_B = Entry(frame_matriz_B, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_coluna_B.grid(row=1, column=3, padx=5, pady=5)
        Button(frame_matriz_B, text="Criar Matriz B", font=("Arial",12), bg="light gray", relief="sunken", bd=2, command=op.criar_matriz_B).grid(row=1, column=4, padx=5, pady=5)
        
        Button(frame, text="Calcular Multiplicação", font=("Arial",12), width=17, bg="light gray", relief="sunken", bd=2, command=op.calcula_multiplicacao).grid(row=1, columnspan=2, padx=10, pady=10)
        Button(frame, text="voltar", font=("Arial",12), width=17, bg="light gray", relief="sunken", bd=2, command=self.destruir_janela).grid(row=2, columnspan=2, padx=10, pady=10)

        self.nova_janela.mainloop()
    # Abre a janela que faz da soma     
    def janela_soma(self):
    
        self.nova_janela = Tk()
        self.nova_janela.protocol("WM_DELETE_WINDOW",self.destruir_janela)
        self.nova_janela.resizable(False,False)
        self.nova_janela.geometry("+350+225")
        self.nova_janela.title("Soma")
        # Frame principal
        frame = Frame(self.nova_janela,bg='peachpuff',relief="groove",bd=2)
        frame.pack(padx=10,pady=10)
        # Frame para a Matriz A
        frame_matriz_A = Frame(frame, relief="groove", bd=2, bg="#FFA07A")
        frame_matriz_A.grid(row=0, column=0, padx=10, pady=10)
        # Frame para a entrada dos valores da matriz A
        self.frame_entradas_A = Frame(frame_matriz_A, bg="#FFA07A")
        self.frame_entradas_A.grid(row=2,columnspan=5,padx=5,pady=5)
        
        Label(frame_matriz_A, text="Matriz A", font=("Arial", 20, "bold"), bg="#FFA07A").grid(row=0, columnspan=5, padx=5, pady=5)
        Label(frame_matriz_A, text="Linhas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_linhas_A = Entry(frame_matriz_A, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_linhas_A.grid(row=1, column=1, padx=5, pady=5)
        Label(frame_matriz_A, text="Colunas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=2, padx=5, pady=5)
        self.entrada_coluna_A = Entry(frame_matriz_A, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_coluna_A.grid(row=1, column=3, padx=5, pady=5)
        Button(frame_matriz_A, text="Criar Matriz A", font=("Arial",12), bg="light gray", relief="sunken", bd=2, command=op.criar_matriz_A).grid(row=1, column=4, padx=5, pady=5)
        # Frame para a Matriz B
        frame_matriz_B = Frame(frame, relief="groove", bd=2, bg="#FFA07A")
        frame_matriz_B.grid(row=0, column=1, padx=10, pady=10)
        # Frame para a entrada dos valores da matriz A
        self.frame_entradas_B = Frame(frame_matriz_B, bg="#FFA07A")
        self.frame_entradas_B.grid(row=2,columnspan=5,padx=5,pady=5)
        
        Label(frame_matriz_B, text="Matriz B", font=("Arial", 20, "bold"), bg="#FFA07A").grid(row=0, columnspan=5, padx=5, pady=5)
        Label(frame_matriz_B, text="Linhas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_linhas_B = Entry(frame_matriz_B, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_linhas_B.grid(row=1, column=1, padx=5, pady=5)
        Label(frame_matriz_B, text="Colunas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=2, padx=5, pady=5)
        self.entrada_coluna_B = Entry(frame_matriz_B, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_coluna_B.grid(row=1, column=3, padx=5, pady=5)
        Button(frame_matriz_B, text="Criar Matriz B", font=("Arial",12), bg="light gray", relief="sunken", bd=2, command=op.criar_matriz_B).grid(row=1, column=4, padx=5, pady=5)
        
        Button(frame, text="Calcular Soma", font=("Arial",12), width=17, bg="light gray", relief="sunken", bd=2, command=op.calcula_soma).grid(row=1, columnspan=2, padx=10, pady=10)
        Button(frame, text="voltar", font=("Arial",12), width=17, bg="light gray", relief="sunken", bd=2, command=self.destruir_janela).grid(row=2, columnspan=2, padx=10, pady=10)

        self.nova_janela.mainloop()       
    # Abre a janela que faz da subtração   
    def janela_subtracao(self):
    
        self.nova_janela = Tk()
        self.nova_janela.protocol("WM_DELETE_WINDOW",self.destruir_janela)
        self.nova_janela.resizable(False,False)
        self.nova_janela.geometry("+350+225")
        self.nova_janela.title("Subtração")
        # Frame principal
        frame = Frame(self.nova_janela,bg='peachpuff',relief="groove",bd=2)
        frame.pack(padx=10,pady=10)
        # Frame para a Matriz A
        frame_matriz_A = Frame(frame, relief="groove", bd=2, bg="#FFA07A")
        frame_matriz_A.grid(row=0, column=0, padx=5, pady=5)
        # Frame para a entrada dos valores da matriz A
        self.frame_entradas_A = Frame(frame_matriz_A, bg="#FFA07A")
        self.frame_entradas_A.grid(row=2,columnspan=5,padx=5,pady=5)
        
        Label(frame_matriz_A, text="Matriz A", font=("Arial", 20, "bold"), bg="#FFA07A").grid(row=0, columnspan=5, padx=5, pady=5)
        Label(frame_matriz_A, text="Linhas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_linhas_A = Entry(frame_matriz_A, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_linhas_A.grid(row=1, column=1, padx=5, pady=5)
        Label(frame_matriz_A, text="Colunas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=2, padx=5, pady=5)
        self.entrada_coluna_A = Entry(frame_matriz_A, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_coluna_A.grid(row=1, column=3, padx=5, pady=5)
        Button(frame_matriz_A, text="Criar Matriz A", font=("Arial",12), bg="light gray", relief="sunken", bd=2, command=op.criar_matriz_A).grid(row=1, column=4, padx=5, pady=5)
        # Frame para a Matriz B
        frame_matriz_B = Frame(frame, relief="groove", bd=2, bg="#FFA07A")
        frame_matriz_B.grid(row=0, column=1, padx=5, pady=5)
        # Frame para a entrada dos valores da matriz A
        self.frame_entradas_A = Frame(frame_matriz_A, bg="#FFA07A")
        self.frame_entradas_A.grid(row=2,columnspan=5,padx=5,pady=5)
        
        Label(frame_matriz_B, text="Matriz B", font=("Arial", 20, "bold"), bg="#FFA07A").grid(row=0, columnspan=5, padx=5, pady=5)
        Label(frame_matriz_B, text="Linhas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_linhas_B = Entry(frame_matriz_B, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_linhas_B.grid(row=1, column=1, padx=5, pady=5)
        Label(frame_matriz_B, text="Colunas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=2, padx=5, pady=5)
        self.entrada_coluna_B = Entry(frame_matriz_B, width=3, font=("Arial",14), relief="sunken", bd=2)
        self.entrada_coluna_B.grid(row=1, column=3, padx=5, pady=5)
        Button(frame_matriz_B, text="Criar Matriz B", font=("Arial",12), bg="light gray", relief="sunken", bd=2, command=op.criar_matriz_B).grid(row=1, column=4, padx=5, pady=5)
        
        Button(frame, text="Calcular Subtração", font=("Arial",12), width=17, bg="light gray", relief="sunken", bd=2, command=op.calcula_subtracao).grid(row=1, columnspan=2, padx=10, pady=10)
        Button(frame, text="Voltar", font=("Arial",12), width=17,bg="light gray", relief="sunken", bd=2, command=self.destruir_janela).grid(row=2, columnspan=2, padx=10, pady=10)

        self.nova_janela.mainloop()       
    # Abre a janela que faz da transposta     
    def janela_transposta(self):
        
        self.nova_janela = Tk()
        self.nova_janela.protocol("WM_DELETE_WINDOW",self.destruir_janela)
        self.nova_janela.resizable(False,False)
        self.nova_janela.geometry("+550+250")
        self.nova_janela.title("Transposta")
        # Frame principal
        frame = Frame(self.nova_janela,bg='peachpuff',relief="groove",bd=2)
        frame.pack(padx=10,pady=10)
        # Frame para a Matriz 
        frame_matriz_A = Frame(frame, relief="groove", bd=2, bg="#FFA07A")
        frame_matriz_A.grid(row=0, column=0, padx=5, pady=5)
        # Frame para a entrada dos valores da matriz A
        self.frame_entradas_A = Frame(frame_matriz_A, bg="#FFA07A")
        self.frame_entradas_A.grid(row=2,columnspan=5,padx=5,pady=5)
        
        Label(frame_matriz_A, text="Matriz", font=("Arial", 20, "bold"), bg="#FFA07A").grid(row=0, columnspan=5, padx=5, pady=5)
        Label(frame_matriz_A, text="Linhas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_linhas_A = Entry(frame_matriz_A, width=4, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_linhas_A.grid(row=1, column=1, padx=5, pady=5)
        Label(frame_matriz_A, text="Colunas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=2, padx=5, pady=5)
        self.entrada_coluna_A = Entry(frame_matriz_A, width=4, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_coluna_A.grid(row=1, column=3, padx=5, pady=5)
        Button(frame_matriz_A, text="Criar Matriz", font=("Arial",12), bg="light gray", relief="sunken", bd=2, command=op.criar_matriz_A).grid(row=1, column=4, padx=5, pady=5)
        
        Button(frame, text="Calcular Trasnposta", font=("Arial",12), width=17,bg="light gray", relief="sunken", bd=2, command=op.calcula_transposta).grid(row=1, columnspan=2, padx=10, pady=10)
        Button(frame, text="Voltar", font=("Arial",12), width=17,bg="light gray", relief="sunken", bd=2, command=self.destruir_janela).grid(row=2, columnspan=2, padx=10, pady=10)
        
        self.nova_janela.mainloop()  
    # Abre a janela que faz do determinate     
    def janela_determinate(self):
    
        self.nova_janela = Tk()
        self.nova_janela.protocol("WM_DELETE_WINDOW",self.destruir_janela)
        self.nova_janela.resizable(False,False)
        self.nova_janela.geometry("+550+250")
        self.nova_janela.title("Nova Janela")
        # Frame principal
        frame = Frame(self.nova_janela,bg='peachpuff',relief="groove",bd=2)
        frame.pack(padx=10,pady=10)
        # Frame para a Matriz
        frame_matriz_A = Frame(frame, relief="groove", bd=2, bg="#FFA07A")
        frame_matriz_A.grid(row=0, column=0, padx=10, pady=10)
        # Frame para a entrada dos valores da matriz A
        self.frame_entradas_A = Frame(frame_matriz_A, bg="#FFA07A")
        self.frame_entradas_A.grid(row=2,columnspan=5,padx=5,pady=5)
        
        Label(frame_matriz_A, text="Matriz", font=("Arial", 20, "bold"), bg="#FFA07A").grid(row=0, columnspan=5, padx=5, pady=5)
        Label(frame_matriz_A, text="Linhas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_linhas_A = Entry(frame_matriz_A, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_linhas_A.grid(row=1, column=1, padx=5, pady=5)
        Label(frame_matriz_A, text="Colunas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=2, padx=5, pady=5)
        self.entrada_coluna_A = Entry(frame_matriz_A, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_coluna_A.grid(row=1, column=3, padx=5, pady=5)
        Button(frame_matriz_A, text="Criar Matriz ", font=("Arial",12), bg="light gray", relief="sunken", bd=2, command=op.criar_matriz_A).grid(row=1, column=4, padx=5, pady=5)
        
        Button(frame, text="Calcular Determinate", font=("Arial",12), width=17, bg="light gray", relief="sunken", bd=2, command=op.calcular_determinate).grid(row=1, columnspan=2, padx=10, pady=10)
        Button(frame, text="Voltar", font=("Arial",12), width=17, bg="light gray", relief="sunken", bd=2, command=self.destruir_janela).grid(row=2, columnspan=2, padx=10, pady=10)

        self.nova_janela.mainloop()       
    # Abre a janela que faz da inversa
    def janela_inversa(self):
        
        self.nova_janela = Tk()
        self.nova_janela.protocol("WM_DELETE_WINDOW",self.destruir_janela)
        self.nova_janela.resizable(False,False)
        self.nova_janela.geometry("+550+250")
        self.nova_janela.title("Nova Janela")
        # Frame principal
        frame = Frame(self.nova_janela,bg='peachpuff',relief="groove",bd=2)
        frame.pack(padx=10,pady=10)
        # Frame para a Matriz
        frame_matriz_A = Frame(frame, relief="groove", bd=2, bg="#FFA07A")
        frame_matriz_A.grid(row=0, column=0, padx=5, pady=5)
        # Frame para a entrada dos valores da matriz A
        self.frame_entradas_A = Frame(frame_matriz_A, bg="#FFA07A")
        self.frame_entradas_A.grid(row=2,columnspan=5,padx=5,pady=5)
        
        Label(frame_matriz_A, text="Matriz", font=("Arial", 20, "bold"), bg="#FFA07A").grid(row=0, columnspan=5, padx=5, pady=5)
        Label(frame_matriz_A, text="Linhas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_linhas_A = Entry(frame_matriz_A, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_linhas_A.grid(row=1, column=1, padx=5, pady=5)
        Label(frame_matriz_A, text="Colunas", font=("Arial",15), bg="#FFA07A").grid(row=1, column=2, padx=5, pady=5)
        self.entrada_coluna_A = Entry(frame_matriz_A, width=3, font=("Arial",15), relief="sunken", bd=2)
        self.entrada_coluna_A.grid(row=1, column=3, padx=5, pady=5)
        Button(frame_matriz_A, text="Criar Matriz ", font=("Arial",12), bg="light gray", relief="sunken", bd=2, command=op.criar_matriz_A).grid(row=1, column=4, padx=5, pady=5)
        
        Button(frame, text="Calcular Inversa", font=("Arial",12), width=17, bg="light gray", relief="sunken", bd=2, command=op.calcula_inversa).grid(row=1, columnspan=2, padx=10, pady=10)
        Button(frame, text="voltar", font=("Arial",12), width=17, bg="light gray", relief="sunken", bd=2, command=self.destruir_janela).grid(row=2, columnspan=2, padx=10, pady=10)

        self.nova_janela.mainloop()
           
op = CalculadoradeMatrizes()
janelas = Janelas()
janelas.janela_pincipal()