#Red Bayesiana Dinámica
#Es una extensión temporal de las redes bayesianas, qu epermite modelar procesos secuenciales o tmeporales, como cambios de estado en el tiempo
#Se compone de: variables en el tiempo t (en ese instante) y t+1 (en el siguiente instante)
#intratiempo (relacion entre variables en el mismo instante) y entertiempo (relacion entre variables de t y t+1)
#Se pueden aplicar en: reconocimiento de gestos, voz o lenguanje, sistemas de diagnostico en tiemppo real, seguimiento de objetos, etc.

#Ejemplo de Red Bayesiana Dinámica

#librerias necesarias 
import random

#definir los estados y observaciones
estados = ['soleado', 'lluvioso'] #estados del clima
observaciones = ['brillante', 'oscuro'] #observaciones del sensor

#modelo de transicion del clima
#probabilida de pasar de estado t a estado t+1
modelo_transicion = {
    'soleado': {'soleado': 0.8, 'lluvioso': 0.2}, #probabilidad de pasar de soleado a soleado y de soleado a lluvioso
    'lluvioso': {'soleado': 0.3, 'lluvioso': 0.7} #probabilidad de pasar de lluvioso a soleado y de lluvioso a lluvioso
} 

#modelo de observacion del sensor
#probabilidad de observar algo dado el estado actual
modelo_observacion = {
    'soleado': {'brillante': 0.9, 'oscuro': 0.1}, #probabilidad de observar brillante o oscuro dado que el clima es soleado
    'lluvioso': {'brillante': 0.2, 'oscuro': 0.8} #probabilidad de observar brillante o oscuro dado que el clima es lluvioso
}

#estado de creencia inicial
creencia = {'soleado': 0.5, 'lluvioso': 0.5} #50% de probabilidad de que el clima sea soleado o lluvioso al inicio

#funcion para predecir el siguiente estado de creencia (prediccion temporal)
def predecir_siguiente(creencia):
    nueva_creencia = {'soleado': 0.0, 'lluvioso': 0.0} #inicializar la nueva creencia
    for estado_actual in estados:
        for estado_siguiente in estados: 
            #calcular la probabilidad de cada estado siguiente dado el estado actual
            nueva_creencia[estado_siguiente] += (
                creencia[estado_actual] * modelo_transicion[estado_actual][estado_siguiente]
            )
    return nueva_creencia #retorna la nueva creencia

#función para actualizar la creencia con una observación
def actualizar_con_observacion(creencia_predicha, observacion_real): 
    creencia_actualizada = {}
    for estado in estados:
        #calcular la probabilidad de cada estado dado la observación
        creencia_actualizada[estado] = (
            modelo_observacion[estado][observacion_real] * creencia_predicha[estado]
        )

    #normalización
    total = sum(creencia_actualizada.values()) #suma de todas las probabilidades
    for estado in creencia_actualizada: #normalizar cada probabilidad
        creencia_actualizada[estado] /= total #dividir cada probabilidad entre la suma total para que sumen 1

    return creencia_actualizada #retorna la creencia actualizada

#simulación por 5 pasos
print("Creencia inicial:", creencia)

estado_real = 'soleado'  #inicialmente el clima es soleado

for t in range(5):
    #simular el cambio de clima real
    estado_real = random.choices(estados, weights=[
        modelo_transicion[estado_real]['soleado'],
        modelo_transicion[estado_real]['lluvioso']
    ])[0]

    #simular la observación del sensor
    observacion = random.choices(observaciones, weights=[
        modelo_observacion[estado_real]['brillante'],
        modelo_observacion[estado_real]['oscuro']
    ])[0]

    #predecir el siguiente estado
    creencia_predicha = predecir_siguiente(creencia) 

    #actualizar con la observación
    creencia = actualizar_con_observacion(creencia_predicha, observacion) 

    print(f"\nTiempo {t+1}") #imprimir el tiempo
    print(f"Estado real: {estado_real}") #imprimir el estado real
    print(f"Observación recibida: {observacion}") #imprimir la observacion recibida
    print(f"Creencia actualizada: {creencia}") #imprimir la creencia actualizada

#Ejemplo de Salida
# Creencia inicial: {'soleado': 0.5, 'lluvioso': 0.5}

# Tiempo 1
# Estado real: soleado
# Observación recibida: brillante
# Creencia actualizada: {'soleado': 0.8461538461538461, 'lluvioso': 0.15384615384615383}

# Tiempo 2
# Estado real: soleado
# Observación recibida: brillante
# Creencia actualizada: {'soleado': 0.9215686274509804, 'lluvioso': 0.07843137254901962}

# Tiempo 3
# Estado real: soleado
# Observación recibida: brillante
# Creencia actualizada: {'soleado': 0.9346895074946466, 'lluvioso': 0.06531049250535333}

# Tiempo 4
# Estado real: soleado
# Observación recibida: brillante
# Creencia actualizada: {'soleado': 0.9368763525977138, 'lluvioso': 0.06312364740228617}

# Tiempo 5
# Estado real: soleado
# Observación recibida: brillante
# Creencia actualizada: {'soleado': 0.9372381857069129, 'lluvioso': 0.06276181429308714}