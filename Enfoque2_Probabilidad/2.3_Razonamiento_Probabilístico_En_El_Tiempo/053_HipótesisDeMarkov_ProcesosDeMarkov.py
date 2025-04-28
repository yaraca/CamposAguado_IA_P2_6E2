#Hipótesis de Markov: Procesos de Markov
# La Hipótesis de Markov dice que: El futuro depende solo del presente, no del pasado.
# Formalmente: P(Xn+1 | Xn, Xn-1, ..., X0) = P(Xn+1 | Xn)
#Es decir: Una vez que conoces el estado actual, los estados anteriores no importan para predecir el siguiente estado.
#Un Proceso de Markov es una secuencia de eventos (o estados) donde el siguiente estado solo depende del estado actual (y no de los anteriores).
#Ejemplo: Movimiento de un robot que sigue un patrón simple, Juegos de tablero donde tu siguiente posición depende solo de la actual.
#Elementos: Estados posibles (por ejemplo: Soleado, Lluvioso), Probabilidad de transición entre estados (matriz de transición), Estado inicial (probabilidades de empezar en cada estado).
#Aplicaciones: predicción del clima, sistemas de recomendación, finanzas, biología, etc.

#Ejemplo de un proceso de Markov
#librerías necesarias
import random

#definir los estados posibles
estados = ["Soleado", "Lluvioso"] #Ejemplo: Soleado y Lluvioso

#definir la matriz de transición de estados
#cada estado tiene una probabilidad de ir a otro estado
P_transicion = {
    "Soleado": {"Soleado": 0.8, "Lluvioso": 0.2}, #probabilidades de transición desde Soleado (80% a Soleado, 20% a Lluvioso)
    "Lluvioso": {"Soleado": 0.4, "Lluvioso": 0.6} #probabilidades de transición desde Lluvioso (40% a Soleado, 60% a Lluvioso)
}

#definir el estado inicial
estado_inicial = "Soleado" #podría ser "Lluvioso" también

#número de pasos (días) que vamos a simular
num_pasos = 10 

#Función para simular el proceso de Markov
def simular_proceso_markov(estado_inicial, P_transicion, num_pasos): # definimos la función que simula el proceso de Markov
    estado_actual = estado_inicial #iniciamos el estado actual con el estado inicial
    trayectoria = [estado_actual] #iniciamos la trayectoria con el estado inicial

    for _ in range(num_pasos): #iteramos num_pasos veces
        #Obtener las probabilidades de transición desde el estado actual
        siguiente_estado = random.choices( #estado_actual), #elegir el siguiente estado basado en las probabilidades de transición
            population=list(P_transicion[estado_actual].keys()), #posibles estados a los que se puede ir
            weights=list(P_transicion[estado_actual].values()) #probabilidades de transición
        )[0]  # random.choices regresa una lista, por eso [0]

        #Agregar el nuevo estado a la trayectoria
        trayectoria.append(siguiente_estado) 

        #Actualizar el estado actual
        estado_actual = siguiente_estado

    return trayectoria #devolver la trayectoria completa

#Ejecutar la simulación
trayectoria = simular_proceso_markov(estado_inicial, P_transicion, num_pasos) #llamar a la función para simular el proceso de Markov

#mostrar la trayectoria simulada
print("Trayectoria del clima simulada:")
for dia, estado in enumerate(trayectoria): #iterar sobre la trayectoria
    print(f"Día {dia}: {estado}") #imprimir el estado de cada día

#ejemplo de salida:
# Trayectoria del clima simulada:
# Día 0: Soleado
# Día 1: Soleado
# Día 2: Soleado
# Día 3: Soleado
# Día 4: Soleado
# Día 5: Soleado
# Día 6: Soleado
# Día 7: Soleado
# Día 8: Lluvioso
# Día 9: Soleado
# Día 10: Soleado
#La salida muestra la trayectoria del clima simulada para 10 días, comenzando desde un estado inicial "Soleado".
# Dependiendo de las probabilidades de transición definidas, el clima puede cambiar entre "Soleado" y "Lluvioso" en cada paso.
# En este caso, la mayoría de los días fueron soleados, pero hubo un día lluvioso en el día 8.
# Esto ilustra cómo un proceso de Markov puede simular una secuencia de eventos donde el futuro depende solo del presente.
#La función random.choices() se utiliza para seleccionar un elemento de una lista con pesos asociados a cada elemento.
