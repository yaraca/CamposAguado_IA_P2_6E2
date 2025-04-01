#Problemas de Sarisfacción de Restricciones (CSP)
#Este algoritmo es un tipo de porblema de inteligencia artificial donde la solucion debe cumplir con un conjunto de variables, dominios y restricciones 
#variables->elementos del problema (ej. colores de un mapa, asignacion de tareas)
#dominios->valores posibles que puede tomar cada variable (ej. colores, tareas)
#restricciones->condiciones que deben cumplirse entre las variables (ej. dos paises no pueden tener el mismo color, una tarea no puede ser asignada a dos personas)
#el objetivo es encontrar una asignacion de valores a las variables que cumpla con todas las restricciones
#se pueden aplicar en mapa de colores, sudoku, horarios, rompecabezas, etc.
#el algoritmo básico es el Backtracking, que consiste en probar diferentes combinaciones de valores para las variables y retroceder cuando se encuentra una restricción no satisfecha

#Implementacion de un problema de satisfaccion de restricciones: Ejemplo Sudoku

#funcion para resolver un sudoku
#parametros: tablero = matriz 9x9 del 1-9 (0 representa una celda vacia)
#retorna: True si el sudoku es valido, False si no es valido
def resolver_sudoku(tablero):
    vacio = encontrar_casilla_vacia(tablero) #buscar una casilla vacia
    if not vacio: #si no hay casillas vacias, el sudoku esta resuelto
        return True
    fila, col = vacio #desempaquetar la tupla

    for num in range(1, 10): #probar numeros del 1 al 9
        if es_valido(tablero, num, (fila, col)): #si el numero es valido
            tablero[fila][col] = num #asignar el numero a la casilla vacia
            if resolver_sudoku(tablero): #llamar a la funcion recursivamente
                return True
            tablero[fila][col] = 0 #deshacer la asignacion si no lleva a la solucion (backtrack)
    return False #si no se encuentra una solucion, retornar False

#funcion para encontrar una casilla vacia en el tablero (representada por un 0)
def encontrar_casilla_vacia(tablero): 
    for i in range (9): #recorrer filas
        for j in range (9): #recorrer columnas
            if tablero[i][j] == 0: #si la casilla es vacia
                return (i,j) #retornar la posicion de la casilla vacia
    return None #si no hay casillas vacias, retornar None

#funcion es_valido: verifica si asignar num en pos cumple con las reglas del sudoku
#parametro: pos = tupla (fila, columna) con la posicion de la casilla
def es_valido(tablero, num, pos): 
    if num in tablero[pos[0]]: #verificar fila
        return False #si el numero ya esta en la fila, retornar False
    if num in [tablero[i][pos[1]] for i in range(9)]: #verificar columna
        return False #si el numero ya esta en la columna, retornar False
    #verificar subcuadro 3x3
    subfila = pos[0] // 3 * 3 #fila del subcuadro
    subcol = pos[1] // 3 * 3 #columna del subcuadro
    for i in range (subfila, subfila + 3): #recorrer filas del subcuadro
        for j in range (subcol, subcol + 3): #recorrer columnas del subcuadro
            if tablero[i][j] == num:  
                return False #si el numero ya esta en el subcuadro, retornar False
    return True #si no se encuentra ninguna restriccion, retornar True

#Ejemplo de problemas de satisfaccion de restricciones (Sudoku)
if __name__ == "__main__": 
    tablero_ejemplo = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if resolver_sudoku(tablero_ejemplo): #si se encuentra una solucion 
        for fila in tablero_ejemplo: #recorrer filas del tablero
            print(fila)
    else: #si no se encuentra una solucion
        print("No hay solucion para el sudoku")

#Ejemplo salida: [5, 3, 4, 6, 7, 8, 9, 1, 2]
#                [6, 7, 2, 1, 9, 5, 3, 4, 8]
#                [1, 9, 8, 3, 4, 2, 5, 6, 7]
#                [8, 5, 9, 7, 6, 1, 4, 2, 3]
#                [4, 2, 6, 8, 5, 3, 7, 9, 1]
#                [7, 1, 3, 9, 2, 4, 8, 5, 6]
#                [9, 6, 1, 5, 3, 7, 2, 8, 4]
#                [2, 8, 7, 4, 1, 9, 6, 3, 5]
#                [3, 4, 5, 2, 8, 6, 1, 7, 9]