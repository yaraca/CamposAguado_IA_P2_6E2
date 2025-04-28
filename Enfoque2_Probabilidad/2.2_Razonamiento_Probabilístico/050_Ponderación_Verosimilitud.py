#Ponderacion de verosimilitud
#Es un algoritmo de muestreo basado en evidencias que mejora el muestreo por rechazo.
#En lugar de descartar muestras que no cumplen la evidencia, las conserva pero les asigna un peso según qué tan verosímiles (probables) son con respecto a la evidencia.
#Se generan muestras de la red bayesiana, fijando las variables de evidencia.
#Se calcula un peso para cada muestra, que es el producto de las probabilidades de la evidencia dada la muestra.
#Las estimaciones se hacen ponderando por estos pesos.
#Se puede aplicar en redes bayesianas grandes, diagnostico con multiples sintomas, sistemas de prediccion con informacion parcial, etc.

#Ejemplo de ponderacion de verosimilitud
#variables:
# Clima: soleado / nublado
# Sprinkler (Rociador): sí / no
# Césped Mojado: sí / no

#librerias necesarias
import random #para generar números aleatorios

#Probabilidades base
P_Clima = {'soleado': 0.7, 'nublado': 0.3} #probabilidad de clima soleado o nublado
P_Sprinkler = {'soleado': {True: 0.1, False: 0.9}, 'nublado': {True: 0.5, False: 0.5}} #probabilidad de que el rociador esté activado o no, dado el clima
P_CespedMojado = { #probabilidad de que el césped esté mojado, dado el clima y si el rociador está activado o no
    (True, 'soleado'): {True: 0.9, False: 0.1}, #probabilidad de césped mojado dado que el clima es soleado y el rociador está activado o no
    (False, 'soleado'): {True: 0.2, False: 0.8}, #probabilidad de césped mojado dado que el clima es soleado y el rociador no está activado
    (True, 'nublado'): {True: 0.8, False: 0.2}, #probabilidad de césped mojado dado que el clima es nublado y el rociador está activado o no
    (False, 'nublado'): {True: 0.3, False: 0.7} #probabilidad de césped mojado dado que el clima es nublado y el rociador no está activado
}

#función para ponderación de verosimilitud
def ponderacion_verosimilitud(n_muestras, evidencia):
    muestras_ponderadas = [] #lista para almacenar las muestras ponderadas

    for _ in range(n_muestras): #iterar n_muestras veces
        peso = 1.0 #inicializar peso de la muestra

        #Elegir clima (no es evidencia)
        clima = random.choices(['soleado', 'nublado'], weights=[0.7, 0.3])[0] #elegir clima aleatoriamente según las probabilidades

        #Elegir rociador (no es evidencia)
        sprinkler = random.choices([True, False], weights=[ #probabilidad de que el rociador esté activado o no según el clima
            P_Sprinkler[clima][True], P_Sprinkler[clima][False]])[0] #elegir si el rociador está activado o no según el clima

        #Evaluar evidencia sobre césped mojado
        if 'CespedMojado' in evidencia: #si hay evidencia de césped mojado
            valor = evidencia['CespedMojado'] #obtener el valor de la evidencia
            prob_evidencia = P_CespedMojado[(sprinkler, clima)][valor] #probabilidad de césped mojado dado el clima y el estado del rociador
            peso *= prob_evidencia #multiplicar el peso por la probabilidad de la evidencia
            cesped_mojado = valor #asignar el valor de la evidencia a la muestra
        else: #si no hay evidencia de césped mojado
            cesped_mojado = random.choices([True, False], weights=[ #elegir si el césped está mojado o no según el clima y el estado del rociador
                P_CespedMojado[(sprinkler, clima)][True], # probabilidad de césped mojado dado que el clima es soleado y el rociador está activado
                P_CespedMojado[(sprinkler, clima)][False]])[0] #probabilidad de césped mojado dado que el clima es soleado y el rociador no está activado

        muestra = (clima, sprinkler, cesped_mojado) #crear la muestra con clima, rociador y césped mojado
        muestras_ponderadas.append((muestra, peso)) #agregar la muestra y su peso a la lista de muestras ponderadas

    return muestras_ponderadas #devolver la lista de muestras ponderadas generadas

#mostrar resultados
#Ponderación con evidencia: Césped mojado = True
print("Ponderación de Verosimilitud (evidencia: Césped mojado = True):")
evidencia = {'CespedMojado': True} #definir la evidencia
muestras_pond = ponderacion_verosimilitud(10, evidencia) #generar 10 muestras ponderadas con evidencia de césped mojado

for m, peso in muestras_pond: #iterar sobre las muestras ponderadas generadas
    print(f"Clima: {m[0]}, Sprinkler: {m[1]}, Césped Mojado: {m[2]} | Peso: {peso:.4f}") #imprimir cada muestra generada con su peso
#El resultado muestra las muestras generadas y sus pesos, que reflejan la verosimilitud de cada muestra con respecto a la evidencia dada.
#La ponderación de verosimilitud permite estimar la probabilidad de eventos en redes bayesianas grandes y complejas, considerando la evidencia disponible.

#ejemplo de salida:
# Ponderación de Verosimilitud (evidencia: Césped mojado = True):
# Clima: soleado, Sprinkler: False, Césped Mojado: True | Peso: 0.2000
# Clima: nublado, Sprinkler: True, Césped Mojado: True | Peso: 0.8000
# Clima: nublado, Sprinkler: True, Césped Mojado: True | Peso: 0.8000
# Clima: soleado, Sprinkler: False, Césped Mojado: True | Peso: 0.2000
# Clima: soleado, Sprinkler: False, Césped Mojado: True | Peso: 0.2000
# Clima: soleado, Sprinkler: False, Césped Mojado: True | Peso: 0.2000
# Clima: soleado, Sprinkler: False, Césped Mojado: True | Peso: 0.2000
# Clima: soleado, Sprinkler: False, Césped Mojado: True | Peso: 0.2000
# Clima: soleado, Sprinkler: False, Césped Mojado: True | Peso: 0.2000
# Clima: soleado, Sprinkler: False, Césped Mojado: True | Peso: 0.2000