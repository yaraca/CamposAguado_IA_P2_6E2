#Algoritmos de Planificación: STRIPS y ADL
#STRIPS es un formalismo clásico en Inteligencia Artificial para representar y resolver problemas de planificación automática.
#es una forma de definir un problema mediante: Un estado inicial. Una meta (objetivo). Un conjunto de acciones que transforman el estado actual en otro.
#Cada acción está definida por:
# Precondiciones: lo que debe cumplirse para que la acción se pueda ejecutar.
# Efectos: cómo cambia el estado al aplicar la acción (qué cosas se añaden o eliminan del estado).
#Funcinamiento: 
# Se empieza desde el estado inicial.
# Se buscan acciones cuyas precondiciones se cumplan en el estado actual.
# Se aplica una acción, lo que modifica el estado.
# Se repite hasta que el estado actual cumple con la meta.
# ADL (Action Description Language) es una extensión de STRIPS. Permite:
# Precondiciones y efectos más complejos (con negaciones, disyunciones, cuantificadores).
# Representaciones más realistas del mundo.

#Ejemplo de STRIPS
#robot que quiere mover una caja de una habitación a otra.

#definir una clase para representar una acción en el sistema de planificación
class Action:
    def __init__(self, name, preconditions, add_effects, del_effects):
        #almacenar el nombre de la acción
        self.name = name
        #convertir las condiciones previas en un conjunto para facilitar la comparación
        self.preconditions = set(preconditions)
        #convertir los efectos que se añaden al estado en un conjunto
        self.add_effects = set(add_effects)
        #convertir los efectos que se eliminan del estado en un conjunto
        self.del_effects = set(del_effects)

    #verificar si la acción puede aplicarse sobre el estado actual
    def is_applicable(self, state):
        return self.preconditions.issubset(state)

    #aplicar la acción al estado actual y retornar el estado modificado
    def apply(self, state):
        #crear un nuevo estado eliminando los efectos negativos
        new_state = state - self.del_effects
        #agregar los efectos positivos al nuevo estado
        new_state = new_state | self.add_effects
        return new_state

#definir una función de planificación basada en búsqueda simple hasta alcanzar la meta
def strips_planner(initial_state, goal_state, actions):
    #crear un conjunto para representar el estado inicial
    state = set(initial_state)
    #crear una lista para almacenar el plan de acciones
    plan = []

    #realizar búsqueda hasta que la meta esté en el estado actual
    while not goal_state.issubset(state):
        #indicar si alguna acción es aplicable en esta iteración
        applicable = False

        #recorrer la lista de acciones posibles
        for action in actions:
            #verificar si la acción se puede aplicar al estado actual
            if action.is_applicable(state):
                #mostrar la acción aplicada
                print(f"Aplicando acción: {action.name}")
                #modificar el estado aplicando la acción
                state = action.apply(state)
                #añadir la acción al plan
                plan.append(action.name)
                #marcar que se aplicó una acción
                applicable = True
                #salir del bucle para aplicar solo una acción por iteración
                break  

        #si ninguna acción fue aplicable, no hay solución
        if not applicable:
            print("No se puede encontrar un plan válido desde el estado actual.")
            return None

    #retornar el plan generado
    return plan

#definir el estado inicial del problema
initial_state = {"en(caja, habitacion1)", "en(robot, habitacion1)"}
#definir el estado objetivo que se desea alcanzar
goal_state = {"en(caja, habitacion2)"}

#definir la lista de acciones posibles en el entorno
actions = [
    #acción para mover el robot de una habitación a otra
    Action(
        name="mover_robot(habitacion1, habitacion2)",
        preconditions={"en(robot, habitacion1)"},
        add_effects={"en(robot, habitacion2)"},
        del_effects={"en(robot, habitacion1)"}
    ),
    #acción para mover la caja con la ayuda del robot
    Action(
        name="mover_caja(habitacion1, habitacion2)",
        preconditions={"en(robot, habitacion2)", "en(caja, habitacion1)"},
        add_effects={"en(caja, habitacion2)"},
        del_effects={"en(caja, habitacion1)"}
    )
]

#ejecutar el planificador para encontrar una secuencia de acciones
plan = strips_planner(initial_state, goal_state, actions)

#mostrar el resultado del plan encontrado
if plan:
    print("\nPlan encontrado:")
    #recorrer cada paso del plan e imprimirlo
    for step in plan:
        print(f"- {step}")
else:
    print("No se encontró un plan.")

#Ejemplo de salida: 
# Aplicando acción: mover_robot(habitacion1, habitacion2)
# Aplicando acción: mover_caja(habitacion1, habitacion2)
# Plan encontrado:
# - mover_robot(habitacion1, habitacion2)
# - mover_caja(habitacion1, habitacion2)

# El ejemplo de salida nos muestra cómo el planificador STRIPS encuentra una secuencia de acciones
# que permite alcanzar el estado objetivo desde el estado inicial. En este caso:
# 1. Primero aplica la acción "mover_robot(habitacion1, habitacion2)", lo que mueve al robot
#    de la habitación 1 a la habitación 2.
# 2. Luego aplica la acción "mover_caja(habitacion1, habitacion2)", lo que mueve la caja
#    de la habitación 1 a la habitación 2 con la ayuda del robot.
# Finalmente, imprime el plan encontrado, que es la lista de acciones en el orden en que
# deben ejecutarse para alcanzar el objetivo.