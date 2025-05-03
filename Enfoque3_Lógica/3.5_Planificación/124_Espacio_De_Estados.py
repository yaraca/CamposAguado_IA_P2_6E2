#Espacio de Estados
#es una representación de todos los posibles estados que puede tomar un sistema o problema
#junto con las transiciones entre esos estados causadas por la aplicación de acciones o reglas.
# Este modelo es fundamental en la planificación porque:
# Permite visualizar todos los caminos que se pueden tomar desde el estado inicial hasta uno que cumpla la meta.
# Sirve de base para aplicar algoritmos de búsqueda
#Funcionamiento:
# Se define: El estado inicial. El estado objetivo (meta). Las acciones que cambian el estado.
# Se explora el espacio de estados (el conjunto de todos los estados alcanzables).
# Se usa una estrategia de búsqueda (por ejemplo, búsqueda en amplitud) para encontrar un camino desde el estado inicial al estado meta.
#Aplicaciones: robotica, juegos, rompecabezas, control automático, etc. 

#Ejemplo de espacio de estados: 
#  El problema del jarrón de agua
#Tenemos dos jarras: Una de 4 litros. Otra de 3 litros.
#Queremos obtener exactamente 2 litros en una de las jarras. Podemos: Llenar una jarra. Vaciar una jarra. Verter de una jarra a otra.
#construir el espacio de estados y aplicar búsqueda en amplitud (BFS) para encontrar el camino al estado objetivo.

#librerias necesarias
from collections import deque

#definir una función para verificar si se alcanzó el objetivo de obtener 2 litros en alguna jarra
def is_goal(state):
    return state[0] == 2 or state[1] == 2

#definir una función para generar los posibles estados sucesores desde un estado dado
def get_successors(state):
    successors = []  #crear una lista para almacenar los estados sucesores
    a, b = state  #desempaquetar el estado actual en las variables a y b
    max_a, max_b = 4, 3  #establecer la capacidad máxima de las jarras

    #llenar la jarra A completamente
    successors.append((max_a, b))
    #llenar la jarra B completamente
    successors.append((a, max_b))
    #vaciar completamente la jarra A
    successors.append((0, b))
    #vaciar completamente la jarra B
    successors.append((a, 0))
    #verter agua de la jarra A a la jarra B hasta el límite de la B
    transfer = min(a, max_b - b)
    successors.append((a - transfer, b + transfer))
    #verter agua de la jarra B a la jarra A hasta el límite de la A
    transfer = min(b, max_a - a)
    successors.append((a + transfer, b - transfer))

    return successors  #retornar la lista de estados sucesores

#definir una función para realizar búsqueda en amplitud en el espacio de estados
def bfs(initial_state):
    visited = set()  #crear un conjunto para registrar los estados visitados
    queue = deque()  #crear una cola para la exploración en amplitud
    queue.append((initial_state, []))  #agregar el estado inicial con un camino vacío

    while queue:  #mientras haya elementos en la cola
        state, path = queue.popleft()  #extraer el primer elemento de la cola

        if state in visited:  #si el estado ya fue visitado, omitirlo
            continue
        visited.add(state)  #marcar el estado como visitado

        if is_goal(state):  #si el estado cumple la condición de meta, retornar el camino completo
            return path + [state]

        for succ in get_successors(state):  #generar los sucesores del estado actual
            if succ not in visited:  #si el sucesor no ha sido visitado, agregarlo a la cola con su camino
                queue.append((succ, path + [state]))

    return None  #si no se encontró una solución, retornar None

#definir el estado inicial con ambas jarras vacías
initial_state = (0, 0)

#ejecutar la búsqueda utilizando búsqueda en amplitud
solution = bfs(initial_state)

#mostrar los resultados del camino hacia la meta
print("Camino hacia el objetivo (2 litros en alguna jarra):")
if solution:
    for step in solution:  #recorrer cada paso en la solución y mostrar el contenido de las jarras
        print(f"Jarra A: {step[0]} L, Jarra B: {step[1]} L")
else:
    print("No se encontró solución.")

#Ejemplo de salida: 
# Camino hacia el objetivo (2 litros en alguna jarra):
# Jarra A: 0 L, Jarra B: 0 L
# Jarra A: 0 L, Jarra B: 3 L
# Jarra A: 3 L, Jarra B: 0 L
# Jarra A: 3 L, Jarra B: 3 L
# Jarra A: 4 L, Jarra B: 2 L

# El ejemplo de salida nos muestra el camino que se sigue en el espacio de estados
# para alcanzar el objetivo de tener exactamente 2 litros en alguna de las jarras.
# Cada paso representa un estado intermedio, indicando cuántos litros hay en la
# jarra A y en la jarra B después de aplicar una acción.