#Exploracion Vs Explotacion
#En explorar: el agente prueba acciones que no conoce bien, lo que lo puede llevar a descubrir mejores resultados.
#En explotar: el agente utiliza el conocimiento actual para maximizar la recompensa, lo que puede llevar a resultados subóptimos si no se exploran otras acciones.
#La clave es encontrar un equilibrio entre explorar nuevas acciones y explotar las que ya se conocen para maximizar la recompensa total esperada.
#Se usa el metdofo epsilon-greedy, donde el agente elige una acción aleatoria con probabilidad epsilon (exploración) y la mejor acción conocida con probabilidad 1-epsilon (explotación).
#Se aplica en: juegos, robótica, finanzas, etc.

#Ejemplo de Exploración vs Explotación
#Simular un agente que elige entre 3 máquinas tragamonedas, donde cada una tiene una probabilidad diferente de ganar.
#El objetivo es aprender cuál es la mejor máquina para jugar.

#Librerias necesarias
import random

#definir las máquinas tragamonedas 
recompensas_reales = {
    'maquina_1': 0.3,  #30% de dar recompensa
    'maquina_2': 0.5,  #50%
    'maquina_3': 0.8   #80%
}

#inicializar los valores estimados por el agente
estimacion_valores = {
    'maquina_1': 0.0, #valor estimado inicial de la máquina 1
    'maquina_2': 0.0, #valor estimado inicial de la máquina 2
    'maquina_3': 0.0 #valor estimado inicial de la máquina 3
}

#cuántas veces se ha jugado cada máquina
conteo_jugadas = {
    'maquina_1': 0, 
    'maquina_2': 0,
    'maquina_3': 0
}

#parámetros
episodios = 1000  #número de juegos
epsilon = 0.1     #tasa de exploración

#simulación
for episodio in range(episodios):
    #elegirs si explorar o explotar
    if random.random() < epsilon:
        #exploración: elige una máquina aleatoria
        accion = random.choice(list(recompensas_reales.keys())) 
    else:
        #explotación: elige la máquina con mejor valor estimado
        accion = max(estimacion_valores, key=estimacion_valores.get)
    
    #simular si esa máquina da recompensa
    probabilidad = recompensas_reales[accion] #probabilidad de ganar
    recompensa = 1 if random.random() < probabilidad else 0 #1 si gana, 0 si no gana
    
    #actualizar el número de veces que se ha usado la máquina
    conteo_jugadas[accion] += 1 

    #actualizar el valor estimado usando promedio incremental
    n = conteo_jugadas[accion] #número de veces que se ha jugado la máquina
    valor_anterior = estimacion_valores[accion] #valor estimado anterior
    nuevo_valor = valor_anterior + (1 / n) * (recompensa - valor_anterior) #actualizar el valor estimado
    estimacion_valores[accion] = nuevo_valor #asignar el nuevo valor estimado a la máquina

#mostrar resultados
print("\nEstimaciones finales de cada máquina:")
for maquina, valor in estimacion_valores.items(): ##iterar sobre cada máquina y su valor estimado
    print(f"{maquina}: {valor:.2f} (jugadas: {conteo_jugadas[maquina]})") #imprimir el valor estimado y el número de jugadas de cada máquina

mejor = max(estimacion_valores, key=estimacion_valores.get) #obtener la máquina con el mejor valor estimado
print(f"\nLa mejor máquina según el agente es: {mejor}")  #imprimir la mejor máquina

#Ejemplo de salida:

# Estimaciones finales de cada máquina:
# maquina_1: 0.27 (jugadas: 33)
# maquina_2: 0.50 (jugadas: 42)
# maquina_3: 0.80 (jugadas: 925)

# La mejor máquina según el agente es: maquina_3