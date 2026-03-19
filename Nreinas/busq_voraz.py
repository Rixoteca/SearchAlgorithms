import time
import sys
import random
from tableroreinas import ChessboardGUI
sys.setrecursionlimit(10000)

def CalcularAtaques(lista):
    length = len(lista)
    Ataques = 0
    for i in range(length - 1):
        for j in range(i + 1, length):
            if (lista[i] == lista[j]):
                Ataques += 2
            elif ((abs(i - j) - abs(lista[i] - lista[j])) == 0):
                Ataques += 2
    return Ataques

def GoalTest(lista):
    Numero_Ataques = CalcularAtaques(lista)
    if (Numero_Ataques == 0):
        return True
    else:
        return False

def Expand(V):
    copia = V.copy()
    arregloBi = []
    reina_n = len(V)
    lista_negra.append(V)
    for j in range(0, reina_n):
        for x in range(0, reina_n):
            var = V[x] + j
            if var >= reina_n:
                V[x] = var - reina_n
                V not in lista_negra and arregloBi.append(V.copy())
                V = copia.copy()
                continue
            V[x] = var
            V not in lista_negra and arregloBi.append(V.copy())
            V = copia.copy()
    return arregloBi

def Evaluar(OS):
    lista = []
    for i in OS:
        Naataques = CalcularAtaques(i)
        lista.append([i, Naataques])
    return lista

def PrimerElemento(F):
    repetidos = 0
    menor = F[0][1]
    for x in range(len(F) - 1):
        if (menor == F[x + 1][1]):
            repetidos = repetidos + 1
        else:
            break
    return F[random.randint(0, repetidos)][0]

def voraz(F):
    if not F:
        print("No hay solucion")
        return  
    EA = F.pop(0)
    if (GoalTest(EA)):
        print(EA, " es solución")
        print("--- %s seconds ---" % (time.time() - start_time))
        gui = ChessboardGUI(len(EA), [EA])
        return
    else:
        OS = Expand(EA)
        OS = Evaluar(OS)
        OS.sort(key = lambda x: x[1])
        F = [PrimerElemento(OS)]
        voraz(F)

lista_negra = []
F = [[]]
for k in range(50):
    F[0].append(0)

start_time = time.time()
voraz(F)