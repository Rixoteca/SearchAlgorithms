"""
Problema N reinas.ipynb
Created by Rixoteca
"""
# Esta funcion es para saber cuantos ataques hay, estas se guardan en la variable ataques
#  y se transfieren a solucion(tablero)
def solucion(tablero):
    n = len(tablero)
    ataques = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Comprueba si hay dos reinas en la misma columna
            if tablero[i] == tablero[j]:
                ataques += 2
            # Comprueba si hay dos reinas en diagonal ascendente o descendente
            if abs(i - j) == abs(tablero[i] - tablero[j]):
                ataques += 2
    # Retorna verdadero si no hay ataques entre reinas
    return ataques
# Se asignan las posiciones de cada reina, la cantidad de datos insertados
# es igual al valor de n
tablero = [3, 1, 4, 2, 5, 6, 8, 7]
# Se verifica si hay ataques y en caso de haber se imprime cuantos hubo
if solucion(tablero) == 0:
    print("No hay ataques")
else:
    print(f"Hay {solucion(tablero)} ataques entre reinas")