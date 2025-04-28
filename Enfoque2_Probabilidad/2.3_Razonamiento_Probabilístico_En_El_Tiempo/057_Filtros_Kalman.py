#Filtros de Kalman
#es un algoritmo de estimación que predice el estado de un sistema dinámico a través del tiempo, combinando:
#Predicción basada en el modelo del sistema y Mediciones ruidosas del mundo real.
#Su objetivo es calcular una estimación óptima del estado actual del sistema, minimizando el error (en términos de varianza).
#Se basa en dos pasos principales en cada instante de tiempo:
#Predicción: Predice el próximo estado y la incertidumbre basada en el modelo.
#Corrección: Corrige la predicción usando la medición real y calcula la nueva incertidumbre.
#Estas etapas dependen de matrices:
# x: Estado estimado del sistema.
# P: 	Matriz de covarianza de error (incertidumbre).
# F: Matriz de transición del estado (modelo dinámico).
# H: Matriz de observación (cómo se relaciona el estado con lo que medimos).
# Q: Matriz de covarianza del ruido del proceso.
# R: Matriz de covarianza del ruido de la medición.
#Se puede aplicar en: navegación (GPS), robótica, finanzas, procesamiento de señales, etc.

#ejemplo de filtro de Kalman
#estimar la posición de un objeto que se mueve en línea recta.

#librerías necesarias
import numpy as np #para operaciones numéricas y matrices
import matplotlib.pyplot as plt #para graficar

#Definir parámetros del sistema
dt = 1.0  #intervalo de tiempo (1 segundo)
F = np.array([[1, dt], #Matriz de transición del estado (modelo dinámico)
              [0, 1]])  

H = np.array([[1, 0]])  #Matriz de observación (mide solo posición)

Q = np.array([[1e-5, 0], #Ruido del proceso (incertidumbre del modelo)
              [0, 1e-5]]) 

R = np.array([[0.1]])  #Ruido de la medición (incertidumbre de la medición)

#Estado inicial (posición y velocidad)
x = np.array([[0],
              [1]]) #Inicialmente en posición 0 con velocidad 1 m/s

P = np.eye(2)  #Incertidumbre inicial (2x2 identidad)

# Simulación de datos: movimiento real + mediciones ruidosas
num_steps = 50 #número de pasos de tiempo
real_position = [] #para almacenar la posición real
measurements = [] #para almacenar las mediciones ruidosas

pos = 0 #posición inicial
vel = 1  # Velocidad constante (1 m/s)

np.random.seed(42) #para reproducibilidad de resultados
# Simulación del movimiento y mediciones
for _ in range(num_steps): # iterar sobre el número de pasos
    pos += vel * dt #actualizar la posición real
    real_position.append(pos) #guardar la posición real
    measurement = pos + np.random.normal(0, np.sqrt(R[0, 0])) #medición ruidosa (agregar ruido gaussiano)
    measurements.append(measurement) #guardar la medición ruidosa

#almacenar estimaciones
estimated_positions = [] 

#Algoritmo de Filtro de Kalman
for z in measurements: #iterar sobre las mediciones ruidosas
    #Predicción
    x = F @ x  #Predice el próximo estado
    P = F @ P @ F.T + Q  #Predice la nueva incertidumbre
    #@ es el operador de multiplicación de matrices
    #F.T es la transpuesta de F

    #Actualización (corrección)
    y = np.array([[z]]) - H @ x  #Residuo (innovación)
    S = H @ P @ H.T + R  #Incertidumbre de la innovación
    K = P @ H.T @ np.linalg.inv(S)  #Ganancia de Kalman
    #H.T es la transpuesta de H

    x = x + K @ y  #Actualiza el estado
    P = (np.eye(2) - K @ H) @ P  #Actualiza la incertidumbre

    #Guardar la posición estimada
    estimated_positions.append(x[0, 0]) 

#Grafiacar resultados
plt.figure(figsize=(10,6)) #tamaño de la figura
plt.plot(real_position, label='Posición real') #posición real
plt.plot(measurements, 'o', label='Mediciones') #mediciones ruidosas
plt.plot(estimated_positions, '-', label='Estimaciones (Filtro de Kalman)') #estimaciones del filtro de Kalman
plt.legend()
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Filtro de Kalman - Seguimiento de Posición')
plt.grid()
plt.show()

#ejemplo de salida:
