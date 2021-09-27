import numpy as np
import pandas as pd
import math 

def kolgomorovSmirnov(numeros,nivelSignificancia):
    numeros.sort()
    Ri = numeros 
    N = len(numeros)

    #Caculate 
    i_n = []
    i_n1 = []
    print(Ri)

    for i in range(1, N + 1): #Calcular i / N
        i_n.append(i/N) 
    
    print(i_n)
    
    for i in range(0, N): #Calcular i / N - Ri
        i_n1.append(abs(i_n[i] - Ri[i] ))
        
    print(i_n1)
    
    ar = [Ri[0]]
    for i in range (1, N): #Calcular Ri - ((i-1)/N)
        ar.append(Ri[i] - i_n[i-1])

    print(ar)

    Dplus = max(i_n1)
    Dminus = max(ar)
    Dtotal = max(Dplus, Dminus)

    tabla = [[.9,.1,.975,.99,.995],
            [.684,.776,.842,.9,.929],
            [.565,.636,.708,.689,.829],
            [.493,.565,.624,.689,.829],
            [.477,.509,.563,.627,.669],
            [.41,.468,.619,.577,.617],
            [.381,.436,.483,.538,.576],
            [.359,.41,.454,.507,.542],
            [.339,.387,.43,.48,.513],
            [1.323,.369,.409,.457,.486],
            [1.308,.352,.391,.437,.468],
            [1.295,.338,.375,.419,.449],
            [1.285,.325,.361,.404,.432],
            [1.275,.314,.349,.39,.418],
            [1.266,.304,.338,.377,.404],
            [2.232,.265,.294,.329,.352],
            [2.208,.238,.264,.295,.317],
            [3.19,.218,.242,.27,.29],
            [4.165,.189,.21,.235,.252]]

    datos = np.array(tabla)

    dato = pd.DataFrame(datos,index = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,25,30,40], columns = [0.2,0.1,0.05,0.02,0.01])

    if(nivelSignificancia == 0.2 or nivelSignificancia == 0.1 or nivelSignificancia == 0.05 or nivelSignificancia == 0.02 or nivelSignificancia == 0.01):
      if(N<41):
        valorCritico = dato[nivelSignificancia][N]
        print("Ev valor critico es:", valorCritico)
      elif(nivelSignificancia == 0.2):
        valorCritico = 1.07 / Math.sqrt(N)
        print("Ev valor critico es:", valorCritico)
      elif(nivelSignificancia == 0.1):
        valorCritico = 1.22 / Math.sqrt(N)
        print("Ev valor critico es:", valorCritico)
      elif(nivelSignificancia == 0.05):
        valorCritico = 1.36 / Math.sqrt(N) 
        print("Ev valor critico es:", valorCritico)
      elif(nivelSignificancia == 0.02):
        valorCritico = 1.52 / Math.sqrt(N) 
        print("Ev valor critico es:", valorCritico)
      elif(nivelSignificancia == 0.01):
        valorCritico = 1.63 / Math.sqrt(N)
        print("Ev valor critico es:", valorCritico) 
      else:
        print("No se puede realizar la operacion")  
    else:
      print("Nivel de Significancia Inválido")
      
    

numeros = [0.44,0.81,0.14,0.05,0.93]
nivelSignificancia = 0.05
kolgomorovSmirnov(numeros, nivelSignificancia)