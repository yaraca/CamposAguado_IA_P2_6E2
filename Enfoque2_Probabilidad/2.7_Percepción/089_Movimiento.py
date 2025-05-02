#Movimiento
#implica detectar y analizar los cambios de posición de los objetos en una secuencia de imágenes (por ejemplo, en video).
#Este tipo de análisis se basa en el seguimiento de píxeles o regiones a lo largo del tiempo.
#Tipos comunes de tecnicas: 
#Diferencia de frames: compara imágenes consecutivas para detectar cambios.
# Sustracción de fondo: detecta objetos en movimiento con base en un fondo estático.
# Flujo óptico: analiza cómo se mueven los píxeles en el tiempo.
#Aplicaciones: sistemas de vigilancia, robótica, realidad aumentada, etc.

#Ejemplo de movimiento
#Detección de Movimiento con diferencia de frames

#librerías necesarias
import cv2 #para procesamiento de imágenes y video
import numpy as np #para operaciones matemáticas y manipulación de matrices

#abrir la cámara 
cap = cv2.VideoCapture(0)  

#leer tres frames consecutivos
ret, frame1 = cap.read() 
ret, frame2 = cap.read()
ret, frame3 = cap.read()

while cap.isOpened():
    #calcular la diferencia entre los frames (restas absolutas)
    diff1 = cv2.absdiff(frame1, frame2) #diferencia entre frame1 y frame2
    diff2 = cv2.absdiff(frame2, frame3) #diferencia entre frame2 y frame3
    
    # Convertir a escala de grises para facilitar el procesamiento
    gray1 = cv2.cvtColor(diff1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(diff2, cv2.COLOR_BGR2GRAY)

    # Hacer una operación AND para encontrar movimiento consistente
    movimiento = cv2.bitwise_and(gray1, gray2)

    # Aplicar un umbral para destacar el movimiento
    _, thresh = cv2.threshold(movimiento, 25, 255, cv2.THRESH_BINARY)
    #25 es el umbral, 255 es el valor máximo, y cv2.THRESH_BINARY es el tipo de umbralización

    #mostrar el resultado
    cv2.imshow("Movimiento Detectado", thresh)

    # actualizar los frames para continuar con el análisis
    frame1 = frame2
    frame2 = frame3
    ret, frame3 = cap.read()
    
    # Si se presiona 's', se sale del bucle
    if cv2.waitKey(30) & 0xFF == ord('s'):
        break

#liberar los recursos
cap.release()
cv2.destroyAllWindows()

#Ejemplo de salida: 
# Al ejecutar el código, se abrirá una ventana que mostrará el movimiento detectado en tiempo real.