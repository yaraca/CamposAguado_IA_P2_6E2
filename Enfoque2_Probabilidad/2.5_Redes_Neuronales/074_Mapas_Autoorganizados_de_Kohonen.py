#Mapas Autoorganizados de Kohonen (SOM)
#son una técnica de aprendizaje no supervisado utilizada para la reducción de dimensiones y la visualización de datos complejos. 
# Proponen una forma de mapear datos multidimensionales en una rejilla de menor dimensión (usualmente 2D) preservando la topología (estructura espacial) de los datos.
# Funcionamiento:
#Inicialización:Se crea una red de neuronas organizada en una malla 2D.
#Entrenamiento: Por cada dato de entrada:
#Se calcula la distancia entre la entrada y todos los pesos de las neuronas.
#Se selecciona la neurona ganadora (Best Matching Unit, BMU).
#Se actualizan los pesos de la BMU y sus vecinas para que se parezcan más al vector de entrada.
##Se reduce gradualmente el radio de vecindad y la tasa de aprendizaje.
#Después del entrenamiento, neuronas cercanas responden a entradas similares → el mapa representa la estructura del conjunto de datos.
#aplicaciones: reducción de dimensionalidad, agrupamiento, visualización de datos, reconocimiento de patrones, etc.

#ejemplo de un mapa autoorganizado de Kohonen (SOM)

#librerias necesarias
import numpy as np #libreria para operaciones matematicas y matrices
from minisom import MiniSom  #libreria para el modelo SOM (MiniSom es una implementación ligera de SOM en Python)
import matplotlib.pyplot as plt #libreria para graficar

#generar datos de ejemplo: 3 grupos de colores (RGB)
datos = np.array([
    [0.9, 0.1, 0.1],  # Rojo
    [0.8, 0.2, 0.2],
    [0.1, 0.9, 0.1],  # Verde
    [0.2, 0.8, 0.2],
    [0.1, 0.1, 0.9],  # Azul
    [0.2, 0.2, 0.8]
])

#inicializar el SOM
som = MiniSom(x=4, y=4, input_len=3, sigma=1.0, learning_rate=0.5) 
#x: número de filas, y: número de columnas, input_len: longitud de la entrada (dimensión de los datos), sigma: radio de vecindad inicial, learning_rate: tasa de aprendizaje

#inicializar los pesos aleatoriamente
som.random_weights_init(datos) 

#entrenar la red (500 iteraciones)
som.train_random(data=datos, num_iteration=500) 

#mostrar el resultado
plt.figure(figsize=(7, 7)) #crear una figura de 7x7 pulgadas
for i, color in enumerate(datos): #iterar por cada dato de entrada y su color
    #buscar la neurona ganadora (coordenadas en el mapa)
    w = som.winner(color) #obtener la posición de la neurona ganadora
    
    #dibujar un punto en esa posición
    plt.text(w[0], w[1], str(i), 
             color=color, fontdict={'weight': 'bold', 'size': 16}) #agregar el índice del dato en la posición de la neurona ganadora

plt.title("Mapa Autoorganizado (SOM)")
plt.xlim(-1, 4) #limites del eje x
plt.ylim(-1, 4) #limites del eje y
plt.grid()
plt.show()

#Ejemplo de salida:
#Unagráfica 2D de 4x4 donde cada punto está etiquetado con un número (0–5), 
#cada uno representando un color (rojo, verde o azul), agrupados visualmente según similitud.
#esto indica que el SOM ha aprendido a organizar los datos en función de sus similitudes,
##colocando los colores similares cerca unos de otros en el mapa.
