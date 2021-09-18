def centrosCuadrados(semillaInicio, numerosAGenerar):
    semilla = int(semillaInicio)
    if len(str(semillaInicio)) == 4 and semilla >= 100 and semilla <= 9999:
        numerosAleatorios = []
        Ris = []
        semillas = []
        generadores = []
        numerosGenerados = 0

        while numerosGenerados < numerosAGenerar:
            semillas.append(semilla)
            semillaCuadrado = semilla * semilla
            if len(str(semillaCuadrado)) < 8:
                complemento = "" 
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

        print(semillas)
        print(generadores)
        print(numerosAleatorios)
        print(Ris)
    else:
        print("La semilla otorgada no es un numero enetero de 4 digitos decimales" + "\n")

def congruencial(semilla, multiplicador, incremento, modulo, numerosAGenerar):
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

        print(semillas)
        print(generadores)
        print(numerosAleatorios)
        print(Ris)

    else:
        print("El modulo tiene que ser mayor a los demas valores; el multiplicador, incremento y semilla deben ser mayores a Cero")

def congruencialMixto(semilla, multiplicador, incremento, modulo, numerosAGenerar):
    if hullDobell(multiplicador, incremento, modulo):
        congruencial(semilla, multiplicador, incremento, modulo, numerosAGenerar)
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

def generadorMultiplicativo(semilla, multiplicador, modulo, numerosAGenerar):
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

        print(semillas)
        print(generadores)
        print(numerosAleatorios)
        print(Ris) 
    else:
        print("Los parametros introducidos por el usuario no cumplen las espeficaciones para este generador")     

def congruencialLinealCombinado(semillasOriginales, multiplicadores, modulos, numerosAGenerar):
    if(separacionValores(semillasOriginales) != False and separacionValores(multiplicadores) != False and separacionValores(modulos) != False): 
        semillas = separacionValores(semillasOriginales)
        multiplicadores = separacionValores(multiplicadores)
        modulos = separacionValores(modulos)

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

        print(numerosAleatorios)

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

def validacionChiCuadrada():
    print("Hola")

def kolgomorovSmirnov():
    print("Hola")

def creacionCarpeta(nombreCarpeta):
    print("Hola")

def escrituraCsv(datos, carpetaArchivo):
    print("Hola")


#centrosCuadrados("7589", 10)
#congruencial(4,5,7,8,5)
#congruencialMixto(4,8121,28411,134456,8)
#generadorMultiplicativo(15,35,64,20)
#congruencialLinealCombinado("15985,33652", "40014,40692", "2147493563,2147483399", 350)

#print(hullDobell(5,7,8))
#print(hullDobell(75,74,65537))
#print(hullDobell(8121,28411,134456))
#print(separacionValores("45678,3939, 20920, 292029282, 212,21292"))