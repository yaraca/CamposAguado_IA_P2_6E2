#Recuperación del Datos (IR)
#es el proceso de buscar información relevante en una gran colección de datos, especialmente documentos, en respuesta a una consulta del usuario.
#En procesamiento del lenguaje natural, este proceso se hace de forma probabilística o estadística.
#Uno de los modelos más conocidos es el modelo de espacio vectorial, pero los enfoques probabilísticos como el modelo de lenguaje o el modelo binario probabilístico usan:
#TF-IDF: Term Frequency - Inverse Document Frequency.
#Cálculo de probabilidades para determinar qué tan relevante es un documento.
#Aplicaciones: motores de búsqueda, sistemas de recomendación, etc.

#Ejemplo de recuperación de datos usando TF-IDF y similitud coseno

#librerías necesarias
import spacy #para procesamiento de lenguaje natural
from sklearn.feature_extraction.text import TfidfVectorizer #para vectorización TF-IDF
from sklearn.metrics.pairwise import cosine_similarity #para calcular similitud coseno

# Carga el modelo de spaCy para español
nlp = spacy.load("es_core_news_sm")

# Documentos a indexar
docs = [
    "el gato duerme en la cama",
    "el perro ladra en el jardín",
    "la gata juega con la pelota",
    "los gatos y los perros duermen juntos",
    "el perro y el gato comen juntos"
]

# Consulta
consulta = "gato duerme" # Consulta de ejemplo

# Función para preprocesar y lematizar texto (eliminar stopwords y puntuación)
def lematizar(texto): 
    doc = nlp(texto.lower())  # Procesa el texto en minúsculas
    lemas = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct] # Lematiza y filtra stopwords y puntuación
    return " ".join(lemas) # Devuelve el texto lematizado como una cadena

# Aplica lematización a los documentos y la consulta
docs_lemas = [lematizar(doc) for doc in docs] # Lematiza cada documento
consulta_lemas = lematizar(consulta) # Lematiza la consulta

# Vectorización TF-IDF
vectorizador = TfidfVectorizer() #crea el vectorizador
X = vectorizador.fit_transform(docs_lemas + [consulta_lemas]) #aplica el vectorizador a los documentos y la consulta

# Calcula la similitud coseno entre cada documento y la consulta
similitudes = cosine_similarity(X[:-1], X[-1:]).flatten()

# Ordena los documentos por similitud descendente
resultados = sorted(zip(docs, similitudes), key=lambda x: x[1], reverse=True) 

# Muestra los resultados
print("Documentos ordenados por relevancia para la consulta:\n")
for i, (doc, score) in enumerate(resultados): #se itera sobre los documentos y sus puntuaciones
    print(f"- Documento {i+1}: \"{doc}\" (Similitud: {score:.4f})") #imprime el documento y su puntuación de similitud

#ejemplo de salida:
# Documentos ordenados por relevancia para la consulta:

# - Documento 1: "el gato duerme en la cama" (Similitud: 0.7114)
# - Documento 2: "el perro y el gato comen juntos" (Similitud: 0.2198)
# - Documento 3: "los gatos y los perros duermen juntos" (Similitud: 0.2198)        
# - Documento 4: "el perro ladra en el jardín" (Similitud: 0.0000)
# - Documento 5: "la gata juega con la pelota" (Similitud: 0.0000)
#como se puede ver, el primer documento es el más relevante para la consulta "gato duerme", seguido por los otros documentos que contienen palabras relacionadas.
#Este enfoque se puede aplicar a grandes colecciones de documentos para recuperar información relevante de manera eficiente.
#El modelo TF-IDF y la similitud coseno son herramientas poderosas en la recuperación de información y se utilizan ampliamente en motores de búsqueda y sistemas de recomendación. 
#Además, la lematización y el preprocesamiento del texto son pasos importantes para mejorar la calidad de los resultados.

