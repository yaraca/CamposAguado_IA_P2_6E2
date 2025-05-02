#Preprocesado: Filtros
#el preprocesado se refiere a los pasos iniciales para mejorar la calidad de la imagen o extraer características relevantes antes de aplicar algoritmos de análisis o reconocimiento.
#Los filtros son operadores que modifican los valores de los píxeles de una imagen con base en sus vecinos. 
#Se aplican mediante convolución con una máscara o kernel.
#Tipos de filtros:
#Media (blur): 	Suavizar imagen, reducir ruido
# Mediana:	Eliminar ruido sal y pimienta
# Gaussiano:	Suavizado suave basado en estadística
# Sobel:	Detección de bordes (gradientes)
# Laplaciano:	Detección de bordes (alta frecuencia)
# Sharpening (enfoque):	Resaltar detalles
#Aplicaciones: eliminar ruido, resaltar bordes, suavizar imágenes, etc.

#Ejemplo de preprocesado de imagen con filtros

#librerías necesarias
import cv2 # OpenCV para procesamiento de imágenes
import numpy as np #para operaciones numéricas y manipulación de matrices
from matplotlib import pyplot as plt #para visualización de imágenes

# Cargar la imagen en escala de grises
imagen = cv2.imread('perritos3.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar filtro Gaussiano para suavizar la imagen
imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)

# Aplicar filtro de Sobel para realzar bordes
sobel_x = cv2.Sobel(imagen_suavizada, cv2.CV_64F, 1, 0, ksize=5) # Sobel en dirección x
#cv2.CV_64F: tipo de dato para la imagen resultante (64 bits en punto flotante)
#1: dirección x, 0: dirección y
#ksize: tamaño del kernel (más grande = más suave)
sobel_y = cv2.Sobel(imagen_suavizada, cv2.CV_64F, 0, 1, ksize=5) # Sobel en dirección y
bordes = cv2.bitwise_or(sobel_x, sobel_y) # Combinar ambos resultados

# Aplicar filtro de mediana para reducir el ruido
imagen_mediana = cv2.medianBlur(imagen, 5) # Tamaño del kernel 5x5

# Mostrar las imágenes resultantes
imagenes = [imagen, imagen_suavizada, bordes, imagen_mediana]
titulos = ['Original', 'Suavizada (Gaussiano)', 'Bordes (Sobel)', 'Mediana']

for i in range(4): # Crear subgráficas
    plt.subplot(2, 2, i+1) # 2 filas, 2 columnas, i+1 para la posición
    plt.imshow(imagenes[i], cmap='gray') # Mostrar imagen en escala de grises
    plt.title(titulos[i]) # Título de la subgráfica
    plt.axis('off')

plt.show()

#ejemplo de salida:
#Imagen original, imagen suavizada (filtro gaussiano), bordes detectados (filtro sobel), imagen con filtro mediana aplicado.