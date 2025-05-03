#Redes Jerárquicas de Tareas (HTN)
#es un enfoque de planificación basado en descomponer tareas complejas en subtareas más simples, hasta llegar a tareas primitivas que pueden ejecutarse directamente.
# Funcionamiento:
# Tarea principal (abstracta): un objetivo general como "preparar una comida".
# Descomposición: se divide en subtareas más manejables como "preparar arroz", "freír vegetales".
# Tareas primitivas: son acciones ejecutables como "encender estufa", "agregar aceite", e
# Red de tareas: se forma una jerarquía donde las tareas abstractas se expanden recursivamente.
#Aplicaciones: planificacion de robots, IA en juegos, sistemas expertos, asistentes personales, etc. 

#Ejemplo de (HTN)
# Tarea abstracta: hacer_te
# Subtareas: hervir_agua, agregar_te, servir_taza

#definir un diccionario con métodos de planificación htn (hierarchical task network)
htn_methods = {
    "hacer_te": ["hervir_agua", "agregar_te", "servir_taza"],  #descomponer la tarea en subtareas
    #las demás tareas son primitivas, no se descomponen más
}

#crear una lista para almacenar el plan final generado
plan = []

#definir una función recursiva para generar el plan a partir de una tarea dada
def planificar(tarea):
    #verificar si la tarea es abstracta (si tiene subtareas en el diccionario)
    if tarea in htn_methods:
        subtareas = htn_methods[tarea]  #obtener la lista de subtareas
        #recorrer cada subtarea y planificarla recursivamente
        for subtarea in subtareas:
            planificar(subtarea)
    else:
        plan.append(tarea)  #si la tarea es primitiva, agregarla directamente al plan

#definir la tarea principal que debe cumplirse
tarea_objetivo = "hacer_te"

#ejecutar la planificación de la tarea principal
planificar(tarea_objetivo)

#mostrar el plan final generado
print("Plan generado:")
#recorrer la lista de pasos del plan y mostrarlos en orden con numeración
for paso, tarea in enumerate(plan, start=1):
    print(f"{paso}. {tarea}")

#Ejemplo de salida: 
# Plan generado:
# 1. hervir_agua
# 2. agregar_te
# 3. servir_taza

# El ejemplo de salida nos muestra el plan generado para cumplir la tarea principal "hacer_te".
# Este plan está compuesto por los pasos necesarios en el orden correcto, descomponiendo la tarea abstracta
# en subtareas primitivas que pueden ejecutarse directamente.