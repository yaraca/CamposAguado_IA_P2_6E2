#Algoritmos de Búsqueda Local
#son métodos que exploran el espacio de soluciones posibles moviéndose de una solución candidata a otra vecina
#con el objetivo de encontrar una solución que satisfaga un conjunto de condiciones o restricciones.
# no exploran todo el espacio de búsqueda, sino que:
# Comienzan con una solución inicial.
# Iteran haciendo pequeños cambios (vecindad).
# Evalúan la calidad o "costo" de la solución actual.
# Se detienen cuando se cumple una condición o no se puede mejorar más.
#Se utilizan especialmente para resolver problemas SAT (Satisfacibilidad proposicional) cuando hay muchas variables y combinaciones posibles.
#El objetivo es asignar valores booleanos (True o False) a las variables de forma que todas las cláusulas de una fórmula en FNC (Forma Normal Conjuntiva) se cumplan.
#Aplicacinoes: optimización, planificación, diseño de circuitos, etc.

#Ejemplo de algorimos de busqueda local 
#Algoritmo GSAT (Greedy SAT) #SAT es un tipo de problema que consiste en determinar si existe una asignación de valores booleanos a un conjunto de variables que haga verdadera una expresión booleana.

#librerías necesarias
import random #para generar asignaciones aleatorias

# Fórmula en FNC (cada cláusula es una lista de literales)
formula = [
    [1, -2],   # p ∨ ¬q
    [-1, 3],   # ¬p ∨ r
    [2, 3]     # q ∨ r
]

variables = [1, 2, 3] #variables de la formula
# 1 = p, 2 = q, 3 = r

#Función para contar cláusulas satisfechas
#Cuenta cuántas cláusulas se cumplen con la asignación actual.
def contar_clausulas_satisfechas(formula, asignacion):
    contador = 0 #inicializa el contador
    for clausula in formula: #recorre cada clausula de la formula
        if any((literal > 0 and asignacion[abs(literal)]) or  #literal positivo y asignación True
               (literal < 0 and not asignacion[abs(literal)])  #literal negativo y asignación False
               for literal in clausula):  #recorre cada literal de la clausula
            contador += 1 #incrementa el contador si la clausula se cumple
    return contador #devuelve el contador

#Función GSAT para encontrar una solución
def gsat(formula, variables, max_intentos=100, max_cambios=50): #máximo de intentos y cambios
    for intento in range(max_intentos): #intenta varias veces
        # Asignación inicial aleatoria
        asignacion = {var: random.choice([True, False]) for var in variables} 

        for cambio in range(max_cambios): #cambia el valor de las variables
            satisfechas = contar_clausulas_satisfechas(formula, asignacion) #cuenta cuántas cláusulas se cumplen
            if satisfechas == len(formula): #si todas las cláusulas se cumplen
                print(f"¡Solución encontrada en intento {intento}, cambio {cambio}!") 
                return asignacion

            # Buscar la mejor variable para voltear
            mejor_var = None #variable que se va a cambiar
            mejor_puntaje = -1 #puntaje inicial
            for var in variables: #recorre cada variable
                asignacion[var] = not asignacion[var]  # Voltear valor
                puntaje = contar_clausulas_satisfechas(formula, asignacion) #cuenta cuántas cláusulas se cumplen con el cambio
                if puntaje > mejor_puntaje: #si el puntaje es mejor que el anterior
                    mejor_puntaje = puntaje #actualiza el puntaje
                    mejor_var = var #actualiza la mejor variable
                asignacion[var] = not asignacion[var]  # Revertir

            if mejor_var is not None: #si hay una mejor variable
                asignacion[mejor_var] = not asignacion[mejor_var]  # Aplicar mejor cambio

    print("No se encontró solución.")
    return None

# Ejecutar GSAT
solucion = gsat(formula, variables)

# Mostrar resultado
if solucion: #si hay una solución
    for var in variables: #recorre cada variable
        print(f"{chr(96 + var).upper()} = {solucion[var]}") #p = True, q = False, r = True

#Ejemplo de salida:
# ¡Solución encontrada en intento 0, cambio 1!
# A = True
# B = True
# C = True
#Como podemos ver, el algoritmo GSAT encontró una solución satisfactoria para la fórmula dada.
#En este caso, la asignación de valores a las variables es:
#p = True, q = True, r = True.
#Esto significa que la fórmula original se cumple con esta asignación de valores.