#Busqueda Online (Online Search)
#Es un algoritmo utilizado en enotornos donde el espacio de estados es desconocido o dinamico.
#El agente debe de tomar decisiones en tiempo real sin tener acceso completo a la informacion del entorno
#El agente aprende y explorar el entorno mientras actúa, sin una representacion previa del grafo o mapa
#Es utilizado en robótica, videojuegos, y sistemas de navegación autónoma.

#Ejemplo de busqueda online en un entorno de laberinto con heurística (distancia Manhattan)
#Librerias necesarias
import heapq #para manejar la cola de prioridad

#funcion busqueda online 
#parametros: inicio = tupla (x,y) con la posicion inicial, meta = tupla (x,y) con la posicion final
#heuristica = funcion que calcula la distancia estimada a la meta, obtener_vecinos = funcion que devuelve movimientos validos desde un estado 
#retorna: lista de movimientos desde el inicio hasta la meta

def busqueda_online(inicio, meta, heuristica, obtener_vecinos):
    visitados = set() #conjunto de nodos visitados
    cola_prioridad = [] #cola de prioridad (prioridad, estado, camino)

    #inicializar la cola de prioridad con el nodo inicial
    heapq.heappush(cola_prioridad, (heuristica(inicio, meta), inicio, [])) #agregar el nodo inicial a la cola de prioridad

    while cola_prioridad: #mientras que la cola no este vacio 
        _, estado_actual, camino = heapq.heappop(cola_prioridad) #sacar el nodo con el menor costo 
        
        if estado_actual == meta: #si el estado actual es la meta 
            return camino
        
        if estado_actual not in visitados: #si el estado no se ha visitado 
            visitados.add(estado_actual) #marcar el estado como visitado
            vecinos = obtener_vecinos(estado_actual) #obtener los vecinos del estado actual
            for vecino in vecinos: 
                if vecino not in visitados: #si el vecino no ha sido visitado
                    nuevo_camino = camino + [vecino]
                    #prioridad = costos acumulado(longitud del camino) + heuristica (distancia estimada a la meta)
                    prioridad = len(nuevo_camino) + heuristica(vecino, meta)
                    heapq.heappush(cola_prioridad, (prioridad, vecino, nuevo_camino)) #agregar el vecino a la cola de prioridad
    return None #si no se encuentra la meta, retornar None

#Funcion distancia Manhattan: entre dos puntos (x1,y1) y (x2,y2)
def distancia_manhattan(p1, p2): 
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) #retorna la distancia Manhattan entre dos puntos

#funcion obtener vecinos: simula un entorno de laberinto 5x5 sin obstaculos 
def ob_vecinos_simulados(estado):
    x, y = estado #desempaquetar la tupla
    movimientos = [ (x+1, y), (x-1, y), (x, y+1), (x, y-1)] #movimientos posibles (derecha, izquierda, abajo, arriba)
    vecinos_validos = [] #lista de vecinos validos
    for nx, ny in movimientos: 
        if 0 <= nx < 5 and 0 <= ny < 5: #limitar el laberinto a 5x5
            vecinos_validos.append((nx, ny)) #agregar el vecino valido a la lista 
    return vecinos_validos #retornar la lista de vecinos validos


#Ejemplo de uso de la busqueda online
if __name__ == "__main__":
    inicio = (0, 0) #posicion inicial 
    meta = (4, 4) #posicion final
    camino = busqueda_online(inicio, meta, distancia_manhattan, ob_vecinos_simulados) #llamar a la funcion de busqueda online
    
    print (f"Camino encontrado: {camino}") #imprimir el camino encontrado

#Ejemplo salida: Camino encontrado: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
#El camino puede variar dependiendo de la heuristica y el entorno simulado
#El camino encontrado es una lista de tuplas que representan los movimientos desde el inicio hasta la meta
#El algoritmo de busqueda online es eficiente en entornos desconocidos o dinamicos, ya que no requiere una representacion completa del entorno

