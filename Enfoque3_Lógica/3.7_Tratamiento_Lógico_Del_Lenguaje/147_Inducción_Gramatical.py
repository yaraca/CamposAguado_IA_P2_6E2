#Inducción Gramatical
#es un enfoque que tiene como objetivo aprender una gramática formal a partir de ejemplos de oraciones o estructuras lingüísticas.
#a inducción gramatical busca inferir reglas lingüísticas que puedan generar o clasificar frases, basándose en ejemplos previos.
#se emplea en el aprendizaje automático, particularmente en el campo del Procesamiento del Lenguaje Natural (PLN)
#está vinculada a la gramática formal y lenguajes formales, que pueden ser utilizados para describir cómo las oraciones se estructuran en un idioma dado.
#Enfoques: 
# Inducción de Gramáticas Libres de Contexto (CFG): Se utiliza para aprender gramáticas que generen un conjunto de oraciones.
# Algoritmos de Aprendizaje Automático: Estos algoritmos utilizan ejemplos etiquetados de oraciones (como árboles de análisis sintáctico) para aprender reglas gramaticales.
# Aprendizaje de Reglas a partir de Datos de Texto: El objetivo es aprender una gramática que sea capaz de generar todas las oraciones posibles de un conjunto de datos, respetando las estructuras gramaticales observadas.
#Funcionamiento: 
# Entrada: Un conjunto de oraciones o ejemplos de frases que incluyen información sobre sus estructuras gramaticales.
# Aprendizaje de la Gramática: El algoritmo busca patrones en las oraciones para descubrir reglas gramaticales. Utiliza técnicas de aprendizaje automático y análisis de sintaxis.
# Generación de Reglas: A partir de los patrones observados, se genera un conjunto de reglas gramaticales que pueden describir las oraciones observadas.
# Evaluación: Las reglas generadas se prueban con nuevas oraciones para verificar si la gramática aprendida puede generar o analizar esas frases correctamente.
#Aplicaciones: reconocimiento de lenguaje natural, traducción automática, análisis de sentimientos, chatbots y asistentes virtuales.

#Ejemplo de Inducción Gramatical 
#aprender una gramática básica que reconozca oraciones como "El perro corre" o "La gata duerme".

#librerías necesarias
import nltk #para el procesamiento del lenguaje natural
from nltk import CFG #para la gramática libre de contexto

# Definir un conjunto de oraciones de ejemplo
sentences = [
    "El perro corre",
    "La gata duerme",
    "El gato juega",
    "El perro duerme",
    "La gata corre"
]

# Preprocesar las oraciones (convertir a listas de palabras)
sentences = [sentence.lower().split() for sentence in sentences] # Convertir a minúsculas y dividir en palabras

# Definir una gramática base (a priori, para aprender)
grammar = CFG.fromstring("""
  S -> NP VP
  NP -> Det N
  VP -> V
  Det -> 'el' | 'la'
  N -> 'perro' | 'gata' | 'gato'
  V -> 'corre' | 'duerme' | 'juega'
""")

# Función para analizar si las oraciones siguen la gramática
def analyze_sentence(sentence, grammar):
    # Crear un analizador sintáctico basado en la gramática
    parser = nltk.ChartParser(grammar)
    
    try: 
        # Analizar la oración
        for tree in parser.parse(sentence): # Generar árboles de análisis sintáctico
            tree.pretty_print()  # Imprimir el árbol de análisis
    except ValueError: # Manejar el caso en que la oración no se puede analizar
        print("No se puede analizar la oración: ", " ".join(sentence)) 

# Analizar las oraciones con la gramática definida
for sentence in sentences: #para cada oración en el conjunto de oraciones
    print(f"\nAnálisis de la oración: {' '.join(sentence)}") # Imprimir la oración
    analyze_sentence(sentence, grammar) ## Llamar a la función de análisis

#Ejemplo de salida: 

# Análisis de la oración: el perro corre
#           S
#       ____|_____
#      NP         VP
#   ___|____      |
# Det       N     V
#  |        |     |
#  el     perro corre


# Análisis de la oración: la gata duerme
#          S
#       ___|_____
#      NP        VP
#   ___|___      |
# Det      N     V
#  |       |     |
#  la     gata duerme


# Análisis de la oración: el gato juega
#          S
#       ___|_____
#      NP        VP
#   ___|___      |
# Det      N     V
#  |       |     |
#  el     gato juega


# Análisis de la oración: el perro duerme
#           S
#       ____|_____
#      NP         VP
#   ___|____      |
# Det       N     V
#  |        |     |
#  el     perro duerme


# Análisis de la oración: la gata corre
#          S
#       ___|_____
#      NP        VP
#   ___|___      |
# Det      N     V
#  |       |     |
#  la     gata corre

# El ejemplo de salida nos demuestra cómo las oraciones de entrada son analizadas y estructuradas
# según la gramática definida. Cada oración se descompone en sus componentes gramaticales (S, NP, VP, etc.),
# mostrando cómo se relacionan entre sí. Esto evidencia que la gramática es capaz de generar árboles
# de análisis sintáctico para las oraciones proporcionadas, validando su estructura gramatical.