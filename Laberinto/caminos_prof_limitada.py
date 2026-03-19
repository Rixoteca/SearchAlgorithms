import copy
import random
import time
from interfazcaminos import Tablero

def GoalTest(EA):
    return EA==objetivo

def B_Profundo_Lim(Frontera,limite):
    if not Frontera:
        print("No se encontró solucion")
        tablero_gui.dibujar(bloqueados,visitados,[objetivo])
        return
    EA = Frontera.pop(0)
    print(EA)
    nv_act=EA[2]
    if GoalTest(EA[0]):
        print(EA[1])
        print("Nivel de la solución: ", nv_act)
        print("--- %s seconds ---" % (time.time() - start_time))
        tablero_gui.dibujar(bloqueados,visitados,[objetivo])
        return
    elif nv_act<limite:
        OS = Expand(EA,nv_act)
        Frontera = OS + Frontera
    else:
        print("No se encontró solución en el limite")
        tablero_gui.dibujar(bloqueados,visitados,[objetivo])
    B_Profundo_Lim(Frontera,limite)

movs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def Expand(EA,nv_act):
    V = []
    nv_act=nv_act+1
    if EA[0] not in visitados:
        aux=EA[1]+[copy.deepcopy(EA[0])]
        visitados.append(EA[0])
        for addx, addy in movs:
            x= EA[0][0] + addx 
            y= EA[0][1] + addy
            if 0 <= x < len(tablero) and 0 <= y < len(tablero[0]) and tablero[x][y] != 1 and (x,y) not in visitados:
                V.append([(x,y),aux,nv_act])
    return V

ancho_tablero=15
largo_tablero=15
porcentaje_bloqueo=10
tablero = [[0]*ancho_tablero for i in range (largo_tablero)]
bloqueos = int (ancho_tablero * largo_tablero * porcentaje_bloqueo / 100)
bloqueados = []
objetivo = (14,14)
inicio=(1,1)
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

visitados = []
start_time = time.time()
tablero_gui = Tablero(ancho_tablero,largo_tablero,15,15)
B_Profundo_Lim([[inicio, [], 0]],29)