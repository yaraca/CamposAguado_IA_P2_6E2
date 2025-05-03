#Gramática Causal Definida
#es un tipo de modelo lingüístico que se usa para describir relaciones causales en el lenguaje.
#Este tipo de gramática puede ser utilizada para representar cómo una acción o evento causa otro evento, describiendo relaciones de causa y efecto de manera formal y lógica.
#Características:
# Identificación de causa y efecto: Se identifican las partes de la frase que expresan causa y efecto.
# Formalización: Utiliza una formalización matemática para entender y predecir las relaciones causales.
# Dependencias temporales: Las acciones en un proceso causal suelen tener una relación temporal, que puede ser importante para el análisis.
#Aplicaciones: redacción de textos, análisis de datos, sistemas de recomendación, etc.

#Ejemplo de gramática causal definida 
#acciones causales en una frase usando dependencias sintácticas.

#librerías necesarias
import spacy  #importar la biblioteca spacy para procesamiento del lenguaje natural

#cargar el modelo preentrenado de spacy para el idioma español
nlp=spacy.load('es_core_news_md')

#definir un texto de ejemplo para analizar relaciones causales
texto="La lluvia causó inundaciones en varias ciudades."

#procesar el texto con el modelo de spacy
doc=nlp(texto)

#mostrar el análisis de dependencias sintácticas entre palabras
print("Análisis de dependencias:")
for token in doc:
    print(f'{token.text} -> {token.dep_} -> {token.head.text}')  #mostrar la relación de dependencia

#inicializar variables para identificar posibles relaciones causales
causa=None
efecto=None

#recorrer cada token en el documento para detectar relaciones causales
for token in doc:
    #identificar la causa: el sujeto (nsubj) del verbo "causar"
    if token.dep_=="nsubj" and token.head.lemma_=="causar":
        causa=token.text
    #identificar el efecto: el objeto directo (obj) del verbo "causar"
    if token.dep_=="obj" and token.head.lemma_=="causar":
        efecto=token.text

#mostrar las relaciones causales encontradas si se detectaron
if causa and efecto:
    print(f"\nRelación causal detectada:")
    print(f"Causa: {causa}")
    print(f"Efecto: {efecto}")
else:
    print("\nNo se detectó una relación causal.")


#Ejemplo de salida: 
# Análisis de dependencias:
# La -> det -> lluvia
# lluvia -> nsubj -> causó
# causó -> ROOT -> causó
# inundaciones -> obj -> causó
# en -> case -> ciudades
# varias -> det -> ciudades
# ciudades -> obl -> causó
# . -> punct -> causó

# Relación causal detectada:
# Causa: lluvia
# Efecto: inundaciones

# El ejemplo de salida nos demuestra cómo se realiza el análisis de dependencias sintácticas
# para identificar las relaciones entre las palabras de una oración. En este caso, se observa
# cómo se detecta el sujeto (nsubj) y el objeto directo (obj) del verbo "causar", lo que permite
# identificar la relación causal entre "lluvia" (causa) e "inundaciones" (efecto).
