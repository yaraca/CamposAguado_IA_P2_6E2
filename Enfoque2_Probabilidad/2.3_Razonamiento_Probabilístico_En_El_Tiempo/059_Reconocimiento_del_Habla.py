#Reconocimiento del habla
#El Reconocimiento del Habla consiste en convertir señales acústicas (ondas de sonido) en texto.
#Esto es una tarea difici porque:
#El sonido es ruidoso y variable, Una misma palabra puede sonar diferente entre personas, Se pronuncian sonidos similares de formas distintas.
#Para resolverlo, se usa un enfoque de Redes Bayesianas Dinámicas, en particular los Modelos Ocultos de Markov (HMMs), que son un tipo de Red Bayesiana que evoluciona en el tiempo.
#Funcionamiento básico:
#Modelo acústico: Relaciona fragmentos de audio (observaciones) con fonemas o palabras (estados ocultos).
#Modelo de lenguaje: Define la probabilidad de secuencias de palabras.
#Inferencia: A partir del audio grabado (observaciones ruidosas), se infiere la secuencia más probable de palabras o fonemas.
#Algoritmos comunes: Hacia adelante-atrás (Forward-Backward): para calcular probabilidades, Viterbi: para encontrar la secuencia más probable de palabras.
#Aplicaciones: Asistentes virtuales (Siri, Alexa, Google Assistant), sistemas de dictado, traduccion simultanea de voz, etc.

#Ejemplo de reconocimiento del habla
#simulación educativa de cómo se puede hacer un reconocimiento de palabras sencillas usando un modelo oculto de Markov (HMM).

#librerias necesarias
import numpy as np #para operaciones numéricas

#definir el vocabulario y las observaciones posibles
estados = ['Hola', 'Mundo'] #palabras que queremos reconocer
observaciones = ['h', 'o', 'l', 'a', 'm', 'u', 'n', 'd', 'o'] #sonidos que pueden ser emitidos (fonemas o letras)

#matriz de transición (probabilidad de pasar de un estado a otro)
P_transicion = np.array([
    [0.7, 0.3],  #Probabilidad de quedarse en 'Hola' o ir a 'Mundo' (70% a 'Hola', 30% a 'Mundo')
    [0.4, 0.6]   #Probabilidad de ir de 'Mundo' a 'Hola' o quedarse en 'Mundo' (40% a 'Hola', 60% a 'Mundo')
])

#Matriz de emisión (probabilidad de que un estado emita un símbolo observado)
P_emision = {
    'Hola': {'h': 0.3, 'o': 0.3, 'l': 0.2, 'a': 0.2, 'm': 0.0, 'u': 0.0, 'n': 0.0, 'd': 0.0}, #Probabilidades de emitir cada símbolo dado el estado 'Hola'
    'Mundo': {'h': 0.0, 'o': 0.3, 'l': 0.0, 'a': 0.0, 'm': 0.3, 'u': 0.2, 'n': 0.1, 'd': 0.1} #Probabilidades de emitir cada símbolo dado el estado 'Mundo'
}

#Secuencia observada (simulación del audio convertido en símbolos)
secuencia_observada = ['h', 'o', 'l', 'a', 'm', 'u', 'n', 'd', 'o']

#Función Viterbi para encontrar la secuencia más probable
def viterbi(observaciones, estados, P_transicion, P_emision, secuencia_observada): #definir la función Viterbi
    T = len(secuencia_observada) #longitud de la secuencia observada
    N = len(estados) #número de estados (palabras)
    
    #inicializar las matrices
    V = np.zeros((N, T))  # V[i,t] = probabilidad más alta de cualquier secuencia que termine en estado i en tiempo t
    path = np.zeros((N, T), dtype=int) # path[i,t] = estado anterior en la mejor secuencia que termina en estado i en tiempo t
    
    #inicialización: t=0
    for i in range(N): #iterar sobre los estados
        V[i,0] = P_emision[estados[i]].get(secuencia_observada[0], 1e-6) #probabilidad de emitir el primer símbolo dado el estado
        path[i,0] = i #guardar el estado inicial
    
    #iteración: t=1 a T-1
    for t in range(1, T): #iterar sobre la secuencia de observaciones desde el segundo elemento
        for j in range(N): #iterar sobre los estados
            prob_transiciones = V[:, t-1] * P_transicion[:, j] * P_emision[estados[j]].get(secuencia_observada[t], 1e-6) #calcular la probabilidad de transición y emisión
            V[j,t] = np.max(prob_transiciones)  #guardar la probabilidad máxima
            path[j,t] = np.argmax(prob_transiciones) #guardar el estado anterior que dio la probabilidad máxima
    
    #Retroceso: encontrar la mejor ruta
    mejor_camino = np.zeros(T, dtype=int) #inicializar el mejor camino
    mejor_camino[T-1] = np.argmax(V[:, T-1]) #estado final con la probabilidad más alta
    
    for t in range(T-2, -1, -1): #iterar hacia atrás para encontrar el mejor camino
        mejor_camino[t] = path[mejor_camino[t+1], t+1] #estado anterior en el mejor camino
    
    #convertir a nombres de estados
    secuencia_estimada = [estados[i] for i in mejor_camino] #convertir índices a nombres de estados
    
    return secuencia_estimada #devolver la secuencia estimada

#ejecutar el algoritmo
resultado = viterbi(observaciones, estados, P_transicion, P_emision, secuencia_observada) #llamar a la función Viterbi para encontrar la secuencia más probable de estados

#mostrar resultados
print("Secuencia observada:") 
print(secuencia_observada)
print("\nSecuencia de estados más probable:")
print(resultado)

#Ejemplo de salida:
# Secuencia observada:
# ['h', 'o', 'l', 'a', 'm', 'u', 'n', 'd', 'o']
# Secuencia de estados más probable:
# ['Hola', 'Hola', 'Hola', 'Hola', 'Mundo', 'Mundo', 'Mundo', 'Mundo', 'Mundo']
#La salida muestra que la secuencia de estados más probable es "Hola" seguido de "Mundo", lo que indica que el modelo ha reconocido correctamente las palabras en la secuencia observada.
