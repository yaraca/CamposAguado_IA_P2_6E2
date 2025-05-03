#Planificación Condicional
#es una técnica de planificación que permite tomar decisiones basadas en condiciones del entorno. 
#Es especialmente útil en entornos no deterministas o parcialmente observables, 
# donde las acciones pueden tener efectos inciertos o donde se requiere observar el entorno antes de continuar.
# Funcionamiento:
# El plan no es lineal, sino ramificado: hay bifurcaciones que dependen de condiciones (como un "si... entonces...").
# Se incluyen acciones de observación para conocer el estado del mundo.
# Se generan diferentes planes para cada posible resultado de una condición.
#Aplicaciones: robots, asistentes inteligentes, planes médicos, etc. 

#Ejemplo de planifcaciones condicional: 
# modelar una situación donde un robot quiere salir de una habitación.
# La puerta puede estar cerrada o abierta, y el robot no lo sabe hasta que la observa.
# Estados posibles: puerta_abierta = True/False (se desconoce al inicio)
# Objetivo:
# Si la puerta está abierta: salir directamente
# Si está cerrada: abrirla y luego salir

#librerias necesarias
import random

import random  #importar el módulo random para generar valores aleatorios

#definir una variable que simula el estado desconocido del entorno
#en la realidad, el robot no sabe si la puerta está abierta, así que lo simulamos con una elección aleatoria
puerta_abierta=random.choice([True, False])  #condición del entorno

#crear una lista vacía para almacenar el plan generado
plan=[]

#definir una función para observar el estado de la puerta
def observar_puerta():
    #simular una acción de observación mostrando un mensaje en pantalla
    print("Observando si la puerta está abierta...")
    #retornar el valor de la variable que representa el estado de la puerta
    return puerta_abierta

#definir una función para generar un plan condicional basado en la observación
def planificar_condicional():
    estado_puerta=observar_puerta()  #observar el entorno y obtener el estado de la puerta
    if estado_puerta:  #si la puerta está abierta
        plan.append("Salir por la puerta abierta")  #agregar la acción de salir directamente
    else:  #si la puerta está cerrada
        plan.append("Abrir la puerta")  #agregar la acción de abrir la puerta
        plan.append("Salir")  #agregar la acción de salir después de abrir la puerta

#ejecutar la planificación condicional
planificar_condicional()

#mostrar el resultado del plan generado
print("\nPlan generado:")
#recorrer la lista de acciones del plan y mostrarlas con numeración
for paso, accion in enumerate(plan, start=1):
    print(f"{paso}. {accion}")

#Ejemplo de salida:
# Observando si la puerta está abierta...

# Plan generado:
# 1. Salir por la puerta abierta

# En este ejemplo de salida, se muestra cómo el robot observa el estado de la puerta
# y genera un plan condicional basado en esa observación. Si la puerta está abierta,
# el plan incluye salir directamente. Si está cerrada, el plan incluye abrir la puerta
# y luego salir. Esto demuestra cómo funciona la planificación condicional en un entorno
# con incertidumbre.