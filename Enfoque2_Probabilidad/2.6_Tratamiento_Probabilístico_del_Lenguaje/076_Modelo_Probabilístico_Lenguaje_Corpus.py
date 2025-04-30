#Modelos probabilistico de lenguaje Corpus
# Un modelo probabilístico del lenguaje tiene como objetivo asignar una probabilidad a una secuencia de palabras
#Esto permite a los sistemas de lenguaje natural:
#Predecir la siguiente palabra. Detectar errores gramaticales. Generar texto automáticamente. Traducir texto o transcribir voz.
#Un corpus es una gran colección de texto utilizada como base de entrenamiento para los modelos probabilísticos. A partir de él, se calculan frecuencias y probabilidades.
#Modelos probabilisticos: 
#Modelo unigram (1-gram): Asume que cada palabra es independiente.
#Modelo bigram (2-gram): Cada palabra depende solo de la anterior.
#Modelo trigram (3-gram): Cada palabra depende de las dos anteriores.
#aplicaciones: correccion gramatical, autocompletado de texto, traduccion automatica, etc.

#ejemplo de modelo probabilístico del lenguaje
#Modelo Unigrama y Bigrama usando un corpus básico

#librerias necesarias
import re #libreria para expresiones regulares
from collections import defaultdict, Counter #libreria para contar elementos y crear diccionarios por defecto

#ejemplo de corpus (texto en español)
corpus = """
el gato duerme en la cama
el perro duerme en el sofá
la gata juega con el gato
el gato y la gata duermen juntos
"""

#Preprocesamiento del texto
#funcion para preprocesar el texto: convertir a minúsculas y eliminar caracteres no deseados
def preprocesar(texto): 
    texto = texto.lower() #convertir a minúsculas
    texto = re.sub(r'[^a-záéíóúñü\s]', '', texto)  #Solo letras y espacios
    return texto.split() #dividir el texto en palabras (tokens)

tokens = preprocesar(corpus) #tokenización: dividir el texto en palabras
print("Tokens del corpus:", tokens) #imprimir los tokens del corpus


#Modelo Unigrama
unigramas = Counter(tokens) #contar la frecuencia de cada palabra (unigrama)
total_palabras = sum(unigramas.values()) #total de palabras en el corpus

print("\nProbabilidades Unigrama:") 
for palabra in unigramas: #iterar por cada palabra
    prob = unigramas[palabra] / total_palabras #calcular la probabilidad de cada palabra
    print(f"P({palabra}) = {prob:.4f}") #imprimir la probabilidad de cada palabra

#Modelo Bigramas
bigramas = defaultdict(int) #crear un diccionario por defecto para contar bigramas (pares de palabras)
for i in range(len(tokens) - 1): #iterar por cada token (excepto el último)
    bigrama = (tokens[i], tokens[i+1]) #crear un bigrama (par de palabras)
    bigramas[bigrama] += 1 #contar la frecuencia de cada bigrama

#frecuencia de palabra anterior (para condicional)
freq_anterior = Counter(tokens[:-1]) #contar la frecuencia de cada palabra anterior (excepto la última)

print("\nProbabilidades Bigramas:")
for (w1, w2), freq in bigramas.items(): #iterar por cada bigrama
    prob = freq / freq_anterior[w1] #calcular la probabilidad condicional P(w2 | w1)
    print(f"P({w2} | {w1}) = {prob:.4f}") #imprimir la probabilidad condicional de cada bigrama

#ejemplo de salida:
# Tokens del corpus: ['el', 'gato', 'duerme', 'en', 'la', 'cama', 'el', 'perro', 'duerme', 'en', 'el', 'sofá', 'la', 'gata', 'juega', 'con', 'el', 'gato', 'el', 'gato', 'y', 'la', 'gata', 'duermen', 'juntos']

# Probabilidades Unigrama:
# P(el) = 0.2000
# P(gato) = 0.1200
# P(duerme) = 0.0800
# P(en) = 0.0800
# P(la) = 0.1200
# P(cama) = 0.0400
# P(perro) = 0.0400
# P(sofá) = 0.0400
# P(gata) = 0.0800
# P(juega) = 0.0400
# P(con) = 0.0400
# P(y) = 0.0400
# P(duermen) = 0.0400
# P(juntos) = 0.0400
#como se puede observar, la palabra "el" es la más frecuente en el corpus, seguida de "gato" y "la".
#El modelo unigramas asigna una probabilidad a cada palabra de forma independiente, sin considerar el contexto de las palabras adyacentes.


# Probabilidades Bigramas:
# P(gato | el) = 0.6000
# P(duerme | gato) = 0.3333
# P(en | duerme) = 1.0000
# P(la | en) = 0.5000
# P(cama | la) = 0.3333
# P(el | cama) = 1.0000
# P(perro | el) = 0.2000
# P(duerme | perro) = 1.0000
# P(el | en) = 0.5000
# P(sofá | el) = 0.2000
# P(la | sofá) = 1.0000
# P(gata | la) = 0.6667
# P(juega | gata) = 0.5000
# P(con | juega) = 1.0000
# P(el | con) = 1.0000
# P(el | gato) = 0.3333
# P(y | gato) = 0.3333
# P(la | y) = 1.0000
# P(duermen | gata) = 0.5000
# P(juntos | duermen) = 1.0000
#como se puede observar, el modelo bigramas asigna una probabilidad a cada palabra considerando la palabra anterior.
#Esto permite capturar relaciones contextuales entre palabras, como la relación entre "el" y "gato", o "duerme" y "en".
#El modelo bigramas es más efectivo que el modelo unigramas para capturar la estructura del lenguaje, ya que considera el contexto de las palabras adyacentes.
#Sin embargo, el modelo bigramas aún tiene limitaciones, ya que solo considera la palabra anterior y no captura relaciones más complejas entre palabras.

