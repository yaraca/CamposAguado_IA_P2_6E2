#Gramáticas Probabilísticas Lexicalizadas
#son una extensión de las PCFG (Gramáticas Libres de Contexto Probabilísticas), que asocian palabras reales (léxicos) con los nodos del árbol sintáctico.
#Esto significa que no solo importa la estructura gramatical, sino también qué palabras específicas aparecen, especialmente en los nodos cabeza de las frases.
#funcionamiento: 
#Se elige un "head word" (palabra cabeza) para cada constituyente.
#Las reglas de producción incluyen esta palabra cabeza.
#Se calculan probabilidades condicionales más específicas como:
#P(NP → Det N | head = "niño")
#Esto permite desambiguar estructuras gramaticales con ayuda de la semántica léxica.
#aplicaciones: analisis sintáctico, traducción automática, y procesamiento del lenguaje natural.

#Ejemplo de gramática lexicalizada

#librerías necesarias
import nltk #para el procesamiento del lenguaje natural
from nltk.grammar import PCFG #para gramáticas probabilísticas libres de contexto
from nltk.parse.viterbi import ViterbiParser #para el análisis sintáctico usando el algoritmo Viterbi

#definir una Gramática Lexicalizada Simulada (agregando el "headword" a la etiqueta)
lexicalized_grammar = PCFG.fromstring("""
S -> NP^niño VP^juega [1.0]
NP^niño -> Det^el N^niño [1.0]
VP^juega -> V^juega NP^pelota [1.0]
NP^pelota -> Det^la N^pelota [1.0]
Det^el -> 'el' [1.0]
Det^la -> 'la' [1.0]
N^niño -> 'niño' [1.0]
N^pelota -> 'pelota' [1.0]
V^juega -> 'juega' [1.0]
""")

#crear un parser Viterbi usando esta gramática
parser = ViterbiParser(lexicalized_grammar)

#oracion de prueba
sentence = ['el', 'niño', 'juega', 'la', 'pelota']

#ejecutar el análisis
print("Árbol sintáctico lexicalizado:\n") 
for tree in parser.parse(sentence): #generar todos los árboles posibles
    print(tree) #imprimir el árbol sintáctico
    print(f"\nProbabilidad total del árbol: {tree.prob():.6f}") #imprimir la probabilidad total del árbol
    tree.pretty_print() #imprimir el árbol de forma legible

#ejemplo de salida: 
# Árbol sintáctico lexicalizado:

# (S
#   (NP^niño (Det^el el) (N^niño niño))
#   (VP^juega
#     (V^juega juega)
#     (NP^pelota (Det^la la) (N^pelota pelota)))) (p=1)

# Probabilidad total del árbol: 1.000000
#                          S
#            ______________|_______
#           |                   VP^juega
#           |               _______|_________
#        NP^niño           |             NP^pelota
#    _______|______        |        _________|________
# Det^el         N^niño V^juega  Det^la            N^pelota
#   |              |       |       |                  |
#   el            niño   juega     la               pelota
#como se puede observar, el árbol sintáctico muestra la estructura de la oración y las probabilidades asociadas a cada regla de producción.
#Esto permite entender cómo se combinan las palabras y cómo se relacionan entre sí dentro de la oración.
