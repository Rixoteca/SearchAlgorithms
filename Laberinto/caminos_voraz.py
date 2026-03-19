import copy
import math
import random
import time
from interfazcaminos import Tablero

def CalcularDistancia(actual):
    x1=actual[0]
    y1=actual[1]
    x2=objetivo[0]
    y2=objetivo[1]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def GoalTest(EA):
    return EA==objetivo

def B_Voraz(Frontera):
    if not Frontera:
        print("No se encontró solucion")
        tablero_gui.dibujar(bloqueados,visitados,[objetivo])
        return
    EA = Frontera.pop(0)
    if GoalTest(EA[0]):
        visitados.append(EA[0])
        print(visitados)
        print("--- %s seconds ---" % (time.time() - start_time))
        tablero_gui.dibujar(bloqueados,visitados,[objetivo])
        return
    else:
        OS = Expand(EA)
        OS = Evaluar(OS)
        OS.sort(key= lambda x: x[2])
        Frontera= PrimerElemento(OS)
    B_Voraz(Frontera)

def Evaluar(OS):
    for i in OS:
        distancia=CalcularDistancia(i[0])
        i.append(distancia)
    return OS

def PrimerElemento(F):
    repetidos = 0
    if not F:
        return
    menor = F[0][2]
    for x in range(len(F)-1):
        if (menor == F[x + 1][2]):
            repetidos = repetidos + 1
        else:
            break
    return [F[random.randint(0, repetidos)]]

movs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def Expand(EA):
    V = []
    if EA[0] not in visitados:
        aux=EA[1]+[copy.deepcopy(EA[0])]
        visitados.append(EA[0])
        for addx, addy in movs:
            x= EA[0][0] + addx 
            y= EA[0][1] + addy
            if 0 <= x < len(tablero) and 0 <= y < len(tablero[0]) and tablero[x][y] != 1 and (x,y) not in visitados:
                V.append([(x,y),aux])           
    return V

ancho_tablero=50
largo_tablero=50
porcentaje_bloqueo=10
tablero = [[0]*ancho_tablero for i in range (largo_tablero)]
bloqueos = int (ancho_tablero * largo_tablero * porcentaje_bloqueo / 100)
bloqueados = []
objetivo = (35,40)
inicio=(0,0)
visitados = []
for k in range(bloqueos):
    i = random.randint(0, largo_tablero-1)  
    j = random.randint(0, ancho_tablero-1)  
    while tablero[i][j] == 1: 
        if (i==objetivo[0] and j==objetivo[1]) or (i==inicio[0] and j==inicio[1]):
            continue
        else:
            i = random.randint(0, largo_tablero-1)
            j = random.randint(0, ancho_tablero-1)
    tablero[i][j] = 1
    bloqueados.append((i,j))
start_time = time.time()
tablero_gui = Tablero(ancho_tablero,largo_tablero,15,15)
B_Voraz([[inicio,[]]])
