#Heurística 
#Es una función que estima el costo de llegar al objetivo desde un nodo dado
#Los algoritmos con heurística buscan reducir el timepo y espacio necesario para encontrar la solución
#El más representativo es A*, que combuna el costo real desde el incio (g(n)) y la estimación heurística al objetivo(h(n))
#f(n) = g(n) + h(n)
#El algoritmo A* utiliza una cola de prioridad para explorar los nodos con menor costo estimado primero
#La heurística debe ser admisible, es decir, nunca sobreestimar el costo real al objetivo
#Se puede aplicar en Pathfinding, sistemas de navegacion(maps), planificacion de movimientos en robotica, juegos, etc.

#Librerias
import heapq # para la cola de prioridad

#Función heurística
#Argumentos: grafo(diccionario) = diccionario con nodos y costos de aristas
#inicio(str) = nodo inicial, objetivo(str) = nodo objetivo, heuristica(funcion) = funcion que estima el costo al objetivo
def heuristica_A(grafo, inicio, objetivo, heuristica):
    #cola de prioridad: (f(n), g(n), nodo, camino)
    cola = [(0 + heuristica(inicio, objetivo), 0, inicio, [inicio])] #inicializar la cola con el nodo inicial y su costo estimado
    visitados = set() #conjunto de nodos visitados

    while cola: #mientras la cola no esté vacía
        f_actual, g_actual, nodo, camino = heapq.heappop(cola) #sacar el nodo con menor costo estimado
        if nodo == objetivo: #si es el nodo objetivo
            return camino
        if nodo not in visitados: #si ya fue visitado
            visitados.add(nodo) #marcar el nodo como visitado
            for vecino, costo in grafo[nodo]: #recorrer los vecinos del nodo
                g_nuevo = g_actual + costo #calcular el nuevo costo
                f_nuevo = g_nuevo + heuristica(vecino, objetivo) #calcular el nuevo costo estimado
                heapq.heappush(cola, (f_nuevo, g_nuevo, vecino, camino + [vecino])) #agregar el nuevo nodo a la cola 
    return None #si no se encuentra el objetivo, retornar None

#Ejemplo de Heurística 
if __name__ == "__main__": 
    #grafo ponderado: {nodo: [(vecino, costo),...]}
    grafo = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('D', 2), ('E', 5)],
        'C': [('A', 4), ('F', 3)],
        'D': [('B', 2)],
        'E': [('B', 5), ('F', 1)],
        'F': [('C', 3), ('E', 1)]
    }

    #heurística: distancia euclidiana entre nodos (en este ejemplo esta simplificado)
    def heuristica(nodo, objetivo): 
        distancias = {
            'A': 3,
            'B': 2,
            'C': 2,
            'D': 1,
            'E': 1,
            'F': 0
        }
        return distancias[nodo] #retornar la distancia al objetivo
    
    inicio = 'A' #nodo inicial 
    objetivo = 'F' #nodo objetivo 

    camino = heuristica_A(grafo, inicio, objetivo, heuristica) #llamar a la función heurística_A
    if camino:
        print(f"Camino óptimo: {' -> '.join(camino)}") #imprimir el camino optimo
    else: 
        print("No hay camino")


#El camino optimo es A -> B -> E -> F tiene un costo total de 7(1+5+1)
#El algoritmo A* es eficiente y encuentra el camino optimo en grafos ponderados
#Es importante elegir una heurística adecuada para el problema en cuestión
