
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("920x450")
        self.title('Generador de Números Aleatorios')

        # initialize data
        self.menu = ("Método de los Centros Cuadrados",
      "Método Congruencial",
      "Método Congruencial Mixto",
      "Generador Multiplicativo",
      "Método Congruencial Lineal Combinado")

        # set up variable
        self.option = tk.StringVar(self)
        
        self.option.set(self.menu[0])
        
        # create widget
        self.create_wigets()

    def create_wigets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # label
        label = ttk.Label(self,  text='SIMULADOR DE NUMEROS RANDOM',font = ("Castellar",15))
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        self.frame = tk.LabelFrame(self,text="Método de los Centros Cuadrados", borderwidth=8, padx=100, pady=50, labelanchor = "nw", font = ("Castellar",12))
        self.frame.place(x=10, y=70)

        # option menu
        option_menu = tk.OptionMenu(
            self,
            self.option,
            *self.menu,
            command=self.option_changed)
        
        helv36 = tkFont.Font(family='Castellar', size=8)
        option_menu.config(font=helv36)
        
        option_menu.place(x=585, y=10)


    def centrosCuadrados(self, semillaInicio, numerosAGenerar):
       semilla = int(semillaInicio)
       
       if len(str(semillaInicio)) == 4 and semilla >= 100 and semilla <= 9999:
           numerosAleatorios = []
           Ris = []
           semillas = []
           generadores = []
           numerosGenerados = 0
        
           while numerosGenerados < numerosAGenerar:
               complemento = "" 
               semillas.append(semilla)
               semillaCuadrado = semilla * semilla
               if len(str(semillaCuadrado)) < 8:
                   
                   for relleno in range((8 - len(str(semillaCuadrado)))):
                       complemento += "0"
               semillaCuadrado = complemento + str(semillaCuadrado)
                
               numeroAleatorio = str(semillaCuadrado)[2:6]
               numerosAleatorios.append(numeroAleatorio)
               semilla = int(numeroAleatorio)
               Ri = int(numeroAleatorio) / 10000
               Ris.append(Ri)
               generador = str(semillaCuadrado)[0:2] + "|" + numeroAleatorio + "|" + str(semillaCuadrado)[6:]
               generadores.append(generador)
                
               numerosGenerados += 1
        
           
           results = tk.Toplevel()
           results.title("Resultados")
           cols = ('Xn','Semilla', 'Generador', 'No. Aleatorio', 'Ri')
           label = tk.Label(results, text="Centros Cuadrados", font=("Arial",30)).grid(row=0, columnspan=3)
           table = ttk.Treeview(results, columns=cols, show='headings',selectmode='browse')
           
           for col in cols:
               table.heading(col, text=col)  
               
           for x in range(len(semillas)):
               table.insert("", "end", values=(x,semillas[x], generadores[x], numerosAleatorios[x], Ris[x]))
               
           table.grid(row=1, column=0, columnspan=2)
           vsb=ttk.Scrollbar(results, orient="vertical", command=table.yview)
           vsb.place(relx=0.978, rely=0.2, relheight=0.8, relwidth=0.020)
           table.configure(yscrollcommand=vsb.set)

       else:
           print("La semilla otorgada no es un numero enetero de 4 digitos decimales" + "\n")
        
    def congruencial(self,semilla, multiplicador, incremento, modulo, numerosAGenerar,titulo):
        if modulo > 0 and modulo > multiplicador and multiplicador > 0 and modulo > incremento and (incremento > 0 or incremento == 0) and modulo > semilla and (semilla > 0 or semilla == 0):
            numerosAleatorios = []
            Ris = []
            semillas = []
            generadores = []
            numerosGenerados = 0
    
            while numerosGenerados < numerosAGenerar:
                semillas.append(semilla)
                generador = "(" + str(multiplicador) + "(" + str(semilla) + ")" + "+ " + str(incremento) + ")" + "mod" + "(" + str(modulo) + ")"
                generadores.append(generador)
                numeroAleatorio = (multiplicador * semilla + incremento) % modulo
                numerosAleatorios.append(numeroAleatorio)
                Ri = numeroAleatorio / modulo
                Ris.append(Ri)
                semilla = numeroAleatorio
    
                numerosGenerados += 1
    
            results = tk.Toplevel()
            results.title("Resultados")
            cols = ('Xn','Semilla', 'Generador', 'No. Aleatorio', 'Ri')
            label = tk.Label(results, text=titulo, font=("Arial",30)).grid(row=0, columnspan=3)
            table = ttk.Treeview(results, columns=cols, show='headings',selectmode='browse')
           
            for col in cols:
                table.heading(col, text=col)  
               
            for x in range(len(semillas)):
                table.insert("", "end", values=(x,semillas[x], generadores[x], numerosAleatorios[x], Ris[x]))
               
            table.grid(row=1, column=0, columnspan=2)
            vsb=ttk.Scrollbar(results, orient="vertical", command=table.yview)
            vsb.place(relx=0.978, rely=0.2, relheight=0.8, relwidth=0.020)
            table.configure(yscrollcommand=vsb.set)
        else:
            print("El modulo tiene que ser mayor a los demas valores; el multiplicador, incremento y semilla deben ser mayores a Cero")
            
    def congruencialMixto(self,semilla, multiplicador, incremento, modulo, numerosAGenerar):
        if self.hullDobell(multiplicador, incremento, modulo):
            titulo="Congruencial Mixto"
            self.congruencial(semilla, multiplicador, incremento, modulo, numerosAGenerar,titulo)
        else:
            print("Los parametros no logran cumplir la evaluacion de Hull-Dobell")

    def hullDobell(self,multiplicador, incremento, modulo): # a es el multiplicador, c es el incremento
        verificadorDivisor = 2
        while verificadorDivisor <= modulo:
            if incremento % verificadorDivisor != 0 or modulo % verificadorDivisor != 0:
                verificadorDivisor += 1
            else:
                return False
                
        numerosPrimosDivisores = []
        for numero in range(2, modulo):
            if modulo % numero == 0 and self.numeroPrimo(numero) == True:
                numerosPrimosDivisores.append(numero)
        for primo in numerosPrimosDivisores:
            if multiplicador % primo == 1:
                continue
            else:
                return False
        
        if modulo % 4 == 0: 
            if (multiplicador - 1) % 4 != 0: return False
            else: return True
    
        return True
    
    def numeroPrimo(self,numero):
        if numero == 2: return True
        for num in range(2, numero):
            if numero % num == 0: 
                return False
        return True
    
    def generadorMultiplicativo(self,semilla, multiplicador, modulo, numerosAGenerar):
        if (semilla == 0 or semilla > 0) and (multiplicador == 0 or multiplicador > 0) and (modulo == 0 or modulo > 0) and modulo > multiplicador and modulo > semilla and float(semilla).is_integer() and float(multiplicador).is_integer() and float(modulo).is_integer():
            numerosAleatorios = []
            Ris = []
            semillas = []
            generadores = []
            numerosGenerados = 0
    
            while numerosGenerados < numerosAGenerar:
                semillas.append(semilla)
                generador = "(" + str(multiplicador) + "*" + str(semilla) + ")" + "mod" + "(" + str(modulo) + ")"
                generadores.append(generador)
                numeroAleatorio = (multiplicador * semilla) % modulo
                numerosAleatorios.append(numeroAleatorio)
                Ri = numeroAleatorio / modulo
                Ris.append(Ri)
                semilla = numeroAleatorio
                
                numerosGenerados += 1
    
            results = tk.Toplevel()
            results.title("Resultados")
            cols = ('Xn','Semilla', 'Generador', 'No. Aleatorio', 'Ri')
            label = tk.Label(results, text="Generador Multiplicativo", font=("Arial",30)).grid(row=0, columnspan=3)
            table = ttk.Treeview(results, columns=cols, show='headings',selectmode='browse')
           
            for col in cols:
                table.heading(col, text=col)  
               
            for x in range(len(semillas)):
                table.insert("", "end", values=(x,semillas[x], generadores[x], numerosAleatorios[x], Ris[x]))
               
            table.grid(row=1, column=0, columnspan=2)
            vsb=ttk.Scrollbar(results, orient="vertical", command=table.yview)
            vsb.place(relx=0.978, rely=0.2, relheight=0.8, relwidth=0.020)
            table.configure(yscrollcommand=vsb.set)
        else:
            print("Los parametros introducidos por el usuario no cumplen las espeficaciones para este generador") 
    
    def separacionValores(self,listaValores):
        arregloValores = []
        valorenCurso = ""
        indice = 0
        for caracter in listaValores:
            if caracter.isdigit():
                valorenCurso += caracter
                if indice == len(listaValores) - 1:
                    (arregloValores).append(int(valorenCurso))
                    valorenCurso = ""
            elif caracter == ",":
                arregloValores.append(int(valorenCurso))
                valorenCurso = ""
            elif caracter.isspace():
                indice += 1
                continue
            else:
                return False
            indice += 1
        return arregloValores 
    
    def congruencialLinealCombinado(self,semillasOriginales, multiplicadores, modulos, numerosAGenerar):
        print("hello")
        if(self.separacionValores(semillasOriginales) != False and self.separacionValores(multiplicadores) != False and self.separacionValores(modulos) != False): 
            semillas = self.separacionValores(semillasOriginales)
            multiplicadores = self.separacionValores(multiplicadores)
            modulos = self.separacionValores(modulos)
    
            Ris = []
            numerosAleatorios = []
            numerosGenerados = 0
    
            while numerosGenerados < numerosAGenerar:
                numerosTemporales = []
                for indice in range(0, len(semillas)):
                    numTemp = (multiplicadores[indice] * semillas[indice]) % modulos[indice]
                    numerosTemporales.append(numTemp)
                numeroAleatorio = numerosTemporales[0]
                for numero in numerosTemporales[1:]:
                    numeroAleatorio -= numero
                numeroAleatorio = numeroAleatorio % (modulos[0] - 1) #Misma cuestion de modulos
                numerosAleatorios.append(numeroAleatorio)
                Ris.append(numeroAleatorio / modulos[0]) #Ris se saca con modulos[0] o modulos[0] - 1
                semillas = numerosTemporales
                numerosTemporales = []
                numerosGenerados += 1
    
            results = tk.Toplevel()
            results.title("Resultados")
            cols = ('Xn','No. Aleatorio')
            label = tk.Label(results, text="Generador Lineal Combinado", font=("Arial",30)).grid(row=0, columnspan=3)
            table = ttk.Treeview(results, columns=cols, show='headings',selectmode='browse')
           
            for col in cols:
                table.heading(col, text=col)  
               
            for x in range(len(numerosAleatorios)):
                table.insert("", "end", values=(x, numerosAleatorios[x]))
               
            table.grid(row=1, column=0, columnspan=2)
            vsb=ttk.Scrollbar(results, orient="vertical", command=table.yview)
            vsb.place(relx=0.978, rely=0.2, relheight=0.8, relwidth=0.020)
            table.configure(yscrollcommand=vsb.set)
    
    
    def cuadrados_frame(self, *args):
        self.frame['text']="Método de los Centros Cuadrados"
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        semilla_label= ttk.Label(self.frame,  text='Semilla:',font = ("Castellar",8)).grid(column=0,row=0,padx=10,pady=10)
        semilla_input = tk.Entry(self.frame, width=20)
        semilla_input.grid(column=1,row=0)
        
        total_label= ttk.Label(self.frame,  text='Total de Números a Generar:',font = ("Castellar",8)).grid(column=0,row=1,padx=10,pady=10)
        total_input = tk.Entry(self.frame, width=20)
        total_input.grid(column=1,row=1)
        
        sumbit_btn= tk.Button(self.frame, text="Generar",font = ("Castellar",8), command = lambda: self.aux_cuadrados_frame(semilla_input,total_input) ).place(relx=0.4, rely=1.1)
        
    def aux_cuadrados_frame(self,semilla_input,total_input):
        x1 = str(semilla_input.get())
        x2=int(total_input.get())  
        self.centrosCuadrados(x1,x2)
        
    def congruencial_frame(self, *args):

        self.frame['text']="Método Congruencial"
        for widget in self.frame.winfo_children():
            widget.destroy()

        
        semilla_label= ttk.Label(self.frame,  text='Semilla:',font = ("Castellar",8)).grid(column=0,row=0,padx=10,pady=10)
        semilla_input = ttk.Entry(self.frame, width=20)
        semilla_input.grid(column=1,row=0)
        
        multiplicador_label= ttk.Label(self.frame,  text='Multiplicador:',font = ("Castellar",8)).grid(column=0,row=1,padx=10,pady=10)
        multiplicador_input = ttk.Entry(self.frame, width=20)
        multiplicador_input.grid(column=1,row=1)
        
        incremento_label= ttk.Label(self.frame,  text='Incremento:',font = ("Castellar",8)).grid(column=0,row=2,padx=10,pady=10)
        incremento_input = ttk.Entry(self.frame, width=20)
        incremento_input.grid(column=1,row=2)
        
        modulo_label= ttk.Label(self.frame,  text='Modulo:',font = ("Castellar",8)).grid(column=0,row=3,padx=10,pady=10)
        modulo_input = ttk.Entry(self.frame, width=20)
        modulo_input.grid(column=1,row=3)
        
        total_label= ttk.Label(self.frame,  text='Total de Números a Generar:',font = ("Castellar",8)).grid(column=0,row=4,padx=10,pady=10)
        total_input = ttk.Entry(self.frame, width=20)
        total_input.grid(column=1,row=4) 
        
        sumbit_btn= tk.Button(self.frame, 
                              text="Generar",
                              font = ("Castellar",8),  
                              command = lambda: self.aux_congruencial_frame(semilla_input,multiplicador_input,incremento_input,modulo_input,total_input) ).place(relx=0.4, rely=1.1)
    
    def aux_congruencial_frame(self,semilla,multiplicador,incremento,modulo,total):
        x1 = int(semilla.get())
        x2=int(multiplicador.get())  
        x3=int(incremento.get())  
        x4=int(modulo.get())
        x5=int(total.get()) 
        titulo="Congurencial Lineal"
        self.congruencial(x1,x2,x3,x4,x5,titulo)
    
    def congruencial_mixto_frame(self, *args):

        self.frame['text']="Método Congruencial Mixto"
        
        for widget in self.frame.winfo_children():
            widget.destroy()

        
        semilla_label= ttk.Label(self.frame,  text='Semilla:',font = ("Castellar",8)).grid(column=0,row=0,padx=10,pady=10)
        semilla_input = ttk.Entry(self.frame, width=20)
        semilla_input.grid(column=1,row=0)
        
        multiplicador_label= ttk.Label(self.frame,  text='Multiplicador:',font = ("Castellar",8)).grid(column=0,row=1,padx=10,pady=10)
        multiplicador_input = ttk.Entry(self.frame, width=20)
        multiplicador_input.grid(column=1,row=1)
        
        incremento_label= ttk.Label(self.frame,  text='Incremento:',font = ("Castellar",8)).grid(column=0,row=2,padx=10,pady=10)
        incremento_input = ttk.Entry(self.frame, width=20)
        incremento_input.grid(column=1,row=2)
        
        modulo_label= ttk.Label(self.frame,  text='Modulo:',font = ("Castellar",8)).grid(column=0,row=3,padx=10,pady=10)
        modulo_input = ttk.Entry(self.frame, width=20)
        modulo_input.grid(column=1,row=3)
        
        total_label= ttk.Label(self.frame,  text='Total de Números a Generar:',font = ("Castellar",8)).grid(column=0,row=4,padx=10,pady=10)
        total_input = ttk.Entry(self.frame, width=20)
        total_input.grid(column=1,row=4) 
        
        sumbit_btn= tk.Button(self.frame, 
                              text="Generar",
                              font = ("Castellar",8),  
                              command = lambda: self.aux_congruencial_mixto_frame(semilla_input,multiplicador_input,incremento_input,modulo_input,total_input) ).place(relx=0.4, rely=1.1)
    
    def aux_congruencial_mixto_frame(self,semilla,multiplicador,incremento,modulo,total):
        x1 = int(semilla.get())
        x2=int(multiplicador.get())  
        x3=int(incremento.get())  
        x4=int(modulo.get())
        x5=int(total.get()) 
        self.congruencialMixto(x1,x2,x3,x4,x5)
        
    def multiplicativo_frame(self, *args):

        self.frame['text']="Generador Multiplicativo"
        for widget in self.frame.winfo_children():
            widget.destroy()
            
        semilla_label= ttk.Label(self.frame,  text='Semilla:',font = ("Castellar",8)).grid(column=0,row=0,padx=10,pady=10)
        semilla_input = ttk.Entry(self.frame, width=20)
        semilla_input.grid(column=1,row=0)
        
        multiplicador_label= ttk.Label(self.frame,  text='Multiplicador:',font = ("Castellar",8)).grid(column=0,row=1,padx=10,pady=10)
        multiplicador_input = ttk.Entry(self.frame, width=20)
        multiplicador_input.grid(column=1,row=1)
        
        modulo_label= ttk.Label(self.frame,  text='Modulo:',font = ("Castellar",8)).grid(column=0,row=2,padx=10,pady=10)
        modulo_input = ttk.Entry(self.frame, width=20)
        modulo_input.grid(column=1,row=2)
        
        total_label= ttk.Label(self.frame,  text='Total de Números a Generar:',font = ("Castellar",8)).grid(column=0,row=3,padx=10,pady=10)
        total_input = ttk.Entry(self.frame, width=20)  
        total_input.grid(column=1,row=3)  
        
        sumbit_btn= tk.Button(self.frame, 
                              text="Generar",
                              font = ("Castellar",8),  
                              command = lambda: self.aux_multiplicativo_frame(semilla_input,multiplicador_input,modulo_input,total_input) ).place(relx=0.4, rely=1.1)
        
    def aux_multiplicativo_frame(self,semilla,multiplicador,modulo,total):
        x1 = int(semilla.get())
        x2=int(multiplicador.get())  
        x3=int(modulo.get())
        x4=int(total.get()) 
        self.generadorMultiplicativo(x1,x2,x3,x4)
        
    def congruencial_lineal_combinado_frame(self, *args):

        self.frame['text']="Método Congruencial Lineal Combinado"
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        
        disclaimer = ttk.Label(self.frame,  text='Introduce tus valores con el siguiente formato: 456, 7891, 7831, ...',font = ("Castellar",8)).grid(column=0,row=0,padx=10,pady=10)
        
        
        semilla_label= ttk.Label(self.frame,  text='Semilla:',font = ("Castellar",8)).grid(column=0,row=1,padx=10,pady=10)
        semilla_input = ttk.Entry(self.frame, width=20)
        semilla_input.grid(column=1,row=1)
        
        multiplicador_label= ttk.Label(self.frame,  text='Multiplicador:',font = ("Castellar",8)).grid(column=0,row=2,padx=10,pady=10)
        multiplicador_input = ttk.Entry(self.frame, width=20)
        multiplicador_input.grid(column=1,row=2)
        
        modulo_label= ttk.Label(self.frame,  text='Modulo:',font = ("Castellar",8)).grid(column=0,row=3,padx=10,pady=10)
        modulo_input = ttk.Entry(self.frame, width=20)
        modulo_input.grid(column=1,row=3)
        
        total_label= ttk.Label(self.frame,  text='Total de Números a Generar:',font = ("Castellar",8)).grid(column=0,row=4,padx=10,pady=10)
        total_input = ttk.Entry(self.frame, width=20)     
        total_input.grid(column=1,row=4)
        
        sumbit_btn= tk.Button(self.frame, 
                              text="Generar",
                              font = ("Castellar",8),  
                              command = lambda: self.aux_congruencial_lineal_combinado_frame(semilla_input,multiplicador_input,modulo_input,total_input) ).place(relx=0.4, rely=1.1)
        
    def aux_congruencial_lineal_combinado_frame(self,semilla,multiplicador,modulo,total):
        x1 = str(semilla.get())
        x2=str(multiplicador.get())  
        x3=str(modulo.get())
        x4=int(total.get()) 
        self.congruencialLinealCombinado(x1,x2,x3,x4)
    
    def option_changed(self, *args):
        if self.option.get() == self.menu[0]:
            self.cuadrados_frame()
        elif self.option.get() == self.menu[1]:
            self.congruencial_frame()
        elif self.option.get() == self.menu[2]:
            self.congruencial_mixto_frame()
        elif self.option.get() == self.menu[3]:
            self.multiplicativo_frame()
        elif self.option.get() == self.menu[4]:
            self.congruencial_lineal_combinado_frame()        

if __name__ == "__main__":
    app = App()
    app.mainloop()