#Filtrado, Predicción, Suavizado y Explicación
#Estos algoritmos se usan para inferir el estado de un sistema dinámico que evoluciona a lo largo del tiempo.
#Filtrado: Calcular la creencia actual P(Xt|e1:t) es decir, la probabilidad del estado en el tiempo actual dado todas las observaciones hasta ahora.
#         sirve para Saber dónde estás ahora basándote en lo que has visto hasta este momento. (como un GPS que te dice tu ubicación actual basándose en los puntos de referencia que has pasado).
#Predicción: calcular la probabilidad futura p(Xt+k|e1:t) donde K>0
#            sirve para Predecir dónde estarás en el futuro basándote en lo que has visto hasta ahora y las observaciones pasadas (como un GPS que te dice dónde podrías estar en el futuro basándose en tu trayectoria actual y en el tráfico esperado).
#Suavizado: Calcular la creencia en un estado pasado P(Xk|e1:t) donde k<t
#           sirve para Mejorar tu estimación sobre dónde estabas antes, usando información que recibiste después. (como un GPS que revisa tu trayectoria pasada y ajusta tu ubicación anterior basándose en el tráfico real que encontraste después).
#Explicación:  Encontrar la secuencia de estados más probable dados los datos observados: argmax P(X1:t|e1:t)
#              sirve para Reconstruir qué pasó exactamente. (como un GPS que revisa tu trayectoria pasada y ajusta tu ubicación anterior basándose en el tráfico real que encontraste después).
#Funcionamiento general: se basa generalmente en Modelos ocultos de Markov (HMM) o Redes dinámicas Bayesianas, Actualizar creencias usando la ley de Bayes y la regla de la cadena.
#requiere: Modelo de transición P(Xt|Xt-1) y Modelo de observación P(Et|Xt).

#Ejemplo de filtrado, prediccion, suavizado y explicacion
#2 estados: "Soleado" o "Lluvioso".
#el sensor de clima puede estar correcto o equivocado con cierta probabilidad.

#librerías necesarias
import numpy as np #para operaciones matemáticas y matrices

#definir los estados
estados = ['Soleado', 'Lluvioso']

#Matriz de transición: P(estado actual | estado anterior)
P_transicion = {
    'Soleado': {'Soleado': 0.8, 'Lluvioso': 0.2},  #probabilidades de transición desde Soleado (80% a Soleado, 20% a Lluvioso)
    'Lluvioso': {'Soleado': 0.3, 'Lluvioso': 0.7} #probabilidades de transición desde Lluvioso (30% a Soleado, 70% a Lluvioso)
}

#Matriz de observación: P(observación | estado actual)
P_observacion = {
    'Soleado': {'Seco': 0.9, 'Mojado': 0.1}, #probabilidades de observación desde Soleado (90% Seco, 10% Mojado)
    'Lluvioso': {'Seco': 0.2, 'Mojado': 0.8} #probabilidades de observación desde Lluvioso (20% Seco, 80% Mojado)
}

#Creencia inicial: ¿qué tan probable es cada estado al inicio?
creencia_actual = {'Soleado': 0.5, 'Lluvioso': 0.5} #50% de probabilidad de estar en cada estado al inicio

#Observaciones recibidas
observaciones = ['Seco', 'Seco', 'Mojado', 'Mojado'] #Ejemplo de observaciones (seco o mojado) en 4 días

#función para normalizar la distribución de probabilidades
def normalizar(distribucion):
    #Normaliza la distribución para que sume 1
    total = sum(distribucion.values()) #suma total de probabilidades
    for estado in distribucion: #iterar sobre cada estado
        distribucion[estado] /= total #dividir cada probabilidad por la suma total
    return distribucion #devolver la distribución normalizada

#funcipón de filtrado para actualizar la creencia con una nueva observación
def filtrado(creencia, observacion):
    nueva_creencia = {}

    #Predicción: propagar la creencia usando la matriz de transición
    for estado_actual in estados: #iterar sobre cada estado
        suma = 0 #inicializar suma
        for estado_anterior in estados: #iterar sobre cada estado anterior
            suma += P_transicion[estado_anterior][estado_actual] * creencia[estado_anterior] #multiplicar la probabilidad de transición por la creencia anterior
        #incorporar la evidencia de la observación
        nueva_creencia[estado_actual] = P_observacion[estado_actual][observacion] * suma #multiplicar la probabilidad de observación por la suma de creencias

    #Normalizar para que las probabilidades sumen 1
    return normalizar(nueva_creencia) #devolver la nueva creencia normalizada

#guardar las creencias a lo largo del tiempo
creencias_filtrado = []

#aplicar filtrado para cada observación
for obs in observaciones: #iterar sobre cada observación
    creencia_actual = filtrado(creencia_actual, obs) #actualizar la creencia actual usando la función de filtrado
    creencias_filtrado.append(creencia_actual.copy()) #guardar la creencia actual en la lista de creencias

#imprimir las creencias
print("Creencias después de cada observación (Filtrado):")
for i, creencia in enumerate(creencias_filtrado): #iterar sobre las creencias
    print(f"Tiempo {i+1} | {creencia}") #imprimir la creencia después de cada observación

#Función PREDICCIÓN paracalcular probabilidad de estado futuro (sin nuevas observaciones)
def prediccion(creencia, pasos):
    ##Predicción de la creencia en el futuro
    creencia_predicha = creencia.copy() #inicializar la creencia predicha con la creencia actual
    for _ in range(pasos): #iterar sobre el número de pasos a predecir
        nueva_creencia = {} #inicializar nueva creencia
        for estado_actual in estados: #iterar sobre cada estado
            suma = 0 #inicializar suma
            for estado_anterior in estados: #iterar sobre cada estado anterior
                suma += P_transicion[estado_anterior][estado_actual] * creencia_predicha[estado_anterior] #multiplicar la probabilidad de transición por la creencia predicha
            nueva_creencia[estado_actual] = suma #asignar la suma a la nueva creencia
        creencia_predicha = normalizar(nueva_creencia) #normalizar la nueva creencia
    return creencia_predicha #devolver la creencia predicha

#Ejemplo: predecir 2 pasos hacia adelante
creencia_predicha = prediccion(creencias_filtrado[-1], 2) #usar la última creencia filtrada para predecir 2 pasos hacia adelante
print("\nPredicción a 2 pasos adelante:", creencia_predicha)

#FUNCION SUAVIZADO: para calcular la probabilidad de un estado pasado usando observaciones futuras
def suavizado(creencias_filtrado, observaciones):
    T = len(observaciones) #Número de observaciones
    suavizadas = [None] * T #Inicializar lista de suavizadas
    suavizadas[-1] = creencias_filtrado[-1]  #Al final, suavizado = filtrado

    #Beta: probabilidad hacia adelante desde el tiempo t+1
    beta = {estado: 1.0 for estado in estados} #inicializar beta con 1.0 para cada estado

    #ir hacia atrás
    for t in reversed(range(T - 1)): #iterar desde el último tiempo hacia atrás
        nueva_beta = {} #inicializar nueva beta
        for estado in estados: #iterar sobre cada estado
            suma = 0 #inicializar suma
            for estado_sig in estados: #iterar sobre cada estado siguiente
                suma += (P_transicion[estado][estado_sig] * # probabilidad de transición
                         P_observacion[estado_sig][observaciones[t + 1]] * # probabilidad de observación
                         beta[estado_sig]) # probabilidad hacia adelante
            nueva_beta[estado] = suma #asignar la suma a la nueva beta

        #multiplicar filtrado por beta y normalizamos
        suavizada = {} #inicializar suavizada
        for estado in estados: #iterar sobre cada estado
            suavizada[estado] = creencias_filtrado[t][estado] * nueva_beta[estado] #multiplicar la creencia filtrada por la nueva beta

        suavizadas[t] = normalizar(suavizada) #normalizar la suavizada
        beta = nueva_beta  #actualizar beta para el siguiente paso atrás

    return suavizadas #devolver la lista de suavizadas

#aplicar el suavizado
creencias_suavizadas = suavizado(creencias_filtrado, observaciones) #usar las creencias filtradas y las observaciones para suavizar

#mostrar las creencias suavizadas
print("\nCreencias suavizadas (usando observaciones futuras):")
for i, creencia in enumerate(creencias_suavizadas): #iterar sobre las creencias suavizadas
    print(f"Tiempo {i+1} | {creencia}") #imprimir la creencia suavizada después de cada observación


#FUNCION EXPLICACION: para encontrar la secuencia de estados más probable usando el algoritmo de Viterbi
def explicacion(observaciones):
    T = len(observaciones) #número de observaciones
    delta = {}  #mejor probabilidad hasta cada estado
    psi = {}    #mejor padre (backpointer)

    #Inicialización
    delta[0] = {} #inicializar delta
    psi[0] = {} #inicializar psi
    for estado in estados: #iterar sobre cada estado
        delta[0][estado] = creencia_actual[estado] * P_observacion[estado][observaciones[0]] #probabilidad inicial
        psi[0][estado] = None #no hay padre en el primer paso

    #Recursión
    for t in range(1, T): #iterar sobre el tiempo desde 1 hasta T-1
        delta[t] = {} #inicializar delta
        psi[t] = {} #inicializar psi
        for estado_actual in estados: #iterar sobre cada estado actual
            max_prob = 0 #inicializar la máxima probabilidad
            mejor_estado = None #inicializar el mejor estado
            for estado_anterior in estados: #iterar sobre cada estado anterior
                prob = (delta[t-1][estado_anterior] * #probabilidad de la mejor secuencia anterior
                        P_transicion[estado_anterior][estado_actual] * #probabilidad de transición
                        P_observacion[estado_actual][observaciones[t]]) #probabilidad de observación
                if prob > max_prob: #si la probabilidad es mayor que la máxima
                    max_prob = prob #actualizar la máxima probabilidad
                    mejor_estado = estado_anterior #actualizar el mejor estado
            delta[t][estado_actual] = max_prob #asignar la máxima probabilidad al estado actual
            psi[t][estado_actual] = mejor_estado #asignar el mejor estado al backpointer

    #reconstrucción del mejor camino
    mejor_camino = [None] * T #inicializar el mejor camino
    #empezar desde el último tiempo
    mejor_estado = max(delta[T-1], key=delta[T-1].get) #encontrar el estado con la máxima probabilidad
    mejor_camino[-1] = mejor_estado #asignar el mejor estado al último tiempo

    #retroceder siguiendo los backpointers
    for t in reversed(range(1, T)): #iterar desde el último tiempo hacia atrás
        mejor_estado = psi[t][mejor_estado] #encontrar el mejor estado anterior
        mejor_camino[t-1] = mejor_estado #asignar el mejor estado al tiempo t-1

    return mejor_camino #devolver el mejor camino

#aplicar explicación (Viterbi) para encontrar la secuencia más probable
secuencia_mas_probable = explicacion(observaciones) #usar la función de explicación para encontrar la secuencia más probable

#mostrar la secuencia de estados más probable
print("\nSecuencia de estados más probable (Explicación):")
for t, estado in enumerate(secuencia_mas_probable): #iterar sobre la secuencia más probable
    print(f"Tiempo {t+1}: {estado}") #imprimir el estado más probable en cada tiempo

#ejemplo de salida:
# Creencias después de cada observación (Filtrado):
# Tiempo 1 | {'Soleado': 0.8461538461538461, 'Lluvioso': 0.15384615384615383}       
# Tiempo 2 | {'Soleado': 0.9215686274509804, 'Lluvioso': 0.07843137254901962}       
# Tiempo 3 | {'Soleado': 0.28445747800586507, 'Lluvioso': 0.7155425219941348}       
# Tiempo 4 | {'Soleado': 0.09016981583353266, 'Lluvioso': 0.9098301841664673}       

# Predicción a 2 pasos adelante: {'Soleado': 0.4725424539583832, 'Lluvioso': 0.5274575460416168}

# Creencias suavizadas (usando observaciones futuras):
# Tiempo 1 | {'Soleado': 0.8705519678971007, 'Lluvioso': 0.12944803210289932}       
# Tiempo 2 | {'Soleado': 0.7981344176034442, 'Lluvioso': 0.2018655823965558}        
# Tiempo 3 | {'Soleado': 0.1392011480507056, 'Lluvioso': 0.8607988519492944}        
# Tiempo 4 | {'Soleado': 0.09016981583353266, 'Lluvioso': 0.9098301841664673}       

# Secuencia de estados más probable (Explicación):
# Tiempo 1: Lluvioso
# Tiempo 2: Lluvioso
# Tiempo 3: Lluvioso
# Tiempo 4: Lluvioso
#como se puede observar, el suavizado mejora la estimación de los estados pasados al incorporar información futura, mientras que el filtrado solo utiliza información pasada. La explicación (Viterbi) encuentra la secuencia más probable de estados dados los datos observados.
#El suavizado y la explicación son útiles para mejorar la estimación de estados pasados y encontrar la secuencia más probable de estados, respectivamente.
#Estos algoritmos son fundamentales en el procesamiento de señales, la robótica y la inteligencia artificial, donde es necesario inferir estados ocultos a partir de observaciones ruidosas y secuenciales.
#El filtrado, la predicción, el suavizado y la explicación son herramientas poderosas para trabajar con sistemas dinámicos y secuencias de datos en el tiempo.