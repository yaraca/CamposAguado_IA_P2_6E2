#Redes Multicapa (MLP)
#es una arquitectura de aprendizaje profundo compuesta por:
#Capa de entrada: Recibe los datos.
#Capas ocultas: Procesan la información (mínimo una).
#Capa de salida: Devuelve el resultado del modelo.
#las MLP pueden modelar relaciones no lineales gracias a sus múltiples capas y funciones de activación no lineales
#funcionamiento: 
#Inicialización: Se crean pesos aleatorios para cada conexión.
#Propagación hacia adelante (Forward Propagation): Se calculan activaciones de cada capa.
#Cálculo del error: Se compara la salida de la red con la salida real.
#Retropropagación (Backpropagation): Se ajustan los pesos para minimizar el error.
#Repetición: Se repite el proceso para múltiples épocas.
#aplicacions: reconocimiento de voz, imagenes y texto, diagnostico medico, clasificación de datos, etc.

#ejemplo de red neuronal multicapa (MLP) para resolver el problema XOR, que no es linealmente separable

#librerias necesarias
import numpy as np #libreria para operaciones matematicas y matrices
from sklearn.neural_network import MLPClassifier #libreria para el modelo MLPClassifier que implementa una red neuronal multicapa
import matplotlib.pyplot as plt #libreria para graficar

#entradas y salidas del problema XOR
X = np.array([[0,0], [0,1], [1,0], [1,1]]) #Entradas XOR
y = np.array([0, 1, 1, 0])  #salidas XOR

#definir y entrenar una red neuronal multicapa
modelo = MLPClassifier(hidden_layer_sizes=(4,), activation='tanh', #tanh: función de activación hiperbólica tangente
                       solver='adam', max_iter=2000, random_state=42) #solver: algoritmo de optimización, max_iter: número máximo de iteraciones, random_state: semilla para reproducibilidad

modelo.fit(X, y) #entrenar el modelo con las entradas y salidas

#predicciones
predicciones = modelo.predict(X) #realizar predicciones con el modelo entrenado

#mostrar resultados
print("Predicciones:", predicciones)

#mostrar cómo se clasifican los puntos en el plano
colores = ['red' if p == 0 else 'blue' for p in predicciones] #colores para las clases 0 y 1
etiquetas = ['Clase 0', 'Clase 1'] #etiquetas para las clases 0 y 1

plt.figure(figsize=(6, 6)) #crear una figura de 6x6 pulgadas
for i, (x, label) in enumerate(zip(X, predicciones)): #iterar por cada punto de entrada y su predicción
    plt.scatter(x[0], x[1], color=colores[i], s=200, edgecolor='k') #graficar el punto con su color correspondiente
    plt.text(x[0] + 0.05, x[1], f'{label}', fontsize=12, color='black') #agregar la etiqueta al punto

plt.title("Clasificación del XOR con Red Neuronal Multicapa")
plt.xlabel("Entrada 1")
plt.ylabel("Entrada 2")
plt.grid(True)
plt.xlim(-0.2, 1.2) #limites del eje x
plt.ylim(-0.2, 1.2) #limites del eje y
plt.show()

#ejemplo de salida:
# Predicciones: [0 1 1 0]
#grafica de la clasificación del XOR con red neuronal multicapa, donde los puntos rojos representan la clase 0 y los azules la clase 1.
#la red neuronal ha aprendido a clasificar correctamente el problema XOR, donde la salida es 1 solo cuando una de las entradas es 1, pero no ambas.
#la red neuronal multicapa es capaz de aprender funciones no lineales y ha ajustado sus pesos y sesgos para minimizar el error cuadrático entre la salida real y la esperada.
