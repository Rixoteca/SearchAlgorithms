"""
Problema N reinas Consola.ipynb
Created by Rixoteca
"""
# Se declara n con un valor vacio, para que no intente tomar el  3 como valor inicial
n = 0
# Solicita al usuario el valor de N mayor a 3 en un ciclo, evitando que se asgine un valor invalido
while n <= 3:
    n = int(input("Ingrese el valor de N (mayor que 3): "))
# Se define la cuestion del ataque
def verificacion(tablero):
    ataques = 0
    # El valor maximo de ataques deberia ser = n * (n - 1), en caso de superar ese numero hay error
    n = len(tablero)
    # No puede haber 2 reinas en la misma columna porque solo se puede asignar un valor por posicion
    # Las reinas iniciaran en la posicion 1
    for i in range(n):
        for j in range(i + 1, n):
            # Comprueba si hay dos reinas en la misma fila
            if tablero[i] == tablero[j]:
                ataques += 2
            # Comprueba si hay reinas atacando en diagonal, empezando con la columna en la posicion j
            if abs(i - j) == abs(tablero[i] - tablero[j]):
                ataques += 2
    # Retorna el numero de ataques entre reinas
    return ataques 
# Crea un vector con N posiciones, inicialmente vacío
tablero = [0] * n
# Se crea un ciclo para obtener el valor de cada posicion vertical
for i in range(n):
    posicion_valida = False
    while not posicion_valida:
        posicion = int(input(f"Ingrese la posición de la reina {i} (fila): "))
        # Se comprueba si la posición ya fue utilizada por otra reina
        if n <= posicion :
            print("Posicion invalida")
        else:
            tablero[i] = posicion
            posicion_valida = True
# Se le asigna el valor del tablero a la variable ataques
ataques = verificacion(tablero)
# Se verifica si la solucion es valida y en caso contrario se devuelve el numero de reinas
if verificacion(tablero) == 0:
    print("No hay ataques")
else:
    print(f"Hay {ataques} ataques entre reinas")