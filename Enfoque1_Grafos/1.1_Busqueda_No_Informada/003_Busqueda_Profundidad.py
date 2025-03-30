#Busqueda en Profundidad (depth-First Search, DFS)
#Es un algoritmo utilizado para recorrer o buscar elementos en un grafo o árbol.
#El algoritmo explora un camino en profundidad antes de retrocedery explorar otros caminos
#Es útil para encontrar un camino entre dos nodos o para explorar todos los nodos de un grafo.
#Se basa en una estructura de pila (stack) para llevar un registro de los nodos visitados y los nodos por visitar 
#El proceso termina cuando todos los nodos han sido visitados o se ha encontrado el nodo objetivo
#Se puede usar en mapas, laberintos, redes sociales, etc.


#Función de busqueda en profundidad
#Parámetros: grafo(diccionario) = lista de adyacencia, inicio(string/int) = nodo de incio, obejtivo(string/int) = nodo objetivo
def profundidad(grafo, inicio, objetivo): 
    pila = [(inicio, [inicio])] #Pila para almacenar los nodos por visitar y el camino hasta el nodo actual
    visitados = set() #Conjunto para almacenar los nodos visitados (evitar ciclos)
    while pila: #mientras haya nodos por visitar
        nodo_actual, camino = pila.pop() #sacar el nodo actual y el camino hasta el nodo actual de la pila
        if nodo_actual == objetivo: #si el nodo actual es el objetivo
            return camino #devuelve el camino hasta el nodo objetivo
        if nodo_actual not in visitados: #si el nodo actual no se ha visitado
            visitados.add(nodo_actual) #marcar el nodo actual como visitado
            for vecino in reversed(grafo[nodo_actual]): #recorrer los vecinos del nodo actual en orden inverso (para mantener el orden original)
                if vecino not in visitados: #si el vecino no se ha visitado
                    pila.append((vecino, camino + [vecino])) #agregar el vecino a la pila con el camino hasta el vecino 
    return None #si no se encuentra el objetivo, devuelve None


#Ejemplo de Busqueda en Profundidad
if __name__ == "__main__":
    #definir un grafo como un diccionario de listas de adyacencia
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    inicio = 'A' #nodo de inicio
    objetivo = 'F' #ndoo objetivo

    camino = profundidad(grafo, inicio, objetivo) #llamar a la función 
    
    if camino: #si se encuentra un camino
        print(f"Camino encontrado desde {inicio} hasta {objetivo}: {'-> '.join(camino)}") #imprimir el camino encontrado
    else: #si no se encuentra un camino
        print(f"No se encontró un camino desde {inicio} hasta {objetivo}")


