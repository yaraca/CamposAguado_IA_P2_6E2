#Planificación de Orden Parcial
#La planificación de orden parcial es una técnica de planificación en inteligencia artificial donde:
# No se requiere definir desde el principio un orden total de las acciones.
# Se permite que algunas acciones queden sin ordenarse entre sí, si no hay una razón lógica para hacerlo.
# Esto se hace porque:
# Permite mayor flexibilidad y reutilización del plan.
# Reduce la complejidad computacional al no tener que explorar todos los posibles órdenes de ejecución.
#COmponentes: 
# Un conjunto de acciones (cada una con precondiciones y efectos).
# Un conjunto de restricciones de orden entre acciones (por ejemplo: A debe ir antes que B).
# Un conjunto de vínculos de causación (por ejemplo: A produce algo que B necesita).
#El algoritmo intenta: 
# Satisfacer todas las precondiciones del objetivo, agregando acciones que las produzcan.
# Agregar restricciones de orden para evitar conflictos.
# Repetir hasta que no haya condiciones sin cumplir ni amenazas.
#Aplicaciones: rbotica, agentes autonomos, sistemas multiagente

#Ejemplo de Planificación de Orden Parcial: Preparar una bebida caliente
#Queremos realizar el plan para hacer té. Las acciones son: Hervir agua, Agregar té, Verter agua, Endulzar

#definir una clase para representar una acción en el sistema de planificación
class Action:
    def __init__(self, name, preconds, effects):
        #almacenar el nombre de la acción
        self.name = name
        #convertir las condiciones previas en un conjunto para facilitar la comparación
        self.preconds = set(preconds)
        #convertir los efectos que genera la acción en un conjunto
        self.effects = set(effects)

#definir un diccionario con las acciones disponibles
actions = {
    #acción para hervir agua sin condiciones previas
    'Hervir Agua': Action('Hervir Agua', [], ['Agua Hervida']),
    #acción para agregar té sin condiciones previas
    'Agregar Té': Action('Agregar Té', [], ['Té en Taza']),
    #acción para verter agua sobre el té si el agua está hervida y el té está en la taza
    'Verter Agua': Action('Verter Agua', ['Agua Hervida', 'Té en Taza'], ['Té Listo']),
    #acción para endulzar el té si el té ya está listo
    'Endulzar': Action('Endulzar', ['Té Listo'], ['Té Endulzado']),
}

#definir el estado inicial como un conjunto vacío
initial_state = set()

#definir el estado objetivo como el conjunto que contiene el té endulzado
goal = set(['Té Endulzado'])

#crear una lista para almacenar el plan generado
plan = []
#crear una copia del estado inicial para usar en el proceso de planificación
state = initial_state.copy()

#definir una función para generar un plan que satisfaga los objetivos
def pop_planner(goal, actions, state):
    #inicializar una lista para almacenar el plan generado
    plan = []
    #convertir los objetivos en una lista para procesarlos
    open_goals = list(goal)

    #iterar mientras haya objetivos pendientes por cumplir
    while open_goals:
        #extraer el último objetivo de la lista
        g = open_goals.pop()

        #si el objetivo ya está presente en el estado, no hacer nada
        if g in state:
            continue

        #buscar una acción que tenga el objetivo como efecto
        for action in actions.values():
            if g in action.effects:
                #añadir la acción al plan
                plan.append(action)
                #añadir sus precondiciones a la lista de objetivos pendientes si aún no están en el estado
                for p in action.preconds:
                    if p not in state:
                        open_goals.append(p)
                #simular la aplicación de la acción actualizando el estado
                state.update(action.effects)
                #salir del bucle después de encontrar una acción que satisfaga el objetivo
                break

    #invertir el plan para que las acciones aparezcan en el orden correcto
    return plan[::-1]

#ejecutar el planificador para generar un plan que cumpla el estado objetivo
final_plan = pop_planner(goal, actions, initial_state)

#imprimir el plan generado
print("Plan parcial para hacer té:")
#iterar sobre el plan final e imprimir cada acción
for a in final_plan:
    print(f"- {a.name}")

#Ejemplo de salida: 
# Plan parcial para hacer té:
# - Agregar Té
# - Hervir Agua
# - Verter Agua
# - Endulzar

# El ejemplo de salida nos muestra el plan generado por el planificador de orden parcial
# para alcanzar el estado objetivo "Té Endulzado". Este plan incluye las acciones necesarias
# en el orden correcto para cumplir con las precondiciones y efectos de cada acción.