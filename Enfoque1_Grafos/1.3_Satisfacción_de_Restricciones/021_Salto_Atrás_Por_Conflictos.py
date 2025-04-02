#Salto atrás por conflictos (Conflict-Directed Backjumping -> CBJ)
#Es una técnica avanzada de backtrancking que mejora la eficiencia al identificar el origen de los conflictos y saltar directamente a la variable
#que causo el conlficto, evitando explorar ramas innecesarias del árbol de búsqueda.
#Es útil en problemas de satisfacción de restricciones (CSP) como el coloreo de grafos, sudoku, asignacion de horarios, entre otros.
#La idea es que al encontrar un conflicto, se retrocede a la variable que causó el conflicto en lugar de retroceder a la última variable asignada.

#Implementacion del algoritmo de salto atrás por conflictos (CBJ)
#CSP = problemas de satisfaccion de restricciones

#Función salto_atras_conflictos: inicia el algoritmo de salto atrás por conflictos
def salto_atras_conflictos(CSP): 
    asignacion = {} #diccionario para almacenar la asignacion de variables a valores
    return CBJ(CSP, asignacion, 0, {}) #llama a la funcion CBJ para resolver el problema

#Funcion CBJ: implementa el algoritmo de salto atras por conflictos
def CBJ(CSP, asignacion, nivel, conflictos_globales):
    if len(asignacion) == len(CSP['variables']): #si todas las variables tienen asignacion 
        return asignacion #retorna la asignacion completa

    var = seleccionar_variable(CSP, asignacion) #selecciona la siguiente variable sin asignar
    conflictos_locales = set() #conjunto para almacenar las varibles en conflicto

    for valor in ordenar_valores(CSP, var, asignacion): #probar cada valor en el dominio
        es_valido, conflicto = es_consistente_con_conflictos(var, valor, asignacion, CSP) #verifica si la asignacion es valida
        if es_valido: #si la asignacion es valida
            asignacion[var] = valor #asigna el valor a la variable
            resultado = CBJ(CSP, asignacion, nivel + 1, conflictos_globales.copy()) #llama ala funcion CBJ recursivamente
            if resultado is not None: #si se encuentra una solucion
                return resultado #retorna la asignacion
            del asignacion[var]  #si no se encuentra una solucion, elimina la asignacion (backtrack)
        else:
            conflictos_locales.update(conflicto)  #registra las variables en conflicto

    #actualizar los conflictos globales y saltar
    if conflictos_locales:
        nivel_conflicto = max(CSP['variables'].index(v) for v in conflictos_locales) #nivel de conflicto
        for v in conflictos_locales: #actualiza los conflictos globales
            conflictos_globales.setdefault(v, set()).update(conflictos_locales) 
        return None  #forzar el retroceso a la variable de conflicto más alta
    return None

#función es_consistente_con_conflictos: verifica la consistencia de la asignación y devuelve variables en conflicto si falla
def es_consistente_con_conflictos(var, valor, asignacion, CSP):
    conflicto = set() #conjunto para almacenar las variables en conflicto
    for v, val in asignacion.items(): #iterar sobre las variables ya asignadas
        if not cumple_restricciones(var, valor, v, val, CSP): #si no cumple la restriccion
            conflicto.add(v) #agregar la variable en conflicto
    return (len(conflicto) == 0, conflicto) #retorna si es valido y las variables en conflicto

#funcion seleccionar_variable: selecciona la variable con el menor dominio
def seleccionar_variable(CSP, asignacion):
    return min([v for v in CSP['variables'] if v not in asignacion], 
               key=lambda v: len(CSP['dominios'][v])) #retorna la variable con el menor dominio

#funcion ordenar_valores: ordena los valores del dominio de la variable en funcion de los conflictos
def ordenar_valores(CSP, var, asignacion):
    return sorted(CSP['dominios'][var], # retorna los valores del dominio de la variable
                 key=lambda val: contar_conflictos(var, val, asignacion, CSP))

#funcion contar_conflictos: cuenta los conflictos de la variable con los valores asignados
def contar_conflictos(var, valor, asignacion, CSP): 
    return sum(1 for v in asignacion if not cumple_restricciones(var, valor, v, asignacion[v], CSP)) #regresa el conteo de la cantidad de conflictos

#funcion cumple_restricciones: verifica si dos valores cumplen las restricciones
def cumple_restricciones(var1, val1, var2, val2, CSP):
    if (var1, var2) in CSP['restricciones']: #verifica si hay restricción entre var1 y var2
        return CSP['restricciones'][(var1, var2)](val1, val2) #aplica la restricción
    elif (var2, var1) in CSP['restricciones']: #verifica si hay restricción entre var2 y var1
        return CSP['restricciones'][(var2, var1)](val2, val1) #aplica la restricción
    return True     #si no hay restricción explícita, se asume que los valores son diferentes

#Ejemplo de uso del algoritmo de salto atras por conflictos
if __name__ == "__main__":
    CSP = {
        'variables': ['A', 'B', 'C'], #nombres de las variables
        'dominios': {   #valores posibles para cada variable
            'A': [1, 2, 3],
            'B': [1, 2, 3],
            'C': [1, 2, 3]
        },
        'restricciones': { #restricciones entre las variables
            ('A', 'B'): lambda x, y: x != y, # A y B deben ser diferentes
            ('B', 'C'): lambda x, y: x != y, # B y C deben ser diferentes
            ('A', 'C'): lambda x, y: x != y # A y C deben ser diferentes
        }
    }

    solucion = salto_atras_conflictos(CSP) #llama a la funcion de salto atras por conflictos
    print("Solución encontrada:", solucion)  

#Ejemplo de Salida: SOlucion encontrada: {'A':1, 'B':2, 'C':3}
