#Backtracking
#es una técnica algorítmica de búsqueda sistemática que prueba posibles soluciones a un problema 
# y retrocede si encuentra que la solución actual no es válida o no puede llevar a una solución final.
#Es común en problemas que requieren exploración de combinaciones, como:
# Problemas de satisfacibilidad lógica. (como SAT que es el problema de satisfacibilidad booleana).
# Satisfacción de restricciones (como Sudoku o N-reinas).
# Búsqueda de soluciones en árboles de decisión o grafos.

#Ejemplo de Backtracking
#Librerías necesarias
from itertools import product # Para generar combinaciones de verdad

#Fórmula lógica en forma de cláusulas (FNC)
#Cada cláusula es una lista de literales, donde ¬p se escribe como -p
#Por ejemplo: (p ∨ ¬q) se escribe como [1, -2]
formula = [
    [1, -2],   # p ∨ ¬q
    [-1, 3],   # ¬p ∨ r
    [2, 3]     # q ∨ r
]

#Variables proposicionales: 1 → p, 2 → q, 3 → r
variables = [1, 2, 3] # Asignación de variables a letras (opcional para mostrar resultados)

#Funcion para verificar si una fórmula es satisfacible
def es_satisfacible(formula, asignacion):
    for clausula in formula: # Iterar sobre cada cláusula
        if not any((literal > 0 and asignacion[abs(literal)]) or  #si el literal es positivo y está asignado a True
                   (literal < 0 and not asignacion[abs(literal)])  #si el literal es negativo y está asignado a False
                   for literal in clausula): # Evaluar la cláusula
            return False  # La cláusula no se cumple
    return True  # Todas las cláusulas se cumplen

# Función de backtracking para SAT
def backtracking_sat(formula, variables):
    # Generar todas las combinaciones posibles de verdad (True/False) para las variables
    for valores in product([False, True], repeat=len(variables)): # Combinaciones de verdad
        asignacion = dict(zip(variables, valores)) # Crear diccionario de asignación
        print(f"Probando asignación: {asignacion}") # Mostrar asignación actual
        if es_satisfacible(formula, asignacion): # Verificar si es satisfacible
            print("¡Solución encontrada!")
            return asignacion #retornar la asignación satisfactoria
    print("No hay solución satisfactoria.") #mostrar mensaje si no hay solución
    return None

# Ejecutar el backtracking
solucion = backtracking_sat(formula, variables)

# Mostrar resultado
if solucion:
    for var in variables: #mostrar la asignación satisfactoria
        print(f"{chr(96 + var).upper()} = {solucion[var]}") 

#ejemplo de salida: 
# Probando asignación: {1: False, 2: False, 3: False}
# Probando asignación: {1: False, 2: False, 3: True}
# ¡Solución encontrada!
# A = False
# B = False
# C = True
#Como se puede ver, la asignación de verdad {1: False, 2: False, 3: True} satisface la fórmula.
#Esto significa que la fórmula es satisfacible y se encontró una solución.
#En este caso, la asignación de verdad es:
#p = False, q = False, r = True. 
