#Análisis Léxico
#es el proceso mediante el cual una secuencia de caracteres se divide en unidades significativas llamadas tokens.
#Es una etapa inicial tanto en compiladores como en procesamiento de lenguaje natural (PLN).
#Funcionamiento: 
# Divide el texto en palabras, símbolos o categorías gramaticales (sustantivo, verbo, etc.).
# Elimina palabras irrelevantes (como “el”, “de”) si es necesario (stopwords).
# Sirve como entrada para análisis sintáctico o semántico.
#Aplicaciones: chatbots, motores de búsqueda, análisis de sentimientos, etc.

#Ejemplo de análisis léxico con spaCy

#librerías necesarias
import spacy  #importar la biblioteca spacy para procesamiento del lenguaje natural

#cargar el modelo de idioma español preentrenado
nlp=spacy.load("es_core_news_sm")

#definir el texto que será analizado
texto="El gato negro duerme profundamente en el sofá."

#procesar el texto utilizando el modelo de spaCy
doc=nlp(texto)

#print texto original antes de iniciar el análisis
print(" Texto original:")
print(texto)
print("\n Análisis léxico:\n")

#recorrer cada token en el documento analizado
for token in doc:
    #mostrar información detallada del token, incluyendo lema, categoría gramatical y etiqueta morfosintáctica
    print(f"Palabra: {token.text}\t | Lema: {token.lemma_}\t | POS: {token.pos_}\t | Etiqueta: {token.tag_}")

#Ejemplo de salida: 
#  Texto original:
# El gato negro duerme profundamente en el sofá.

#  Análisis léxico:

# Palabra: El      | Lema: el      | POS: DET      | Etiqueta: DET
# Palabra: gato    | Lema: gato    | POS: NOUN     | Etiqueta: NOUN
# Palabra: negro   | Lema: negro   | POS: ADJ      | Etiqueta: ADJ
# Palabra: duerme  | Lema: dormir  | POS: VERB     | Etiqueta: VERB
# Palabra: profundamente   | Lema: profundamente   | POS: ADV      | Etiqueta: ADV  
# Palabra: en      | Lema: en      | POS: ADP      | Etiqueta: ADP
# Palabra: el      | Lema: el      | POS: DET      | Etiqueta: DET
# Palabra: sofá    | Lema: sofá    | POS: NOUN     | Etiqueta: NOUN
# Palabra: .       | Lema: .       | POS: PUNCT    | Etiqueta: PUNCT

# El ejemplo de salida nos demuestra cómo spaCy realiza el análisis léxico de un texto.
# Cada palabra o símbolo del texto original se identifica como un token.
# Para cada token, se proporciona información como:
# - El texto original del token.
# - El lema, que es la forma base o raíz de la palabra.
# - La categoría gramatical (POS, Part of Speech), como sustantivo, verbo, adjetivo, etc.
# - La etiqueta morfosintáctica, que da más detalles sobre la función gramatical del token.
# Esto es útil para tareas de procesamiento de lenguaje natural como análisis gramatical, extracción de información, etc.