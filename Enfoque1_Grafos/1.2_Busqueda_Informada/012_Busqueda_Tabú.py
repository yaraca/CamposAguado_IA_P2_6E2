#Busqueda tabú 
#Es un algoritmo de optimización que se utiliza para resolver problemas de busqueda en espacios grandes y complejos 
#Se basa en la idea de explorar soluciones candidatas mientras evita volver a soluciones previamente visitadas
#El algoritmo utiliza una lista tabú para almacenar soluciones que no deben ser consideradas en la búsqueda actual
#Esto ayuda a evitar ciclos y permite al algoritmo escapar de óptimos locales
#El algoritmo comienza con una solución inicial y explora soluciones vecinas en cada iteración
#Si una solución vecina es mejor que la solución actual, se acepta como la nueva solución actual
#Si no hay soluciones vecinas mejores, se selecciona una solución de la lista tabú para ser aceptada
#El algoritmo continúa hasta que se alcanza un criterio de parada, como un número máximo de iteraciones o una solución óptima encontrada
#Sus aplicaciones incluyen optimización de rutas, planifiacion de horarios y asignación de recursos,optimización en ingenieria y finanzas

#Librerias necesarias
import random

#funcion de busqueda tabú
#parametros: funcion_objetivo: evaluar que tan buena es una solución, generar_vecinos: generar soluciones vecinas
#estado_inicial: solución inicial, max_iteraciones: número máximo de iteraciones, tamano_tabú: tamaño de la lista tabú
#retorna la mejor solución encontrada y su valor de la función objetivo
def busqueda_tabu(funcion_objetivo, generar_vecinos, estado_inicial, max_iteraciones = 100, tamano_tabu = 10):
    estado_actual = estado_inicial #se inicia con un estado aleatorio
    mejor_estado= estado_actual #se guarda la mejor solución encontrada
    mejor_valor = funcion_objetivo(estado_actual) #se evalua la mejor solución
    lista_tabu = [] #se inicializa la lista tabú para almacenar soluciones no deseadas

    for _ in range(max_iteraciones):
        vecinos = generar_vecinos(estado_actual) #se generan soluciones vecinas
        vecinos = [vecino for vecino in vecinos if vecino not in lista_tabu] #se eliminan los vecinos que estan en la lista tabu 
        if not vecinos: #si no hay vecinos disponibles, se termina la busqueda
            break
        #se selecciona el mejor vecino segun la funcion objetivo
        mejor_vecino = max(vecinos, key=funcion_objetivo) #se evalua el mejor vecino
        mejor_valor_vecino = funcion_objetivo(mejor_vecino) 
        #si el vecino mejora la mejor solución encontrada, se actualiza la mejor solución
        if mejor_valor_vecino > mejor_valor:
            mejor_estado, mejor_valor = mejor_vecino, mejor_valor_vecino #se actualiza la mejor solución
        #se actualiza el estado actual
        estado_actual = mejor_vecino
        #se agrega el estado actual a la lista tabú y se controla su tamaño 
        lista_tabu.append(mejor_vecino)
        if len(lista_tabu) > tamano_tabu:
            lista_tabu.pop(0) #se elimina el primer elemento de la lista tabú si excede el tamaño máximo
    return mejor_estado, mejor_valor #se retorna la mejor solución encontrada y su valor de la función objetivo

#Ejemplo de busqueda tabú
if __name__ == "__main__":
    #funcion objetivo: maximizar la suma de los elementos de una lista
    #f(x) = -x^2 + 4x (máximo en x = 2)
    def funcion_objetivo(x):
        return -x**2 + 4*x
    
    #funcipon generar vecinos: generar soluciones vecinas
    #generar vecino alrededor de x con pequeños cambios aleatorios
    def generar_vecinos(x):
        return [x + random.uniform(-0.5, 0.5) for _ in range(5)] #se generan 5 vecinos aleatorios alrededor de x
    
    estado_inicial = random.uniform(-10, 10) #se genera un estado inicial aleatorio entre -10 y 10
    mejor_x, mejor_f_x = busqueda_tabu(funcion_objetivo, generar_vecinos, estado_inicial) #se llama a la funcion de busqueda tabú

    print(f"Mejor x encontrado: {mejor_x:.4f}, f(x) = {mejor_f_x:.4f}") #se imprime la mejor solución encontrada y su valor de la función objetivo

#Ejemplo de salida: Mejor x encontrado: 2.0031, f(x) = 4.0000
