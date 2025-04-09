#Aprendizaje por Refuerzo Pasivo
#En este el agente sigue una política fija, y a partir de la experiencia en el entorno estima el valor de cada estado (utilidad o recompensa)
#La idea es evaluar una politica sin intentar mejorarla
#Se compone de: política fija, interaccon con el entorno, actualición del valor (TD(0)), convergencia
#Actualización del valor: V(s) = V(s) + α * (R + γ * V(s') - V(s))
#donde V(s) es el valor del estado s, α es la tasa de aprendizaje, R es la recompensa, γ es el factor de descuento y s' es el siguiente estado.
#Se aplica en: evaluacion de estrategias, modelos de decision, estimacion de estados, etc.

#Ejemplo de Aprendizaje por Refuerzo Pasivo
#4 entornos: S0=estado inicial, S1 y S2=estados intermedios, S3=estado terminal
#Politica fija: S0->S1, S1->S2, S2->S3 con recompensa 1

#librerias necesarias
import random

#definir el conjunto de estados
estados = ['S0', 'S1', 'S2', 'S3']  #S3 será el estado terminal

#definir la política fija (para estados no terminales)
#la política "avanza" de S0 a S1, de S1 a S2 y de S2 a S3.
politica = {
    'S0': 'avanzar',
    'S1': 'avanzar',
    'S2': 'avanzar'
}

#inicializar la función de valor para cada estado en 0
V = {estado: 0 for estado in estados}

#parámetros del aprendizaje por refuerzo
alpha = 0.1    #tasa de aprendizaje (cuánto se ajusta la estimación en cada paso)
gamma = 0.9    #factor de descuento (importancia de recompensas futuras)
episodios = 1000  #número de episodios para entrenar

#función para simular un episodio siguiendo la política fija
def simular_ep():
    episodio = []  #lista para almacenar las transiciones: (estado, recompensa, siguiente_estado)
    estado_actual = 'S0'  #comenzar en S0
    
    while estado_actual != 'S3':  #continuar hasta llegar al estado terminal
        accion = politica[estado_actual]  #la acción es fija: 'avanzar'
        
        #simulación del movimiento:
        if estado_actual == 'S0': #si estamos en S0
            siguiente_estado = 'S1' #avanzamos a S1
            recompensa = 0  #sin recompensa al avanzar
        elif estado_actual == 'S1': #si estamos en S1
            siguiente_estado = 'S2' #avanzamos a S2
            recompensa = 0 #sin recompensa al avanzar
        elif estado_actual == 'S2': #si estamos en S2
            siguiente_estado = 'S3' #avanzamos a S3
            recompensa = 1  #recompensa al llegar al estado final
        
        #guardar la transición en el episodio
        episodio.append((estado_actual, recompensa, siguiente_estado))
        estado_actual = siguiente_estado  #actualizar el estado
        
    return episodio #devolver el episodio completo

#algoritmo de Aprendizaje por Refuerzo Pasivo con TD(0)
for ep in range(episodios):
    #simular un episodio completo
    episodio = simular_ep()
    
    #actualizar la función de valor para cada transición del episodio
    for estado, recompensa, siguiente_estado in episodio:
        #TD(0): V(s) = V(s) + α * [r + γ * V(s') - V(s)]
        delta = recompensa + gamma * V[siguiente_estado] - V[estado]
        V[estado] = V[estado] + alpha * delta

#mostrar la función de valor estimada para cada estado
print("Valores estimados para cada estado:")
for estado in estados:
    print(f"{estado}: {V[estado]:.2f}") 

#Ejemplo de salida: 
# Valores estimados para cada estado:
# S0: 0.81
# S1: 0.90
# S2: 1.00
# S3: 0.00