#Algortimo EM (Expectation-Maximization)
#es un algoritmo iterativo para encontrar máximos verosímiles (que parecen verdaderos) cuando hay datos incompletos o variables ocultas.
#Cuando no observamos todos los datos directamente, EM nos ayuda a inferir los parámetros del modelo de manera óptima.
#Funcionamiento: 1. E-step (Expectation - Paso de Esperanza): Estimar los valores esperados de las variables ocultas, dados los parámetros actuales.
#2. M-step (Maximization - Paso de Maximización): Maximizar la función de verosimilitud usando las "completaciones" de los datos del E-step.
#Así: "Estimo las variables ocultas" → "Actualizo los parámetros" → "Estimo otra vez..." → hasta que converge.
#Diagrama básico del algoritmo EM:
#Inicializar parámetros θ, Repetir hasta convergencia: a. E-step: Estimar variables ocultas usando θ,  b. M-step: Recalcular θ maximizando la función de verosimilitud
#Aplicaciones: Agruopamiento de datos, reconocimiento de patrones, análisis de imágenes, procesamiento de señales, etc.

#Ejemplo de Algoritmo EM
#ajustar dos distribuciones Gaussianas a un conjunto de datos sin saber de qué distribución viene cada dato.

#librerías necesarias
import numpy as np #para operaciones matemáticas y matrices
import matplotlib.pyplot as plt #para graficar
from scipy.stats import norm #para funciones de distribución normal

#Generar datos de ejemplo: mezcla de dos gaussianas
np.random.seed(42) #para reproducibilidad
data = np.concatenate([
    np.random.normal(0, 1, 150),  # Media 0, desviación 1, 150 datos
    np.random.normal(5, 1, 150)   # Media 5, desviación 1, 150 datos
])

#Inicializar parámetros de las dos Gaussianas
mu1, mu2 = np.random.choice(data, 2)  #Medias aleatorias
sigma1, sigma2 = 1.0, 1.0             #Desviaciones estándar iniciales
pi1, pi2 = 0.5, 0.5                   #Pesos iniciales (probabilidad de pertenecer a cada gaussiana)

print(f"Inicialización: mu1={mu1:.2f}, mu2={mu2:.2f}") #imprimir medias iniciales

#Algoritmo EM
n_iteraciones = 20 #Número de iteraciones
n = len(data) #número de datos

for iteracion in range(n_iteraciones): ##Iterar para ajustar los parámetros
    #E-step: calcular la responsabilidad (probabilidad de pertenecer a cada gaussiana)
    r1 = pi1 * norm.pdf(data, mu1, sigma1) #responsabilidad de la gaussiana 1
    r2 = pi2 * norm.pdf(data, mu2, sigma2) #responsabilidad de la gaussiana 2
    r_total = r1 + r2 #suma de responsabilidades
    gamma1 = r1 / r_total #probabilidad de pertenecer a la gaussiana 1
    gamma2 = r2 / r_total #probabilidad de pertenecer a la gaussiana 2

    #M-step: actualizar los parámetros
    N1 = np.sum(gamma1) #número de datos asignados a la gaussiana 1
    N2 = np.sum(gamma2) #número de datos asignados a la gaussiana 2

    mu1 = np.sum(gamma1 * data) / N1 #media de la gaussiana 1
    mu2 = np.sum(gamma2 * data) / N2 #media de la gaussiana 2

    sigma1 = np.sqrt(np.sum(gamma1 * (data - mu1)**2) / N1) #desviación de la gaussiana 1
    sigma2 = np.sqrt(np.sum(gamma2 * (data - mu2)**2) / N2) #desviación de la gaussiana 2

    pi1 = N1 / n #peso de la gaussiana 1
    pi2 = N2 / n #peso de la gaussiana 2

    print(f"Iteración {iteracion+1}: mu1={mu1:.2f}, mu2={mu2:.2f}, sigma1={sigma1:.2f}, sigma2={sigma2:.2f}")
    #imprimir parámetros ajustados en cada iteración

#Graficar resultados
x = np.linspace(min(data)-1, max(data)+1, 1000) #valores de x para graficar
pdf1 = pi1 * norm.pdf(x, mu1, sigma1) #pdf=funcion de densidad de probabilidad de la gaussiana 1
pdf2 = pi2 * norm.pdf(x, mu2, sigma2) #pdf=funcion de densidad de probabilidad de la gaussiana 2

plt.hist(data, bins=30, density=True, alpha=0.5, color='gray') #histograma de los datos
plt.plot(x, pdf1, label='Componente 1', color='red') #pdf=funcion de densidad de probabilidad de la gaussiana 1
plt.plot(x, pdf2, label='Componente 2', color='blue') #pdf=funcion de densidad de probabilidad de la gaussiana 2
plt.title("Estimación EM de mezcla de Gaussianas") 
plt.legend()
plt.show()

#Ejemplo de salida:
# Inicialización: mu1=6.77, mu2=4.18
# Iteración 1: mu1=5.91, mu2=1.73, sigma1=0.81, sigma2=2.44
# Iteración 2: mu1=5.61, mu2=1.63, sigma1=0.71, sigma2=2.48
# Iteración 3: mu1=5.47, mu2=1.48, sigma1=0.68, sigma2=2.44
# Iteración 4: mu1=5.39, mu2=1.33, sigma1=0.69, sigma2=2.39
# Iteración 5: mu1=5.35, mu2=1.18, sigma1=0.72, sigma2=2.32
# Iteración 6: mu1=5.32, mu2=1.03, sigma1=0.76, sigma2=2.23
# Iteración 7: mu1=5.29, mu2=0.86, sigma1=0.79, sigma2=2.10
# Iteración 8: mu1=5.27, mu2=0.67, sigma1=0.83, sigma2=1.93
# Iteración 9: mu1=5.25, mu2=0.46, sigma1=0.88, sigma2=1.69
# Iteración 10: mu1=5.21, mu2=0.22, sigma1=0.93, sigma2=1.38
# Iteración 11: mu1=5.14, mu2=0.03, sigma1=0.96, sigma2=1.11
# Iteración 12: mu1=5.10, mu2=-0.06, sigma1=0.98, sigma2=0.97
# Iteración 13: mu1=5.08, mu2=-0.08, sigma1=1.00, sigma2=0.94
# Iteración 14: mu1=5.08, mu2=-0.08, sigma1=1.01, sigma2=0.94
# Iteración 15: mu1=5.08, mu2=-0.08, sigma1=1.01, sigma2=0.94
# Iteración 16: mu1=5.08, mu2=-0.08, sigma1=1.01, sigma2=0.94
# Iteración 17: mu1=5.08, mu2=-0.08, sigma1=1.01, sigma2=0.94
# Iteración 18: mu1=5.08, mu2=-0.08, sigma1=1.01, sigma2=0.94
# Iteración 19: mu1=5.08, mu2=-0.08, sigma1=1.01, sigma2=0.94
# Iteración 20: mu1=5.08, mu2=-0.08, sigma1=1.01, sigma2=0.94

#las medias y desviaciones se van ajustando poco a poco a los verdaderos grupos.
#En la gráfica, las dos campanas de Gauss coinciden con las dos agrupaciones de los datos.
#El histograma muestra la distribución de los datos, y las curvas representan las dos Gaussianas ajustadas.
#El algoritmo EM ha encontrado las dos Gaussianas que mejor describen los datos.
