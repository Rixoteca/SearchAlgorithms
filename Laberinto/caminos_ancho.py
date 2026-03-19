import copy
import random
import time
from interfazcaminos import Tablero

def GoalTest(EA):
    return EA==objetivo

def B_Ancho(Frontera):
    if not Frontera:
        print("No se encontró solucion")
        tablero_gui.dibujar(bloqueados,visitados,[objetivo])
        return
    EA = Frontera.pop(0)
    if GoalTest(EA[0]):
        print(EA[1])
        print("--- %s seconds ---" % (time.time() - start_time))
        tablero_gui.dibujar(bloqueados,visitados,[objetivo])
        return
    else:
        OS = Expand(EA)
        Frontera += OS
        
    B_Ancho(Frontera)

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

ancho_tablero=10
largo_tablero=10
porcentaje_bloqueo=10
tablero = [[0]*ancho_tablero for i in range (largo_tablero)]
bloqueos = int (ancho_tablero * largo_tablero * porcentaje_bloqueo / 100)
bloqueados = []
objetivo = (6,6)
inicio=(0,0)
for k in range(bloqueos):
    i = random.randint(0, largo_tablero-1)  
    j = random.randint(0, ancho_tablero-1)  
    while tablero[i][j] == 1: 
        if i==objetivo[0] and j==objetivo[1]:
            continue
        elif (i==inicio[0] and j==inicio[1]):
            continue
        else:
            i = random.randint(0, largo_tablero-1)
            j = random.randint(0, ancho_tablero-1)
    tablero[i][j] = 1
    bloqueados.append((i,j))
tablero_gui = Tablero(ancho_tablero,largo_tablero,15,15)
visitados = []
start_time = time.time()
B_Ancho([[inicio,[]]])

