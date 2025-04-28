#Monte Carlo Para Cadenas De Markov (MCMC)
# Es un método de inferencia probabilística que combina:
# Cadenas de Markov: procesos estocásticos que transitan de un estado a otro con cierta probabilidad.
# Muestreo de Monte Carlo: genera muestras aleatorias para estimar distribuciones complejas.
# MCMC genera muestras dependientes entre sí a través de una cadena de Markov, y estas muestras convergen a la distribución deseada.
# Se parte de un estado inicial arbitrario.
# En cada iteración: Se propone un nuevo estado, Se acepta o rechaza con una probabilidad basada en la distribución objetivo.
# Después de muchas iteraciones (y un tiempo de calentamiento llamado burn-in), las muestras generadas se usan para estimar probabilidades.
#Se puede aplicar en: Estimación de distribuciones posteriores en redes bayesianas, Problemas con muchas variables ocultas, Inferencia probabilística en IA, física, estadística y genética.

#Ejemplo de MCMC
#Implementar un algoritmo de Metropolis-Hastings para muestreo de una distribución normal.
#Se quiere muestrear una distribución binomial no normalizada: P(x) ∝ exp(-x^2/2)
#donde x es un número real, y la función de densidad de probabilidad es proporcional a la exponencial negativa del cuadrado de x dividido por 2.

#librerías necesarias
import random #para generar números aleatorios
import math #para funciones matemáticas
import matplotlib.pyplot as plt #para graficar

#parametros del MCMC
num_iteraciones = 10000 #número de iteraciones del algoritmo
estado_actual = 0.0  # Estado inicial
muestras = [] #lista para almacenar las muestras generadas


#función de la distribución objetivo
# P(x) ∝ exp(-x^2 / 2)
def distribucion_objetivo(x):
    return math.exp(-x**2 / 2) #distribución normal no normalizada

#algoritmo MCMC: Metropolis-Hastings
for i in range(num_iteraciones): #iterar num_iteraciones veces
    #Proponer nuevo estado x' = x_actual + ruido
    propuesta = estado_actual + random.gauss(0, 1)  #propuesta de nuevo estado con ruido gaussiano

    #Calcular razón de aceptación
    p_actual = distribucion_objetivo(estado_actual) #probabilidad del estado actual
    p_propuesta = distribucion_objetivo(propuesta) #probabilidad de la propuesta
    aceptacion = min(1, p_propuesta / p_actual) #razón de aceptación

    #Aceptar o rechazar
    if random.random() < aceptacion: #si un número aleatorio es menor que la razón de aceptación
        estado_actual = propuesta  #Acepta propuesta

    #Guardar muestra
    muestras.append(estado_actual) #agregar el estado actual a la lista de muestras

#mostrar resultados
plt.hist(muestras, bins=50, density=True, alpha=0.7, color='skyblue') #histograma de las muestras generadas
plt.title('Distribución aproximada con MCMC (Metropolis-Hastings)')
plt.xlabel('x')
plt.ylabel('Probabilidad estimada')
plt.grid(True)
plt.show()
#la grafica muestra la distribución aproximada de las muestras generadas por el algoritmo MCMC.
#La forma de la distribución se asemeja a una distribución normal, lo que indica que el algoritmo ha convergido a la distribución objetivo.
#El histograma muestra la densidad de probabilidad estimada a partir de las muestras generadas por el algoritmo MCMC.
#bin=50: número de intervalos en el histograma.
#density=True: normaliza el histograma para que la suma de las áreas de los intervalos sea igual a 1.
#alpha=0.7: establece la transparencia del color de las barras del histograma.
#color='skyblue': color de las barras del histograma.
#El algoritmo MCMC es útil para muestrear distribuciones complejas y de alta dimensión, donde los métodos tradicionales pueden ser ineficaces.