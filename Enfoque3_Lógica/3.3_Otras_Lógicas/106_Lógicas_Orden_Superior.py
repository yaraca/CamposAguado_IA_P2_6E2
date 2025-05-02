#Lógicas de Orden Superior
#son una extensión de la lógica de primer orden.
#En lógica de primer orden, puedes cuantificar sobre individuos (como personas, objetos). En lógica de orden superior, puedes además cuantificar sobre:
# Funciones (por ejemplo: "para toda función f, se cumple...")
# Predicados (por ejemplo: "para todo predicado P, se cumple...")
#La logica de orden superior Cuantifica sobre objetos, tiene una Menor capacidad expresiva y Menor complejidad computacional
#Aplicaciones:  matemáticas, informática, filosofía, lingüística, inteligencia artificial, etc

#Ejemplo de Lógica de Orden Superior
#Implementar una pequeña simulación donde:
# Hay funciones que representan propiedades (como “esPar”, “esMayorQue3”).
# Un evaluador aplica esas funciones a una lista de números.
# Se cuantifica sobre predicados: “¿existe un predicado tal que todos los elementos lo cumplen?”

# Lista de números a analizar
numeros = [2, 4, 6, 8, 10] 

#Función para definir predicados (funciones) de orden superior
def es_par(x): # Devuelve True si x es par
    return x % 2 == 0 

#Función mayor_que_3
def mayor_que_3(x): #devuelve True si x es mayor que 3
    return x > 3

#Función divisible_por_5
def divisible_por_5(x): #devuelve True si x es divisible por 5
    return x % 5 == 0

# Lista de predicados
predicados = [es_par, mayor_que_3, divisible_por_5] # Lista de funciones (predicados) a evaluar

#Función de Cuantificador universal: todos los elementos cumplen con el predicado
def para_todo(predicado, elementos): # Devuelve True si todos los elementos cumplen el predicado
    return all(predicado(x) for x in elementos)

#FUnción de Cuantificador existencial: existe un predicado tal que todos los elementos lo cumplen
def existe_predicado_que_cumple_todo(predicados, elementos):
    for p in predicados: #iterar sobre cada predicado
        if para_todo(p, elementos):  #si todos los elementos cumplen el predicado
            return True, p.__name__  #devolver el nombre del predicado que cumple
    return False, None

#Prueba de ejemplo
resultado, nombre_predicado = existe_predicado_que_cumple_todo(predicados, numeros) #evaluar si existe un predicado que cumple para todos los elementos de la lista


print("Lista:", numeros)
if resultado:   #si existe un predicado que cumple para todos los elementos
    print(f"Existe un predicado tal que todos los elementos lo cumplen: {nombre_predicado}") 
else: #si no existe un predicado que cumple para todos los elementos
    print("No existe ningún predicado que todos los elementos cumplan.")

#Ejemplo de salida: 
# Lista: [2, 4, 6, 8, 10]
# Existe un predicado tal que todos los elementos lo cumplen: es_par
#Como se puede ver, la función "es_par" cumple para todos los elementos de la lista, ya que todos son números pares.
#Si cambiamos la lista a [2, 4, 6, 8, 10, 11], el resultado sería "No existe ningún predicado que todos los elementos cumplan." porque el número 11 no es par.
#Esto demuestra cómo la lógica de orden superior permite cuantificar sobre funciones y predicados, lo que proporciona una mayor flexibilidad y expresividad en la lógica.