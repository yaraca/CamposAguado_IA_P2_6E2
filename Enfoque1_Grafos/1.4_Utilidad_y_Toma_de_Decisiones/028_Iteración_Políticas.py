#Iteracion de políticas 
#Es un algoritmo que se utiliza para encontrar una política óptima en un entorno modelado como un proceso de decisión de Markov (MDP).
#en lugar de calcular directamente los valores optimos, el algoritmo evalua una politica y luego la mejora 
#inicializa una politica, la evalua y luego la mejora iterativamente hasta que converge a una politica optima.
#El algoritmo de iteración de políticas se basa en la ecuación de Bellman, que describe la relación entre el valor de un estado y los valores de sus estados vecinos.

#Ejemplo de iteracion de politicas
#matriz 3x4 
#librerias necesarias
from collections import defaultdict

#definir los estados de la matriz de 3x4
estados = [(i, j) for i in range(3) for j in range(4)] #Lista de tuplas que representan los estados
estados_terminales = [(0, 3), (1, 3)] #lista de estados terminales

#recompensas por estado
recompensas = defaultdict(lambda: -0.04) #penalizacion por moverse
recompensas[(0, 3)] = 1.0 #recompensa por llegar a la meta positiva
recompensas[(1, 3)] = -1.0 #recompensa por llegar a la meta negativa

#acciones disponibles
acciones = ['arriba', 'bajo', 'izquierda', 'derecha'] #Lista de acciones posibles

#función para determinar el estado siguiente
def movimiento(estado, accion):
    i, j = estado
    if estado in estados_terminales: #si el estado es terminal, no se mueve
        return estado

    if accion == 'arriba': 
        i = max(i - 1, 0) # no se puede mover arriba si ya está en la fila 0
    elif accion == 'bajo':
        i = min(i + 1, 2) # no se puede mover abajo si ya está en la fila 2
    elif accion == 'izquierda':
        j = max(j - 1, 0) # no se puede mover izquierda si ya está en la columna 0
    elif accion == 'derecha':
        j = min(j + 1, 3) # no se puede mover derecha si ya está en la columna 3

    if (i, j) == (1, 1):  # muro
        return estado

    return (i, j)

#algoritmo de Iteración de Políticas
def iteracion_politica(gamma=0.9, limite=0.001): #gamma=coeficiente de descuento, limite=error maximo permitido
    #inicializar política aleatoria
    politica = {s: 'arriba' for s in estados if s not in estados_terminales and s != (1, 1)} #inicializar política de cada estado a una acción aleatoria S=estados
    V = {s: 0 for s in estados} #inicializar el valor de cada estado a 0 V=valores

    while True: #evaluacion política
        while True:
            delta = 0 #inicializar el error a 0 para verificar convergencia
            for s in estados: #iterar sobre todos los estados
                if s in estados_terminales or s == (1, 1): #si el estado es terminal o es la celda (1,1) no se actualiza el valor
                    continue

                a = politica[s] #obtener la acción de la política a=accion 
                estado_siguiente = movimiento(s, a) #obtener el estado siguiente s'=estado siguiente
                recompensa = recompensas[estado_siguiente] #obtener la recompensa del estado siguiente
                valor = recompensa + gamma * V[estado_siguiente] #calcular el valor del estado actual
                delta = max(delta, abs(V[s] - valor)) #actualizar el error
                V[s] = valor #actualizar el valor del estado actual
            if delta < limite: #si el error es menor que el limite, se considera convergencia
                break

        #mejor politica
        politica_estable = True #inicializar la política estable a True
        for s in estados:
            if s in estados_terminales or s == (1, 1): #si el estado es terminal o es la celda (1,1) no se actualiza la política
                continue

            accion_pasada = politica[s] #obtener la acción pasada
            mejor_valor = float('-inf') #inicializar el valor máximo a menos infinito
            mejor_accion = accion_pasada #inicializar la mejor acción a la acción pasada

            for a in acciones:
                estado_siguiente = movimiento(s, a) #obtener el estado siguiente al mover el agente
                recompensa = recompensas[estado_siguiente] #obtener la recompensa del estado siguiente
                valor = recompensa + gamma * V[estado_siguiente] #calcular el valor de la acción
                if valor > mejor_valor: #si el valor de la acción es mayor que el máximo encontrado
                    mejor_valor = valor #actualizar el valor máximo
                    mejor_accion = a #actualizar la mejor acción

            politica[s] = mejor_accion #actualizar la política del estado
            if mejor_accion != accion_pasada: #si la mejor acción es diferente a la acción pasada
                politica_estable = False #la política no es estable

        if politica_estable: #si la política es estable, se considera convergencia
            break

    return V, politica #retornar el valor y la política final

#ejecutar el algoritmo
valores, politica = iteracion_politica() #obtener el valor y la política final

#mostrar resultados
print("Valores de los estados:")
for i in range(3):
    for j in range(4):
        print(f"{valores[(i, j)]:6.2f}", end="  ") #imprimir el valor de cada estado
    print()

print("\nPolítica óptima:")
for i in range(3):
    for j in range(4):
        if (i, j) in estados_terminales: 
            print(" T  ", end="  ") #imprimir T para los estados terminales
        elif (i, j) == (1, 1): #si el estado es la celda (1,1)
            print("#  ", end="  ")  # muro
        else:
            print(f"{politica[(i, j)][:1].upper()}  ", end="  ") #imprimir la acción de la política
    print()

#Ejemplo de salida:
# Valores de los estados:
#   0.73    0.86    1.00    0.00
#   0.62    0.00    0.86    0.00
#   0.52    0.62    0.73    0.62

# Política óptima:
# D    D    D     T
# A    #    A     T
# A    D    A    I
#Este algoritmo nos ayudo a encontrar la mejor politica para el agente en el entorno dado, maximizando las recompensas y evitando los estados terminales negativos.