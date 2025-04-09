#Busqueda de la Política
#Es un metodo que aprende directamente de la política, es decir, una funcion que mapea estados a acciones 
#Sin la necesidad de calcular valores intermedios 
#Conceptos clave: Politica(π) es una funcion que indica qué accion tomar en cada estodo, se busca una política optima que maximice la recompensa esperada
#Se puede representar como estocástica(mapea estados a distribuciones de probabilidad sobre acciones) o determinista(mapea estados a acciones fijas)
#Se puede aplicar en: juegos, robótica, finanzas, etc.

#Ejemplo de Búsqueda de la Política
#Aprender la mejor direccion (izquierda o derecha) para llegar a una meta
#librerias necesarias
import random

#simulación de un entorno muy simple de 1 dimensión
#el agente empieza en 0 y quiere llegar a +10
#puede moverse a la derecha (+1) o izquierda (-1)

#Función que simula la ejecución de una política durante un número de pasos
def ejecutar_politica(politica, pasos=20): 
    posicion = 0
    for _ in range(pasos):
        accion = politica()  #ejecuta la política
        posicion += accion #actualiza la posición
    #recompensa: entre más cerca de 10, mejor
    recompensa = -abs(10 - posicion) #recompensa negativa si se aleja de 10
    return recompensa 

#búsqueda de política simple: probar aleatoriamente y quedarse con la mejor
mejor_politica = None #inicializa la mejor política
mejor_recompensa = float('-inf') #inicializa la mejor recompensa

#probar muchas políticas distintas
for i in range(1000):
    #definir una política estocástica aleatoria
    prob_derecha = random.uniform(0, 1) #probabilidad de moverse a la derecha
    
    #función que define la política
    def politica():
        return 1 if random.random() < prob_derecha else -1 #moverse a la derecha con probabilidad prob_derecha, izquierda con 1 - prob_derecha

    recompensa = ejecutar_politica(politica) #ejecutar la política y obtener recompensa

    #si es mejor, se guarda
    if recompensa > mejor_recompensa: 
        mejor_recompensa = recompensa #actualiza la mejor recompensa
        mejor_politica = prob_derecha #actualiza la mejor política

#mostrar resultados
print(f"La mejor política encontrada mueve a la derecha con probabilidad: {mejor_politica:.2f}") #imprime la mejor política
print(f"Recompensa obtenida con esa política: {mejor_recompensa}") #imprime la recompensa obtenida con la mejor política

#Ejemplo de salida:
# La mejor política encontrada mueve a la derecha con probabilidad: 0.55
# Recompensa obtenida con esa política: 0