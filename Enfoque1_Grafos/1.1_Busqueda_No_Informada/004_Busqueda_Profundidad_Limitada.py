#Busqueda en profundidad limitada (Depth-Limited Search)
#Este algoritmo impone un límite en la profundidad de exploración del árbol de búsqueda
#Esto evita que el algoritmo entre en bucles infinitos en grafos con ciclos o ramas muy profundas
#Optimiza la búsqueda cuando sabemos que la solución no está más alla de cierta profundidad
#Se puede usar en problemas con profundidad restringida o en juegos donde el tiempo de búsqueda es limitado

#Función de busqueda en profundidad limitada
#Parámetros: grafo(diccionario) = diccionario de listas de adyacencia,
#inicio(str/int) = nodo inicial, objetivo(str/int) = nodo objetivo, limite_profundidad(int) = máxima profundidad
#Retorna lista de caminos desde inicio hasta objetivo (si se encuentra dentro del límite)
def profundidad_limitada(grafo, inicio, objetivo, limite_profundidad):
    pila = [(inicio, [inicio], 0)] #inicializa la pila con el nodo inicial, la ruta y la profundidad
    visitados = set() #inicializa el conjunto de nodos visitados
    
    while pila: #mientras la pila no esté vacia 
        nodo_actual, camino, profundidad = pila.pop() #saca el nodo actual, el camino y la profundidad de la pila
        if nodo_actual == objetivo: #si el nodo actual es el objetivo 
            return camino #retorna el camino encontrado
        if profundidad >= limite_profundidad: #si la profundidad es mayor o igual al límite 
            continue #no explora más allá de este punto
        if nodo_actual not in visitados: #si el nodo actual no se ha visitado
            visitados.add(nodo_actual) #marca el nodo como visitado
            for vecino in reversed(grafo[nodo_actual]): #itera sobre los vecinos del nodo actual en orden inverso para explorar primero los más profundos
                if vecino not in visitados: #si el vecino no se ha visitado
                    pila.append((vecino, camino + [vecino], profundidad + 1)) #agregar el vecino a la pila con el nuevo camino y profundidad
    return None #si no se encuentra el objetivo, retorna None


#Ejemplo de busqueda de profundidad limitada
if __name__ == "__main__":
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    inicio = 'A' #nodo inicial
    objetivo = 'F' #nodo objetivo
    limite_profundidad = 2 #límite de profundidad

    camino = profundidad_limitada(grafo, inicio, objetivo, limite_profundidad) #llama a la función

    if camino: #si se encuentra un camino
        print(f"Camino encontrado dentro del límite {limite_profundidad}: {' -> '.join(camino)}") #imprime el camino encontrado
    else: #si no se encuentra un camino
        print(f"No se encontró un camino hasta {objetivo} dentro del límite de profundidad {limite_profundidad}.")

#Ejemplo de salida: camino encontrado dentro del límite 2: A -> C -> F
#Si el limite fuera = 1, no se encontraría el camino
