#Explicaciones de Información Relevante
#En lugar de aprender por generalización directa (como en el algoritmo AQ), aquí se aprende al entender por qué algo funciona, usando el conocimiento previo.
#Es como cuando un estudiante no solo memoriza un problema resuelto, sino que aprende por qué se resuelve así, para aplicarlo en situaciones similares.
#Funcionamiento: 
# Entrada: un ejemplo positivo y un conjunto de conocimientos previos (dominio).
# Explicación: se construye una prueba lógica o inferencia que explique por qué ese ejemplo es verdadero.
# Generalización: se identifican los elementos relevantes para la explicación y se eliminan los irrelevantes.
# Salida: una regla general que sirve para reconocer o resolver nuevos ejemplos similares más rápidamente.
#Aplicaciones: sistemas expertos, diagnóstico médico, sistemas de recomendación, etc.

#Ejemplo de EBL (Explicaciones de Información Relevante): Diagnóstico de plantas
# Si una planta tiene hojas amarillas y está en sombra, entonces está enferma.
# El ejemplo positivo es: "Mi planta tiene hojas amarillas y está en sombra, y está enferma".

#definir una base de conocimientos con reglas de implicación lógica
conocimiento=[
    (["hojas_amarillas", "en_sombra"], "enferma"),  #si las hojas están amarillas y en sombra, la planta está enferma
    (["tierra_seca"], "sedienta"),  #si la tierra está seca, la planta necesita agua
    (["hojas_caidas", "sin_luz"], "débil")  #si las hojas han caído y no recibe luz, la planta está débil
]

#definir un ejemplo positivo con hechos observados y su conclusión esperada
ejemplo={
    "hechos": ["hojas_amarillas", "en_sombra", "maceta_grande"],  #hechos observados en la planta
    "conclusion": "enferma"  #conclusión esperada según los hechos
}

#definir una función para intentar encontrar una explicación en la base de conocimientos
def encontrar_explicacion(conocimiento, hechos, conclusion):
    explicaciones=[]  #crear una lista para almacenar posibles explicaciones
    for premisas, concl in conocimiento:  #recorrer las reglas en la base de conocimientos
        if concl==conclusion:  #verificar si la conclusión coincide con la esperada
            if all(p in hechos for p in premisas):  #verificar si todas las premisas están en los hechos observados
                explicaciones.append(premisas)  #agregar la premisa a la lista de explicaciones
    return explicaciones  #retornar las explicaciones encontradas

#definir la función principal del algoritmo ebl simplificado
def ebl(conocimiento, ejemplo):
    hechos=ejemplo["hechos"]  #obtener los hechos observados
    conclusion=ejemplo["conclusion"]  #obtener la conclusión esperada

    explicaciones=encontrar_explicacion(conocimiento, hechos, conclusion)  #buscar explicaciones en la base de conocimientos

    if not explicaciones:  #si no se encuentran explicaciones, mostrar un mensaje de error
        print(" No se encontró una explicación basada en el conocimiento.")
        return None

    #seleccionar la primera explicación válida y mostrar los elementos que la conforman
    explicacion_relevante=explicaciones[0]
    print(" Explicación encontrada:")
    for e in explicacion_relevante:  #recorrer los elementos de la explicación relevante
        print(f" - {e}")

    #generar la regla aprendida a partir de la explicación encontrada
    regla=(explicacion_relevante, conclusion)
    return regla  #retornar la regla generada

#ejecutar el algoritmo de explicación basada en el aprendizaje
regla_aprendida=ebl(conocimiento, ejemplo)

#mostrar la regla aprendida si se generó correctamente
if regla_aprendida:
    condiciones, conclusion=regla_aprendida  #extraer las condiciones y la conclusión de la regla
    condiciones_str=" Y ".join(condiciones)  #formatear las condiciones en una cadena de texto
    print(f"\n Regla aprendida: SI {condiciones_str} ENTONCES {conclusion}")  #mostrar la regla final generada

#Ejemplo de salida: 
#  Explicación encontrada:
#  - hojas_amarillas
#  - en_sombra

#  Regla aprendida: SI hojas_amarillas Y en_sombra ENTONCES enferma

# El ejemplo de salida nos demuestra cómo el algoritmo EBL (Explicación Basada en el Aprendizaje) 
# puede identificar los elementos relevantes de un conjunto de hechos observados para explicar 
# una conclusión esperada. En este caso, se encontró que las condiciones "hojas_amarillas" y 
# "en_sombra" son suficientes para explicar por qué la planta está "enferma". 
# Además, el algoritmo genera una regla general que puede ser utilizada para diagnosticar 
# otras plantas con características similares.