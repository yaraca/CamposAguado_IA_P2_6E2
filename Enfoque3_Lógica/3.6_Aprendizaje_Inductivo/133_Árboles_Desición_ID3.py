#Árboles de Decisión: ID3
#Un arbol de decisión Es una estructura jerárquica que divide datos en subconjuntos según decisiones basadas en atributos, para llegar a una clasificación o predicción.
#el ID3 construye el árbol de decisión utilizando una métrica llamada Ganancia de Información. Este selecciona el atributo que mejor separa los datos.
# Funcionamiento básico de ID3:
# Calcular la Entropía del conjunto de datos.
# Para cada atributo, calcular la ganancia de información.
# Elegir el atributo con mayor ganancia de información como nodo de decisión.
# Dividir el dataset y repetir recursivamente para cada subconjunto.
# Finalizar cuando todos los ejemplos estén correctamente clasificados o no queden atributos.
#Aplicaciones: diagnóstico médico, clasificación de correos electrónicos, análisis de riesgo crediticio, etc.

#Ejemplo de ID3
#clasifica si una persona jugará al tenis en función del clima

#librerías necesarias
import math #para cálculos matemáticos
from collections import Counter #para contar elementos en listas

import math  #importar el módulo math para cálculos matemáticos
from collections import Counter  #importar el módulo Counter para contar elementos en listas

#definir un conjunto de datos de ejemplo para jugar tenis
#cada entrada representa [Outlook, Temperature, Humidity, Wind] con una etiqueta de "Yes" o "No"
dataset=[
    (['Sunny', 'Hot', 'High', 'Weak'], 'No'),
    (['Sunny', 'Hot', 'High', 'Strong'], 'No'),
    (['Overcast', 'Hot', 'High', 'Weak'], 'Yes'),
    (['Rain', 'Mild', 'High', 'Weak'], 'Yes'),
    (['Rain', 'Cool', 'Normal', 'Weak'], 'Yes'),
    (['Rain', 'Cool', 'Normal', 'Strong'], 'No'),
    (['Overcast', 'Cool', 'Normal', 'Strong'], 'Yes'),
    (['Sunny', 'Mild', 'High', 'Weak'], 'No'),
    (['Sunny', 'Cool', 'Normal', 'Weak'], 'Yes'),
    (['Rain', 'Mild', 'Normal', 'Weak'], 'Yes'),
    (['Sunny', 'Mild', 'Normal', 'Strong'], 'Yes'),
    (['Overcast', 'Mild', 'High', 'Strong'], 'Yes'),
    (['Overcast', 'Hot', 'Normal', 'Weak'], 'Yes'),
    (['Rain', 'Mild', 'High', 'Strong'], 'No')
]

#definir una lista de atributos en los datos
atributos=['Outlook', 'Temperature', 'Humidity', 'Wind']

#definir una función para calcular la entropía de un conjunto de instancias
def entropia(instancias):
    total=len(instancias)  #calcular el número total de instancias
    clases=Counter([etiqueta for _, etiqueta in instancias])  #contar ocurrencias de cada etiqueta
    return -sum((v/total)*math.log2(v/total) for v in clases.values())  #calcular la entropía según la fórmula

#definir una función para calcular la ganancia de información al dividir por un atributo
def ganancia(instancias, indice_atributo):
    total_entropia=entropia(instancias)  #calcular la entropía del conjunto original
    valores={}  #crear un diccionario para agrupar instancias por el valor del atributo

    for entrada, etiqueta in instancias:  #recorrer las instancias
        key=entrada[indice_atributo]  #obtener el valor del atributo en la instancia
        if key not in valores:
            valores[key]=[]  #inicializar lista de instancias para ese valor
        valores[key].append((entrada, etiqueta))  #agregar la instancia al grupo correspondiente

    #calcular la entropía ponderada después de dividir el conjunto
    ponderada=sum((len(sub)/len(instancias))*entropia(sub) for sub in valores.values())
    return total_entropia-ponderada  #calcular la ganancia de información

#definir una función para construir el árbol de decisión de manera recursiva utilizando id3
def id3(instancias, atributos_disponibles):
    etiquetas=[etiqueta for _, etiqueta in instancias]  #obtener las etiquetas de las instancias
    if etiquetas.count(etiquetas[0])==len(etiquetas):  #si todas las instancias tienen la misma etiqueta
        return etiquetas[0]  #retornar la etiqueta como resultado

    if not atributos_disponibles:  #si no quedan atributos para dividir
        return Counter(etiquetas).most_common(1)[0][0]  #retornar la etiqueta más común

    #calcular la ganancia de información de cada atributo disponible
    ganancias=[(ganancia(instancias, i), i) for i in atributos_disponibles]
    mejor_ganancia, mejor_indice=max(ganancias, key=lambda x: x[0])  #seleccionar el mejor atributo
    mejor_atributo=mejor_indice  #guardar el índice del mejor atributo

    #crear un diccionario para almacenar la estructura del árbol
    arbol={atributos[mejor_atributo]: {}}
    valores_unicos=set([entrada[mejor_atributo] for entrada, _ in instancias])  #obtener valores únicos del atributo

    #crear ramas para cada posible valor del mejor atributo
    for valor in valores_unicos:
        subconjunto=[(entrada, etiqueta) for entrada, etiqueta in instancias if entrada[mejor_atributo]==valor]
        nuevos_atributos=[i for i in atributos_disponibles if i!=mejor_atributo]  #remover el mejor atributo de la lista
        arbol[atributos[mejor_atributo]][valor]=id3(subconjunto, nuevos_atributos)  #llamada recursiva para crear el árbol

    return arbol  #retornar el árbol construido

#entrenar el árbol de decisión utilizando el conjunto de datos
arbol_decision=id3(dataset, list(range(len(atributos))))

#mostrar el árbol de decisión resultante
import pprint  #importar el módulo pprint para impresión formateada
print("Árbol de decisión construido:\n")
pprint.pprint(arbol_decision)

#Ejemplo de salida:
# Árbol de decisión construido:

# {'Outlook': {'Overcast': 'Yes',
#              'Rain': {'Wind': {'Strong': 'No', 'Weak': 'Yes'}},
#              'Sunny': {'Humidity': {'High': 'No', 'Normal': 'Yes'}}}}

#Si el clima es Overcast, siempre se juega (Yes).
# Si el clima es Rain:
# Si el viento es Strong, No se juega.
# Si el viento es Weak, Sí se juega.
# Si el clima es Sunny:
# Si la humedad es High, No se juega.
# Si la humedad es Normal, Sí se juega.
#resume la lógica de decisión para el conjunto de datos de entrenamiento.
#Cada nodo evalúa un atributo y cada rama representa un valor posible de ese atributo, llegando a una conclusión final (Yes o No).
