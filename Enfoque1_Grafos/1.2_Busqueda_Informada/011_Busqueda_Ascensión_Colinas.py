#Busqueda de ascenso de colinas (hill climbing search)
#Algoritmo se basa en la heuristica para encontrar una solución optima 
#Siempre se mueve hacia el estado con el mejor valor heurística, como si estuvieras subiendo una colina 
#El algoritmo se detiene cuando no hay un estado vecino que tenga un valor heurístico mejor que el estado actual
#El algoritmo no garantiza encontrar la solución óptima, ya que puede quedar atrapado en un máximo local
#Algunas de sus aplicaciones son en la optimización de rutas, redes neuronales, juegos y robótica, diseño de circuitos electrónicos, etc.

#Librerias necesarias
import random

#Función para la busqueda de ascenso de colinas 
#Argumentos: problema(dict) = diccionario con vecinos y heuristica, estado_inicial(str) = estado inicial
#max_iteracion(int) = maximo de iteraciones
#Retorna tupla (estado, heuristica) = estado final y su heuristica
def colinas(problema, estado_inicial, max_iteracion=1000):
    estado_actual = estado_inicial 
    valor_actual = problema['heuristica'](estado_actual) #valor heurístico del estado actual

    for _ in range(max_iteracion): #iterar hasta el máximo de iteraciones 
        vecinos = problema['vecinos'](estado_actual) #obtener los vecinos del estado actual 
        if not vecinos: #si no hay vecinos, salir del bucle 
            break
        #Seleccionar un vecino aleatorio
        mejor_vecino = max(vecinos, key=lambda x: problema['heuristica'](x)) #obtener el vecino con el mejor valor heurístico 
        valor_vecino = problema['heuristica'](mejor_vecino) #valor heuristico del vecino 
        if valor_vecino <= valor_actual: #si el valor heurístico del vecino es menor o igual al del estado actual, salir del bucle 
            break

        estado_actual, valor_actual = mejor_vecino, valor_vecino #actualizar el estado actual y su valor heurístico
    return estado_actual, valor_actual #retornar el estado final y su valor heurístico

#Ejemplo de uso de la función colinas
if __name__ == "__main__":
    #Problema: Maximizar f(x) = -x^2 + 4x (maximo en x=2)
    problema = {
        'vecinos': lambda x: [x + random.uniform(-0.5, 0.5) for _ in range(10)], #generar 10 vecinos aleatorios
        'heuristica': lambda x: -x**2 + 4*x #funcion heuristica a maximizar
    }

    estado_inicial = random.uniform(-10, 10) #estado inicial aleatorio entre -10 y 10
    mejor_estado, valor = colinas(problema,estado_inicial) #llamar a la funcion colinas

    print(f"Mejor estado encontrado: x= {mejor_estado:.2f}, f(x)= {valor:.2f}") #imprimir el mejor estado encontrado y su valor heurístico

#Ejemplo de salida: 
#Mejor estado encontrado: x= 1.96, f(x)= 4.00
#Promedio de x encontrado: 1.9642
#Cantidad de veces que x ≈ 2: 976 de 1000

