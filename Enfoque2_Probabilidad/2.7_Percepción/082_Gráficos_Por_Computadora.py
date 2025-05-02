#Graficos por computadora
#son una rama de la informática encargada de la generación, manipulación y representación visual de imágenes y escenas mediante algoritmos matemáticos y computacionales.
#se utilizan para simular entornos visuales, generar datos sintéticos, o representar de forma visual lo que un sistema percibe
#los sistemas de percepción (como visión por computadora) detectan o generan información del mundo visual. Gráficos por computador permiten representar esa percepción
#Componentes clave:
#Modelado geométrico: Representar la forma de los objetos (líneas, polígonos, curvas, 3D).
# Transformaciones: Mover, escalar o rotar objetos.
# Iluminación y sombreado: Simular cómo la luz interactúa con los objetos.
# Renderizado: Convertir los modelos en imágenes visibles.
#Aplicaciones: simuladores para IA, videojuegos, visualización científica, diseño gráfico, etc.

#ejemplo de graficos por computadora en Python usando Pygame
#Este código crea una ventana donde un círculo rojo se mueve de izquierda a derecha, mientras que un rectángulo azul permanece estático.

#librerías necesarias
import pygame #para crear la ventana y manejar gráficos
import sys #para manejar el sistema y cerrar la ventana correctamente

#inicializar la ventana
pygame.init()

#definir el tamaño de la ventana
ancho = 800
alto = 600
ventana = pygame.display.set_mode((ancho, alto)) #crear la ventana con el tamaño definido
pygame.display.set_caption("Gráficos por Computador - Movimiento")

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

# Posición inicial del círculo (objeto que se moverá)
x = 100
y = 300
velocidad = 5  # velocidad de movimiento

# Bucle principal
while True: 
    for evento in pygame.event.get(): #manejar eventos de la ventana
        if evento.type == pygame.QUIT: #si se cierra la ventana
            pygame.quit() #cerrar Pygame
            sys.exit() #salir del programa

    #movimienro automático del objeto hacia la derecha
    x += velocidad #aumentar la posición x del círculo
    if x > ancho: #si el círculo se sale de la pantalla por la derecha
        x = 0  # vuelve al inicio si se sale de la pantalla

    #dibujar en pantalla
    ventana.fill(BLANCO)  #limpiar con fondo blanco
    pygame.draw.rect(ventana, AZUL, (200, 250, 100, 100))  # Dibuja un rectángulo azul (objeto estático)
    pygame.draw.circle(ventana, ROJO, (x, y), 30)  # Dibuja un círculo rojo (objeto en movimiento)

    #actualizar la pantalla
    pygame.display.update()
    pygame.time.delay(30)  # pequeña pausa para controlar la velocidad del bucle

#Ejemplo de salida:
#Una ventana de 800x600 píxeles con un fondo blanco, un rectángulo azul estático y un círculo rojo que se mueve de izquierda a derecha.