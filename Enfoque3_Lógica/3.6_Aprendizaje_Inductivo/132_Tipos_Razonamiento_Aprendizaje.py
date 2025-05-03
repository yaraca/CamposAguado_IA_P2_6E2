#Tipos de Razonamiento y Aprendizaje
#El razonamiento es el proceso mental (o computacional) de extraer conclusiones lógicas a partir de conocimientos previos.
#Tipos de razonamiento:
# Deductivo: De lo general a lo particular. Ej: Todos los perros tienen 4 patas → Mi perro es un perro → Tiene 4 patas.
# Inductivo: De lo particular a lo general. Ej: He visto 10 cisnes blancos → Probablemente todos los cisnes sean blancos.
# Abductivo: La mejor explicación para una observación. Ej: La calle está mojada → Probablemente llovió.
#El aprendizaje Es una técnica en la que una máquina aprende reglas o patrones generales a partir de ejemplos específicos.
#Aplicaciones: clasificadores, sistemas de recomendación, detección de fraudes, etc.

#Ejemplo de tipos de razonamiento y aprendizaje inductivo
#algoritmo inductivo simple que aprenda a clasificar frutas como "dulces" o "no dulces" en base a sus características (color y tamaño).

#definir una lista de datos de entrenamiento con frutas caracterizadas por color, tamaño y etiqueta de dulzura
datos_entrenamiento=[
    {"color": "rojo", "tamaño": "grande", "etiqueta": "dulce"},
    {"color": "verde", "tamaño": "pequeño", "etiqueta": "no dulce"},
    {"color": "amarillo", "tamaño": "mediano", "etiqueta": "dulce"},
    {"color": "verde", "tamaño": "grande", "etiqueta": "dulce"},
    {"color": "rojo", "tamaño": "pequeño", "etiqueta": "no dulce"},
]

#realizar aprendizaje inductivo analizando qué colores y tamaños son más frecuentes en frutas dulces
from collections import Counter  #importar el módulo Counter para contar elementos en listas

#inicializar contadores para colores y tamaños de frutas dulces
colores_dulces=Counter()
tamaños_dulces=Counter()

#recorrer cada fruta en los datos de entrenamiento
for fruta in datos_entrenamiento:
    if fruta["etiqueta"]=="dulce":  #verificar si la fruta está etiquetada como dulce
        colores_dulces[fruta["color"]]+=1  #contabilizar el color en el conjunto de frutas dulces
        tamaños_dulces[fruta["tamaño"]]+=1  #contabilizar el tamaño en el conjunto de frutas dulces

#definir una función para predecir si una fruta es dulce o no según los patrones aprendidos
def predecir_dulzura(color, tamaño):
    puntuacion=0  #inicializar un contador de puntuación
    if colores_dulces[color]>0:  #verificar si el color ha aparecido en frutas dulces
        puntuacion+=1
    if tamaños_dulces[tamaño]>0:  #verificar si el tamaño ha aparecido en frutas dulces
        puntuacion+=1
    return "dulce" if puntuacion>=2 else "no dulce"  #clasificar la fruta como dulce si cumple ambos criterios

#definir una lista de frutas nuevas para clasificar
nuevas_frutas=[
    {"color": "rojo", "tamaño": "grande"},
    {"color": "verde", "tamaño": "pequeño"},
    {"color": "amarillo", "tamaño": "grande"},
    {"color": "morado", "tamaño": "mediano"},
]

#clasificar las nuevas frutas utilizando el modelo aprendido
for fruta in nuevas_frutas:
    prediccion=predecir_dulzura(fruta["color"], fruta["tamaño"])
    print(f"Fruta con color {fruta['color']} y tamaño {fruta['tamaño']} → Predicción: {prediccion}")

#Ejemplo de salida:
# Fruta con color rojo y tamaño grande → Predicción: dulce
# Fruta con color verde y tamaño pequeño → Predicción: no dulce
# Fruta con color amarillo y tamaño grande → Predicción: dulce
# Fruta con color morado y tamaño mediano → Predicción: no dulce

# El ejemplo de salida nos muestra cómo el modelo inductivo clasifica nuevas frutas
# basándose en los patrones aprendidos de los datos de entrenamiento. En este caso:
# - Una fruta roja y grande se clasifica como "dulce" porque ambos atributos son comunes en frutas dulces.
# - Una fruta verde y pequeña se clasifica como "no dulce" porque ninguno de los atributos es común en frutas dulces.
# - Una fruta amarilla y grande se clasifica como "dulce" porque al menos uno de los atributos es común en frutas dulces.
# - Una fruta morada y mediana se clasifica como "no dulce" porque ninguno de los atributos aparece en frutas dulces.