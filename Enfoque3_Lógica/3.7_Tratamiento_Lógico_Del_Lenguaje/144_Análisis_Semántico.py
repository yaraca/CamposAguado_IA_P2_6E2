#Análisis Semántico
#es una etapa del procesamiento del lenguaje natural (PLN) encargada de interpretar el significado de las palabras, frases y oraciones.
#Mientras que el análisis sintáctico se centra en la estructura, el semántico busca comprender.
#Objetivos:
# Asociar palabras con su significado (desambiguación semántica).
# Entender relaciones entre conceptos.
# Detectar sinonimia, hiperonimia o contradicciones.
# Extraer información relevante.
#Funcionamiento: 
# Reglas lógicas: Representación de significados con lógica formal.
# Vectores semánticos: Representación matemática de significados (word embeddings).
# Redes semánticas: Modelos como WordNet o spaCy que relacionan conceptos.
#Aplicaciones: Chatbots, motores de búsqueda, análisis de sentimientos, traducción automática.

#Ejemplo de análisis semántico con spaCy

#librerías necesarias
import spacy  #importar la biblioteca spacy para procesamiento del lenguaje natural

#cargar el modelo de lenguaje en español preentrenado
nlp=spacy.load("es_core_news_sm")

#definir un texto de ejemplo para el análisis de entidades y relaciones sintácticas
texto="El presidente de México, Andrés Manuel López Obrador, visitó Estados Unidos en 2023 para reunirse con Joe Biden."

#procesar el texto con el modelo de spaCy
doc=nlp(texto)

#analizar y mostrar las entidades nombradas encontradas en el texto
print("Entidades nombradas:")
for ent in doc.ents:
    print(f"{ent.text} - {ent.label_}")  #mostrar el nombre de la entidad y su clasificación

#analizar y mostrar las dependencias sintácticas entre palabras
print("\nDependencias sintácticas:")
for token in doc:
    print(f"{token.text} ({token.dep_}) -> {token.head.text}")  #mostrar la palabra, su relación gramatical y su cabeza sintáctica

#extraer y mostrar relaciones semánticas entre entidades según dependencias clave
print("\nRelaciones semánticas identificadas:")
for token in doc:
    if token.dep_ in ('nsubj', 'dobj', 'prep'):  #seleccionar dependencias relevantes (sujeto, objeto directo, preposición)
        print(f"{token.dep_}: {token.text} -> {token.head.text}")  #mostrar la relación entre palabras en el contexto del texto


#Ejemplo de salida: 
# Entidades nombradas:
# México - LOC
# Andrés Manuel López Obrador - PER
# Estados Unidos - LOC
# Joe Biden - PER

# Dependencias sintácticas:
# El (det) -> presidente
# presidente (nsubj) -> visitó
# de (case) -> México
# México (nmod) -> presidente
# , (punct) -> Andrés
# Andrés (appos) -> presidente
# Manuel (flat) -> Andrés
# López (flat) -> Andrés
# Obrador (flat) -> Andrés
# , (punct) -> Andrés
# visitó (ROOT) -> visitó
# Estados (obj) -> visitó
# Unidos (flat) -> Estados
# en (case) -> 2023
# 2023 (obl) -> visitó
# para (mark) -> reunirse
# reunirse (advcl) -> visitó
# con (case) -> Joe
# Joe (obj) -> reunirse
# Biden (flat) -> Joe
# . (punct) -> visitó

# Relaciones semánticas identificadas:
# nsubj: presidente -> visitó

# El ejemplo de salida nos demuestra cómo spaCy identifica entidades nombradas en el texto, clasificándolas en categorías como LOC (ubicaciones) y PER (personas).
# También nos muestra cómo se analizan las dependencias sintácticas entre las palabras, indicando las relaciones gramaticales y las palabras principales asociadas.
# Finalmente, se identifican relaciones semánticas clave, como el sujeto (nsubj) y el objeto directo (dobj), lo que permite comprender mejor el significado del texto.