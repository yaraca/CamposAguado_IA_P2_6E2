#Ambigüedad
#se refiere a la capacidad de una palabra, frase o estructura gramatical para tener más de un significado
#En el contexto del tratamiento lógico del lenguaje, la ambigüedad puede ser tanto léxica como sintáctica.
#Ambigüedad Léxica: Se presenta cuando una palabra tiene múltiples significados posibles.
#Ambigüedad Sintáctica: Se presenta cuando una frase tiene una estructura que puede ser interpretada de diferentes maneras debido a la gramática
#En este tipo de algoritmos, el objetivo es identificar y resolver ambigüedades en una oración utilizando información contextual o reglas gramaticales
#Tecnicas: 
#Desambiguación Léxica: Se puede realizar mediante el uso de diccionarios, redes semánticas (como WordNet) o modelos basados en contexto, como las redes neuronales.
#Desambiguación Sintáctica: Utiliza árboles sintácticos para determinar la interpretación más probable de una oración, considerando el contexto y las reglas gramaticales.
#Aplicaciones: proceso de lenguaje natural, traducción automática, sistemas de preguntas y respuestas, chatbots, etc.

#Ejemplo de ambigÜedad léxica
#desambiguar el significado de la palabra "banco"

#librerias necesarias
import spacy  #importar la biblioteca spacy para procesamiento del lenguaje natural
from nltk.corpus import wordnet as wn  #importar wordnet desde nltk para manejo de significado de palabras
from nltk.tokenize import word_tokenize  #importar función para tokenizar palabras

#cargar el modelo en español de spacy para análisis lingüístico
nlp=spacy.load("es_core_news_md")

#definir una oración de ejemplo con ambigüedad léxica
texto="Voy a ir al banco a retirar dinero."

#procesar el texto con el modelo de spacy
doc=nlp(texto)

#mostrar el análisis de dependencias sintácticas del texto
print("Análisis de dependencias:")
for token in doc:
    print(f'{token.text} -> {token.dep_} -> {token.head.text}')  #mostrar la relación de dependencia de cada palabra

#inicializar una variable para verificar si la palabra "banco" está presente en el texto
banco_found=False

#recorrer cada token en el documento para realizar la desambiguación léxica de "banco"
for token in doc:
    if token.text.lower()=="banco":  #verificar si el token es "banco"
        banco_found=True
        #comprobar el contexto: si la palabra "dinero" está cerca, "banco" se refiere a una institución financiera
        if "dinero" in [t.text.lower() for t in doc]:
            banco_sentido="banco (institución financiera)"
        else:
            banco_sentido="banco (lugar físico para sentarse)"
        print(f"\nAmbigüedad resuelta para 'banco': {banco_sentido}")  #mostrar la interpretación encontrada

#si la palabra "banco" no se encuentra en el texto, mostrar un mensaje
if not banco_found:
    print("\nLa palabra 'banco' no se encuentra en el texto.")


#Ejemplo de salida: 
# Análisis de dependencias:
# Voy -> aux -> ir
# a -> mark -> ir
# ir -> ROOT -> ir
# al -> case -> banco
# banco -> obl -> ir
# a -> mark -> retirar
# retirar -> advcl -> ir
# dinero -> obj -> retirar
# . -> punct -> ir

# Ambigüedad resuelta para 'banco': banco (institución financiera)

# El ejemplo de salida nos demuestra cómo se realiza el análisis de dependencias sintácticas del texto,
# mostrando las relaciones gramaticales entre las palabras de la oración.
# Además, nos muestra cómo se puede resolver la ambigüedad léxica de la palabra "banco"
# utilizando el contexto proporcionado por la oración, en este caso, la presencia de la palabra "dinero".