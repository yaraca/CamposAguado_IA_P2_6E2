#Acondicionamiento de Corte
#Es un algoritmo híbrido que combina el backtracking con la propagación de restricciones.
#Primero identifica un conjunto de corte (variables) que al ser eliminadas, convierte el grafo de restricciones en un árbol
#luego aplica backtracking sobre estas variables mientras resuelve el resto mediante propagación de restricciones.
#Esto permite resolver problemas de satisfacción de restricciones (CSP) de manera más eficiente al reducir el espacio de búsqueda.
#es util con problemas con estructura de grado casi-arbores, planificacion, diseño de redes, etc.

#Librerias necesarias
import itertools #para combinaciones
from collections import defaultdict #para contar conflictos

#función cutset_conditioning: implementa el algoritmo de acondicionamiento de corte
#parametros: csp = problema de satisfaccion de restricciones (CSP)
def cutset_conditioning(csp):
    #encontrar un cutset mínimo
    cutset = encontrar_cutset(csp) ##encontrar un conjunto de corte
    if not cutset: 
        return resolver_arbol(csp) #si no hay cutset, resolver el CSP como un árbol
    
    #backtracking sobre el cutset con verificación explícita
    for asignacion_cutset in generar_combinaciones(csp, cutset): ##generar todas las combinaciones posibles de valores para el cutset
        csp_reducido = reducir_csp(csp, asignacion_cutset) #reducir el CSP fijando las variables del cutset
        solucion_arbol = resolver_arbol(csp_reducido) #resolver el CSP reducido como un árbol
        
        if solucion_arbol is not None: #si se encuentra una solución
            solucion_completa = {**asignacion_cutset, **solucion_arbol} #combinar la solución del cutset con la solución del árbol
            if es_solucion_valida(solucion_completa, csp): #verificar si la solución completa es válida
                return solucion_completa #retornar la solución completa
    return None #si no se encuentra solución, retornar None

#función encontrar_cutset: encuentra un cutset mínimo que rompa ciclos en el grafo de restricciones
def encontrar_cutset(csp):
    grafo = {var: vecinos.copy() for var, vecinos in csp['vecinos'].items()} #crear una copia del grafo de vecinos
    cutset = set() #conjunto para almacenar el cutset
    
    #ordenar variables por grado descendente
    variables_ordenadas = sorted(grafo.keys(), key=lambda v: -len(grafo[v])) #ordenar variables por grado
    
    for var in variables_ordenadas: #iterar sobre las variables ordenadas
        if var in grafo:  #verificar si no fue eliminada previamente
            if not es_arbol(grafo): #verificar si el grafo es un árbol
                cutset.add(var) #agregar la variable al cutset
                #eliminar la variable y sus conexiones
                for vecino in grafo[var]: #eliminar conexiones de la variable
                    grafo[vecino].remove(var) #eliminar la variable de los vecinos
                del grafo[var] #eliminar la variable del grafo
            else: #si el grafo es un árbol, salir del bucle
                break
    return cutset

#función es_arbol: verifica si un grafo es un árbol (sin ciclos y conexo)
def es_arbol(grafo):
    if not grafo: #si el grafo está vacío, es un árbol
        return True 
    
    visitados = set() #conjunto para almacenar los nodos visitados
    pila = [(next(iter(grafo)), None)]  # (nodo, padre) inicializa la pila con un nodo y su padre
    
    while pila: #iterar mientras haya nodos en la pila
        nodo, padre = pila.pop() #sacar un nodo de la pila
        if nodo in visitados: #si el nodo ya fue visitado, hay un ciclo
            return False
        visitados.add(nodo) #marcar el nodo como visitado
        for vecino in grafo[nodo]: #iterar sobre los vecinos del nodo
            if vecino != padre: #si el vecino no es el padre, agregarlo a la pila
                pila.append((vecino, nodo)) #agregar el vecino a la pila con el nodo actual como padre
    return len(visitados) == len(grafo) #verificar si todos los nodos fueron visitados

#función generar_combinaciones: genera todas las combinaciones posibles de valores para el cutset
def generar_combinaciones(csp, cutset):
    dominios = [csp['dominios'][var] for var in cutset] #obtener los dominios de las variables del cutset
    for combinacion in itertools.product(*dominios): #generar todas las combinaciones de valores
        yield dict(zip(cutset, combinacion)) #asignar cada variable del cutset a un valor de su dominio

#función reducir_csp: reduce el CSP fijando las variables del cutset y propagando restricciones
def reducir_csp(csp, asignacion): 
    nuevo_dominio = {} #diccionario para almacenar los nuevos dominios de las variables
    for var in csp['variables']: #iterar sobre todas las variables del CSP
        if var not in asignacion: #si la variable no está en el cutset
            #filtrar valores inconsistentes con las asignaciones del cutset
            dominio_filtrado = [ 
                val for val in csp['dominios'][var] # obtener el dominio original de la variable
                if all(
                    csp['restricciones'].get((var, v), lambda x, y: True)(val, asignacion[v]) and
                    csp['restricciones'].get((v, var), lambda x, y: True)(asignacion[v], val)
                    for v in asignacion if (var, v) in csp['restricciones'] or (v, var) in csp['restricciones']
                ) #verificar si el valor es consistente con las asignaciones del cutset
            ]
            nuevo_dominio[var] = dominio_filtrado #asignar el dominio filtrado a la variable
    
    return {
        'variables': [var for var in csp['variables'] if var not in asignacion], #filtrar variables que no están en el cutset
        'dominios': nuevo_dominio, #asignar los nuevos dominios filtrados
        'restricciones': { # filtrar restricciones que no involucran el cutset
            (var1, var2): csp['restricciones'][(var1, var2)]
            for var1, var2 in csp['restricciones'] # iterar sobre las restricciones
            if var1 not in asignacion and var2 not in asignacion #verificar si las variables no están en el cutset
        },
        'vecinos': { # filtrar vecinos que no involucran el cutset
            var: [v for v in vecinos if v not in asignacion]
            for var, vecinos in csp['vecinos'].items() # iterar sobre los vecinos
            if var not in asignacion #verificar si la variable no está en el cutset
        }
    }

#función resolver_arbol: resuelve un CSP que es un árbol usando eliminación de hojas
def resolver_arbol(csp):
    asignacion = {} #diccionario para almacenar la asignación de variables a valores
    orden = orden_eliminacion(csp) #obtener el orden de eliminación de las variables
    
    for var in orden:
        #encontrar un valor consistente con las asignaciones previas
        for valor in csp['dominios'][var]: #iterar sobre los valores del dominio de la variable
            valido = all( #verificar si el valor es consistente con las asignaciones previas
                csp['restricciones'].get((var, v), lambda x, y: True)(valor, asignacion[v]) and 
                csp['restricciones'].get((v, var), lambda x, y: True)(asignacion[v], valor) # verificar si el valor es consistente con las asignaciones previas
                for v in asignacion # iterar sobre las variables ya asignadas
            )
            if valido: #si el valor es consistente
                asignacion[var] = valor #asignar el valor a la variable
                break
        else:
            return None  #no hay valor válido
    return asignacion

#función orden_eliminacion: determina el orden de eliminación de las variables en el CSP
def orden_eliminacion(csp):
    grafo = csp['vecinos'] #obtener el grafo de vecinos
    grados = {var: len(vecinos) for var, vecinos in grafo.items()} #contar los grados de cada variable
    orden = [] #lista para almacenar el orden de eliminación
    
    while grados: #mientras haya variables en el grafo
        #encontrar una hoja (nodo con grado 1 o 0)
        hoja = next(var for var, grado in grados.items() if grado <= 1) #encontrar una hoja en el grafo
        orden.append(hoja) #agregar la hoja al orden de eliminación
        #reducir grados de los vecinos
        for vecino in grafo[hoja]: #iterar sobre los vecinos de la hoja
            if vecino in grados: 
                grados[vecino] -= 1 #reducir el grado del vecino
        del grados[hoja] #eliminar la hoja del grafo
    return orden #invertir el orden para la eliminación

#función es_solucion_valida: verifica si una asignación cumple todas las restricciones
def es_solucion_valida(asignacion, csp):
    for (var1, var2), restriccion in csp['restricciones'].items(): #iterar sobre las restricciones
        if var1 in asignacion and var2 in asignacion: #verificar si ambas variables están asignadas
            if not restriccion(asignacion[var1], asignacion[var2]): #verificar si cumplen la restricción
                return False #si no cumplen, retornar False
    return True

#Ejemplo de uso del algoritmo de acondicionamiento de corte
if __name__ == "__main__":
    csp_ejemplo = {
        'variables': ['A', 'B', 'C', 'D'], #nombres de las variables
        'dominios': {  #valores posibles para cada variable
            'A': [1, 2],
            'B': [1, 2],
            'C': [1, 2],
            'D': [1, 2]
        },
        'restricciones': { #restricciones entre las variables
            ('A', 'B'): lambda x, y: x != y,
            ('B', 'C'): lambda x, y: x != y,
            ('C', 'D'): lambda x, y: x != y,
            ('D', 'A'): lambda x, y: x != y
        },
        'vecinos': { #vecinos de cada variable
            'A': ['B', 'D'],
            'B': ['A', 'C'],
            'C': ['B', 'D'],
            'D': ['C', 'A']
        }
    }

    print("Buscando solución...")
    solucion = cutset_conditioning(csp_ejemplo) #llama a la funcion de acondicionamiento de corte
    
    if solucion:
        print("\nSolución válida encontrada:")
        for var in csp_ejemplo['variables']: #imprimir la solución
            print(f"{var}: {solucion[var]}")
        
        #verificación manual de restricciones
        print("\nVerificación de restricciones:") 
        restricciones = csp_ejemplo['restricciones'] #obtener las restricciones
        for (var1, var2) in restricciones: #iterar sobre las restricciones
            val1, val2 = solucion[var1], solucion[var2] #obtener los valores asignados
            print(f"{var1}({val1}) ≠ {var2}({val2}): {val1 != val2}") #verificar si los valores son diferentes
    else:
        print("No se encontró solución.")

#Ejemplo de salida: 
# Solución válida encontrada:
# A: 1
# B: 2
# C: 1
# D: 2

# Verificación de restricciones:
# A(1) ≠ B(2): True
# B(2) ≠ C(1): True
# C(1) ≠ D(2): True
# D(2) ≠ A(1): True