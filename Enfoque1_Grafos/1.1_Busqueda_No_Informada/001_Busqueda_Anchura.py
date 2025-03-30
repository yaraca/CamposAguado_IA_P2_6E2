#Busqueda en Anchura (BFS- Breadth First Search)
#Algoritmos de exploración de grafos que busca de manera sistemática en todas las direcciones a partir del nodo inicial.
#La búsqueda en anchura es un algoritmo de búsqueda no informada que explora todos los nodos a la misma profundidad antes de pasar a la siguiente profundidad.
#Es útil para encontrar la ruta más corta en un grafo no ponderado.
#Es un algoritmo de búsqueda no informada que utiliza una cola para almacenar los nodos a explorar.
#El algoritmo comienza en el nodo inicial, lo añade a la cola y lo marca como visitado.

#Importar deque de la librería collections para usar como cola
from collections import deque

#Función de búsqueda en anchura
#Parametros: grafo (diccionario de listas)= diccionario que representa el grafo, inicio (string/int)=nodo inciial, objetivo (string/int)=nodo objetivo
#Devuelve: lista = camino desde el nodo incial hasta el nodo objetivo o None si no se encuentra el camino
#La función utiliza una cola para almacenar los nodos a explorar y un conjunto para almacenar los nodos visitados.
def anchura (grafo, inicio, objetivo): 
    #Crear una cola para almacenar los nodos a explorar
    #Cada elemento de la cola es una tupla que contiene el nodo actual y el camino desde el nodo inicial hasta el nodo actual
    cola = deque([(inicio, [inicio])]) 
    #Crear un conjunto para almacenar los nodos visitados 
    visitados = set()
    while cola: #mientras la cola no esté vacía
        nodo_actual, camino = cola.popleft() #sacar el primer elemento de la cola
        if nodo_actual == objetivo: #si el nodo actual es el nodo objetivo
            return camino #devolver el camino desde el nodo inicial hasta el nodo objetivo 
        if nodo_actual not in visitados: #si elnodo actual no ha sido visitado
            visitados.add(nodo_actual) #marcar el nodo actual como visitado 
            for vecino in grafo[nodo_actual]: #para cada vecino del nodo actual
                if vecino not in visitados: #si el vecino no ha sido visitado
                    cola.append((vecino, camino + [vecino])) #añadir el vecino a la cola con el camino desde el nodo incial hasta el vecino
    return "No hay camino entre {} y {}".format(inicio, objetivo) #devolver un mensaje indicando que no hay camino entre el nodo inicial y el nodo objetivo

#Ejemplo de uso de la fución Búsqueda en Anchura
if __name__ == "__main__": #Ejecutar el código solo si se ejecuta directamente
    #Definir un grafo como un diccionario de listas
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

inicio = 'A' #Nodo incial
objetivo = 'F' #Nodo objetivo

camino = anchura(grafo, inicio, objetivo) #Llamar a la función busqueda en anchura

if camino: #si se encuentra un camino
    print("Camino encontrado desde {} hasta {}: {}".format(inicio, objetivo, camino)) #imprimir el camino desde el nodo inicial hasta el nodo objetivo
else: #si no se encuentra un camino
    print("No se encontró un camino desde {} hasta {}".format(inicio, objetivo)) #imprimir el mensaje que no se encontró un camino entre el nodo inicial y el nodo objetivo