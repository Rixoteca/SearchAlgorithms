import copy
import math
import random
import sys
import time
import threading
from interfaz2caminos import Tablero
sys.setrecursionlimit(10000)

def CalcularDistancia(actual):
    x1 = actual[0]
    y1 = actual[1]
    x2 = objetivo[0]
    y2 = objetivo[1]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def GoalTest(EA):
    return EA == objetivo

def B_A_Estrella(Frontera, visitados):
    if not Frontera:
        print("No se encontró solucion")
        return 
    EA = Frontera.pop(0)
    if GoalTest(EA[0]):
        print("Se encontró solución")
        print(EA[1])
        print("Costo de la solución: ", EA[3])
        print("--- %s seconds ---" % (time.time() - start_time))
        
        return EA[1] 
    else:
        OS = Expand(EA, visitados)
        OS = Evaluar(OS)
        OS.sort(key= lambda x: x[3])
        Frontera = Frontera + OS
    return B_A_Estrella(Frontera,visitados)

def Evaluar(OS):
    for i in OS:
        hx = CalcularDistancia(i[0])
        gx = i[2]
        fx = hx + gx
        i[3] = fx
    return OS

movs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def Expand(EA,visitados):
    V = []
    if EA[0] not in visitados:
        aux = EA[1] + [copy.deepcopy(EA[0])]
        visitados.append(EA[0])
        for addx, addy in movs:
            x = EA[0][0] + addx 
            y = EA[0][1] + addy
            if 0 <= x < len(tablero) and 0 <= y < len(tablero[0]) and tablero[x][y] != 1 and (x,y) not in visitados:
                V.append([(x, y), aux, EA[2] + 1, 0])
    return V

ancho_tablero = 47
largo_tablero = 47
porcentaje_bloqueo = 25
tablero = [[0] * ancho_tablero for i in range (largo_tablero)]
bloqueos = int (ancho_tablero * largo_tablero * porcentaje_bloqueo / 100)
bloqueados = []


objetivo = (24, 24)
inicio1 = (0, 0)
inicio2 = (44, 44)
inicio3 = (0, 44)
inicio4 = (44, 0)
visitados = []
for k in range(bloqueos):
    i = random.randint(0, largo_tablero - 1)  
    j = random.randint(0, ancho_tablero - 1)  
    while tablero[i][j] == 1: 
        if (i == objetivo[0] and j == objetivo[1]) or (i == inicio1[0] and j == inicio1[1]) or (i == inicio2[0] and j == inicio2[1]):
            continue
        else:
            i = random.randint(0, largo_tablero-1)
            j = random.randint(0, ancho_tablero-1)
    tablero[i][j] = 1
    bloqueados.append((i,j))
start_time = time.time()
tablero_gui = Tablero(ancho_tablero, largo_tablero, 15, 15)

ruta_hilo_1 = []
ruta_hilo_2 = []
ruta_hilo_3 = []
ruta_hilo_4 = []
def hilo_1():
    global ruta_hilo_1
    visitados = []
    ruta_hilo_1 = B_A_Estrella([[inicio1, [], 0, 0]],visitados)

def hilo_2():
    global ruta_hilo_2
    visitados = []
    ruta_hilo_2 = B_A_Estrella([[inicio2, [], 0, 0]], visitados)

def hilo_3():
    global ruta_hilo_3
    visitados = []
    ruta_hilo_3 = B_A_Estrella([[inicio3, [], 0, 0]], visitados)

def hilo_4():
    global ruta_hilo_4
    visitados = []
    ruta_hilo_4 = B_A_Estrella([[inicio4, [], 0, 0]], visitados)

h1 = threading.Thread(target = hilo_1)
h2 = threading.Thread(target = hilo_2)
h3 = threading.Thread(target = hilo_3)
h4 = threading.Thread(target = hilo_4)

h1.start()
h2.start()
h3.start()
h4.start()

h1.join()
h2.join()
h3.join()
h4.join()

tablero_gui.dibujar(bloqueados, ruta_hilo_1, ruta_hilo_2, ruta_hilo_3, ruta_hilo_4, [objetivo])