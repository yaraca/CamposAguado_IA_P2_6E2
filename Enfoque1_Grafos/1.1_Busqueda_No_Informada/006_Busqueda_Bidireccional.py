#Busqueda Bidireccional
#Es una técnica para encontrar la ruta más corta entre un nodo incial y un nodo objetivo
#Hace dos busquedas en paralelo, del incio al objetivo y del objetivo al inicio
#Cuando las dos busquedas se encuentran, se unen los caminos y se obtiene la ruta más corta
#Se puede utilizar en navegación gps, cubo rubik, redes y telecomunicaciones

#Librerías necesarias
from collections import deque #para usar las colas

#Función de busqueda bidireccional
#Parametros: grafo(diccionario) = diccionario de listas de adyacencia, inicio(str/int)= nodo inicial
# objetivo(str/int)= nodo objetivo
#Retorna: lista con el camino más corto entre el nodo inicial y el nodo objetivo
def busqueda_bidireccional(grafo, inicio, objetivo):
    cola_inicio = deque([(inicio, [inicio])]) #cola para la busqueda desde el inicio
    cola_objetivo = deque([(objetivo, [objetivo])]) #cola para la busqueda desde el objetivo
    visitados_inicio = {inicio: [inicio]} #nodos visitados desde el inicio
    visitados_objetivo = {objetivo: [objetivo]} #nodos visitados desde el objetivo

    while cola_inicio and cola_objetivo: #mientras haya nodos en las colas
        nodo_actual, camino_inicio = cola_inicio.popleft() #sacar el nodo actual y su camino desde la cola de inicio
        if nodo_actual in visitados_objetivo: #si el nodo actual ya fue visitado desde el objetivo 
            camino_objetivo = visitados_objetivo[nodo_actual] #obtenemos el camino desde el objetivo
            return camino_inicio + camino_objetivo[::-1][1:] #unimos los caminos y retornamos el resultado
        
        for vecino in grafo[nodo_actual]: #recorremos los vecinos del nodo actual
            if vecino not in visitados_inicio: #si el vecino no fue visitado desde el inicio
                visitados_inicio[vecino] = camino_inicio + [vecino] #agregar el vecino a los visitados desde el incio
                cola_inicio.append((vecino, camino_inicio + [vecino])) #agregar el vecino a la cola de inicio
        
        nodo_actual, camino_objetivo = cola_objetivo.popleft() #sacar el nodo actual y su camino desde la cola de objetivo
        if nodo_actual in visitados_inicio: #si el nodo actual ya fue visitado desde el inicio
            camino_inicio = visitados_inicio[nodo_actual] #obtener el camino desde el inicio para el nodo actual 
            return camino_inicio + camino_objetivo[::-1][1:] #unir ambos caminos y retornar el resultado
        
        for vecino in grafo[nodo_actual]: #recorremos los vecinos del nodo actual
            if vecino not in visitados_objetivo: #si el vecino no fue visitado desde el objetivo
                visitados_objetivo[vecino] = camino_objetivo + [vecino] #agregar el vecino a los visitados desde el objetivo
                cola_objetivo.append((vecino, camino_objetivo + [vecino])) #agregar el vecino a la cola del objetivo
    return None #si no se encuentra un camino, retornar None

#Ejemplol de busqueda bidireccional
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

    camino = busqueda_bidireccional(grafo, inicio, objetivo) #llamar a la función 
    if camino: #si se encuentra un camino
        print(f"Camino encontrado: {' -> '.join(camino)}")
    else: #si no se encuentra un camino
        print("NO se encontró un camino")

#Salida esperada: Camino encontrado: A -> C -> F