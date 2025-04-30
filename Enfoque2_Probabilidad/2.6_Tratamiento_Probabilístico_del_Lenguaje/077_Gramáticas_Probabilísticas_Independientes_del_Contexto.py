#Gramaticas probabilisticas independientes del contexto (CFG)
#define reglas para generar estructuras sintácticas de un lenguaje. Se compone de:
#Variables (No terminales): Símbolos como S (oración), NP (sintagma nominal), VP (sintagma verbal).
#Símbolos terminales: Palabras reales (el, niño, juega, etc).
#Producciones: Reglas de reescritura (como S → NP VP).
#Símbolo inicial: Normalmente S.
#Una Gramática Probabilística Libre de Contexto asocia una probabilidad a cada regla de producción. Estas probabilidades se usan para:
#Escoger la derivación más probable. Resolver ambigüedad sintáctica. Aprender patrones sintácticos del lenguaje a partir de un corpus.

#ejemplo de gramática probabilística independiente del contexto (PCFG) y su uso en análisis sintáctico

#Librerías necesarias
import nltk #librería para procesamiento de lenguaje natural
from nltk.grammar import PCFG #gramática probabilística independiente del contexto
from nltk.parse.viterbi import ViterbiParser #parser Viterbi para análisis sintáctico probabilístico

#definir la gramática PCFG
grammar = PCFG.fromstring("""
S -> NP VP [1.0] 
NP -> Det N [0.6] | Det Adj N [0.4]
VP -> V NP [0.5] | V [0.5]
Det -> 'el' [0.5] | 'la' [0.5]
N -> 'niño' [0.5] | 'pelota' [0.5]
Adj -> 'roja' [1.0]
V -> 'juega' [1.0]
""")
#s = S (oración), NP = sintagma nominal, VP = sintagma verbal, Det = determinante, N = sustantivo, Adj = adjetivo, V = verbo

#crear el parser Viterbi (elige la derivación más probable)
parser = ViterbiParser(grammar) #gramática probabilística independiente del contexto

#oración a analizar
sentence = ['el', 'niño', 'juega', 'la', 'pelota']

#analizar la oración
print("Árboles de análisis sintáctico y probabilidad total:\n")
for tree in parser.parse(sentence): #iterar por cada árbol de análisis sintáctico
    print(tree) #imprimir el árbol de análisis sintáctico
    print(f"\nProbabilidad total del árbol: {tree.prob():.6f}") #imprimir la probabilidad total del árbol
    tree.pretty_print() #imprimir el árbol de análisis sintáctico en formato legible

#ejemplo de salida:
# Árboles de análisis sintáctico y probabilidad total:

# (S
#   (NP (Det el) (N niño))
#   (VP (V juega) (NP (Det la) (N pelota)))) (p=0.01125)

# Probabilidad total del árbol: 0.011250
#                S
#       _________|____
#      |              VP
#      |          ____|___
#      NP        |        NP
#   ___|___      |     ___|____
# Det      N     V   Det       N
#  |       |     |    |        |
#  el     niño juega  la     pelota

#como se puede observar, el árbol de análisis sintáctico muestra la estructura jerárquica de la oración,
#donde cada nodo representa una categoría gramatical (S, NP, VP, etc.) y las hojas representan las palabras de la oración.
#La probabilidad total del árbol indica la probabilidad de que la oración dada sea generada por la gramática definida.