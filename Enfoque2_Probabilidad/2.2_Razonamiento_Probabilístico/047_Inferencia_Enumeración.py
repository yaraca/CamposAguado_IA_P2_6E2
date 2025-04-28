#Inferencia por Enumeración 
#es un método exacto que calcula la probabilidad de una variable de consulta (por ejemplo, P(X|e)) en una red bayesiana sumando todas las probabilidades posibles compatibles con la evidencia.
#Dado un conjunto de variables de consulta X, evidencia e y variables ocultas Y, formula es:
#P(X|e) = α * ∑(y) P(X, Y, e) 
#donde α es una constante de normalización que asegura que la suma de las probabilidades sea 1.
#Se enumeran todas las asignaciones posibles de las variables ocultas Y
#Se usa el modelo de la red para calcular P(X, Y, e) para cada caso
#Se normaliza para obtener probabilidades que sumen 1.
#Es preciso pero costoso computacionalmente para redes grandes, debido a la cantidad de combinaciones posibles de variables ocultas.
#Se puede aplicar en: predicciones medicas, diagnósticos, sistemas de recomendación, etc.

#Ejemplo de Inferencia por Enumeración
#Supongamos la siguiente red bayesiana:
#Burglary(allanamiento de morada) -> Alarm <- Earthquake, Alarm -> JohnCalls, Alarm -> MaryCalls
#Burglary y Earthquake son variables de entrada, Alarm es una variable intermedia y JohnCalls y MaryCalls son variables de salida.
#queremos calcular la probabilidad de que haya una alarma, dado que John llamó y Mary llamó

#librerias necesarias
from itertools import product

#definir la red bayesiana como un diccionario 
#cada variable tiene:
# - 'padres': lista de padres
# - 'tabla': tabla de probabilidad condicional
red = { #definimos la red bayesiana
    "Burglary": { 
        "padres": [], #no tiene padres
        "tabla": { #tabla de probabilidad condicional
            (): 0.001 #probabilidad de que haya un allanamiento de morada
        }
    },
    "Earthquake": {
        "padres": [], #no tiene padres
        "tabla": { #tabla de probabilidad condicional
            (): 0.002 #probabilidad de que haya un terremoto
        }
    },
    "Alarm": {
        "padres": ["Burglary", "Earthquake"], #padres son Burglary y Earthquake
        "tabla": {
            (True, True): 0.95, #probabilidad de que suene la alarma si hay un allanamiento y un terremoto
            (True, False): 0.94, #probabilidad de que suene la alarma si hay un allanamiento y no hay terremoto
            (False, True): 0.29, #probabilidad de que suene la alarma si no hay un allanamiento y hay un terremoto
            (False, False): 0.001 #probabilidad de que suene la alarma si no hay un allanamiento y no hay un terremoto
        }
    },
    "JohnCalls": {
        "padres": ["Alarm"], #padre es Alarm
        "tabla": {
            (True,): 0.90, #probabilidad de que John llame si suena la alarma
            (False,): 0.05 #probabilidad de que John llame si no suena la alarma
        }
    },
    "MaryCalls": {
        "padres": ["Alarm"], #padre es Alarm
        "tabla": {
            (True,): 0.70, #probabilidad de que Mary llame si suena la alarma
            (False,): 0.01 #probabilidad de que Mary llame si no suena la alarma
        }
    }
}

#función para obtener la probabilidad de una variable
def prob(variable, valor, evidencia): 
    padres = red[variable]["padres"] #obtenemos los padres de la variable
    # Si la variable ya está en la evidencia, devolvemos su valor
    tabla = red[variable]["tabla"] #obtenemos la tabla de probabilidad condicional
    valores_padres = tuple(evidencia[p] for p in padres) #obtenemos los valores de los padres en la evidencia
    p = tabla[valores_padres] #obtenemos la probabilidad de la variable dada los padres
    return p if valor else 1 - p #probabilidad de que la variable sea True o False

# Función recursiva para enumerar todas las variables ocultas
def enumerar_variables(variables, evidencia):
    if not variables: #si no hay variables, devolvemos 1.0
        return 1.0
    Y = variables[0] #obtenemos la primera variable
    resto = variables[1:] #obtenemos el resto de las variables
    if Y in evidencia: #si la variable ya está en la evidencia, la eliminamos de las variables ocultas
        return prob(Y, evidencia[Y], evidencia) * enumerar_variables(resto, evidencia) #calculamos la probabilidad de la variable dada la evidencia y el resto de las variables
    else: #si la variable no está en la evidencia, iteramos sobre sus valores posibles (True y False)
        suma = 0 #inicializamos la suma en 0
        for y in [True, False]: #iteramos sobre los valores posibles de la variable
            evidencia_copia = evidencia.copy() #hacemos una copia de la evidencia
            evidencia_copia[Y] = y #agregamos la variable a la evidencia
            suma += prob(Y, y, evidencia_copia) * enumerar_variables(resto, evidencia_copia) #calculamos la probabilidad de la variable dada la evidencia y el resto de las variables
        return suma #devolvemos la suma de las probabilidades de la variable dada la evidencia y el resto de las variables
    
#funcion principal de inferencia por enumeración
def inferencia_por_enumeracion(variable_consulta, evidencia):
    Q = {} #diccionario para almacenar las probabilidades de la variable de consulta
    variables = list(red.keys()) #obtenemos todas las variables de la red
    for val in [True, False]: #iteramos sobre los valores posibles de la variable de consulta (True y False)
        evidencia_copia = evidencia.copy() #hacemos una copia de la evidencia
        evidencia_copia[variable_consulta] = val #agregamos la variable de consulta a la evidencia
        Q[val] = enumerar_variables(variables, evidencia_copia) #calculamos la probabilidad de la variable de consulta dada la evidencia y la variable de consulta

    #Normalizar
    total = sum(Q.values()) #sumar todas las probabilidades
    for val in Q: #iteramos sobre los valores de la variable de consulta
        Q[val] /= total #normalizamos la probabilidad dividiendo por la suma total
    return Q #devolvemos el diccionario con las probabilidades de la variable de consulta

# Ejemplo: P(Alarm | JohnCalls=True, MaryCalls=True) (probabilidad de que suene la alarma dado que John y Mary llamaron)
evidencia = {"JohnCalls": True, "MaryCalls": True} #definir la evidencia
resultado = inferencia_por_enumeracion("Alarm", evidencia) #llamar a la función de inferencia por enumeración

#mostrar resultados
print("P(Alarm | JohnCalls=True, MaryCalls=True):")
for val in resultado: #iteramos sobre los valores de la variable de consulta
    print(f"  Alarm={val}: {resultado[val]:.4f}") #mostramos la probabilidad de la variable de consulta dada la evidencia

#Ejemplo de salida:
# P(Alarm | JohnCalls=True, MaryCalls=True):
#   Alarm=True: 0.7607
#   Alarm=False: 0.2393
#esto significa que la probabilidad de que suene la alarma dado que John y Mary llamaron es de aproximadamente 0.7607 (76.07%)
#y la probabilidad de que no suene la alarma dado que John y Mary llamaron es de aproximadamente 0.2393 (23.93%)
#esto indica que es más probable que suene la alarma dado que John y Mary llamaron, lo cual es consistente con la lógica de la red bayesiana
