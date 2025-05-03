#Vigilancia de Ejecución y Replanificación
# Es un enfoque de planificación reactiva que combina:
# Ejecución de un plan predefinido
# Monitoreo continuo del entorno durante la ejecución
# Replanificación automática si el entorno cambia o algo sale mal
#Funcionamiento: 
# Se genera un plan inicial.
# Se ejecutan las acciones una a una.
# Después de cada acción, se verifica que el estado del entorno sea el esperado.
# Si el estado es incorrecto o ha cambiado inesperadamente, se genera un nuevo plan (replanificación)
#Aplicaciones: Robótica móvil, vehículos autónomos, sistemas de control industrial, etc.

#Ejemplo de vigilancia de ejecución y replanificación
# Un robot quiere moverse en una cuadrícula del punto (0,0) al punto (2,2).
# A veces aparecen obstáculos inesperados, y el robot debe detectar el problema y recalcular su camino.

#librerías necesarias
import random # Para generar obstáculos aleatorios

import random  #importar el módulo random para generar valores aleatorios

#definir el tamaño del mapa como una matriz 3x3 inicializada con valores de 0 (espacios libres)
MAPA=[[0 for _ in range(3)] for _ in range(3)]  #0=libre, 1=obstáculo
#definir la posición del objetivo en el mapa
objetivo=(2, 2)
#definir la posición inicial del robot
inicio=(0, 0)

#generar un obstáculo aleatorio en una celda que no sea la inicial ni la del objetivo
ox, oy=random.choice([(x, y) for x in range(3) for y in range(3) if (x, y) not in [inicio, objetivo]])
MAPA[ox][oy]=1  #colocar el obstáculo en la celda seleccionada

#definir una función para generar un plan de movimiento desde la posición inicial hasta el objetivo
def generar_plan(x, y):
    plan=[]  #crear una lista para almacenar los movimientos
    while (x, y)!=objetivo:  #repetir mientras no se alcance la meta
        #si es posible moverse hacia abajo, hacerlo
        if x<2 and MAPA[x+1][y]==0:
            x+=1
            plan.append((x, y))
        #si no es posible moverse abajo pero sí a la derecha, hacerlo
        elif y<2 and MAPA[x][y+1]==0:
            y+=1
            plan.append((x, y))
        else:
            return None  #retornar None si el camino está bloqueado
    return plan  #retornar el plan generado

#definir una función para ejecutar el plan y vigilar obstáculos inesperados
def ejecutar_plan(plan):
    x, y=inicio  #iniciar desde la posición inicial
    for paso in plan:  #recorrer cada paso en el plan
        #si el robot detecta un obstáculo en el camino, interrumpir el plan
        if MAPA[paso[0]][paso[1]]==1:
            print(f"Obstáculo inesperado en {paso}, replanificando...")
            return False  #indicar que el plan falló y se necesita replanificación
        print(f" Moviéndose a {paso}")  #mostrar el movimiento exitoso
    return True  #retornar éxito si el plan se ejecutó completamente

#definir el proceso completo de vigilancia y replanificación
def vigilancia_y_replanificacion():
    print(f"Inicio: {inicio}, Objetivo: {objetivo}")
    print(f"Obstáculo inesperado en: ({ox}, {oy})")

    while True:  #repetir hasta alcanzar el objetivo o determinar que es inalcanzable
        plan=generar_plan(*inicio)  #generar un plan inicial
        if plan is None:  #si el plan no se puede generar, terminar el proceso
            print(" No se puede generar un plan. Objetivo inalcanzable.")
            break
        print("\n Plan generado:", plan)  #mostrar el plan generado
        exito=ejecutar_plan(plan)  #intentar ejecutar el plan
        if exito:  #si el plan es exitoso, finalizar el proceso
            print(" Objetivo alcanzado con éxito.")
            break
        else:
            print(" Intentando nuevo plan...")  #mensaje de replanificación
            MAPA[ox][oy]=0  #retirar el obstáculo para permitir la replanificación

#ejecutar el proceso completo de planificación y vigilancia
vigilancia_y_replanificacion()

#Ejemplo de salida:
# Inicio: (0, 0), Objetivo: (2, 2)
# Obstáculo inesperado en: (0, 2)

#  Plan generado: [(1, 0), (2, 0), (2, 1), (2, 2)]
#  Moviéndose a (1, 0)
#  Moviéndose a (2, 0)
#  Moviéndose a (2, 1)
#  Moviéndose a (2, 2)
#  Objetivo alcanzado con éxito.

# El ejemplo de salida nos muestra:
# 1. La posición inicial del robot y el objetivo que debe alcanzar.
# 2. La ubicación de un obstáculo inesperado en el mapa.
# 3. El plan generado por el algoritmo para llegar al objetivo evitando obstáculos.
# 4. Los movimientos realizados por el robot siguiendo el plan.
# 5. Un mensaje indicando que el objetivo fue alcanzado con éxito.