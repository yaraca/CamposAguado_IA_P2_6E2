#Busqueda de haz local (local beam search)
#Es un algoritmo de optimización que mejor la eficiiencia de la busqueda en espacio de estado grnades al mantener y explorar multiples soluciones simultaneamente.
#El haz local trabaja ocn un conjunto de k soluciones en cada iteración 
#en lugar de una sola solución. En cada iteración, el algoritmo selecciona las k mejores soluciones de un conjunto de soluciones candidatas y las expande para generar nuevas soluciones.
#Este proceso se repite hasta que se alcanza una solución satisfactoria o se cumple un criterio de parada.
#El algoritmo de haz local es útil en problemas donde la búsqueda exhaustiva es impracticable debido al tamaño del espacio de búsqueda.
#Se puede aplicar en la optimizacion combinatoria, la inteligencia artificial y el aprendizaje automático.

#Librerias necesarias
import random

#función de busqueda de haz loca
#parametros: funcion_objetivo= Función a optimizar, generar_vecinos= función que genera soluciones vecinas, estados_iniciales= lista con los k estados iniciales
#k= numero de soluciones a mantener en cada iteracion, max_iteraciones= numero maximo de iteraciones
#retorna: mejor solucion encontrada y su valor en la función objetivo
def haz_local(funcion_objetivo, generar_vecinos, estados_iniciales, k = 3, max_iteraciones = 100):
    poblacion = estados_iniciales #se inicializa la poblacion con los k estaods iniciales 

    for _ in range(max_iteraciones):
        #generar todos los vecinos de los estados actuales
        vecinos = [] #se inicializa la lista de vecinos
        for estado in poblacion: #se itera sobre la poblacion
            vecinos.extend(generar_vecinos(estado)) #se generan los vecinos de cada estado y se añaden a la lista de vecinos 
        
        #seleccionar los k mejores vecinos segun la funcion objetivo 
        poblacion= sorted(vecinos, key=funcion_objetivo, reverse=True)[:k] 
    
    mejor_estado = poblacion[0] #se selecciona el mejor estado de la poblacion
    mejor_valor = funcion_objetivo(mejor_estado) #se evalua la funcion objetivo en el mejor estado
    return mejor_estado, mejor_valor #se retorna el mejor estado y su valor en la funcion objetivo 

#ejemplo de busqueda de haz local
if __name__ == "__main__":
    #funcion objetivo: Maximizar f(x) = -x^2 + 4x (máximo en x = 2)
    def funcion_objetivo(x):
        return -x**2 + 4*x
    
    #funcion generar vecinos: 5 vecins aleatorios cerca de x
    def generar_vecinos(x):
        return [x + random.uniform(-0.5, 0.5) for _ in range(5)]
    
    #generar estados iniciales aleatorios entre -10 y 10
    k = 3
    estados_iniciales = [random.uniform(-10, 10) for _ in range(k)] 

    #llamar a la funcion 
    mejor_x, mejor_f_x = haz_local(funcion_objetivo, generar_vecinos, estados_iniciales, k)

    print(f"Mejor x encontrado: {mejor_x:.4f}, f(x) = {mejor_f_x:.4f}") #imprime el mejor estado encontrado y su valor en la funcion objetivo

#Ejemplo de salida: Mejor x encontrado: 1.9945, f(x) = 4.0000