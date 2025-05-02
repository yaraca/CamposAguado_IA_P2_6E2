#Etiquetados de lineas
#es una técnica de procesamiento de imágenes que detecta líneas o bordes en una imagen binaria o en escala de grises, y luego etiqueta cada línea o borde identificado con una etiqueta única. 
#Esto es útil para identificar contornos, estructuras geométricas o segmentos significativos en imágenes.
#Funcionamiento:
# Detección de bordes: se aplica un filtro (como Sobel o Canny) para encontrar los bordes en una imagen.
# Binarización: se convierte la imagen a blanco y negro, donde los bordes tienen valor 1.
# Etiquetado: cada grupo de píxeles conectados que forman una línea o borde se etiqueta con un número diferente.
# Visualización: cada línea etiquetada se puede visualizar con un color único.
#Aplicaciones: reconocimiento de formas geometricas, análisis de planos, robotica, etc. 

#Ejemplo de etiquetados de lineas

#librerias necesarias
# cv2: para operaciones de procesamiento de imágenes como la detección de bordes.
# numpy: para manejar matrices y realizar operaciones numéricas.
# matplotlib.pyplot: para la visualización de imágenes y gráficos.
# skimage.measure.label: para etiquetar componentes conectados en una imagen.
# skimage.color.label2rgb: para convertir etiquetas en una imagen en color.
import cv2  
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from skimage.color import label2rgb

#Cargar una imagen en escala de grises
imagen = cv2.imread("perritos3.jpg", cv2.IMREAD_GRAYSCALE)
if imagen is None:
    raise ValueError("No se pudo cargar la imagen. Verifica la ruta o el nombre del archivo.")

#Aplicar detección de bordes con Canny
bordes = cv2.Canny(imagen, 50, 150)

#Etiquetar los componentes conectados (líneas detectadas)
etiquetas = label(bordes, connectivity=2)

#Convertir etiquetas a una imagen en color para visualización
imagen_etiquetada = label2rgb(etiquetas, bg_label=0)

#Mostrar resultados
plt.figure(figsize=(12, 4))

 # Imagen original en escala de grises
plt.subplot(1, 3, 1)
plt.title("Imagen Original (escala de grises)")
plt.imshow(imagen, cmap='gray')
plt.axis('off')

# Bordes detectados
plt.subplot(1, 3, 2) 
plt.title("Bordes detectados")
plt.imshow(bordes, cmap='gray')
plt.axis('off')

# Imagen etiquetada
plt.subplot(1, 3, 3) 
plt.title("Líneas etiquetadas")
plt.imshow(imagen_etiquetada)
plt.axis('off')

plt.tight_layout()
plt.show()

#Mostrar cantidad de líneas detectadas
print(f"Número de líneas etiquetadas: {etiquetas.max()}")

#Ejemplo de salida:
#3 imagenes: la original, la de bordes detectados y la etiquetada.