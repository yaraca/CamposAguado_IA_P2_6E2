#Gramáticas: Jerarquía de Chomsky
#La Jerarquía de Chomsky es una clasificación de las gramáticas formales que describe el poder expresivo de los lenguajes que pueden generar. 
#Tipos de gramáticas en la jerarquía:
# 0	Gramática irrestricta	            α → β	          Máquina de Turing
# 1	Gramática sensible al contexto	    αAβ → αγβ	      Autómata linealmente acotado
# 2	Gramática libre de contexto (CFG)	A → γ	          Autómata de pila
# 3	Gramática regular	                A → aB o A → a	  Autómata finito
#Aplicaciones: Procesamiento de Lenguaje Natural (NLP), compiladores, diseño de lenguajes de programación, etc.

#Ejemplo de chomsky
#Analizador sintáctico para una gramática libre de contexto (CFG)

#librerias necesarias
import nltk #para el procesamiento de lenguaje natural
from nltk import CFG #para la gramática libre de contexto

# Definimos la gramática libre de contexto (CFG)
gramatica = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V
Det -> 'El' | 'La'
N -> 'gato' | 'niña' | 'perro'
V -> 'come' | 'duerme' | 'corre'
""")

# Creamos el analizador sintáctico
parser = nltk.ChartParser(gramatica)

# Oraciones de prueba
oraciones = [
    ['El', 'gato', 'come'],
    ['La', 'niña', 'duerme'],
    ['El', 'perro', 'corre'],
    ['El', 'niña', 'corre']  # Esta es incorrecta (El + niña)
]

# Analizamos las oraciones
for oracion in oraciones: #para cada oración en la lista de oraciones
    print(f"\n Analizando: {' '.join(oracion)}") #imprimimos la oración
    try: #intenta analizar la oración
        encontrado = False #bandera para verificar si se encontró un árbol de análisis
        for arbol in parser.parse(oracion): #para cada árbol de análisis generado por el analizador
            arbol.pretty_print() #imprimimos el árbol de análisis
            encontrado = True #si se encontró un árbol de análisis
        if not encontrado: #si no se encontró un árbol de análisis
            print(" Oración inválida según la gramática.") #imprimimos que la oración es inválida
    except ValueError as e: #si ocurre un error de valor
        print(" Error de análisis:", e) #imprimimos el error de análisis

#Ejemplo de salida: 

#  Analizando: El gato come
#          S
#       ___|____
#      NP       VP
#   ___|___     |
# Det      N    V
#  |       |    |
#  El     gato come


#  Analizando: La niña duerme
#          S
#       ___|_____
#      NP        VP
#   ___|___      |
# Det      N     V
#  |       |     |
#  La     niña duerme


#  Analizando: El perro corre
#           S
#       ____|_____
#      NP         VP
#   ___|____      |
# Det       N     V
#  |        |     |
#  El     perro corre


#  Analizando: El niña corre
#          S
#       ___|_____
#      NP        VP
#   ___|___      |
# Det      N     V
#  |       |     |
#  El     niña corre

# El ejemplo de salida nos demuestra cómo se analizan las oraciones según la gramática definida.
# Para cada oración válida, se genera un árbol de análisis sintáctico que muestra su estructura gramatical.
# En el caso de oraciones inválidas (como "El niña corre"), aunque se genera un árbol, este no cumple con las reglas semánticas esperadas.
# Esto ilustra cómo las gramáticas libres de contexto pueden validar la estructura sintáctica, pero no necesariamente la semántica.
