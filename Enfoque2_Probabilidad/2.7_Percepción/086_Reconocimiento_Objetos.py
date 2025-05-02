#Reconocimiento de objetos
#Consiste en identificar y clasificar objetos dentro de una imagen o video. 
#Este proceso es crucial para aplicaciones como la conducción autónoma, la robótica, la seguridad, y muchas más.
#Funcionamiento:
# Adquisición de la Imagen: Capturar la imagen o video que contiene los objetos a reconocer.
# Preprocesamiento: Mejorar la calidad de la imagen mediante técnicas como el filtrado, la normalización y la segmentación.
# Extracción de Características: Identificar características distintivas de los objetos, como bordes, texturas y colores.
# Clasificación: Utilizar algoritmos de aprendizaje automático para clasificar las características extraídas en categorías de objetos conocidos.
# Postprocesamiento: Refinar los resultados y presentar la información de manera útil.
#Aplicaciones: conducción autónoma, robótica, seguridad, análisis de imágenes médicas, etc.

#Ejemplo de reconocimiento de objetos

#librerias necesarias
import cv2 #libreria de vision por computadora
import numpy as np #libreria de computo numerico y algebra lineal
import matplotlib.pyplot as plt #graficar 
from skimage.measure import label, regionprops #etiquetar 

#Cargar imagen
imagen = cv2.imread("perritos3.jpg")
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)#convertir a RGB

#Función Clasificador
def clasificador(imagen):
    m, n, c = imagen.shape #obtener dimensiones de la imagen
    imagenb = np.zeros((m, n), dtype=np.uint8) #crear imagen binaria
    
    for x in range(m): #recorrer filas
        for y in range(n): #recorrer columnas
            if 11 < imagen[x, y, 0] < 227 and 0 < imagen[x, y, 1] < 235 and 1 < imagen[x, y, 2] < 234: #si el pixel es blanco
                imagenb[x, y] = 255 #asignar valor 255 (blanco) a la imagen binaria
                
    return imagenb #devolver imagen binaria

#Usar el clasificador en la imagen
imagenb = clasificador(imagen)

#Separar los objetos por numero
etiquetas = label(imagenb, connectivity=2)

#filtrar errores de objetos 
eti_filtrada = np.zeros_like(etiquetas) #crear imagen filtrada
area_min = 500  #área minima para ser objeto
for region in regionprops(etiquetas): #recorrer las regiones etiquetadas
    if region.area >= area_min: #si el area es mayor a la minima
        eti_filtrada[etiquetas == region.label] = region.label #asignar etiqueta a la imagen filtrada

#imagen con colores para ver etiquetas
img_etiquetada = np.uint8(plt.cm.plasma(eti_filtrada / eti_filtrada.max())[:, :, :3] * 255)
#para cambiar los colores de etiqueta, otras opciones son (plt.cm._):
    #jet,viridis,plasma,tab10,nimpy_spectral

#poner números en las etiquetas
for i, region in enumerate(regionprops(eti_filtrada), start=1): #enumerar las regiones
    ymin, xmin, ymax, xmax = region.bbox  #obtener coordenadas del rectángulo alrededor de los objetos
    centro = (int((xmin + xmax) / 2), int((ymin + ymax) / 2))  #calcular el centro
    cv2.putText(img_etiquetada, str(i), centro, cv2.FONT_HERSHEY_SIMPLEX, 
                0.9, (255, 255, 255), 2, cv2.LINE_AA)#colocar no. de la etiqueta en el centro del objeto

#dibujar los rectangulos
img_ventana = imagen.copy()

for region in regionprops(eti_filtrada): #recorrer las regiones
    ymin, xmin, ymax, xmax = region.bbox #obtener coordenadas del rectángulo alrededor de los objetos
    cv2.rectangle(img_ventana, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2) #dibujar rectángulo en la imagen original
    #255,0,0 es el color azul en BGR, 2 es el grosor del rectángulo

#mostrar imagenes
fig, axes = plt.subplots(1, 4, figsize=(10, 5)) #crear subgráficas
axes[0].imshow(imagen) #imagen original
axes[1].set_title("Clasificación") 
axes[3].imshow(img_ventana) #imagen con rectángulos
axes[3].set_title("Localización")

for ax in axes:
    ax.axis("off")

plt.show()

#Ejemplo de salida:
#Imagen original, imagen con rectángulos detectando el objeto
