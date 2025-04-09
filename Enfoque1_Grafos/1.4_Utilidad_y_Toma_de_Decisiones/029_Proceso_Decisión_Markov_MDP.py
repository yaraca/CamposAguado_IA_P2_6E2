#Proceso de decisión de Markov (MDP) 
#Es un modelo matemático que representa un entorno en el que un agente toma decisiones secuenciales 
#Con el fin de maximizar una recompensa acumulada esperada. 
#Un MDP se define por un conjunto de estados, un conjunto de acciones, una función de transición de estado,
#una función de recompensa y un factor de descuento.
#Observa el estado actual, elige una accion, responde con una nueva recompensa y estado
#Su objetivo es aprender una politica optima que maximice la suma de recompensas
#Se usa en robotica, juegos, planificacion de inventarios, sistemas de recomendacion, optimizacion de rutas 

#Ejemplo de un MDP
#matriz 3x4
#librerias necesarias
from collections import defaultdict #para crear un diccionario con valores por defecto

#definir estado matriz 3x4
estados = [(i, j) for i in range(3) for j in range(4)] #lista de tuplas que representan los estados
estados_terminales = [(0, 3), (1, 3)]  #estados donse terminan el juego

#recompensas por estado
recompensas = defaultdict(lambda: -0.04)  #penalización por moverse
recompensas[(0, 3)] = 1.0 #llegar a la meta positiva
recompensas[(1, 3)] = -1.0 #llegar a la meta negativa

#acciones disponibles
acciones = ['arriba', 'abajo', 'izquierda', 'derecha'] #lista de acciones posibles

#funcion de transicion de estados
def siguiente_estado(estado, accion): 
    i, j = estado #descomponemos el estado en filas y columnas
    if estado in estados_terminales: #si el estado es terminal, no se mueve
        return estado  

    #movimiento en la matriz
    if accion == 'arriba':
        i = max(i - 1, 0) #no se puede mover arriba si ya está en la fila 0
    elif accion == 'abajo':
        i = min(i + 1, 2) #no se puede mover abajo si ya está en la fila 2
    elif accion == 'izquierda':
        j = max(j - 1, 0) #no se puede mover izquierda si ya está en la columna 0
    elif accion == 'derecha':
        j = min(j + 1, 3) #no se puede mover derecha si ya está en la columna 3

    if (i, j) == (1, 1): #muro
        return estado

    return (i, j) #retorna el nuevo estado

#funcion de proceso de decision de markov
def mdp_iteracion_valores(gamma=0.9, umbral=0.001): #gamma=coeficiente de descuento, umbral=error maximo permitido
    #inicializar los valores de los estados en 0
    V = {s: 0 for s in estados} #V=valores de los estados
    
    while True:
        delta = 0  #diferencia máxima en una iteración
        for s in estados:
            if s in estados_terminales or s == (1, 1): #si el estado es terminal o es la celda (1,1) no se actualiza el valor
                continue 
            
            max_valor = float('-inf') #inicializar el valor máximo a menos infinito
            for a in acciones: #iterar sobre todas las acciones
                estado_siguiente = siguiente_estado(s, a) #obtener el estado siguiente
                recompensa = recompensas[estado_siguiente]  #obtener la recompensa del estado siguiente
                valor = recompensa + gamma * V[estado_siguiente] #calcular el valor del estado actual
                if valor > max_valor: #si el valor es mayor que el máximo, actualizar el máximo
                    max_valor = valor 

            delta = max(delta, abs(V[s] - max_valor)) #actualizar el error
            V[s] = max_valor #actualizar el valor del estado actual

        if delta < umbral: #si el error es menor que el umbral, se considera convergencia
            break  #cuando el cambio es muy pequeño

    return V #retorna los valores de los estados

#llamar a la funcion
valores = mdp_iteracion_valores()

#mostrar resultados
print("Valores estimados para cada estado:")
for i in range(3):
    for j in range(4): 
        if (i, j) == (1, 1):  #si el estado es un muro, imprimir un espacio
            print(" #  ", end=" ")  #imprimir el muro
        else:
            print(f"{valores[(i, j)]:5.2f}", end=" ") #imprimir el valor de cada estado
    print()

#Ejemplo de salida:
# Valores estimados para cada estado:
#  0.73  0.86  1.00  0.00
#  0.62  #    0.86  0.00
#  0.52  0.62  0.73  0.62