import os
import csv
import numpy
import time
import math
import decimal
from scipy.stats import chi2

errorPercentages = numpy.array([0.995, 0.99, 0.975, 0.95, 0.90, 0.75, 0.5, 0.25, 0.10, 0.05, 0.025, 0.01, 0.005]) #99.5%, 99%, 97.5%, 95%, 90%, 75%, 50%, 25%, 10%, 5%, 2.5%, 1%, 0.5% 
tablaChiCuadrada = numpy.array(range(1,100)).reshape(-1,1)
tablaChiCuadrada = chi2.isf(errorPercentages, tablaChiCuadrada)
indiceErrores = 2

def centrosCuadrados(semillaInicio, numerosAGenerar):
    semilla = int(semillaInicio)
    if len(str(semillaInicio)) == 4 and semilla >= 100 and semilla <= 9999 and type(semillaInicio) == int and type(numerosAGenerar) == int and numerosAGenerar >= 1:
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

        creacionCarpeta("Centros_Cuadrados")
        datos = [semillas, generadores, numerosAleatorios, Ris]
        columnas = ["Semilla", "Generador", "Aletorio", "Ri"]
        carpetaArchivo = "Centros_Cuadrados"
        escrituraCsv(datos, columnas, carpetaArchivo)

    else:
        print("La semilla otorgada no es un numero enetero de 4 digitos decimales o la cantidad de numeros a generar es invalida" + "\n")

def congruencial(semilla, multiplicador, incremento, modulo, numerosAGenerar, linealOMixto, chiCuadrada, kolmogorovSmirnov):
    if modulo > 0 and modulo > multiplicador and multiplicador > 0 and modulo > incremento and (incremento > 0 or incremento == 0) and modulo > semilla and (semilla > 0 or semilla == 0) and numerosAGenerar >= 1 and type(semilla) == int and type(multiplicador) == int and type(incremento) == int and type(modulo) == int and type(numerosAGenerar) == int:
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

        if linealOMixto == 0:
            creacionCarpeta("Congruencial")
            datos = [semillas, generadores, numerosAleatorios, Ris]
            columnas = ["Semilla", "Generador", "Aletorio", "Ri"]
            carpetaArchivo = "Congruencial"
            escrituraCsv(datos, columnas, carpetaArchivo)
        else:
            creacionCarpeta("Congruencial_Mixto")
            datos = [semillas, generadores, numerosAleatorios, Ris]
            columnas = ["Semilla", "Generador", "Aletorio", "Ri"]
            carpetaArchivo = "Congruencial_Mixto"
            escrituraCsv(datos, columnas, carpetaArchivo)

        if chiCuadrada == 1:
            validacionChiCuadrada(Ris, indiceErrores)
        if kolmogorovSmirnov == 1: 
            kolgomorovSmirnov(Ris)

    else:
        print("El modulo tiene que ser mayor a los demas valores; el multiplicador, incremento y semilla deben ser mayores a Cero; los valores presentados no son validos")

def congruencialMixto(semilla, multiplicador, incremento, modulo, numerosAGenerar, chiCuadrada, kolmogorovSmirnov):
    if hullDobell(multiplicador, incremento, modulo):
        congruencial(semilla, multiplicador, incremento, modulo, numerosAGenerar, 1, chiCuadrada, kolmogorovSmirnov)
    else:
        print("Los parametros no logran cumplir la evaluacion de Hull-Dobell")

def hullDobell(multiplicador, incremento, modulo): # a es el multiplicador, c es el incremento
    verificadorDivisor = 2
    while verificadorDivisor <= modulo:
        if incremento % verificadorDivisor != 0 or modulo % verificadorDivisor != 0:
            verificadorDivisor += 1
        else:
            return False
            
    numerosPrimosDivisores = []
    for numero in range(2, modulo):
        if modulo % numero == 0 and numeroPrimo(numero) == True:
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

def numeroPrimo(numero):
    if numero == 2: return True
    for num in range(2, numero):
        if numero % num == 0: 
            return False
    return True

def generadorMultiplicativo(semilla, multiplicador, modulo, numerosAGenerar, chiCuadrada, kolmogorovSmirnov):
    if (semilla == 0 or semilla > 0) and (multiplicador == 0 or multiplicador > 0) and (modulo == 0 or modulo > 0) and modulo > multiplicador and modulo > semilla and float(semilla).is_integer() and float(multiplicador).is_integer() and float(modulo).is_integer() and numerosAGenerar >= 1 and type(numerosAGenerar) == int:
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

        creacionCarpeta("Generador_Multiplicativo")
        datos = [semillas, generadores, numerosAleatorios, Ris]
        columnas = ["Semilla", "Generador", "Aletorio", "Ri"]
        carpetaArchivo = "Generador_Multiplicativo"
        escrituraCsv(datos, columnas, carpetaArchivo)

        if chiCuadrada == 1:
            validacionChiCuadrada(Ris, indiceErrores)
        if kolmogorovSmirnov == 1: 
            kolgomorovSmirnov(Ris)

    else:
        print("Los parametros introducidos por el usuario no cumplen las espeficaciones para este generador")     

def congruencialLinealCombinado(semillasOriginales, multiplicadores, modulos, numerosAGenerar):
    if(separacionValores(semillasOriginales) != False and separacionValores(multiplicadores) != False and separacionValores(modulos) != False and numerosAGenerar >= 1 and type(numerosAGenerar) == int): 
        semillas = separacionValores(semillasOriginales)
        multiplicadores = separacionValores(multiplicadores)
        modulos = separacionValores(modulos)

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

        creacionCarpeta("Lineal_Combinado")
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
        escrituraCsv(datos, columnas, carpetaArchivo)

    else:
        print("No se puede llevar acabo el el metodo ya que los parametros no cumplen con las especificaciones")

def separacionValores(listaValores):
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

def validacionChiCuadrada(numeros, porcentajeError):
    numeros.sort()
    numeroMenor = numeros[0]
    numeroMayor = numeros[len(numeros) - 1]
    rango = numeroMayor - numeroMenor
    k = math.floor(1 + (3.322 * math.log10(len(numeros))))
    sizeClase = round(rango / k, 5)
    
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
    
    limitesClases = reasignacionClases(limitesClases, frecuenciasAbsolutas)[0]
    frecuenciasAbsolutas = reasignacionClases(limitesClases, frecuenciasAbsolutas)[1]

    probabilidades = []
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
    
    print(k)
    print(limitesClases)
    print(frecuenciasAbsolutas)
    print(probabilidades)
    print(frecuenciasEsperadas)
    print(elementosEstadisticoPrueba)
    estadisticoPrueba = round(sum(elementosEstadisticoPrueba), 5)
    print(estadisticoPrueba)
    gradosLibertad = (k - 1) 
    estadisticoChiCuadrada = round(tablaChiCuadrada[(gradosLibertad-1),porcentajeError], 5)
    print(estadisticoChiCuadrada)

def reasignacionClases(limitesClases, frecuenciasAbsolutas):
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

def kolgomorovSmirnov(numeros):
    print("Hola")

def creacionCarpeta(nombreCarpeta):
    pathActual = os.getcwd()
    pathActual = pathActual.replace("\\", "/")
    pathCarpeta = pathActual + "/" + nombreCarpeta + "/"
    if os.path.exists(pathCarpeta):
        pass
    else:
        os.mkdir(pathCarpeta)

def escrituraCsv(datos, columnas, carpetaArchivo):
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


#centrosCuadrados("9575", 200)
#congruencial(4,5,7,8,8,0)
#congruencialMixto(4,8121,28411,134456,8)
#generadorMultiplicativo(15,35,64,25)
#congruencialLinealCombinado("15985,33652", "40014,40692", "2147493563,2147483399", 20)

#print(hullDobell(5,7,8))
#print(hullDobell(75,74,65537))
#print(hullDobell(8121,28411,134456))
#print(separacionValores("45678,3939, 20920, 292029282, 212,21292"))
#creacionCarpeta("Centros_Cuadrados")
#escrituraCsv([[4,5,6,7], [4,5,6,7],[4,5,6,7], [4,5,6,7]], ["Semilla", "Generador", "Aletorio", "Ri"], "Centros_Cuadrados")
prueba = [8.223, 0.836, 2.634, 4.778, 0.406, 0.517, 2.33, 2.563, 0.511, 6.426, 2.23, 3.81, 1.624, 1.507, 2.343, 1.458, 0.774, 0.023, 0.225, 3.214, 2.92, 0.968, 0.333, 4.025, 0.538, 0.234, 3.323, 3.334, 2.325, 7.514, 0.761, 4.49, 1.594, 1.064, 5.088, 1.401, 0.294, 3.491, 2.921, 0.334, 1.064, 0.186, 2.782, 3.246, 5.587, 0.685, 1.725, 1.267, 1.702, 1.849]
for indice in range(0, len(prueba)):
    prueba[indice] = prueba[indice] / 10
#validacionChiCuadrada(prueba, 9)