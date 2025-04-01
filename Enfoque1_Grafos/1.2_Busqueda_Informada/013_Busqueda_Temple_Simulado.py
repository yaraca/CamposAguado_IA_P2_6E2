#Busqueda de temple simulado (Simulated Annealing SA)
#Es un algoritmo de optimización inspirado en le proceso de enfriamiento de metales
#Donde la estructura del material se reorganiza para alcanzar un estado de menor energía 
#El algoritmo busca minimizar una función de costo, explorando soluciones vecinas y aceptando soluciones peores con cierta probabilidad
#Para evitar quedar atrapado en un óptimo local
#Se puede aplicar en optimización combinatoria, redes neuronales, diseño de circuitos electrónicos,etc.

#Librerias necesarias
import random
import math

#Función de busqueda de temple simulado
#parametros: funcion_objetivo= función a optimizar, generar_vecinos= función que genera soluciones vecinas, estados_inicial= estado inicial de la busqueda
#temp_inicial= temperatura inicial, factor_enfriamiento= facto para reducir la temperatura en cada iteración
#min_temp = temperatura minima antes de detener la busqueda, max_iteraciones= maximo de iteraciones
#retorna la mejor solución encontrada y su costo

def temple_simulado(funcion_objetivo, generar_vecinos, estado_inicial, temp_inicial = 100, factor_enfriamiento = 0.99, min_temp = 0.1, max_iteraciones = 1000):
    estado_actual = estado_inicial #Estado inicial
    mejor_estado = estado_actual #se guarda la mejor solución encontrada
    mejor_valor = funcion_objetivo(estado_actual) #evaluamos la función objetivo en el estado inicial
    temperatura = temp_inicial #temperatura inicial

    for _ in range(max_iteraciones):
        if temperatura < min_temp:#si la temperatura es menor a la minima, se detiene la busqueda
            break
        vecino = generar_vecinos(estado_actual) #generamos un vecino del estado actual
        valor_vecino = funcion_objetivo(vecino) #evaluamos la función objetivo en el vecino

        diferencia = valor_vecino - funcion_objetivo(estado_actual) #calculamos la diferencia entre el valor del vecino y el estado actual

        if diferencia > 0 or random.uniform(0,1) < math.exp(diferencia / temperatura): #si la diferencia es positiva o si se acepta la solución peor con cierta probabilidad
            estado_actual = vecino #se actualiza el estado actual 
        
        if funcion_objetivo(estado_actual) > mejor_valor: #si el valor del estado actual es mejor que el mejor valor encontrado
            mejor_estado, mejor_valor = estado_actual, funcion_objetivo(estado_actual) #se actualiza la mejor solución encontrada
        
        temperatura *= factor_enfriamiento #se reduce la temperatura
    return mejor_estado, mejor_valor #se retorna la mejor solución encontrada y su costo

#Ejemplo de busqueda de temple simulado 
if __name__ == "__main__":
    #función objetivo a maximizar: f(x) = -x^2 + 4x (máximo en x = 2)
    def funcion_objetivo(x):
        return -x**2 + 4*x
    
    #función para generar un vecino aleatorio cerca de x
    def generar_vecinos(x):
        return x + random.uniform(-0.5, 0.5)
    
    #estado inicial 
    estado_inicial = random.uniform(-10, 10) #valor aleatorio entre -10 y 10

    mejor_x, mejor_f_x = temple_simulado(funcion_objetivo, generar_vecinos, estado_inicial) #se llama a la función de busqueda de temple simulado

    print(f"Mejor x encontrado: {mejor_x:.4f}, f(x) = {mejor_f_x:.4f}") #se imprime la mejor solución encontrada y su costo

#Ejemplo de salida:Mejor x encontrado: 1.9932, f(x) = 4.0000
        

