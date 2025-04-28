#Red Bayes. Dinámica: Filtrado de Partículas
#El Filtrado de Partículas es una técnica de inferencia aproximada que se utiliza para seguir (rastrear) el estado de un sistema dinámico cuando el modelo es no lineal y/o el ruido no es gaussiano.
#En lugar de mantener toda la distribución de probabilidad (lo cual sería muy costoso), el filtrado de partículas representa la distribución conjunto de muchas "partículas" (muestras) que representan posibles estados del sistema.
#Cada partícula representa una posible hipótesis del estado del sistema.
#Funcionamiento básico:
#Inicialización: Generar un conjunto de partículas al azar, basado en el conocimiento inicial del sistema.
#Predicción: Avanzar cada partícula a su nuevo estado usando el modelo dinámico del sistema.
#Actualización: Asignar un peso a cada partícula basado en qué tan bien predice la medición real.
#Re-muestreo: Seleccionar partículas (con reemplazo) basándose en sus pesos para formar el nuevo conjunto de partículas.
#Estimación: Estimar el estado promedio ponderado.
#Se puede abircar en: seguiento de objetos, robótica, visión por computadora, procesamiento de señales, etc.

#Ejemplo de filtro de partículas
#seguir un objeto que se mueve en línea recta con algo de ruido.

#librerías necesarias
import numpy as np #para operaciones numéricas y matrices
import matplotlib.pyplot as plt #para graficar

#definir el número de partículas
N = 1000

#movimiento real del objeto (posición real)
dt = 1.0 #intervalo de tiempo (1 segundo)
velocidad_real = 1.0 #velocidad real (1 m/s)
pos_real = 0 #posición inicial (0 m)

#modelo de observación: medirposición, pero con ruido
ruido_medicion = 1.0 #desviación estándar del ruido de medición

#Inicializar partículas: distribuidas alrededor de 0 ± 10
particulas = np.random.normal(0.0, 10.0, N) #partículas iniciales distribuidas aleatoriamente alrededor de 0 ± 10

#Inicializar pesos uniformemente
pesos = np.ones(N) / N #pesos iniciales uniformemente distribuidos (1/N)

#Para almacenar posiciones reales, mediciones y estimaciones
pos_reales = []
mediciones = []
estimaciones = []

np.random.seed(42)  #para reproducibilidad de resultados

#Filtrado de partículas en varios pasos de tiempo
for t in range(50): #iterar sobre el número de pasos
    #Movimiento real
    pos_real += velocidad_real * dt #actualizar la posición real
    pos_reales.append(pos_real) #guardar la posición real
    
    #Medición (con ruido)
    medicion = pos_real + np.random.normal(0.0, ruido_medicion) #medición ruidosa (agregar ruido gaussiano)
    mediciones.append(medicion) #guardar la medición ruidosa
    
    #Predicción: mover partículas (aplicar modelo con algo de ruido)
    particulas += velocidad_real * dt + np.random.normal(0.0, 0.5, N) #mover partículas con ruido
    
    #Actualización: calcular pesos basados en la medición
    pesos = np.exp(-0.5 * ((medicion - particulas) ** 2) / (ruido_medicion ** 2)) #calcular pesos usando la función de verosimilitud
    pesos += 1.e-300  #Evitar pesos exactamente cero
    pesos /= np.sum(pesos)  #Normalizar
    
    #Re-muestreo: seleccionar partículas basándose en pesos
    indices = np.random.choice(N, size=N, p=pesos) #seleccionar índices de partículas basándose en los pesos
    particulas = particulas[indices] 
    pesos = np.ones(N) / N  #Reiniciar los pesos uniformemente
    
    #Estimación: calcular el promedio de las partículas
    estimacion = np.mean(particulas) #calcular la estimación como el promedio de las partículas
    estimaciones.append(estimacion) #guardar la estimación

#graficar resultados
plt.figure(figsize=(10,6)) #crear una figura de tamaño 10x6
plt.plot(pos_reales, label='Posición Real') #graficar la posición real
plt.plot(mediciones, 'o', label='Mediciones (ruidosas)') #graficar las mediciones ruidosas
plt.plot(estimaciones, '-', label='Estimaciones (Filtro de partículas)') #graficar las estimaciones del filtro de partículas
plt.legend()
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Filtrado de Partículas - Seguimiento de Posición')
plt.grid()
plt.show()

#Ejemplo de salida:
#esta gráfica muestra la posición real del objeto, las mediciones ruidosas y las estimaciones del filtro de partículas.
#El filtro de partículas sigue la posición real del objeto a pesar del ruido en las mediciones.
#Se puede observar que las estimaciones son más suaves y siguen la tendencia de la posición real, a pesar de las mediciones ruidosas.
#linea azul: posición real del objeto (sin ruido)
#puntos naranjas: mediciones ruidosas (con ruido)
#línea verde: estimaciones del filtro de partículas (suave y sigue la tendencia de la posición real)
