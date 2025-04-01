#Algoritmos genéticos (AG)
#Son una tecnica de optimizacion inspirada en la evolucion biologica y la seleccion natural.
#Usan mecanismos como la mutacion, cruce y seleccion para mejorar iterativamente una poblacion de soluciones a un problema dado.
#Los AG son utiles para resolver problemas complejos donde la busqueda exhaustiva es impracticable.
#Se aplican en la optimizacion de funciones matemáticas, entrenamiento de redes neuronales, resolucion de problemas combinatorios , etc

#Librerias necesarias
import random 

#parámetros del algoritmo genético
tamaño_poblacion = 10 #numero de soluciones en la poblacion
generaciones = 50 #numero máximo de iteraciones 
tasa_cruce = 0.8 #probabilidad de cruzar dos soluciones
tasa_mutacion = 0.1 #probabilidad de mutar una solución

#funcion objetivo: f(x) = -x^2 + 4x (máximo en x=2)
def funcion_objetivo(x):
    return -x**2 + 4*x

#funcion generar individuo aleatorio dentro del rango [-10, 10]
def generar_individuo():
    return random.uniform(-10, 10)

#funcion evaluar poblacion: evalucar cada individuo en la poblacion con la funcion objetivo
def evaluar_poblacion(poblacion):
    return [funcion_objetivo(individuo) for individuo in poblacion]

#funcion seleccionar padres: seleccionar dos padres usando seleccion por torneo
def seleccionar_padres(poblacion, aptitudes):
    torneo = random.sample(list(zip(poblacion, aptitudes)), k=3) #seleccionar 3 individuos aleatorios
    torneo.sort(key=lambda x: x[1], reverse=True) #ordenar por aptitud
    return torneo[0][0], torneo[1][0] #retornar los dos mejores individuos del torneo

#funcion cruzar: realiza el cruce d eun solo punto entre dos padres
def cruzar(padre1, padre2):
    if random.random() < tasa_cruce: #si se cumple la tasa de cruce
        alpha = random.uniform(0, 1) #seleccionar un punto de cruce aleatorio
        hijo1 = alpha * padre1 + (1 - alpha) * padre2 #crea el primer hijo 
        hijo2 = alpha * padre2 + (1 - alpha) * padre1 #crea el segundo hijo
    return padre1, padre2 #si no hay cruce, los hijos son copias de los padres

#funcion mutar: realiza mutacion aleatoria en un individuo
def mutar(individuo):
    if random.random() < tasa_mutacion: #si se cumple la tasa de mutacion 
        individuo += random.uniform(-0.5, 0.5)#cambia el individuo aleatoriamente
    return individuo #retorna el individuo mutado

#Funcion algoritmo genético
def algoritmo_genetico():
    #inicializar la poblacion aleatoriamente
    poblacion = [generar_individuo() for _ in range(tamaño_poblacion)] 

    for generacion in range(generaciones): #iterar sobre el numero de generaciones
        #evaluar la poblacion
        aptitudes = evaluar_poblacion(poblacion) 

        #crear nueva poblacion
        nueva_poblacion = [] #inicializar la nueva poblacion
        for _ in range(tamaño_poblacion // 2): #se generan parejas de padres
            padre1, padre2 = seleccionar_padres(poblacion, aptitudes) #seleccionar los padres
            hijo1, hijo2 = cruzar(padre1, padre2) #generar el cruce
            nueva_poblacion.extend([mutar(hijo1), mutar(hijo2)]) #añadir los hijos a la nueva poblacion
        
        #reemplazar la poblacion anterior por la nueva
        poblacion = nueva_poblacion 
    
    #obtener el mejor individuo de la poblacion final de las generaciones 
    mejor_individuo = max(poblacion, key=funcion_objetivo) #seleccionar el mejor individuo
    mejor_valor = funcion_objetivo(mejor_individuo) #evaluar la funcion objetivo en el mejor individuo
    return mejor_individuo, mejor_valor #retornar el mejor individuo y su valor en la funcion objetivo

#Ejemplode algoritmos genéticos 
if __name__ == "__main__":
    mejor_x, mejor_f_x = algoritmo_genetico() #llamar a la funcion
    print(f"Mejor x encontrado: {mejor_x:.4f}, f(x) = {mejor_f_x:.4f}") #imprimir el mejor individuo encontrado y su valor en la funcion objetivo

#Ejemplo de salida: Mejor x encontrado: 2.0027, f(x) = 4.0000


