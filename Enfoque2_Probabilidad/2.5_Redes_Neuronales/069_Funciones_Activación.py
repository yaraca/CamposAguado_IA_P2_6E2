#Funciones de Activación
#son las encargadas de decidir si una neurona se activa o no, basándose en la información que recibe.
#Sin función de activación, una red neuronal solo haría operaciones lineales (suma y multiplicación).
#La activación introduce no linealidad, permitiendo aprender cosas más complejas
# Cuando una neurona recibe una entrada ponderada (peso × entrada + sesgo), la función de activación transforma esa suma en un número de salida:
# Si la activación es alta ➔ la neurona "se activa" (sale un valor grande).
#Si la activación es baja ➔ la neurona "se apaga" (sale un valor pequeño o cero).
#Tipos de funciones de activación:
#Sigmoid: Saca valores entre 0 y 1. Ideal para probabilidades. f(x) = 1 / (1 + e^(-x)).
#ReLU (Rectified Linear Unit): 	Convierte negativos en 0. Es muy rápida. f(x) = max(0, x).
#Tanh (Tangente hiperbólica): Saca valores entre -1 y 1. Mejor centrado que sigmoid. f(x) = tanh(x).
#Softmax: Convierte vectores en probabilidades. (usado en clasificación multinomial). f(xi) = e^(xi) / ∑(e^(xj)) para j en todas las clases.
#Aplicaciones: reconocimiento de imágenes, procesamiento de lenguaje natural, juegos, etc.

#Ejemplo de funciones de activación

#librerías necesarias
import numpy as np #para operaciones matemáticas y matrices
import matplotlib.pyplot as plt #para graficar

#Función Sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x)) # Función sigmoide: transforma valores a un rango entre 0 y 1

#Función ReLU
def relu(x):
    return np.maximum(0, x) #función ReLU: devuelve 0 para valores negativos y el mismo valor para positivos

#Función Tanh
def tanh(x):
    return np.tanh(x) #función tangente hiperbólica: transforma valores a un rango entre -1 y 1

#Función Softmax (aplicada sobre un vector)
def softmax(x):
    exp_x = np.exp(x - np.max(x))  #restar el máximo para evitar números grandes
    return exp_x / np.sum(exp_x) #función softmax: convierte un vector en probabilidades

# Generamos datos para probar
x = np.linspace(-10, 10, 100) #generar 100 puntos entre -10 y 10

#aplicar cada función
y_sigmoid = sigmoid(x) #aplicar la función sigmoide
y_relu = relu(x) #aplicar la función ReLU
y_tanh = tanh(x) #aplicar la función tangente hiperbólica
y_softmax = softmax(x)  # Solo aplicable al vector completo

#graficar los resultados
plt.figure(figsize=(12, 8)) #tamaño de la figura

#Subplot 1: Sigmoid
plt.subplot(2, 2, 1) #crear un subplot para la función sigmoide con 2 filas y 2 columnas y este en la posición 1
plt.plot(x, y_sigmoid, label="Sigmoid", color="blue") #graficar la función sigmoide
plt.title("Función Sigmoid")
plt.grid(True)

#Subplot 2: ReLU
plt.subplot(2, 2, 2) #crear un subplot para la función ReLU con 2 filas y 2 columnas y este en la posición 2
plt.plot(x, y_relu, label="ReLU", color="green")
plt.title("Función ReLU")
plt.grid(True)

#Subplot 3: Tanh
plt.subplot(2, 2, 3) #crear un subplot para la función tangente hiperbólica con 2 filas y 2 columnas y este en la posición 3
plt.plot(x, y_tanh, label="Tanh", color="red")
plt.title("Función Tanh")
plt.grid(True)

#Subplot 4: Softmax
plt.subplot(2, 2, 4) #crear un subplot para la función softmax con 2 filas y 2 columnas y este en la posición 4
plt.plot(x, y_softmax, label="Softmax", color="purple")
plt.title("Función Softmax")
plt.grid(True)

plt.tight_layout() #ajustar el espaciado entre subplots
plt.show()

#ejemplo de salida graficas:
#Sigmoid ➔ curva en forma de "S", entre 0 y 1.
#ReLU ➔ línea recta en 0, todo negativo se convierte en 0. Crece linealmente para positivos.
#Tanh ➔ curva en forma de "S", entre -1 y 1. Más centrada que la sigmoide.
#Softmax ➔ convierte los valores en probabilidades (todos entre 0 y 1 y la suma da 1).
