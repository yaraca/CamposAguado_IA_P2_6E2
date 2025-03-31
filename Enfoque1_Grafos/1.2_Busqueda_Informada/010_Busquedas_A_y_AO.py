#Busqueda A* y AO* (A estrella y A estrella óptimo)
#El A* es el algoritmo de busque informada más famoso que comina el costo real (g(n)) y la heuristica (h(n)) que nunca sobrestima el costo real.
#Su formula es f(n) = g(n) + h(n)
#El AO* es una variante para grafos AND-OR, donde los nodos pueden tener múltiples padres y se busca la mejor solución considerando todos los caminos posibles.
#Esos son usados en IA para problemas de planificación 
#El A* se usa para el pathfinding, videojuego, robotica, gps, etc.
#El AO* se usa para la planificación automática, toma de decisiones bajo incertidumbre, etc.

#-----------------------------------------------------------------------------------------------------------
#Implementación de A* 
import heapq #para la cola de prioridad

#función A*
#Argumentos: grafo(diccionario) = {nodo: [(vecino, costo)]} , inicio(str) = nodo inicial 
#objetivo(str) = nodo objetivo , heuristica(funcion) = h(nodo, objetivo)
def a_estrella(grafo, inicio, objetivo, heuristica):
    #(f(n), g(n), nodo, camino)
    cola = [(0 + heuristica(inicio, objetivo), 0, inicio, [inicio])] #inicializar la cola de prioridad en el nodo inicial 
    visitados = set() #nodos visitados 

    while cola: 
        f_actual, g_actual, nodo, camino = heapq.heappop(cola) #sacar el nodo con menor f(n) de la cola
        if nodo == objetivo: #si el nodo es el objetivo
            return camino #devolver el camino
        
        if nodo not in visitados: #si el nodo no ha sido visitado
            visitados.add(nodo) #marcar como nodo visitado
            for vecino, costo in grafo[nodo]: #recorrer los vecinos del nodo
                if vecino not in visitados: #si el vecino no se ha visitado
                    g_nuevo = g_actual + costo #calcular el nuevo costo g(n)
                    f_nuevo = g_nuevo + heuristica(vecino, objetivo) #calcular el nuevo f(n)
                    heapq.heappush(cola, (f_nuevo, g_nuevo, vecino, camino + [vecino])) #agregar el nuevo nodo a la cola
    return None #si no se encuentra el objetivo, devolver None


#Ejemplo de uso de A*
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [], #nodo sin vecinos
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}
#función heurística (h(n))
def heuristica_a(nodo, objetivo):
    distancias = {
        'A': 3,
        'B': 2,
        'C': 2,
        'D': 1,
        'E': 1,
        'F': 0
    }
    return distancias[nodo] #devolver la distancia heurística del nodo al objetivo

camino = a_estrella(grafo, 'A', 'F', heuristica_a) #llamar a la función A*
print(f"Camino A*: {' -> '.join(camino)}") #imprimir el camino encontrado por A*
#Ejemplo de salida: Camino A*: A -> B -> E -> F
#-----------------------------------------------------------------------------------------------------------

#Implementación de AO*
#Librerías necesarias
from itertools import product #para el producto cartesiano
#función AO*
#Argumentos: grafo_and_or(diccionario) = {nodo: {'OR': [vecinos], 'AND': (conjunto_vecinos, costo)}}
#inicio(str) = nodo inicial, objetivo(str) = nodo objetivo, heuristica(funcion) = h(nodo, objetivo)
#retorna lista de camino optimo o None si no se encuentra
def ao_estrella(grafo_and_or, inicio, objetivo, heuristica):
    cola = [(heuristica(inicio, objetivo), inicio, [inicio])] #inicializar la cola de prioridad en el nodo inicial
    visitados = set() #nodos visitados

    while cola: 
        f_actual, nodo, camino = heapq.heappop(cola) #sacar el nodo con menor f(n) de la cola
        if nodo == objetivo: #si el nodo es el obejtivo
            return camino #devolver el camino
        
        if nodo not in visitados: #si el nodo no se ha visitado
            visitados.add(nodo) #marcar como nodo visitado

            if isinstance(nodo, str): #si el nodo es un string (nodo normal)
                #nodos OR (elige un solo vecino)
                for vecino in grafo_and_or[nodo].get('OR', []): #recorrer los vecinos de nodo hacia el objetivo
                    f_nuevo = heuristica(vecino, objetivo) #calcular el nuevo f(n)
                    heapq.heappush(cola, (f_nuevo, vecino, camino + [vecino])) #agregar el nuevo nodo a la cola
                #nodos AnD (elige todos los vecinos)
                for conjunto, costo in grafo_and_or[nodo].get('AND', []): #recorrer los conjuntos de vecinos
                    f_nuevo = sum(heuristica(vecino, objetivo) for vecino in conjunto) + costo #hacer el la suma de los costos 
                    nuevo_camino = camino + [f"AND: {conjunto}"] #agregar el nuevo camino
                    for vecino in conjunto: #agregar los vecinos al camino
                        heapq.heappush(cola, (f_nuevo, vecino, nuevo_camino)) #agregar el nuevo nodo a la cola
    return None #si no se encuentra el objetivo, devolver None

#Ejemplo de uso de AO*
grafo_and_or = {
    'A': {'OR': ['B'], 'AND': [({'C', 'D'}, 3)]},
    'B': {'OR': ['E']},
    'C': {'OR': ['F']},
    'D': {'OR': ['F']},
    'E': {'OR': ['F']},
    'F': {}
}

#función heuristica par AO* (h(n))
def heuristica_ao(nodo, objetivo):
    distancias = {
        'A': 3,
        'B': 2,
        'C': 1,
        'D': 1,
        'E': 1,
        'F': 0
    }
    return distancias[nodo] #devolver la distancia heurística del nodo al objetivo

camino_ao = ao_estrella(grafo_and_or, 'A', 'F', heuristica_ao) #llamar a la función AO*
print(f"Camino AO*: {' -> '.join(camino_ao)}") #imprimir el camino encontrado por AO*
#Ejemplo de salida: Camino AO*: ['A', 'B', 'E', 'F']
#AO* prioriza caminos con menor costo estimado f(n) y busca la mejor solución considerando todos los caminos posibles.
#Que en este caso es la rama OR de A a B y luego a E y F.

#-----------------------------------------------------------------------------------------------------------
