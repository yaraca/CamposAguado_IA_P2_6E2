#Busqueda Voraz Primero El Mejor (Greedy Best First Search)
#Es un algoritmoque siempre elige expandir el nodo que parece estar más cerca de la meta, segun una función heurística
#este metodo usa la información heurística para decidir el siguiente nodo a expandir
#Este algoritmo no garantiza la optimalidad de la solución, pero es más eficiente que la búsqueda en amplitud o profundidad
#en algunos casos, ya que no explora todos los nodos del espacio de búsqueda.
#Es útil para problemas donde la solución se encuentra cerca de la raíz del árbol de búsqueda o donde la función heurística es muy informativa.
#Se puede usae en busqueda gps y mapas, videojuegos y pathfinding, busqueda de información, etc.

#Librerias necesarias
import heapq #para usar la cola de prioridad

#Función de busqueda voraz
#Argumentos: grafo(diccionario) = diccionario de listas de adyacencia, inicio(str) = nodo inicial
#objetivo(str) = nodo objetivo, heurística(funcion) = h(n) estima costo al objetivo
#Retorna lista de camino encontrado o None si no se encuentra
def busqueda_voraz(grafo, inicio, objetivo, heuristica):
    #Cola de prioridad (h(n), nodo, camino)
    cola = [(heuristica(inicio, objetivo), inicio, [inicio])] #inicializa la cola con el nodo inicial y su heuristica
    visitados = set() #nodos visitados
    
    while cola: #mientras la cola no este vacia
        #saca el nodo con menor heuristica de la cola
        _, nodo_actual, camino = heapq.heappop(cola) 
        if nodo_actual == objetivo: #si el nodo actual es el objetivo
            return camino #retorna el camino encontrado
        if nodo_actual not in visitados: #si el nodo no ha sido visitado
            visitados.add(nodo_actual) #Marcar el nodo como visitado
            for vecino in grafo[nodo_actual]: #para cada vecino del nodo actual
                if vecino not in visitados: #si el vecino no ha sido visitado
                    heapq.heappush(cola, (heuristica(vecino, objetivo), vecino, camino + [vecino])) #agregar el vecino a la cola con su heuristica y el camino
    return None #si no se encuentra el objetivo, retorna None

#Ejemplo de busqueda voraz
if __name__ == "__main__":
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    #función heuristica: distancia estimada al objetivo 'F
    def heuristica(nodo, objetivo): 
        distancias = {
            'A': 2,
            'B': 1,
            'C': 1,
            'D': 2,
            'E': 1,
            'F': 0
        }
    
    inicio = 'A' #nodo inicial
    objetivo = 'F' #nodo objetivo

    camino = busqueda_voraz(grafo, inicio, objetivo, heuristica) #llama a la función
    if camino: 
        print(f"Camino encontrado: {' -> '.join(camino)}") #si se encuentra el camino, lo imprime
    else: 
        print("No se encontró un camino al objetivo.")

#Ejemplo de salida: Camino encontrado: A -> B -> E -> F
#La busqueda voraz primero el mejor encuentra un camino desde el nodo A hasta el nodo F, pasando por los nodos B y E.
#La busqueda voraz no garantiza la optimalidad de la solución, pero es más eficiente que la búsqueda en amplitud o profundidad en algunos casos.
#En este caso estaban las dos opciones de B y C, pero el algoritmo elige el primero que encuentre en la cola de prioridad, que depende del orden en el grafo
#Una vez que elige B, ignora C hasta agotar todas las opciones de B, y luego sigue con C.
