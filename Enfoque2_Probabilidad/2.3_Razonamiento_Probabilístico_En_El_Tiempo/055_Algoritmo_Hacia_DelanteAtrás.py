#Algoritmo hacia adelante y hacia atrás
#se utiliza en modelos ocultos de Markov (HMM) para calcular probabilidades posteriores de los estados ocultos a partir de observaciones.
#Su objetivo principal es estimar de manera eficiente la probabilidad de estar en un estado en un momento dado, considerando todas las observaciones (pasadas y futuras).
#Funcionamiento: 
#Hacia adelante: Calcula para cada instante de tiempo t, la probabilidad conjunta de:
#                Haber observado la secuencia de observaciones hasta t, Estar en cierto estado X1 (esto se llama mensaje hacia adelante αt(Xt)).
#Hacia atrás: Calcula para cada instante de tiempo t, la probabilidad conjunta de:
#                ver todas las observaciones futuras dadas el estado Xt (esto se llama mensaje hacia atrás βt(Xt)).
#Formulas basicas: 
#hacia adelante: αt(xt) = P(O1, O2, ..., Ot, Xt)
#hacia atrás: βt(xt) = P(Ot+1, Ot+2, ..., OT|Xt) 
#posterior: P(xt|O1:T) ∝ αt(xt) * βt(xt)
#donde O1:T es la secuencia de observaciones desde el tiempo 1 hasta T. 
#Se puede aplicar en: reconocimiento de voz, procesamiento de lenguaje natural, bioinformática, etc.

#Ejemplo de algoritmo hacia adelante y hacia atrás
#modelo oculto de Markov sobre el clima (Soleado o Lluvioso) basado en si alguien lleva paraguas.

#librerías necesarias
import numpy as np

#definir los estados ocultos
estados = ['Soleado', 'Lluvioso'] 

#Observaciones posibles
observaciones = ['No Paraguas', 'Paraguas'] 

#Probabilidad inicial de cada estado
prob_inicial = {'Soleado': 0.6, 'Lluvioso': 0.4} #Ejemplo: 60% de probabilidad de que el día comience soleado y 40% lluvioso

#Matriz de transición entre estados
prob_transicion = {
    'Soleado': {'Soleado': 0.7, 'Lluvioso': 0.3}, #70% de probabilidad de que un día soleado siga siendo soleado y 30% de que cambie a lluvioso
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6} #40% de probabilidad de que un día lluvioso cambie a soleado y 60% de que siga lluvioso
}

#Matriz de emisión: probabilidad de observar cada evidencia en cada estado
prob_emision = {
    'Soleado': {'No Paraguas': 0.9, 'Paraguas': 0.1}, #90% de probabilidad de no llevar paraguas en un día soleado y 10% de llevarlo
    'Lluvioso': {'No Paraguas': 0.2, 'Paraguas': 0.8} #20% de probabilidad de no llevar paraguas en un día lluvioso y 80% de llevarlo
}

#Secuencia de observaciones (por ejemplo, vimos: paraguas, no paraguas, paraguas)
observacion_seq = ['Paraguas', 'No Paraguas', 'Paraguas']

#función de Algoritmo hacia adelante
def forward(estados, observacion_seq, prob_inicial, prob_transicion, prob_emision):
    alpha = [] # Lista para almacenar los mensajes hacia adelante (α)

    #inicialización
    alpha_t = {} #mensaje hacia adelante en el tiempo t
    for estado in estados: #iterar sobre los estados
        alpha_t[estado] = prob_inicial[estado] * prob_emision[estado][observacion_seq[0]] #calcular el mensaje hacia adelante para el primer estado
    alpha.append(alpha_t) #agregar el mensaje hacia adelante inicial a la lista

    #recursión
    for t in range(1, len(observacion_seq)): #iterar sobre la secuencia de observaciones desde el segundo elemento
        alpha_t = {} #mensaje hacia adelante en el tiempo t
        for estado_actual in estados: #iterar sobre los estados
            suma = sum(alpha[t-1][estado_anterior] * prob_transicion[estado_anterior][estado_actual] # calcular la suma de los mensajes hacia adelante del tiempo anterior
                       for estado_anterior in estados) #iterar sobre los estados anteriores
            alpha_t[estado_actual] = suma * prob_emision[estado_actual][observacion_seq[t]] #calcular el mensaje hacia adelante para el estado actual
        alpha.append(alpha_t) #agregar el mensaje hacia adelante al tiempo t a la lista

    return alpha #devolver la lista de mensajes hacia adelante

#función Algoritmo hacia atrás
def backward(estados, observacion_seq, prob_transicion, prob_emision):
    beta = [] #lista para almacenar los mensajes hacia atrás (β)

    #Inicialización
    beta_T = {estado: 1 for estado in estados} #mensaje hacia atrás en el tiempo T (último tiempo)
    beta.insert(0, beta_T) #agregar el mensaje hacia atrás inicial a la lista

    #Recursión hacia atrás
    for t in reversed(range(len(observacion_seq) - 1)): #iterar sobre la secuencia de observaciones en orden inverso
        beta_t = {} #mensaje hacia atrás en el tiempo t
        for estado_actual in estados: #iterar sobre los estados
            suma = sum(prob_transicion[estado_actual][estado_siguiente] * # calcular la suma de los mensajes hacia atrás del tiempo siguiente
                       prob_emision[estado_siguiente][observacion_seq[t+1]] * 
                       beta[0][estado_siguiente]
                       for estado_siguiente in estados) #iterar sobre los estados siguientes
            beta_t[estado_actual] = suma #calcular el mensaje hacia atrás para el estado actual
        beta.insert(0, beta_t) #agregar el mensaje hacia atrás al tiempo t a la lista

    return beta #devolver la lista de mensajes hacia atrás

#Combinar forward y backward para calcular la distribución posterior
def forward_backward(estados, observacion_seq, prob_inicial, prob_transicion, prob_emision):
    #Calcula la distribución posterior de los estados ocultos dado la secuencia de observaciones
    alpha = forward(estados, observacion_seq, prob_inicial, prob_transicion, prob_emision) #llamar a la función hacia adelante
    beta = backward(estados, observacion_seq, prob_transicion, prob_emision) #llamar a la función hacia atrás

    posterior = [] #lista para almacenar las distribuciones posteriores
    for t in range(len(observacion_seq)): #iterar sobre la secuencia de observaciones
        posterior_t = {} #distribución posterior en el tiempo t
        normalizador = sum(alpha[t][estado] * beta[t][estado] for estado in estados) #calcular el normalizador
        for estado in estados: #iterar sobre los estados
            posterior_t[estado] = (alpha[t][estado] * beta[t][estado]) / normalizador #calcular la distribución posterior para el estado actual
        posterior.append(posterior_t) #agregar la distribución posterior al tiempo t a la lista
    return posterior #devolver la lista de distribuciones posteriores

#ejecutrar el algoritmo
posterior = forward_backward(estados, observacion_seq, prob_inicial, prob_transicion, prob_emision)

#mostrar resultados
print("Probabilidades posteriores:")
for t, dist in enumerate(posterior): #iterar sobre las distribuciones posteriores
    print(f"Tiempo {t}:") #imprimir el tiempo
    for estado in estados: #iterar sobre los estados
        print(f"  {estado}: {dist[estado]:.4f}") #imprimir la probabilidad posterior para cada estado

#ejemplo de salida:
# Probabilidades posteriores:
# Tiempo 0:
#   Soleado: 0.1962
#   Lluvioso: 0.8038
# Tiempo 1:
#   Soleado: 0.6847
#   Lluvioso: 0.3153
# Tiempo 2:
#   Soleado: 0.1789
#   Lluvioso: 0.8211
# Al inicio, es más probable que esté "Lluvioso" (por la observación de "Paraguas").
# Luego cambia a "Soleado" (no vimos paraguas).
# Luego regresa a "Lluvioso" (vimos paraguas otra vez).
# Esto muestra cómo el algoritmo puede inferir la probabilidad de los estados ocultos (clima) a partir de las observaciones (uso del paraguas).
