#Retropropagación del Error
#Es un algoritmo de entrenamiento supervisado para redes neuronales multicapa. 
#Se utiliza para ajustar los pesos sinápticos de cada neurona en función del error cometido por la red.
#funcionamiento:
#Propagación hacia adelante (forward pass): Se pasa la entrada a través de la red y se calcula la salida.
#Cálculo del error: Se compara la salida de la red con la salida esperada (error).
#Retropropagación (backward pass): Se propaga el error hacia atrás, desde la salida hasta las capas anteriores, calculando los gradientes de los pesos.
#Actualización de pesos: Se ajustan los pesos utilizando gradiente descendente (o alguna variante).
#formulas clave: 
#Error de salida: e = Yreal - Ypredicha
#actualización de pesos: Wnuevo = Wviejo + n*error*entrada
#donde n es la tasa de aprendizaje, error es la diferencia entre la salida real y la predicha, y entrada es la entrada a la neurona.
#aplicaciones: reconocimiento de patrones, clasificación, juegos, robotica, etc.

#ejemplo de retropropagación del error
#resolver el problema XOR con red multicapa usando retropropagación manual.

#librerias necesarias
import numpy as np #libreria para operaciones matematicas y matrices

#función de activación: sigmoide y su derivada
def sigmoid(x): 
    return 1 / (1 + np.exp(-x)) #función sigmoide

def sigmoid_derivada(x):
    return x * (1 - x) #derivada de la función sigmoide

#datosde entrenamiento (XOR)
entradas = np.array([[0,0], [0,1], [1,0], [1,1]]) #Entradas XOR
salidas_esperadas = np.array([[0], [1], [1], [0]]) #salidas esperadas XOR

#inicialización de pesos y parámetros
np.random.seed(42) #fijar la semilla para reproducibilidad
pesos_entrada_oculta = np.random.uniform(size=(2, 4))  #2 entradas -> 4 neuronas ocultas
pesos_oculta_salida = np.random.uniform(size=(4, 1))  #4 ocultas -> 1 salida
bias_oculta = np.random.uniform(size=(1, 4)) #bias para las neuronas ocultas (bias es un término adicional que se suma a la entrada de la neurona para ajustar la salida)
bias_salida = np.random.uniform(size=(1, 1)) #bias para la neurona de salida

tasa_aprendizaje = 0.5 #tasa de aprendizaje (learning rate)
epocas = 10000 #número de épocas (iteraciones) para el entrenamiento

#entrenamiento de la red neuronal
for epoca in range(epocas): #entrenamiento por épocas
    #propagación hacia adelante
    capa_oculta_activacion = sigmoid(np.dot(entradas, pesos_entrada_oculta) + bias_oculta) #capa oculta activada
    salida = sigmoid(np.dot(capa_oculta_activacion, pesos_oculta_salida) + bias_salida) #salida activada

    #error y retropropagación
    error = salidas_esperadas - salida #calculo del error (diferencia entre la salida esperada y la salida real)
    d_salida = error * sigmoid_derivada(salida) #derivada de la salida (error multiplicado por la derivada de la función sigmoide)
 
    error_oculta = d_salida.dot(pesos_oculta_salida.T) #propagación del error hacia atrás (desde la salida a la capa oculta)
    d_oculta = error_oculta * sigmoid_derivada(capa_oculta_activacion) #derivada de la capa oculta (error multiplicado por la derivada de la función sigmoide)

    #actualización de pesos
    pesos_oculta_salida += capa_oculta_activacion.T.dot(d_salida) * tasa_aprendizaje #actualiza los pesos de la capa oculta a la salida
    bias_salida += np.sum(d_salida, axis=0, keepdims=True) * tasa_aprendizaje #actualiza el bias de la salida

    pesos_entrada_oculta += entradas.T.dot(d_oculta) * tasa_aprendizaje #actualiza los pesos de la entrada a la capa oculta
    bias_oculta += np.sum(d_oculta, axis=0, keepdims=True) * tasa_aprendizaje #actualiza el bias de la capa oculta

#predicción final
print("Predicción final después del entrenamiento:")
print(np.round(salida, 3)) #imprime la salida final redondeada a 3 decimales

#Ejemplo de salida:
# Predicción final después del entrenamiento:
# [[0.016]
#  [0.983]
#  [0.988]
#  [0.015]]
#La salida muestra que la red neuronal ha aprendido a clasificar correctamente el problema XOR
#  donde la salida es 1 solo cuando una de las entradas es 1, pero no ambas.
#  La red neuronal ha ajustado sus pesos y sesgos para minimizar el error cuadrático entre la salida real y la esperada.
#  La salida final es cercana a 0 para las entradas (0,0) y (1,1), y cercana a 1 para las entradas (0,1) y (1,0).
