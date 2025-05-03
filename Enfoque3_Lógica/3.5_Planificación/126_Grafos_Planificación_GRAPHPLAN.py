#Grafos de Planificación: GRAPHPLAN
# GRAPHPLAN es un algoritmo de planificación en inteligencia artificial que:
# Utiliza una estructura tipo grafo para representar estados y acciones a lo largo del tiempo.
# GRAPHPLAN construye un grafo por niveles, que alterna entre:
# Niveles de hechos (o fluents): condiciones que son verdaderas en un momento.
# Niveles de acciones: acciones que pueden ejecutarse si sus precondiciones están en el nivel de hechos anterior.
# Además, GRAPHPLAN detecta y usa mutuas exclusiones (mutex):
# Si dos acciones no pueden ocurrir al mismo tiempo (por conflicto en efectos o precondiciones), se marcan como mutuamente excluyentes.
# Igual para hechos que no pueden ser ciertos al mismo tiempo.
#Aplicaciones: planificación en robotica y videojuegos, agentes autonomos, sistemas expertos, etc.

#Ejemplo de GRAPHPLAN: Encender una lámpara
#un robot logre el objetivo: Lámpara encendida, empezando desde el estado donde:
# El robot tiene una batería cargada. ó El interruptor está apagado.
# Acciones:
# Cargar batería → No necesaria al inicio.
# Presionar interruptor → Precondición: batería cargada, interruptor apagado → Efecto: interruptor encendido.
# Encender lámpara → Precondición: interruptor encendido → Efecto: lámpara encendida.

#definir una clase para representar una acción en el sistema de planificación
class Action:
    def __init__(self, name, preconds, adds):
        #almacenar el nombre de la acción
        self.name = name
        #convertir las precondiciones en un conjunto para facilitar la comparación
        self.preconds = set(preconds)
        #convertir los efectos que genera la acción en un conjunto
        self.adds = set(adds)

#definir una clase para implementar el método de planificación basado en grafos
class GraphPlan:
    def __init__(self, actions, initial_state, goal):
        #almacenar la lista de acciones disponibles en el planificador
        self.actions = actions
        #crear una lista para almacenar los niveles de estado del grafo y inicializar con el estado inicial
        self.state_levels = [set(initial_state)]
        #crear una lista para almacenar los niveles de acción en el grafo
        self.action_levels = []
        #definir el estado meta como un conjunto de condiciones a cumplir
        self.goal = set(goal)

    #expande el grafo añadiendo nuevos niveles de acciones y estados
    def expand_graph(self):
        #obtener el estado actual desde el último nivel del grafo
        current_state = self.state_levels[-1]
        #crear una lista para almacenar las acciones aplicables
        applicable_actions = []

        #buscar acciones cuyas precondiciones están contenidas en el estado actual
        for action in self.actions:
            if action.preconds.issubset(current_state):
                applicable_actions.append(action)

        #agregar las acciones encontradas al nivel de acción del grafo
        self.action_levels.append(applicable_actions)

        #crear un nuevo nivel de estado aplicando los efectos de las acciones
        new_state = current_state.copy()
        for action in applicable_actions:
            new_state.update(action.adds)

        #verificar si el nuevo estado es igual al anterior (nivel fijo)
        if new_state == current_state:
            return False  #detener la expansión si no hay cambios en el estado

        #agregar el nuevo estado a la lista de niveles de estado
        self.state_levels.append(new_state)
        return True  #indicar que la expansión fue exitosa

    #genera el grafo y busca un nivel donde los objetivos estén presentes
    def plan(self):
        while True:
            #obtener el último nivel de estado del grafo
            last_state = self.state_levels[-1]

            #imprimir el estado actual del nivel
            print(f"Nivel {len(self.state_levels)-1}: {last_state}")

            #verificar si el estado actual contiene la meta
            if self.goal.issubset(last_state):
                print("¡Meta alcanzada!")
                return True  #confirmar que se alcanzó la meta

            #expandir el grafo, si ya no es posible, detener la planificación
            if not self.expand_graph():
                print("No se pudo alcanzar la meta.")
                return False

#definir la lista de acciones disponibles
actions = [
    #acción para presionar el interruptor si está apagado y la batería está cargada
    Action("Presionar Interruptor", ["Interruptor Apagado", "Batería Cargada"], ["Interruptor Encendido"]),
    #acción para encender la lámpara si el interruptor está encendido
    Action("Encender Lámpara", ["Interruptor Encendido"], ["Lámpara Encendida"]),
]

#definir el estado inicial con el interruptor apagado y la batería cargada
initial_state = ["Interruptor Apagado", "Batería Cargada"]

#definir el estado meta donde la lámpara esté encendida
goal = ["Lámpara Encendida"]

#crear una instancia del planificador basado en grafos
gp = GraphPlan(actions, initial_state, goal)

#ejecutar el proceso de planificación
gp.plan()

#Ejemplo de salida: 
# Nivel 0: {'Batería Cargada', 'Interruptor Apagado'}
# Nivel 1: {'Interruptor Encendido', 'Batería Cargada', 'Interruptor Apagado'}      
# Nivel 2: {'Interruptor Encendido', 'Batería Cargada', 'Lámpara Encendida', 'Interruptor Apagado'}
# ¡Meta alcanzada!

#Este ejemplo ilustra cómo el algoritmo GraphPlan construye niveles de un grafo de planificación, 
# mostrando los estados alcanzables en cada nivel hasta cumplir con el objetivo.

