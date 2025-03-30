#Busqueda en profundidad iterativa (Iterative Deepening Search IDS)
#Es una combinacion de busqueda en profundidad y busqueda en amplitud
#Se usa principalmente cunado no se conoce la profundidad de la solución 
#y se quiere evitar el alto consumo de memoria de la busqueda en aplitud
#La idea es realizar una busqueda en profundidad con un limite de profundidad
#y aumentar el limite de profundidad en cada iteracion
#El algoritmo se detiene cuando encuentra la solución
#Se puede usar en laberintos donde no se conoce la profundidad de la salida, en ajedraz o en problemas de busqueda de caminos


#Función de busqueda en profundidad iterativa 
#Parámetros: grafo(diccinario) = diccionario de listas adyacentes
#           inicio (string/int) = nodo inciial y objetivo (string/int) = nodo objetivo
def profundidad_iterativa(grafo, incio, objetivo):
    limite = 0 #inicializar el limite de profundidad
    
    while True: #mientras no se encuentre la solución 
        resultado = profundidad_limitada(grafo, incio, objetivo, limite) #llamar a la función 
        if resultado is not None: #si se encuentra la solución 
            return resultado #retorna el resultado
        limite += 1 #aumentar el límite de profundidad

#función auxiliar de búsqueda en profundidad con límite
#Parámetros: grafo(diccionario) = diccionario de listas de adyacencia,
#nodo(str/int) = nodo inicial, objetivo(str/int) = nodo objetivo, limite(int) = limite de profundidad
#visitados(set) = conjunto de nodos visitados, camino(lista) = lista de nodos en el camino
#Retorna una lista con el camino encontrado o None si no se encuentra la solución
def profundidad_limitada(grafo, nodo, objetivo, limite, visitados=None, camino=None):
    if visitados is None: #si no se ha inicializado el conjunto de visitados
        visitados = set() #inicializa el conjunto de visitados
    if camino is None: #si no se ha inicializado el camino
        camino = [] #inicializa el camino
    
    camino.append(nodo) #agrega el nodo actual al camino
    if nodo == objetivo: #si el nodo actual es el objetivo
        return camino
    if len(camino) -1 >= limite: #si el camino es mayor o igual al límite (-1 porque el camino incluye el nodo inicial)
        return None 
    
    visitados.add(nodo) #marca el nodo como visitado
    for vecino in reversed(grafo[nodo]): #recorre los vecinos del nodo en orden inverso para que se visiten en el orden correcto
        if vecino not in visitados: #si el vecino no se ha visitado
            resultado = profundidad_limitada(grafo, vecino, objetivo, limite, visitados, camino) #llama a la función
            if resultado is not None: #si se encuentra la solución
                return resultado
            

#Ejemplo de busqueda de profundidad iterativa
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

    camino = profundidad_iterativa(grafo, inicio, objetivo) #llama a la función 

    if camino: #si se encuentra el camino
        print(f"Camino encontrado: {' -> '.join(camino)}") #imprime el camino encontrado
    else: #si no se encuentra el camino
        print("No se encontró un camino.")
#Ejemplo de salida:
#Limite = 0 -> Camino encontrado: A -> C -> F





