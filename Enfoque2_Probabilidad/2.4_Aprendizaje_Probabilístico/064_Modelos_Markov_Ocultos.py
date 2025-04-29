#Modelos de Markov Ocultos (HMM)
#es un modelo probabilístico que describe un sistema que:
#evoluciona a lo largo del tiempo (como una cadena de Markov).
#tiene estados ocultos: no podemos ver directamente el estado real del sistema
#Solo se observan "síntomas" o "señales" relacionados a esos estados.
#Funcionamiento: El sistema está en alguno de estos estados, pero no podemos verlo directamente,
#                Lo que podemos ver depende de en qué estado está el sistema.
#                Probabilidad: Matriz de transición A: Probabilidad de pasar de un estado a otro.
#                              Matriz de emisión B: Probabilidad de observar cierto valor dado el estado oculto.
#                              Vector inicial π: Probabilidad de empezar en cada estado.
#Aplicaciones: reconocimiento de voz, procesamiento de lenguaje natural, análisis de secuencias biológicas, etc.

#Ejemplo de HMM
#Estados ocultos: Soleado o Lluvioso.
#Observaciones: Caminar, Comprar, Limpiar.

#librerías necesarias
import numpy as np #para operaciones matemáticas y matrices

#Definir los parámetros del modelo
estados = ['Soleado', 'Lluvioso'] #Estados ocultos
observaciones = ['Caminar', 'Comprar', 'Limpiar'] #Observaciones

#Matriz de transición A: Probabilidad de pasar de un estado a otro
A = np.array([ 
    [0.8, 0.2],
    [0.4, 0.6]
])

#Matriz de emisión B: Probabilidad de observar cierto valor dado el estado oculto
B = np.array([
    [0.6, 0.3, 0.1],
    [0.1, 0.4, 0.5]
])

pi = np.array([0.7, 0.3]) #Vector inicial: Probabilidad de empezar en cada estado

np.random.seed(42) #Para reproducibilidad
n_pasos = 10 #número de pasos a simular

secuencia_estados = [] #Lista para almacenar la secuencia de estados ocultos
secuencia_observaciones = [] #Lista para almacenar la secuencia de observaciones

#Primer estado
estado_actual = str(np.random.choice(estados, p=pi)) #Elegir el primer estado basado en la probabilidad inicial
secuencia_estados.append(estado_actual) #almacenar el primer estado en la secuencia

indice_estado = estados.index(estado_actual) #Obtener el índice del estado actual
observacion = str(np.random.choice(observaciones, p=B[indice_estado])) #Elegir la primera observación basada en el estado actual
secuencia_observaciones.append(observacion) #almacenar la primera observación en la secuencia

# Simulación de los siguientes estados
for _ in range(n_pasos - 1):
    indice_estado = estados.index(estado_actual) #Obtener el índice del estado actual
    estado_actual = str(np.random.choice(estados, p=A[indice_estado])) #Elegir el siguiente estado basado en la matriz de transición
    secuencia_estados.append(estado_actual) #almacenar el nuevo estado en la secuencia

    indice_estado = estados.index(estado_actual) #Obtener el índice del nuevo estado
    observacion = str(np.random.choice(observaciones, p=B[indice_estado])) #Elegir la observación basada en el nuevo estado
    secuencia_observaciones.append(observacion) #almacenar la nueva observación en la secuencia

#mostrar resultado
print("Secuencia de estados ocultos:")
print(secuencia_estados) #imprimir la secuencia de estados ocultos

print("\nSecuencia de observaciones:")
print(secuencia_observaciones) #imprimir la secuencia de observaciones

#Ejemplo de salida:
# Secuencia de estados ocultos:
# ['Soleado', 'Soleado', 'Soleado', 'Soleado', 'Soleado', 'Soleado', 'Lluvioso', 'Soleado', 'Soleado', 'Soleado']

# Secuencia de observaciones:
# ['Limpiar', 'Caminar', 'Caminar', 'Comprar', 'Comprar', 'Limpiar', 'Comprar', 'Caminar', 'Caminar', 'Caminar']
#El modelo ha generado una secuencia de estados ocultos y observaciones basadas en las probabilidades definidas.
#Los estados ocultos son Soleado o Lluvioso, y las observaciones son Caminar, Comprar o Limpiar.
#La secuencia de estados ocultos y observaciones puede variar en cada ejecución debido a la aleatoriedad introducida por el uso de np.random.choice.
#Aunque vemos las observaciones, los estados ocultos son teóricos (en una aplicación real no sabríamos cuáles son).