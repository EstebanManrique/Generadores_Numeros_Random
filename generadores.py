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
    if modulo > 0 and modulo > multiplicador and multiplicador > 0 and modulo > incremento and incremento > 0 and modulo > semilla and semilla > 0:
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

def congruencialMixto():
    print("Hola")

def hullDobell():
    print("Hola")

def generadorMultiplicativo():
    print("Hola")

def congruencialLinealCombinado():
    print("Hola")

def validacionChiCuadrada():
    print("Hola")

def kolgomorovSmirnov():
    print("Hola")


#centrosCuadrados("7589", 10)
congruencial(4,5,7,8,5)