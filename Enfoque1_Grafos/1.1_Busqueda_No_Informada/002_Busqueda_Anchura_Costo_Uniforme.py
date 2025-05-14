#Busqueda de costo uniforme (UCS- Uniform Cost Search)
#Es una busqueda no informada que se utiliza para encontrar el camino de costo minimo en un grafo ponderado.
#Este expande el nodo con el menor costo aucmulado desde el nodo incial
#UCS considera los costos variables entre los nodos, por lo que es óptimo para grafos ponderados.
#Aplicaciones: rutas de navegación, planificación de rutas, etc.

#Importamos las librerias
import heapq #libreria para manejar colas de prioridad (colas ordenadas por costo)

#Función costos_uniforme que implementa la búsqueda de costo uniforme
#Parametros: grafo(diccinario) = donde las claves son nodos y los valores son listas de tuplas (vecino, costo)
#           inicio (string/int) = nodo inciial y objetivo (string/int) = nodo objetivo
#Retorna: tupla (costo_total, camino) o None donde CT = costo total y camino = lista de nodos del camino
def costo_uniforme(grafo, inicio, objetivo): 
    cola = [(0, inicio, [inicio])] #cola de prioridad: costo acumulado, nodo actual, camino
    costos_minimos = {inicio: 0} #diccionario para el menor costo conocido hasta cada nodo
    while cola: #mientras la cola no esté vacía
        costo_acumulado, nodo_actual, camino = heapq.heappop(cola) #sacar el nodo con menor costo acumulado
        if nodo_actual == objetivo: #si el nodo actual es el objetivo
            return costo_acumulado, camino #retorna el costo total y el camino
        if costo_acumulado > costos_minimos.get(nodo_actual, float('inf')): #si el costo acumulado es mayor al costo conocido
            continue #si ya hay un camino mejor se ignora este
        for vecino, costo in grafo[nodo_actual]: #iterar sobre los vecinos del nodo actual
            nuevo_costo = costo_acumulado + costo #calcular el nuevo costo acumulado
            if vecino not in costos_minimos or nuevo_costo < costos_minimos[vecino]: #si el vecino no ha sido visitado o el nuevo costo es menor
                costos_minimos[vecino] = nuevo_costo #actualizar el costo minimo conocido
                heapq.heappush(cola, (nuevo_costo, vecino, camino + [vecino])) #agregar el vecino a la cola con el nuevo costo acumulado y el nuevo camino 
    return None #si no se encuentra el objetivo, retorna None

#Ejemplo de uso
if __name__ == "__main__": #definimos el grafo como un diccionario 
    grafo = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('D', 2), ('E', 2)],
        'C': [('A', 4), ('F', 3)],
        'D': [('B', 2)],
        'E': [('B', 5), ('F', 1)],
        'F': [('C', 3), ('E', 1)]
    } #Nodo : [(vecino, costo), ...]

    inicio = 'A' #nodo incial
    objetivo = 'F' #nodo objetivo

    resultado = costo_uniforme(grafo, inicio, objetivo) #llamar a la función 

    if resultado: #si se encuentra el camino
        costo, camino = resultado #desempaqutar el resultado
        print(f"Camino encontrado de {inicio} a {objetivo}: {' -> '.join(camino)}") #imprimir el camino
        print(f"Costo total: {costo}")
    else: #si no se encuentra el camino
        print(f"No se encontró un camino de {inicio} a {objetivo}.") #no se encontró el camino 
