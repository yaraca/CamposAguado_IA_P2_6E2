#Búsqueda Local: Mínimos-Conflictos
#este algoritmo es una técnica de busqueda local para problemas de satisfacción de restricciones (CSP) que busca minimizar los conflictos en la asignación de variables.
#en lugar de construir una solucion desde cero, comienza con una asignacion completa y la mejora iterativamente reduciendo los conflictos.
#no requiere d ememoria adicional como el backtracking y es útil en problemas como el coloreo de grafos, sudoku, asignacion de horarios, entre otros.

#Impleentacion de minimos conflictos para N-Reinas
#N-Reinas es un problema clásico de CSP donde se deben colocar N reinas en un tablero de ajedrez de N x N de manera que no se ataquen entre sí.
#esto significa que no pueden estar en la misma fila, columna o diagonal.

#Librerias necesarias
import random

#Funcion de minimos_conflictos: implementacion del algoritmo de minimos conflictos para el problema de N-Reinas
#parametros: n = tamaño del tablero (n x n), max_iter = maximo numero de iteraciones
def minimos_conflictos(n, max_iter=1000):
    #inicializar aleatoriamente la asignacion de reinas en el tablero
    asignacion = {col: random.randint(0, n-1) for col in range(n)}
    
    for _ in range(max_iter): #verificar si la asignación actual es solución
        conflictos = contar_conflictos_total(asignacion, n) #contar conflictos totales
        if conflictos == 0: #si no hay conflictos, se encontró una solución
            return asignacion
        
        #seleccionar una variable (columna) en conflicto aleatoria
        col = seleccionar_columna_conflicto(asignacion, n)
        
        #encontrar el valor (fila) que minimice conflictos para esa columna
        fila_optima = encontrar_fila_min_conflictos(asignacion, col, n)
        asignacion[col] = fila_optima #asignar la fila óptima a la columna
    return None #si no se encuentra solución en el número máximo de iteraciones

#funcion contar_conflictos_total: cuenta el número total de conflictos en la asignación
def contar_conflictos_total(asignacion, n):
    conflictos = 0 #inicializar el contador de conflictos
    for col1 in range(n): #iterar sobre todas las columnas
        for col2 in range(col1 + 1, n): #iterar sobre las columnas restantes
            if en_conflicto(col1, asignacion[col1], col2, asignacion[col2]): #verificar si hay conflicto
                conflictos += 1 #aumentar el contador de conflictos
    return conflictos

#funcion en_conflicto: verifica si dos reinas están en conflicto (misma fila o diagonal)
def en_conflicto(col1, fila1, col2, fila2):
    return fila1 == fila2 or abs(col1 - col2) == abs(fila1 - fila2) #verifica si las reinas están en la misma fila o diagonal

#funcion seleccionar_columna_conflicto: selecciona aleatoriamente una columna con al menos un conflicto
def seleccionar_columna_conflicto(asignacion, n):
    columnas_conflicto = [col for col in range(n) if contar_conflictos_columna(asignacion, col, n) > 0] #filtrar columnas con conflictos
    return random.choice(columnas_conflicto) ##seleccionar aleatoriamente una columna con conflictos

#funcion contar_conflictos_columna: cuenta cuántas reinas están en conflicto con la reina en la columna 'col'
def contar_conflictos_columna(asignacion, col, n):
    return sum(1 for otra_col in range(n) if otra_col != col and 
               en_conflicto(col, asignacion[col], otra_col, asignacion[otra_col])) #contar conflictos con la reina en la columna 'col'

#funcion encontrar_fila_min_conflictos: encuentra la fila que minimiza conflictos para una columna dada
def encontrar_fila_min_conflictos(asignacion, col, n):
    conflictos_por_fila = [] #lista para almacenar el número de conflictos por fila
    for fila in range(n):
        #contar conflictos si se mueve la reina a esta fila
        conflictos = sum(1 for otra_col in range(n) if otra_col != col and 
                         en_conflicto(col, fila, otra_col, asignacion[otra_col])) #contar conflictos con la reina en la fila 'fila'
        conflictos_por_fila.append(conflictos) #agregar el conteo de conflictos por fila
    
    #elegir aleatoriamente entre las filas con mínimo conflicto
    min_conflictos = min(conflictos_por_fila) #encontrar el mínimo número de conflictos
    mejores_filas = [fila for fila, cnt in enumerate(conflictos_por_fila) if cnt == min_conflictos] #filtrar filas con el mínimo número de conflictos
    return random.choice(mejores_filas) #seleccionar aleatoriamente una fila entre las que tienen el mínimo número de conflictos

#Ejemplo de uso del algoritmo de minimos conflictos para el problema de N-Reinas
if __name__ == "__main__":
    n = 8  #tamaño del tablero (8x8)
    solucion = minimos_conflictos(n) #llamar a la funcion de minimos conflictos
    
    if solucion: #si se encontró una solución
        print("Solución encontrada:")
        for col, fila in sorted(solucion.items()): ##imprimir la solución
            print(f"Columna {col}: Fila {fila}")
    else: #si no se encontró solución
        print("No se encontró solución en el número máximo de iteraciones.")

#Ejemplo de salida:
# Solución encontrada:
# Columna 0: Fila 3
# Columna 1: Fila 6
# Columna 2: Fila 0
# Columna 3: Fila 7
# Columna 4: Fila 4
# Columna 5: Fila 1
# Columna 6: Fila 5
# Columna 7: Fila 2