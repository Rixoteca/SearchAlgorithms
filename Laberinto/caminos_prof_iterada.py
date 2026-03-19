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
        return False
    EA = Frontera.pop(0)
    print(EA)
    nv_act=EA[2]
    if GoalTest(EA[0]):
        print(EA[1])
        print("Nivel de la solución: ", nv_act)
        print("--- %s seconds ---" % (time.time() - start_time))
        tablero_gui.dibujar(bloqueados,visitados,[objetivo])
        return True
    elif nv_act<limite:
        OS = Expand(EA,nv_act)
        Frontera = OS + Frontera
    else:
        print("No se encontró solución en el limite")
        return False
    return B_Profundo_Lim(Frontera,limite)
movs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def Expand(EA,nv_act):
    V = []
    nv_act=nv_act+1
    if EA[0] not in visitados:
        aux=EA[1]+[copy.deepcopy(EA[0])]
        visitados.append(EA[0])
        print("Visitados", visitados)
        for addx, addy in movs:
            print("Posicion actual: ",EA[0])
            x= EA[0][0] + addx 
            y= EA[0][1] + addy
            print("x,y: ",x, y)
            if 0 <= x < len(tablero) and 0 <= y < len(tablero[0]) and tablero[x][y] != 1 and (x,y) not in visitados:
                V.append([(x,y),aux,nv_act])
    return V
def B_Profundo_It(F1):
    limite = 2
    sol = False
    while(sol is not True):
       F=copy.deepcopy(F1)
       visitados.clear()
       sol = B_Profundo_Lim(F, limite)
       print(sol)
       limite += 2
       print("EEEEEEEEEEEEEE", limite)
ancho_tablero=15
largo_tablero=15
porcentaje_bloqueo=40
tablero = [[0]*ancho_tablero for i in range (largo_tablero)]
bloqueos = int (ancho_tablero * largo_tablero * porcentaje_bloqueo / 100)
bloqueados = []
objetivo = (10,10)
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
visitados = []
start_time = time.time()
tablero_gui = Tablero(ancho_tablero,largo_tablero,15,15)
B_Profundo_It([[inicio, [], 0]])