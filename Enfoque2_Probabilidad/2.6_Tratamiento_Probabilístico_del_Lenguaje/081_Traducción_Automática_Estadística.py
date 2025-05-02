#Traducción automatizada estadística (SMT)
#Es un enfoque de traducción automática que utiliza modelos estadísticos aprendidos a partir de grandes corpus de texto bilingüe
#En lugar de reglas lingüísticas, SMT se basa en la probabilidad de que una secuencia de palabras en un idioma (idioma fuente) se traduzca a otra secuencia en otro idioma (idioma destino).
#Formula: P(f|e) = P(e|f) * P(f) / P(e)
#donde P(f|e) es la probabilidad de la secuencia de palabras en el idioma destino (f) dado el idioma fuente (e).
#P(e|f) es la probabilidad de la secuencia de palabras en el idioma fuente dado el idioma destino.
#Funcionamiento:
#Entrenamiento: Se usa un corpus paralelo (por ejemplo, oraciones alineadas en inglés-español).
#               Se extraen frases, palabras y sus alineaciones.
#               Se estiman probabilidades usando frecuencias.
#Traducción: Para traducir una nueva oración, se busca la mejor secuencia de palabras en el idioma destino que maximice la probabilidad de la secuencia en el idioma fuente.
#Decodificador: Compara muchas combinaciones posibles y selecciona la mejor según el modelo estadístico.
#Aplicaciones: traductores automáticos, sistemas de subtitulado, etc.

#Ejemplo de traduccion automatizada estadistica
#Usar un pequeño corpus bilingüe y una versión muy simplificada del proceso SMT.

#librerías necesarias
import random # Para la aleatoriedad
from collections import defaultdict # Para contar ocurrencias y probabilidades

# Corpus bilingüe de ejemplo
corpus = [
    ("el gato", "the cat"), #palabra en español, palabra en inglés
    ("el perro", "the dog"),
    ("la casa", "the house"),
    ("la gata", "the female cat"),
    ("un perro grande", "a big dog"),
    ("una casa bonita", "a nice house"),
    ("brinca", "jump")
]

#Construcción de tabla de traducción palabra a palabra
translation_prob = defaultdict(lambda: defaultdict(float))

#Contar ocurrencias
count_ef = defaultdict(lambda: defaultdict(int)) # count_ef[e][f] = número de veces que la palabra f se traduce como e
count_e = defaultdict(int) # count_e[e] = número de veces que aparece la palabra e

for esp, eng in corpus: # Para cada par de palabras en el corpus
    esp_words = esp.split() #dividir la frase en palabras
    eng_words = eng.split() #dividir la frase en palabras
    for e in eng_words: # Para cada palabra en inglés
        count_e[e] += 1 #contar la palabra en inglés
        for f in esp_words: #para cada palabra en español
            count_ef[e][f] += 1 #contar la palabra en español

#Calcular probabilidades: P(f|e)
for e in count_ef: # Para cada palabra en inglés
    total = sum(count_ef[e].values()) #total de palabras en español que se traducen a e
    for f in count_ef[e]: #para cada palabra en español
        translation_prob[e][f] = count_ef[e][f] / total #probabilidad de que f se traduzca como e

#función de raducción de una nueva oración
def translate(sentence_esp): 
    words = sentence_esp.split() #dividir la frase en palabras
    result = [] #lista para guardar la traducción
    for f in words: # Para cada palabra en español
        best_translation = None #mejor traducción
        best_prob = 0.0 #probabilidad de la mejor traducción
        for e in translation_prob: # Para cada palabra en inglés
            prob = translation_prob[e].get(f, 0) #obtener la probabilidad de que f se traduzca como e
            if prob > best_prob: #si la probabilidad es mayor que la mejor probabilidad
                best_translation = e #guardar la mejor traducción
                best_prob = prob #guardar la mejor probabilidad
        if best_translation: #si hay una mejor traducción
            result.append(best_translation) #agregar la mejor traducción a la lista
        else: #si no hay mejor traducción
            result.append(f"[{f}]")  # palabra no encontrada
    return " ".join(result) #unir la lista en una cadena

# Ejemplo
frase = "el perro brinca" 
traduccion = translate(frase) #traducir la frase
print(f"Traducción de '{frase}': {traduccion}") 

#ejemplo de salida:
#Traducción de 'el perro brinca': the dog jump
#como se puede ver se traduce la oración "el perro brinca" a "the dog jump"
