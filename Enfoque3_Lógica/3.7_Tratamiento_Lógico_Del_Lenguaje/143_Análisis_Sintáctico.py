#Análisis Sintáctico
#es una etapa del procesamiento del lenguaje natural (PLN) que se encarga de examinar la estructura gramatical de una oración y cómo las palabras se relacionan entre sí.
#Este análisis produce un árbol sintáctico, que representa las relaciones jerárquicas entre las partes de la oración.
#Su objetvo es: Determinar si una oración está bien formada gramaticalmente según una gramática dada.
#Funcionamiento: 
# Entrada: Texto en lenguaje natural.
# Tokenización: División en palabras.
# Etiquetado morfosintáctico: Determina el tipo gramatical de cada palabra.
# Análisis sintáctico: Construcción de un árbol que muestra la estructura jerárquica.
#Aplicaciones: Análisis de sentimientos, Resumen automático, Traducción automática, etc.

#Ejemplo de análisis sintáctico con spaCy

#Librerías necesarias
import spacy  #importar la biblioteca spacy para procesamiento del lenguaje natural
from spacy import displacy  #importar displacy para la visualización de estructuras sintácticas

#cargar el modelo de idioma español preentrenado
nlp=spacy.load("es_core_news_sm")

#definir el texto que será analizado
texto="El gato negro duerme profundamente en el sofá."

#procesar el texto utilizando el modelo de spaCy
doc=nlp(texto)

#print texto original antes de iniciar el análisis sintáctico
print(" Texto original:")
print(texto)
print("\n Análisis sintáctico:\n")

#recorrer cada token en el documento analizado
for token in doc:
    #mostrar la dependencia gramatical de cada palabra, incluyendo lema, tipo de palabra y relación sintáctica
    print(f"Palabra: {token.text:15} | Lema: {token.lemma_:10} | Tipo: {token.pos_:6} | Depende de: {token.head.text:15} | Relación: {token.dep_}")

#Ejemplo de salida: 
#  Texto original:
# El gato negro duerme profundamente en el sofá.

#  Análisis sintáctico:

# Palabra: El              | Lema: el         | Tipo: DET    | Depende de: gato            | Relación: det
# Palabra: gato            | Lema: gato       | Tipo: NOUN   | Depende de: duerme          | Relación: nsubj
# Palabra: negro           | Lema: negro      | Tipo: ADJ    | Depende de: gato            | Relación: amod
# Palabra: duerme          | Lema: dormir     | Tipo: VERB   | Depende de: duerme          | Relación: ROOT
# Palabra: profundamente   | Lema: profundamente | Tipo: ADV    | Depende de: duerme          | Relación: advmod
# Palabra: en              | Lema: en         | Tipo: ADP    | Depende de: sofá            | Relación: case
# Palabra: el              | Lema: el         | Tipo: DET    | Depende de: sofá            | Relación: det
# Palabra: sofá            | Lema: sofá       | Tipo: NOUN   | Depende de: duerme          | Relación: obl
# Palabra: .               | Lema: .          | Tipo: PUNCT  | Depende de: duerme          | Relación: punct

# El ejemplo de salida nos demuestra cómo spaCy analiza la estructura gramatical de una oración.
# Cada palabra (token) es descompuesta en sus componentes gramaticales, como el lema, el tipo gramatical,
# la palabra de la que depende y la relación sintáctica que tiene con ella.
# Esto permite entender cómo las palabras se relacionan entre sí y cómo se organiza la oración jerárquicamente.
# Además, muestra cómo se puede utilizar esta información para tareas de procesamiento del lenguaje natural.