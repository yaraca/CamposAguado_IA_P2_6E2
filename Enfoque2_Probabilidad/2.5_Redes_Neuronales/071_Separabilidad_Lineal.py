#Separabilidad Lineal
#Un conjunto de datos es linealmente separable si se puede trazar una línea (en 2D), un plano (en 3D), o un hiperplano (en más dimensiones) que divida perfectamente las clases sin errores.
#Por ejemplo el problema AND es linealmente separable.
#y el problema XOR no es linealmente separable.
#es importante porque  redes neuronales y modelos como el perceptrón, la separación lineal determina si una sola neurona (o modelo lineal) es suficiente para resolver el problema.
#Si los datos son linealmente separables, un modelo lineal puede aprender a clasificarlos correctamente. Si no lo son, se necesitarán modelos más complejos (como redes neuronales profundas) para resolver el problema.
#Aplicaciones: Clasificaición de imágenes, detección de spam, reconocimiento de voz, diagnostico medico, etc.
#Funcionamiento: 
#Definir puntos de entrada X y etiquetas y.
#Usar un modelo lineal (como perceptrón) para ver si puede encontrar un hiperplano separador.
#El perceptrón ajusta sus pesos y sesgo para minimizar el error entre las predicciones y las etiquetas reales.
#Finalmente, evaluar la clasificación de los puntos.

#ejemplo de separabilidad lineal

#librerias necesarias
import numpy as np #libreria para operaciones matematicas y matrices
import matplotlib.pyplot as plt #libreria para graficar
from sklearn.linear_model import Perceptron #libreria para el modelo Perceptrón

#Datos de entrada (2D)
X = np.array([
    [2, 1],  #Clase 0
    [1, 3],  #Clase 0
    [5, 4],  #Clase 1
    [6, 2],  #Clase 1
])

#etiquetas: 0 o 1
y = np.array([0, 0, 1, 1]) 

#crear un modelo Perceptrón (modelo lineal)
model = Perceptron(max_iter=1000, eta0=0.1) #max_iter: número máximo de iteraciones, eta0: tasa de aprendizaje
model.fit(X, y)  #entrenar el modelo

#predecr las clases para los puntos de entrenamiento
predicciones = model.predict(X) #predicciones para los puntos de entrada X

#mostrar resultados
print("Pesos del modelo:", model.coef_)
print("Término de sesgo:", model.intercept_)
print("Predicciones:", predicciones)

#graficar los puntos y la línea de decisión
for i in range(len(X)): #iterar por cada punto de entrada
    if y[i] == 0: #si la etiqueta es 0
        plt.scatter(X[i, 0], X[i, 1], color='red', label='Clase 0' if i == 0 else "") #graficar el punto en rojo
    else: #si la etiqueta es 1
        plt.scatter(X[i, 0], X[i, 1], color='blue', label='Clase 1' if i == 2 else "") #graficar el punto en azul

#linea de decisión: w0*x + w1*y + b = 0 → y = -(w0/w1)*x - (b/w1)
w = model.coef_[0] #coeficientes del modelo (pesos)
b = model.intercept_[0] #término de sesgo (intercepto)
x_line = np.linspace(0, 7, 10) #valores de x para la línea de decisión
y_line = -(w[0]/w[1]) * x_line - (b/w[1]) #valores de y para la línea de decisión
plt.plot(x_line, y_line, color='black', linestyle='--', label='Frontera de decisión') #graficar la línea de decisión

plt.xlabel("X1")
plt.ylabel("X2")
plt.title("Separabilidad Lineal con Perceptrón")
plt.legend()
plt.grid(True)
plt.show()

#Ejemplo de salida:
#Pesos del modelo: [[ 0.4 -0.3]]
# Término de sesgo: [-0.8]
# Predicciones: [0 0 1 1]
#El grafico muestra los puntos de entrada y la línea de decisión que separa las clases 0 y 1.
#Esta salida indica que el modelo ha aprendido a clasificar correctamente los puntos de entrada en dos clases separadas por una línea.
#Los pesos y el término de sesgo indican la orientación y posición de la línea de decisión en el espacio 2D.
#La línea de decisión se ha trazado en el gráfico, mostrando cómo el modelo separa las dos clases. Los puntos rojos representan la clase 0 y los puntos azules representan la clase 1.
#La línea negra discontinua representa la frontera de decisión aprendida por el modelo Perceptrón.
#Esta línea separa las dos clases de manera que los puntos de clase 0 están por un lado y los puntos de clase 1 están por el otro lado.
#Significa que los datos son linealmente separables y el modelo funcionó correctamente