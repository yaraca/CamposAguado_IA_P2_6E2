#Proceso de Decisión de Markov Parcialmente Observable (POMDP)
#Un POMDP es una extensión de un MDP que permite que el agente no observe completamente el estado del entorno.
#sino que recibe una observacion incompleta o parcial del entorno
#Por eso en vez de tomar decisiones con base en el estado, lo hace usando una creencia sobre el estado
#se compone de: S=Conjunto de estados posibles, A=Conjunto de acciones, T=Función de transición de estados,
#R=funcion de recompensa, Z=Conjunto de observaciones, O=Función de observación, b=Creencia inicial, y=factor de descuento gamma
#Los POMDP se utilizan en robótica, sistemas de recomendación, planificación y control de procesos.

#Ejemplo de un POMDP
#Un robot no sabe en qué habitacion está (A o B), pero puede moverse y hacer observaciones ruidosas para decidir qué hacer

#librerias necesarias
import random

#definir estados, acciones y observaciones
estados = ['A', 'B'] #dos habitaciones
acciones = ['moverse'] #solo puede moverse entre habitaciones
observaciones = ['veo_A', 'veo_B'] #observaciones ruidosas (puede ver A o B)

#modelo de transicion 
#so el agente se mueve, tiene 100% de probabilidad de moverse a la otra habitacion
transicion = {
    'A': {'moverse': 'B'}, #si está en A y se mueve, va a B
    'B': {'moverse': 'A'} #si está en B y se mueve, va a A
}

#modelo de observacion (ruidoso)
#si el agente está en A, tiene 80% de probabilidad de ver A y 20% de ver B
observacion_prob = {
    'A': {'veo_A': 0.8, 'veo_B': 0.2}, #si está en A, ve A con 80% de probabilidad
    'B': {'veo_A': 0.2, 'veo_B': 0.8} #si está en B, ve A con 20% de probabilidad
}

#recompensas
recompensas = {'A': 1, 'B': -1} #recompensa por estar en A es 1, en B es -1

#estado de creencia inicial
creencia = {'A': 0.5, 'B': 0.5} #50% de probabilidad de estar en A o B

#funcion actualizar creencia
def actualizar_creencia(creencia, accion, observacion): # creencia=probabilidad de estar en A o B, accion=accion a realizar, observacion=observacion recibida
    nueva_creencia = {} #diccionario para almacenar la nueva creencia

    for s_prima in estados: #iterar sobre los estados posibles
        suma = 0
        for s in estados:
            prob_trans = 1 if transicion[s][accion] == s_prima else 0 #probabilidad de transicion de s a s'
            suma += creencia[s] * prob_trans #probabilidad de estar en s y moverse a s'

        #multiplicar por la probabilidad de la observación
        nueva_creencia[s_prima] = observacion_prob[s_prima][observacion] * suma #probabilidad de observar s' dado que se movió a s'

    #normalizar
    normalizador = sum(nueva_creencia.values()) #suma de todas las probabilidades
    for s in nueva_creencia:
        nueva_creencia[s] /= normalizador #dividir cada probabilidad por la suma total para normalizar

    return nueva_creencia #retorna la nueva creencia normalizada

#funcion para ejecutar el POMDP
def ejecutar_pomdp(creencia, accion):
    #simular el estado real (solo para esta prueba)
    estado_real = random.choices(estados, weights=[creencia['A'], creencia['B']])[0] #estado real del agente (A o B)
    
    #hacer la transición (en este caso solo moverse)
    nuevo_estado = transicion[estado_real][accion] #nuevo estado después de moverse

    #simular observación desde nuevo estado
    observacion = random.choices( 
        observaciones, #observaciones posibles
        weights=[ #probabilidad de ver A, probabilidad de ver B]
            observacion_prob[nuevo_estado]['veo_A'],
            observacion_prob[nuevo_estado]['veo_B']
        ]
    )[0]

    #actualizar creencia basada en la observación
    nueva_creencia = actualizar_creencia(creencia, accion, observacion) 

    print(f"Estado real después de moverse: {nuevo_estado}") ##estado real después de moverse
    print(f"Observación: {observacion}") #observación recibida
    print(f"Nueva creencia: {nueva_creencia}") #nueva creencia después de la observación
    
    return nueva_creencia

#ejecutar iteracion del POMDP
print("Creencia inicial:", creencia) #imprimir creencia inicial
creencia = ejecutar_pomdp(creencia, 'moverse') #ejecutar el POMDP con la acción de moverse

#Ejemplo salida:
# Creencia inicial: {'A': 0.5, 'B': 0.5}
# Estado real después de moverse: A
# Observación: veo_A
# Nueva creencia: {'A': 0.8, 'B': 0.2}
