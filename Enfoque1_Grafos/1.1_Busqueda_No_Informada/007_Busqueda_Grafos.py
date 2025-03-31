#Busqueda en Grafos (Graph Search)
# En este ejemplo se implementa una busqueda en grafos utilizando un algoritmo de busqueda en profundidad (DFS) y una busqueda en anchura (BFS).
#Este tipo de algoritmo incluye un mecanismo para evitar ciclos, es decir, no visitar un nodo que ya ha sido visitado.
#Es esencial para trabajar con grafos que contienen ciclos, ya que de lo contrario el algoritmo entraria en un bucle infinito.
#Se puede aplicar en Pathfinding en videojuegos, Crawlers web, análisis de redes sociales, etc.
#El algoritmo de busqueda en profundidad (DFS) explora un camino hasta el final antes de retroceder y explorar otros caminos.
#El algoritmo de busqueda en anchura (BFS) explora todos los nodos a un nivel antes de pasar al siguiente nivel.
#Ambos algoritmos son utilizados para encontrar el camino mas corto entre dos nodos en un grafo.
#La diferencia entre ambos algoritmos es que DFS utiliza una pila para almacenar los nodos a visitar, mientras que BFS utiliza una cola.

#Librerias necesarias
from collections import deque #para usar las colas en BFS

#Funcion de busqueda en grafos 
#Parametros: grafo(diccionario) = diccionario de listas de adyacencia, inicio(str/int)= nodo inicial
# objetivo(str/int)= nodo objetivo, estrategia(str)= estrategia de busqueda (DFS o BFS)
#Retorna: lista con el camino más corto entre el nodo inicial y el nodo objetivo
def busqueda_grafo(grafo, inicio, objetivo, estrategia='bfs'): #la estrategia por defecto es BFS
    cola = deque([(inicio, [inicio])]) #cola para la busqueda en anchura (BFS)
    visitados = set() #conjunto para almacenar los nodos visitados

    while cola: #mientras haya nodos en la cola
        if estrategia == 'bfs': #si la estrategia es BFS (anchura)
            nodo_actual, camino = cola.popleft() #sacar el nodo actual y su camino de la cola
        else: #si la estrategia es DFS (profundidad)
            nodo_actual, camino = cola.pop() #sacar el nodo actual y su camino de la cola (pila)

        if nodo_actual == objetivo: #si el nodo actual es el objetivo
            return camino #retornar el camino encontrado
        if nodo_actual not in visitados: #si el nodo actual no fue visitado
            visitados.add(nodo_actual) #agregar el nodo actual a los visitados
            for vecino in reversed(grafo[nodo_actual]): #recorrer los vecinos del nodo actual (reverso para DFS)
                if vecino not in visitados: #si el vecino no fue visitado
                    cola.append((vecino, camino + [vecino])) #agregar el vecino a la cola con su camino
    return None #si no se encuentra un camino, retornar None

#Ejemplo de busqueda en grafos
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

    #llamar a la función de busqueda en grafos con BFS (anchura)
    camino_bfs = busqueda_grafo(grafo, inicio, objetivo, estrategia='bfs') #llamar la función
    print(f"BFS(anchura) - Camino encontrado: {' -> '.join(camino_bfs) if camino_bfs else 'No se encontro un camino'}") 
    
    #llamar a la función de busqueda en grafos con DFS (profundidad)
    camino_dfs = busqueda_grafo(grafo, inicio, objetivo, estrategia='dfs') #llamar la función
    print(f"DFS(profundidad) - Camino encontrado: {' -> '.join(camino_dfs) if camino_dfs else 'No se encontro un camino'}") 

#Ejemplo de salida
#BFS(anchura) - Camino encontrado: A -> C -> F
#DFS(profundidad) - Camino encontrado: A -> B -> E -> F
#En este ejemplo se puede observar que el camino encontrado por BFS es diferente al encontrado por DFS.
#Esto se debe a que ambos algoritmos utilizan diferentes estrategias para explorar los nodos del grafo.
#BFS explora todos los nodos a un nivel antes de pasar al siguiente nivel, mientras que DFS explora un camino hasta el final antes de retroceder y explorar otros caminos.
#Por lo tanto, el camino encontrado por BFS es más corto que el encontrado por DFS.

