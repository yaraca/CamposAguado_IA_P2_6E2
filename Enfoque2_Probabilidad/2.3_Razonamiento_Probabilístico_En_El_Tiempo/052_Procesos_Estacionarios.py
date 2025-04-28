#Procesos Estacionarios
#Un proceso estocástico (un sistema que evoluciona aleatoriamente con el tiempo) es estacionario si sus propiedades estadísticas no cambian con el tiempo.
#Es decir:
# Su media, varianza y autocorrelación son constantes en el tiempo.
# Matematicamente: P(Xt) = P(Xt+k) para cualquier k.
#Funcionamiento:
# Se define una distribución inicial.
# Se define una matriz de transición que no cambia con el tiempo.
# Se simula el sistema a lo largo de varios pasos temporales.
# Como las reglas son iguales en cada instante, el sistema evoluciona de forma "estable" estadísticamente.
#Se puede aplicar en: modelado de series de tiempo, reconocimiento del habla, prediccion meteorologica, finanzas, etc.

#Ejemplo de un proceso estacionario
#Supongamos 2 estados: A y B.
#Una matriz de transicion constante:
#De/A   A     B
# A     0.7  0.3
# B     0.4  0.6
#La matriz indica que si el sistema está en A, tiene un 70% de probabilidad de permanecer en A y un 30% de pasar a B. Si está en B, tiene un 40% de probabilidad de volver a A y un 60% de permanecer en B.

#librerías necesarias
import random
import matplotlib.pyplot as plt

#deifnir el proceso estacionario
#Estados posibles
estados = ['A', 'B']

#matriz de transición estacionaria
#cada fila representa un estado actual, cada columna el próximo estado
#por ejemplo, transiciones[A][B] = 0.3
transiciones = {
    'A': {'A': 0.7, 'B': 0.3}, #probabilidades de transición desde A
    'B': {'A': 0.4, 'B': 0.6} #probabilidades de transición desde B
}

#estado inicial
estado_actual = 'A' #podría ser 'B' también

#número de pasos a simular
num_pasos = 1000

#lista para guardar la secuencia de estados
historial = []

#simulación del proceso
for _ in range(num_pasos): #iterar num_pasos veces
    historial.append(estado_actual)  #guardar el estado actual

    #elegir el próximo estado basado en las probabilidades de transición
    if random.random() < transiciones[estado_actual]['A']: #si un número aleatorio es menor que la probabilidad de permanecer en A
        estado_actual = 'A' #permanecer en A
    else: #si no, cambiar a B
        estado_actual = 'B'


#Visualización de resultados
#contar cuántas veces se estuvo en cada estado
conteo = {estado: historial.count(estado) for estado in estados} #crear un diccionario con el conteo de cada estado

#mostrar la distribución final
plt.bar(conteo.keys(), conteo.values(), color=['blue', 'orange']) #crear un gráfico de barras con los conteos
plt.title('Frecuencia de estados en un Proceso Estacionario')
plt.xlabel('Estado')
plt.ylabel('Número de visitas')
plt.grid(True)
plt.show()

#imprimir las frecuencias relativas
for estado in estados: #iterar sobre los estados
    print(f"Frecuencia de {estado}: {conteo[estado]/num_pasos:.4f}") #imprimir la frecuencia relativa de cada estado

#ejemplo de salida:
#Grafica
# Frecuencia de A: 0.5750
# Frecuencia de B: 0.4250
#La grafica muestra la frecuencia de los estados A y B en el proceso estacionario.
#La frecuencia relativa indica que el sistema pasó aproximadamente el 57.5% del tiempo en A y el 42.5% en B.
#Esto sugiere que el sistema tiene una tendencia a permanecer en A más que en B, lo que es consistente con la matriz de transición dada.
#El proceso es estacionario porque la distribución de estados no cambia con el tiempo, y las probabilidades de transición son constantes.
#El proceso se comporta de manera predecible a largo plazo, lo que es una característica clave de los procesos estacionarios.
