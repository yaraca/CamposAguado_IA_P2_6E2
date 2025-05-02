#Extracción de Información (IE)
#es el proceso de identificar y extraer automáticamente datos estructurados (como nombres, fechas, lugares, relaciones, etc.) 
# a partir de textos no estructurados, como noticias, correos, artículos o redes sociales.
#Componentes principales:
#Reconocimiento de entidades nombradas (NER):Detecta entidades como personas, organizaciones, lugares, fechas, etc.
#Extracción de relaciones: Determina cómo están conectadas las entidades (por ejemplo, "Barack Obama nació en Hawái").
#Normalización y desambiguación:  Relaciona entidades con bases de datos existentes o corrige ambigüedades.
#Funcionamiento: 
#Usa técnicas de procesamiento del lenguaje natural (NLP).
#Combina modelos estadísticos, reglas lingüísticas y aprendizaje automático (ML).
#Puede utilizar modelos probabilísticos para predecir qué secuencia de palabras representa una entidad o una relación
#Aplicaciones: motores de búsqueda, análisis de sentimientos, chatbots, sistemas de recomendación, etc.

#Ejemplo de Extracción de Información con spaCy 

#librerias necesarias
import spacy #para procesamiento de lenguaje natural

#cargar el modelo de lenguaje en español de spaCy
nlp = spacy.load("es_core_news_md")

# Texto de ejemplo
texto = "Pedro Sánchez nació en Madrid y trabaja para el gobierno de España desde 2018."

# Procesamos el texto con spaCy
doc = nlp(texto)

#imrpimir las entidades encontradas
print("Entidades encontradas en el texto:\n")
for ent in doc.ents: ##iterar sobre las entidades encontradas
    print(f"- {ent.text} ({ent.label_})") #imprimir el texto y la etiqueta de la entidad

#ejemplo de salida:
# Entidades encontradas en el texto:

# - Pedro Sánchez (PER)
# - Madrid (LOC)
# - España (LOC)
#Como se puede ver, el modelo ha identificado "Pedro Sánchez" como una persona (PER), "Madrid" y "España" como ubicaciones (LOC)
# y ha extraído la información relevante del texto.
#Este es un ejemplo básico, pero la extracción de información puede ser mucho más compleja, incluyendo relaciones entre entidades y normalización.

