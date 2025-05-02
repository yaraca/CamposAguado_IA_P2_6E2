#Texturas y Sombras
#el análisis de texturas y sombras es crucial para entender y segmentar diferentes regiones de una imagen.
#Estas técnicas se utilizan para identificar patrones repetitivos (texturas) y áreas oscuras (sombras) que pueden afectar la interpretación visual.
#Las texturas son patrones repetitivos en una imagen que proporcionan información sobre la superficie de los objetos.
#El análisis de texturas se utiliza para:
#Segmentación de Imágenes: Dividir una imagen en regiones basadas en diferentes texturas.
#Clasificación de Materiales: Identificar diferentes materiales en una imagen.
#Reconocimiento de Objetos: Ayudar en la identificación de objetos basados en sus texturas.
#Las sombras son áreas oscuras en una imagen que se forman cuando un objeto bloquea la luz.
#La detección de sombras es importante para:
# Mejora de la Segmentación: Eliminar sombras que pueden confundirse con objetos.
# Reconocimiento de Objetos: Mejorar la precisión al eliminar áreas que no pertenecen a los objetos de interés.
# Análisis de Escenas: Entender la iluminación y la disposición de objetos en una escena.
#Aplicaciones: visión por computadora, robótica, análisis de imágenes médicas, etc.

#Ejemplo de texturas y sombras
#Deteccion de sombras

#librerias necesarias
import cv2 #libreria de procesamiento de imagenes
import numpy as np #libreria de computo numerico y algebra lineal
from skimage.feature import graycomatrix, graycoprops #libreria para calcular la matriz de co-ocurrencia de niveles de gris (GLCM) y sus propiedades
#skimage es una libreria de procesamiento de imagenes en python
#skimage.feature es un submodulo de skimage que contiene funciones para la extraccion de caracteristicas de imagenes
#graycomatrix calcula la matriz de co-ocurrencia de niveles de gris (GLCM) para una imagen
#graycoprops calcula las propiedades de la GLCM, como contraste, homogeneidad, energia, etc.
from matplotlib import pyplot as plt #libreria para graficar

# Cargar la imagen
image = cv2.imread('perritos3.jpg', cv2.IMREAD_GRAYSCALE)

# Análisis de texturas utilizando GLCM
distances = [1] # Distancia entre píxeles para la GLCM
angles = [0, np.pi/4, np.pi/2, 3*np.pi/4] # Ángulos para la GLCM (0, 45, 90 y 135 grados)
glcm = graycomatrix(image, distances, angles, symmetric=True, normed=True) # Calcular la GLCM para cada distancia y ángulo (niveles de gris normalizados)

# Calcular propiedades de la textura
properties = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']
textures = {}

for prop in properties: #para cada propiedad de textura
    textures[prop] = graycoprops(glcm, prop).mean() # Calcular la media de cada propiedad a través de todas las distancias y ángulos

print("Propiedades de la textura:") 
for prop, value in textures.items(): #para cada propiedad de textura
    print(f"{prop}: {value}") # Imprimir las propiedades de la textura

# Detección de sombras
# Convertir la imagen a espacio de color HSV
hsv_image = cv2.cvtColor(cv2.imread('perritos3.jpg'), cv2.COLOR_BGR2HSV)

# Umbralización en el canal de valor (V) para detectar sombras
_, shadow_mask = cv2.threshold(hsv_image[:, :, 2], 100, 255, cv2.THRESH_BINARY_INV) 
#hsv_image[:, :, 2] es el canal de valor (V) en el espacio de color HSV
#100 es el valor de umbral para detectar sombras y 255 es el valor máximo para la máscara
#cv2.threshold devuelve dos valores: el primer valor es el umbral aplicado y el segundo es la máscara binaria resultante

# Mostrar las imágenes resultantes
images = [image, shadow_mask]
titles = ['Imagen Original', 'Detección de Sombras']

for i in range(2): #para cada imagen
    plt.subplot(1, 2, i+1) # Crear un subplot para cada imagen
    plt.imshow(images[i], cmap='gray') # Mostrar la imagen en escala de grises
    plt.title(titles[i])
    plt.axis('off')

plt.show()

#Ejemplo de salida: 
#Propiedades de la textura:
# contrast: 55.27024865807792
# dissimilarity: 4.110913875277236
# homogeneity: 0.35505266017241127
# energy: 0.05630369517153937
# correlation: 0.99256006723367
# ASM: 0.003209935006214872
#Una imagen de la detección de sombras se mostrará junto a la imagen original.