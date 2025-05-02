#Detección de aristas y segmentación de imágenes
#son técnicas fundamentales en el procesamiento de imágenes y la visión por computadora. 
#Estas técnicas se utilizan para identificar y delimitar objetos o regiones dentro de una imagen.
#La detección de aristas se refiere al proceso de identificar puntos en una imagen donde la intensidad de los píxeles cambia abruptamente.
#Estos cambios suelen corresponder a los bordes de los objetos. 
#Los algoritmos más comunes para la detección de aristas incluyen:
#Filtro de Sobel: Utiliza convoluciones para calcular gradientes en la imagen.
#Filtro de Canny: Un algoritmo más sofisticado que utiliza múltiples pasos, incluyendo suavizado, cálculo de gradientes, supresión de no máximos y umbralización con histéresis.
#La segmentación es el proceso de dividir una imagen en múltiples segmentos o regiones, donde cada segmento corresponde a un objeto o parte de un objeto
#Los métodos de segmentación incluyen:
#Umbralización (Thresholding): Convierte una imagen en escala de grises en una imagen binaria.
#Crecimiento de Regiones: Agrupa píxeles en regiones basadas en criterios de similitud
#Watershed: Un método basado en la analogía de inundación para segmentar imágenes.
#Aplicaciones: reconocimiento de objetos, análisis de imágenes médicas, visión robótica, etc.

#Ejemplo de detección de aristas y segmentación de imágenes 
#Utilizando el filtro de Canny y la segmentación utilizando umbralización en una imagen

#librerías necesarias
import cv2 #librería de OpenCV para procesamiento de imágenes
import numpy as np #librería NumPy para operaciones numéricas
from matplotlib import pyplot as plt #librería Matplotlib para visualización de imágenes

# Cargar la imagen
image = cv2.imread('perritos3.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar el filtro de Canny para la detección de aristas
edges = cv2.Canny(image, 100, 200)

# Aplicar umbralización para la segmentación
_, thresholded_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
#127 es el valor de umbral, 255 es el valor máximo que se asigna a los píxeles que superan el umbral, y cv2.THRESH_BINARY es el tipo de umbralización que se aplica.

# Mostrar las imágenes resultantes
images = [image, edges, thresholded_image] 
titles = ['Imagen Original', 'Detección de Aristas (Canny)', 'Segmentación (Umbralización)']

for i in range(3): #Iterar sobre las imágenes y títulos
    plt.subplot(1, 3, i+1) #Crear subgráficas
    plt.imshow(images[i], cmap='gray') #Mostrar la imagen en escala de grises
    plt.title(titles[i])
    plt.axis('off')

plt.show()

#Ejemplo de salida:
#La imagen original, la imagen con bordes detectados y la imagen segmentada se mostrarán en una sola ventana.
