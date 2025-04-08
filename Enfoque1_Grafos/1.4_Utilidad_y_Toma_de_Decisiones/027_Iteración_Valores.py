#Iteracion de valores
#Es algoritmo que se usa para encontrar una política óptima en un entorno modelado como un proceso de decisión de Markov (MDP).
#El algoritmo itera sobre los valores de los estados hasta que converge a una solución estable.
#Busca responder a cuál es la mejor accion que deberia tomar en cada estado para maximizar la recompensa esperada a largo plazo.
#El algoritmo de iteración de valores se basa en la ecuación de Bellman, que describe la relación entre el valor de un estado y los valores de sus estados vecinos.
#La formula es: V(s) = max_a ∑ P(s'|s,a) * [R(s,a,s') + γ * V(s')]
#Donde: V(S)=valor del estado s, a=accion, P(s'|s,a)=probabilidad de transitar al estado s' dado el estado s y la acción a, R(s,a,s')=recompensa al tomar la acción a en el estado s y llegar al estado s'
# γ=coeficiente de descuento (0<γ<1), V(s')=valor del estado s'.

#Ejemplo de iteracion de valores 
#Laberinto en el que el agente quiere llegar a una meta maximizando su recompensa.

#Librerias necesarias
from collections import defaultdict #Para crear un diccionario con valores por defecto

#definir los estados del mundo como una matriz 3x4
estados = [(i,j) for i in range(3) for j in range(4)] #Lista de tuplas que representan los estados

#estados donde termina el juego
estados_terminales = [(0,3),(1,3)] #Lista de estados terminales

#recompensas por estado
recompensas = defaultdict(lambda: -0.04) #penalizacion po moverse
recompensas[(0,3)] = 1.0 #recompensa por llegar a la meta positiva
recompensas[(1,3)] = -1.0 #recompensa por llegar a la meta negativa

#accioes posibles en cada estado
acciones = ['arriba', 'abajo', 'izquierda', 'derecha'] #Lista de acciones posibles

#funcion de qué pasa si el agente se mueve a una dirección
def movimiento(estado, accion): 
    i, j = estado #desempaquetar la tupla en sus componentes
    if estado in estados_terminales:
        return estado #si el estado es terminal, no se mueve
    #definir los limites de movimiento
    if accion == 'arriba':
        i = max(i - 1, 0)  #no se puede mover arriba si ya esta en la fila 0
    elif accion == 'abajo':
        i = min(i + 1, 2) #no se puede mover abajo si ya esta en la fila 2
    elif accion == 'izquierda':
        j = max(j - 1, 0) #no se puede mover izquierda si ya esta en la columna 0
    elif accion == 'derecha':
        j = min(j + 1, 3) #no se puede mover derecha si ya esta en la columna 3
    
    if (i, j) == (1, 1): #si el agente se mueve a la celda (1,1) se cae y vuelve a la celda (1,0)
        return estado #no se mueve
    
    return (i, j) #retorna el nuevo estado

#funcion de iteracion de valores
def iteracion_valores(gamma=0.9, limite=0.001): #gamma=coeficiente de descuento, limite=error maximo permitido
    valor = { estado: 0 for estado in estados } #inicializar el valor de cada estado a 0
    politica = { estado: None for estado in estados } #inicializar la politica de cada estado a None

    while True: 
        delta = 0 #inicializar el error a 0 para verificar convergencia

        for estado in estados: #iterar sobre todos los estados
            if estado in estados_terminales or estado == (1, 1): #si el estado es terminal o es la celda (1,1) no se actualiza el valor
                continue #saltar a la siguiente iteracion

            max_valor = float('-inf') #inicializar el valor maximo a menos infinito
            mejor_accion = None #inicializar la mejor accion a None

            for accion in acciones: #iterar sobre todas las acciones posibles
                nuevo_estado = movimiento(estado, accion) #obtener el nuevo estado al mover el agente
                recompensa = recompensas[nuevo_estado] #obtener la recompensa del nuevo estado
                valor_accion = recompensa + gamma * valor[nuevo_estado] #calcular el valor de la accion
                if valor_accion > max_valor: #si el valor de la accion es mayor que el maximo encontrado
                    max_valor = valor_accion #actualizar el valor maximo
                    mejor_accion = accion #actualizar la mejor accion
            
            delta = max(delta, abs(valor[estado] - max_valor)) #calcular el error
            valor[estado] = max_valor #actualizar el valor del estado
            politica[estado] = mejor_accion #actualizar la politica del estado
        
        if delta < limite: #si el error es menor que el limite
            break
    return valor, politica #retornar el valor y la politica final

#ejecutar la funcion de iteracion de valores
valores, politica = iteracion_valores() #obtener el valor y la politica final

print("Valores de los estados:")
for i in range(3): 
    for j in range(4):
        print(f"{valores[(i, j)]:6.2f}", end="  ") #imprimir el valor de cada estado
    print()

print("\nPolítica óptima:")
for i in range(3):
    for j in range(4):
        if (i,j) in estados_terminales: #si el estado es terminal
            print("  T  ", end=" ") #imprimir T para los estados terminales
        elif (i,j) == (1, 1): #si el estado es la celda (1,1)
            print("#  ", end="  ")  # muro
        else:
            print(f"{politica[(i, j)][:1].upper()}  ", end="  ")
    print()

#Ejemplo de salida:
# Valores de los estados:
#   0.73    0.86    1.00    0.00
#   0.62    0.00    0.86    0.00
#   0.52    0.62    0.73    0.62

# Política óptima:
# D    D    D      T
# A    #    A      T
# A    D    A      I 
