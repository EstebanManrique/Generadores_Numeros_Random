
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import os
import csv
import numpy
import time
import math
import decimal


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x450")
        self.title('Generador de Números Aleatorios')

        # initialize data
        self.menu = ("Método de los Centros Cuadrados",
      "Método Congruencial",
      "Método Congruencial Mixto",
      "Generador Multiplicativo",
      "Método Congruencial Lineal Combinado")
        
        self.porcentajes=(
            "99.5%", "99%", "97.5%", "95%", "90%", "75%", "50%", "25%", "10%", "5%", "2.5%", "1%", "0.5%"
            )

        # set up variable
        self.option = tk.StringVar(self)
        
        self.option.set(self.menu[0])
        
        self.option2 = tk.StringVar(self)
        
        self.option2.set(self.porcentajes[0])
        
        self.chi=tk.IntVar()
        self.kov=tk.IntVar()
        
        # create widget
        self.create_wigets()

    def create_wigets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # label
        label = ttk.Label(self,  text='SIMULADOR DE NUMEROS RANDOM',font = ("Castellar",15))
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        self.frame = tk.LabelFrame(self,text="Método de los Centros Cuadrados", borderwidth=8, padx=175, pady=50, labelanchor = "nw", font = ("Castellar",12))
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

    def creacionCarpeta(self,nombreCarpeta):
        pathActual = os.getcwd()
        pathActual = pathActual.replace("\\", "/")
        pathCarpeta = pathActual + "/" + nombreCarpeta + "/"
        if os.path.exists(pathCarpeta):
            pass
        else:
            os.mkdir(pathCarpeta)
    
    def escrituraCsv(self,datos, columnas, carpetaArchivo):
        pathActual = os.getcwd()
        pathActual = pathActual.replace("\\", "/")
        pathActual = pathActual + "/" + carpetaArchivo + "/"
    
        columnas = numpy.array([columnas])
        t = time.localtime()
        nombreArchivo = time.strftime("%H:%M:%S", t)
        nombreArchivo = nombreArchivo.replace(":", "_") 
        nombreArchivo += carpetaArchivo + ".csv"
        nombreArchivo = pathActual + nombreArchivo
    
        with open(nombreArchivo, "w", newline = "") as file:
            escritor = csv.writer(file, delimiter = ",")
            escritor.writerows(columnas)
            for indices in range(0, len(datos[0])):
                renglon = []
                for indice in range(0, len(datos)):
                    renglon.append(datos[indice][indices])
                renglon = numpy.array([renglon])
                escritor.writerows(renglon)


    def reasignacionClases(self,limitesClases, frecuenciasAbsolutas):
            for indice in range(0, len(frecuenciasAbsolutas)):
                if frecuenciasAbsolutas[indice] < 5 and indice < len(frecuenciasAbsolutas) - 1:
                    while frecuenciasAbsolutas[indice] < 5 and indice < len(frecuenciasAbsolutas) - 1:
                        frecuenciasAbsolutas[indice] += frecuenciasAbsolutas[indice + 1]
                        limitesClases[indice][1] = limitesClases[indice + 1][1]
                        frecuenciasAbsolutas.pop(indice + 1)
                        limitesClases.pop(indice + 1)
                if indice >= len(frecuenciasAbsolutas) - 1:
                    break
            return [limitesClases, frecuenciasAbsolutas]    
    
    def chi_frame(self,menor,mayor,claseLongitud,clases,fo,fe,prob,grados,aprob,formula,clasesSinAjuste,feSinAjuste):
        
        chiFrame = tk.Toplevel()
        chiFrame.title("Chi-Cuadrada")
        
        label = tk.Label(chiFrame, text="Rango: ", font=("Arial",17),padx=15, pady=15)
        label.grid(row=0,column=0)
        labelRango = tk.Label(chiFrame, text=(menor+" - "+mayor), font=("Arial",15),padx=15, pady=15)
        labelRango.grid(row=0,column=1)
        
        label2 = tk.Label(chiFrame, text="Clase (Longuitud): ", font=("Arial",17),padx=15, pady=15)
        label2.grid(row=2,column=0)
        labelClase = tk.Label(chiFrame, text=str(claseLongitud), font=("Arial",15),padx=15, pady=15)
        labelClase.grid(row=2,column=1)
        
        label3 = tk.Label(chiFrame, text="K: ", font=("Arial",17),padx=15, pady=15)
        label3.grid(row=1,column=0)
        labelK = tk.Label(chiFrame, text=str(len(clases)), font=("Arial",15),padx=15, pady=15)
        labelK.grid(row=1,column=1)
        
        labelBlank = tk.Label(chiFrame, text="  ", font=("Arial",17),padx=15, pady=15)
        labelBlank.grid(row=3,column=0)
        
        labelTable = tk.Label(chiFrame, text="Clases Sin Ajustar", font=("Arial",17),padx=15, pady=15)
        labelTable.place(x=200,y=180)
        
        cols = ('K','Clase', 'FOi observado', 'Probabilidad', 'FEi esperado', '(FO - FE)^2/FE')
        cols2 = ('K','Clase','FOi observado')
        #, '(FO - FE)^2/FE'
        
        clasesStr=[]
        clasesStr2=[]
        
        if(aprob==1):
            color="green"
        else:
            color="red"
        
        for x in range(len(clases)):
            aux=""
            aux=str(clases[x][0])+" - " + str(clases[x][1]) 
            clasesStr.append(aux)
            
        for x in range(len(clasesSinAjuste)):
            aux=""
            aux=str(clasesSinAjuste[x][0])+" - " + str(clasesSinAjuste[x][1]) 
            clasesStr2.append(aux)

        table = ttk.Treeview(chiFrame, columns=cols, show='headings',selectmode='browse')
        
        table2 = ttk.Treeview(chiFrame, columns=cols2, show='headings',selectmode='browse')
       
        for col in cols:
            table.heading(col, text=col,anchor="center") 
            table.column(col, stretch=0, anchor="center")
            
        for col in cols2:
            table2.heading(col, text=col,anchor="center") 
            table2.column(col, stretch=0, anchor="center")
           
        for x in range(len(clases)):
            table.insert("", "end", values=(x,clasesStr[x],fo[x],prob[x],fe[x],formula[x]))
            
        for x in range(len(clasesSinAjuste)):
            table2.insert("", "end", values=(x,clasesStr2[x],feSinAjuste[x]))
            
        table2.grid(row=4, column=0,columnspan=5)
        table.grid(row=5, column=0, columnspan=2)
        
        vsb=ttk.Scrollbar(chiFrame, orient="vertical", command=table.yview)
        vsb.place(relx=0.98, rely=0.58, relheight=0.27, relwidth=0.020)
        table.configure(yscrollcommand=vsb.set)

        vsb2=ttk.Scrollbar(chiFrame, orient="vertical", command=table2.yview)
        vsb2.place(relx=0.73, rely=0.30, relheight=0.268, relwidth=0.020)
        table2.configure(yscrollcommand=vsb2.set)
        
        label4 = tk.Label(chiFrame, text="Grados de Libertdad: ", font=("Arial",17),padx=15, pady=15)
        label4.grid(row=6,column=0)
        labelGrados = tk.Label(chiFrame, text=str(grados), font=("Arial",15),padx=15, pady=15)
        labelGrados.grid(row=6,column=1)
        
        label5 = tk.Label(chiFrame, text="Estadístico Prueba: ", font=("Arial",17),padx=15, pady=15)
        label5.grid(row=7,column=0)
        labelEst = tk.Label(chiFrame, text="3 < 5", font=("Arial",15),padx=15, pady=15,bg=color)
        labelEst.grid(row=7,column=1)
        
    def validacionChiCuadrada(self,numeros,resultados):
        numeros.sort()
        numeroMenor = numeros[0]  #RANGO
        numeroMayor = numeros[len(numeros) - 1]  #RANGO
        rango = numeroMayor - numeroMenor #RANGO
        k = math.floor(1 + (3.322 * math.log10(len(numeros))))
        sizeClase = round(rango / k, 5)  #Clase (Longuitud)
        
        limitesClases = []
        bandera = 0
        while bandera <= numeroMayor:
            limitesClases.append([round(bandera, 5), round(bandera + sizeClase, 5)])
            bandera += sizeClase
        frecuenciasAbsolutas = []
        for intervalo in limitesClases:
            frecuenciasAbsolutas.append(sum(map(lambda x: x >= intervalo[0] and x < intervalo[1], numeros)))
    
        #print(limitesClases)
        #print(frecuenciasAbsolutas)
        clasesSinAjuste=limitesClases
        feSinAjuste=frecuenciasAbsolutas
        
        limitesClases = self.reasignacionClases(limitesClases, frecuenciasAbsolutas)[0] #Columna 2
        frecuenciasAbsolutas = self.reasignacionClases(limitesClases, frecuenciasAbsolutas)[1]
    
        probabilidades = [] #Columna 4
        frecuenciasEsperadas = []
        elementosEstadisticoPrueba = []
        for indice in range(0, len(frecuenciasAbsolutas)):
            if indice != len(frecuenciasAbsolutas) - 1:
                probabilidades.append(1*(limitesClases[indice][1] - limitesClases[indice][0]))
                frecuenciasEsperadas.append(round(len(numeros) * probabilidades[indice], 3))
            else:
                probabilidades.append(1 - sum(probabilidades))
                frecuenciasEsperadas.append(round(len(numeros) - sum(frecuenciasEsperadas), 3))
            elementosEstadisticoPrueba.append(round(math.pow((frecuenciasAbsolutas[indice] - frecuenciasEsperadas[indice]),2) / frecuenciasEsperadas[indice], 5)) 
        
        
        print(frecuenciasAbsolutas) #Columna 3
        print(frecuenciasEsperadas) #Columna 5
        #print(elementosEstadisticoPrueba) #Columna 6
        estadisticoPrueba = round(sum(elementosEstadisticoPrueba), 5)
        print(estadisticoPrueba)
        gradosLibertad = (k - 1) 
        print(gradosLibertad) 

        numeroMenorStr=str(numeroMenor)
        numeroMayorStr=str(numeroMayor)
        condicion=1
        
        label = tk.Label(resultados, text="Chi-Cuadrada", font=("Arial",17)).grid(row=2, column=0)
        if condicion==1:
            label2 = tk.Label(resultados, text=str(gradosLibertad), font=("Arial",17), fg="green")
            label2.grid(row=2, column=1)
            label2.bind("<Button-1>", lambda event, a=numeroMenorStr, b=numeroMayorStr, c=sizeClase, d=limitesClases, 
                        e=frecuenciasAbsolutas, f=frecuenciasEsperadas, g=probabilidades, h=gradosLibertad, i=condicion, j=elementosEstadisticoPrueba,
                        k=clasesSinAjuste, l=feSinAjuste:
                        self.chi_frame(a,b,c,d,e,f,g,h,i,j,k,l) )
        else:
            label2 = tk.Label(resultados, text=str(gradosLibertad), font=("Arial",17), fg="red")
            label2.grid(row=2, column=1)
            label2.bind("<Button-1>", lambda event, a=numeroMenorStr, b=numeroMayorStr, c=sizeClase, d=limitesClases, 
                        e=frecuenciasAbsolutas, f=frecuenciasEsperadas, g=probabilidades, h=gradosLibertad, i=condicion, j=elementosEstadisticoPrueba,
                        k=clasesSinAjuste, l=feSinAjuste: 
                        self.chi_frame(a,b,c,d,e,f,g,h,i,j,k,l) )
        

        

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
        
           self.creacionCarpeta("Centros_Cuadrados")
           datos = [semillas, generadores, numerosAleatorios, Ris]
           columnas = ["Semilla", "Generador", "Aletorio", "Ri"]
           carpetaArchivo = "Centros_Cuadrados"
           self.escrituraCsv(datos, columnas, carpetaArchivo)
           
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
    
            
            if titulo == "Congurencial Lineal":
                self.creacionCarpeta("Congruencial")
                datos = [semillas, generadores, numerosAleatorios, Ris]
                columnas = ["Semilla", "Generador", "Aletorio", "Ri"]
                carpetaArchivo = "Congruencial"
                self.escrituraCsv(datos, columnas, carpetaArchivo)
            else:
                self.creacionCarpeta("Congruencial_Mixto")
                datos = [semillas, generadores, numerosAleatorios, Ris]
                columnas = ["Semilla", "Generador", "Aletorio", "Ri"]
                carpetaArchivo = "Congruencial_Mixto"
                self.escrituraCsv(datos, columnas, carpetaArchivo)
            
            
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
            
            print(self.chi.get())
            
            if self.chi.get() == 1:
                self.validacionChiCuadrada(Ris,results)
                
                
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
            
            self.creacionCarpeta("Generador_Multiplicativo")
            datos = [semillas, generadores, numerosAleatorios, Ris]
            columnas = ["Semilla", "Generador", "Aletorio", "Ri"]
            carpetaArchivo = "Generador_Multiplicativo"
            self.escrituraCsv(datos, columnas, carpetaArchivo)
            
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
            
            if self.chi.get() == 1:
                self.validacionChiCuadrada(Ris,results)
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
        if(self.separacionValores(semillasOriginales) != False and self.separacionValores(multiplicadores) != False and self.separacionValores(modulos) != False): 
            semillas = self.separacionValores(semillasOriginales)
            multiplicadores = self.separacionValores(multiplicadores)
            modulos = self.separacionValores(modulos)
    
            Ris = []
            numerosAleatorios = []
            semillasHistoricas = []
            for semilla in range(0, len(modulos)):
                semillasHistoricas.append([])
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
                for semilla in range(0, len(modulos)):
                    semillasHistoricas[semilla].append(semillas[semilla])
                semillas = numerosTemporales
                numerosTemporales = []
                numerosGenerados += 1
                
            self.creacionCarpeta("Lineal_Combinado")
            datos = []
            for semilla in range(0, len(modulos)):
                datos.append(semillasHistoricas[semilla])
            datos.append(numerosAleatorios)
            datos.append(Ris)
            indice = 1
            columnas = []
            for semilla in range(0, len(modulos)):
                columnas.append("Semilla" + str(indice))
                indice += 1
            columnas.append("Aleatorio")
            columnas.append("Ri")
            carpetaArchivo = "Lineal_Combinado"
            self.escrituraCsv(datos, columnas, carpetaArchivo)
    
            results = tk.Toplevel()
            results.title("Resultados")
            cols = ('Xn','No. Aleatorio')
            label = tk.Label(results, text="Generador Lineal Combinado", font=("Arial",30)).grid(row=0, columnspan=3)
            table = ttk.Treeview(results, columns=columnas, show='headings',selectmode='browse')
           
            for col in columnas:
                table.heading(col, text=col)  
            

            for x in range(len(numerosAleatorios)):
                table.insert("", "end", values=([y[x] for y in datos]) )
               
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
        
        chi_cuadrada=tk.Checkbutton(self.frame, text="Chi-Cuadrada",variable=self.chi)
        chi_cuadrada.place(relx=-0.4, rely=0.0)
        
        kolmogorov=tk.Checkbutton(self.frame, text="Kolmogorov-Smirnov", variable=self.kov)
        kolmogorov.place(relx=-0.4, rely=0.2)
        
        
        porcentaje_Menu = tk.OptionMenu(
            self.frame,
            self.option2,
            *self.porcentajes,
           )
        
        helv36 = tkFont.Font(family='MS Sans Serif', size=10)
        porcentaje_Menu.config(font=helv36)
        porcentaje_Menu.place(relx=-0.4, rely=0.4)
        
        
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
        
        chi_cuadrada=tk.Checkbutton(self.frame, text="Chi-Cuadrada", variable=self.chi)
        chi_cuadrada.place(relx=-0.4, rely=0.0)
        
        kolmogorov=tk.Checkbutton(self.frame, text="Kolmogorov-Smirnov", variable=self.kov)
        kolmogorov.place(relx=-0.4, rely=0.20)
        
        porcentaje_Menu = tk.OptionMenu(
            self.frame,
            self.option2,
            *self.porcentajes,
           )
        
        helv36 = tkFont.Font(family='MS Sans Serif', size=10)
        porcentaje_Menu.config(font=helv36)
        porcentaje_Menu.place(relx=-0.4, rely=0.4)
        
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
        
        chi_cuadrada=tk.Checkbutton(self.frame, text="Chi-Cuadrada", variable=self.chi)
        chi_cuadrada.place(relx=-0.4, rely=0.0)
        
        kolmogorov=tk.Checkbutton(self.frame, text="Kolmogorov-Smirnov", variable=self.kov)
        kolmogorov.place(relx=-0.4, rely=0.2)
        
        porcentaje_Menu = tk.OptionMenu(
            self.frame,
            self.option2,
            *self.porcentajes,
           )
        
        helv36 = tkFont.Font(family='MS Sans Serif', size=10)
        porcentaje_Menu.config(font=helv36)
        porcentaje_Menu.place(relx=-0.4, rely=0.4)
        
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