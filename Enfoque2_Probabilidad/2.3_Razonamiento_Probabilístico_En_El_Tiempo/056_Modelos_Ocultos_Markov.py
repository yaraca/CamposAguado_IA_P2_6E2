#Modelos Ocultos de Markov (HMM)
#es un modelo probabilístico para secuencias temporales en donde:
# El sistema es un proceso de Markov con estados ocultos (no observamos directamente el estado real).
# Solo podemos observar salidas (observaciones) que dependen de esos estados ocultos.
#por ejemplo Si alguien lleva paraguas todos los días, puedes inferir si el clima fue "lluvioso" o "soleado", aunque nunca viste el clima directamente
#Un HMM se define por:
#Estados ocultos (S): Los estados verdaderos que no vemos directamente (ej., "soleado", "lluvioso").
#Observaciones (O): Lo que vemos (ej., "persona con paraguas").
#Probabilidades de transición: Probabilidad de cambiar de un estado a otro.
#Probabilidades de emisión: Probabilidad de observar algo dado un estado.
#Distribución inicial: Probabilidad de empezar en un estado dado.
#Se puede aplicar en: reconocimiento de voz, procesamiento de lenguaje natural, bioinformática, vision artificial, etc.

#Ejemplo de algoritmo de modelos ocultos de Markov (HMM)
# Estados ocultos: Soleado, Lluvioso
# Observaciones: Paraguas, No paraguas
# Secuencia observada: ["Paraguas", "Paraguas", "No paraguas"]

#librerías necesarias
import numpy as np #para operaciones numéricas

#definir los estados
estados = ['Soleado', 'Lluvioso']

#Observaciones posibles
observaciones = ['No Paraguas', 'Paraguas']

#Secuencia observada
observaciones_seq = ['Paraguas', 'Paraguas', 'No Paraguas']

#Probabilidad inicial de estar en cada estado
prob_inicial = {'Soleado': 0.5, 'Lluvioso': 0.5} #50% de probabilidad de que el día comience soleado y 50% lluvioso

#Matriz de transición de estados
prob_transicion = {
    'Soleado': {'Soleado': 0.8, 'Lluvioso': 0.2}, #80% de probabilidad de que un día soleado siga siendo soleado y 20% de que cambie a lluvioso
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6} #40% de probabilidad de que un día lluvioso cambie a soleado y 60% de que siga lluvioso
}

#Matriz de emisión (probabilidad de observaciones dado el estado)
prob_emision = {
    'Soleado': {'No Paraguas': 0.9, 'Paraguas': 0.1}, #90% de probabilidad de no llevar paraguas en un día soleado y 10% de llevarlo
    'Lluvioso': {'No Paraguas': 0.3, 'Paraguas': 0.7} #30% de probabilidad de no llevar paraguas en un día lluvioso y 70% de llevarlo
}

#Función Forward para calcular la probabilidad de la secuencia observada
def forward(estados, observaciones_seq, prob_inicial, prob_transicion, prob_emision):
    alpha = [] #lista para almacenar los mensajes hacia adelante (α)
    #Inicialización
    alpha_t = {} #mensaje hacia adelante en el tiempo t
    for estado in estados: #iterar sobre los estados
        alpha_t[estado] = prob_inicial[estado] * prob_emision[estado][observaciones_seq[0]] #calcular el mensaje hacia adelante para el primer estado
    alpha.append(alpha_t) #agregar el mensaje hacia adelante inicial a la lista

    #Recursión
    for t in range(1, len(observaciones_seq)): #iterar sobre la secuencia de observaciones desde el segundo elemento
        alpha_t = {} #mensaje hacia adelante en el tiempo t
        for estado_actual in estados: #iterar sobre los estados
            suma = sum(alpha[t-1][estado_prev] * prob_transicion[estado_prev][estado_actual]  # calcular la suma de los mensajes hacia adelante del tiempo anterior
                       for estado_prev in estados) #iterar sobre los estados anteriores
            alpha_t[estado_actual] = suma * prob_emision[estado_actual][observaciones_seq[t]] #calcular el mensaje hacia adelante para el estado actual
        alpha.append(alpha_t) #agregar el mensaje hacia adelante al tiempo t a la lista

    #Terminación
    prob_total = sum(alpha[-1][estado] for estado in estados) #probabilidad total de observar la secuencia
    
    return alpha, prob_total #devolver la lista de mensajes hacia adelante y la probabilidad total

#ejecutar el algoritmo foward
alpha, probabilidad_total = forward(estados, observaciones_seq, prob_inicial, prob_transicion, prob_emision) #llamar a la función para calcular la probabilidad de la secuencia observada

#mostrar resultados
print("Resultados paso a paso:")
for t, alpha_t in enumerate(alpha): #iterar sobre los mensajes hacia adelante
    print(f"Tiempo {t} (Observación: {observaciones_seq[t]}):") #imprimir el tiempo y la observación
    for estado in estados: #iterar sobre los estados
        print(f"  P({estado}) = {alpha_t[estado]:.4f}") #imprimir la probabilidad de cada estado

print(f"\nProbabilidad total de observar la secuencia: {probabilidad_total:.4f}") 

#ejemplo de salida:
# Resultados paso a paso:
# Tiempo 0 (Observación: Paraguas):
#   P(Soleado) = 0.0500
#   P(Lluvioso) = 0.3500
# Tiempo 1 (Observación: Paraguas):
#   P(Soleado) = 0.0180
#   P(Lluvioso) = 0.1540
# Tiempo 2 (Observación: No Paraguas):
#   P(Soleado) = 0.0684
#   P(Lluvioso) = 0.0288

# Probabilidad total de observar la secuencia: 0.0972
#como se puede ver, la probabilidad total de observar la secuencia es 0.0972, lo que indica que es poco probable que ocurra esta secuencia de observaciones dada la configuración del modelo.
#esto puede ser útil para evaluar la calidad del modelo y ajustar los parámetros si es necesario.

