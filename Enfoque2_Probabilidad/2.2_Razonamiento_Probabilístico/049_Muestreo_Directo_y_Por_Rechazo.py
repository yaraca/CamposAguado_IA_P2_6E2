#Muestreo Directo (direct sampling) y Por Rechazo (rejection sampling)
#Es una técnica para estimar distribuciones de probabilidad usando datos generados aleatoriamente, especialmente útil cuando hay muchas variables o relaciones condicionales complicadas.
#Muestreo directo:Se generan muestras siguiendo la distribución completa, Utiliza el orden topológico de las variables para generar valores coherentes.
# Aplicación: Ideal cuando se tiene una red bayesiana completa, Útil para generar datos artificiales o estimar distribuciones marginales.
#Muestreo por rechazo: Se generan muestras de una distribución más simple y se rechazan aquellas que no cumplen con ciertas condiciones, Se utiliza una función de aceptación para decidir si se acepta o rechaza una muestra.
# Aplicación: Útil cuando se desea estimar distribuciones condicionales, como P(A|B=b).

#Ejemplo de muestreo directo y por rechazo
#variables: 
# Clima (soleado, nublado)
# Sprinkler (rociador activado)
# Césped mojado (sí/no)

#librerias necesarias
import random #para generar números aleatorios

#Probabilidades base (a priori)
P_Clima = {'soleado': 0.7, 'nublado': 0.3} #probabilidad de clima soleado o nublado
P_Sprinkler = {'soleado': {True: 0.1, False: 0.9}, 'nublado': {True: 0.5, False: 0.5}} #probabilidad de que el rociador esté activado o no, dado el clima
P_CespedMojado = { #probabilidad de que el césped esté mojado, dado el clima y si el rociador está activado o no
    (True, 'soleado'): {True: 0.9, False: 0.1}, #probabilidad de césped mojado dado que el clima es soleado y el rociador está activado o no
    (False, 'soleado'): {True: 0.2, False: 0.8}, #probabilidad de césped mojado dado que el clima es soleado y el rociador no está activado
    (True, 'nublado'): {True: 0.8, False: 0.2}, #probabilidad de césped mojado dado que el clima es nublado y el rociador está activado o no
    (False, 'nublado'): {True: 0.3, False: 0.7} #probabilidad de césped mojado dado que el clima es nublado y el rociador no está activado
}

#función para muestreo directo
def muestreo_directo(n_muestras):
    muestras = [] #lista para almacenar las muestras generadas
    for _ in range(n_muestras): #iterar n_muestras veces
        clima = random.choices(['soleado', 'nublado'], weights=[0.7, 0.3])[0] #elegir clima aleatoriamente según las probabilidades
        sprinkler = random.choices([True, False], weights=[ # elegir si el rociador está activado o no según el clima
            P_Sprinkler[clima][True], P_Sprinkler[clima][False]])[0] #probabilidad de que el rociador esté activado o no
        cesped_mojado = random.choices([True, False], weights=[ # elegir si el césped está mojado o no según el clima y el estado del rociador
            P_CespedMojado[(sprinkler, clima)][True], P_CespedMojado[(sprinkler, clima)][False]])[0] #probabilidad de que el césped esté mojado o no
        muestras.append((clima, sprinkler, cesped_mojado)) #agregar la muestra generada a la lista de muestras
    return muestras #devolver la lista de muestras generadas

#funcion para muestreo por rechazo
def muestreo_por_rechazo(n_muestras, evidencia):
    muestras_validas = [] #lista para almacenar las muestras válidas que cumplen con la evidencia
    while len(muestras_validas) < n_muestras: #mientras no se hayan generado suficientes muestras válidas
        muestra = muestreo_directo(1)[0]  # obtener una muestra aleatoria
        cumple = True #variable para verificar si la muestra cumple con la evidencia
        for variable, valor_esperado in evidencia.items(): #iterar sobre las variables de evidencia y sus valores esperados
            if variable == 'Clima' and muestra[0] != valor_esperado: # verificar si la muestra cumple con la evidencia
                cumple = False #si la variable es clima y no coincide con el valor esperado
            elif variable == 'Sprinkler' and muestra[1] != valor_esperado: # verificar si la muestra cumple con la evidencia
                cumple = False #if la variable es rociador y no coincide con el valor esperado
            elif variable == 'CespedMojado' and muestra[2] != valor_esperado: # verificar si la muestra cumple con la evidencia
                cumple = False  #if la variable es césped mojado y no coincide con el valor esperado 
        if cumple: #si la muestra cumple con la evidencia
            muestras_validas.append(muestra) #agregar la muestra válida a la lista de muestras válidas
    return muestras_validas #devolver la lista de muestras válidas generadas

#mostrar resultados
#Muestreo directo
print("Muestreo Directo:")
muestras = muestreo_directo(10) #generar 10 muestras
for m in muestras: #iterar sobre las muestras generadas
    print("Clima:", m[0], "| Sprinkler:", m[1], "| Césped Mojado:", m[2]) #imprimir cada muestra generada

#Muestreo por rechazo con evidencia: Césped mojado = True
print("\nMuestreo por Rechazo (evidencia: Césped mojado = True):") #generar muestras con evidencia de césped mojado
evidencia = {'CespedMojado': True} #definir la evidencia
muestras_filtradas = muestreo_por_rechazo(5, evidencia) #generar 5 muestras válidas que cumplan con la evidencia
for m in muestras_filtradas: #iterar sobre las muestras válidas generadas
    print("Clima:", m[0], "| Sprinkler:", m[1], "| Césped Mojado:", m[2]) #imprimir cada muestra válida generada

#ejemplo de salida:
# Muestreo Directo:
# Clima: soleado | Sprinkler: False | Césped Mojado: False
# Clima: soleado | Sprinkler: False | Césped Mojado: False
# Clima: soleado | Sprinkler: False | Césped Mojado: False
# Clima: nublado | Sprinkler: True | Césped Mojado: True
# Clima: soleado | Sprinkler: False | Césped Mojado: False
# Clima: soleado | Sprinkler: False | Césped Mojado: False
# Clima: soleado | Sprinkler: False | Césped Mojado: False
# Clima: soleado | Sprinkler: False | Césped Mojado: False
# Clima: soleado | Sprinkler: False | Césped Mojado: False
# Clima: nublado | Sprinkler: False | Césped Mojado: False

# Muestreo por Rechazo (evidencia: Césped mojado = True):
# Clima: nublado | Sprinkler: True | Césped Mojado: True
# Clima: soleado | Sprinkler: True | Césped Mojado: True
# Clima: soleado | Sprinkler: True | Césped Mojado: True
# Clima: nublado | Sprinkler: True | Césped Mojado: True
# Clima: nublado | Sprinkler: True | Césped Mojado: True