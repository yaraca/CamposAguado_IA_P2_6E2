#K-NN, k-Medias y Clustering
#k-NN (k-Nearest Neighbors)
#Es un algoritmo de clasificación supervisada. Clasifica un punto desconocido basándose en sus "k" vecinos más cercanos en el conjunto de entrenamiento.
#Se calcula la distancia entre el nuevo punto y todos los puntos de entrenamiento.
#Se eligen los "k" vecinos más cercanos.
#Se vota la clase más frecuente entre esos vecinos.
#Aplicaciones: reconocimiento de patrones, clasificación de imágenes, detección de fraudes, etc.
#k-Means (k-Medias)
#Es un algoritmo de agrupamiento no supervisado. Agrupa los datos en "k" clusters basándose en la similitud.
#Se inicializan "k" centros de cluster (aleatoriamente).
#Cada punto se asigna al centro más cercano.
#Se recalculan los centros como la media de los puntos asignados.
#Se repite hasta que no cambien los centros.
#Aplicaciones: segmentación de clientes, análisis de imágenes, compresión de datos, etc.
#Clustering (Agrupamiento)
#Es una técnica donde el objetivo es agrupar datos similares sin etiquetas.
#k-Means es solo un tipo de clustering.

#Ejemplo de k-NN y k-Means

#librerías necesarias
import numpy as np #para operaciones matemáticas y matrices
import matplotlib.pyplot as plt #para graficar
from sklearn.datasets import make_blobs #para generar datos de ejemplo
from sklearn.neighbors import KNeighborsClassifier #para k-NN
from sklearn.cluster import KMeans # para k-Means

#Crear datos de ejemplo
#usar make_blobs para generar 2 clusters (con etiquetas)
X, y = make_blobs(n_samples=300, centers=2, random_state=42, cluster_std=1.5) #300 muestras, 2 centros, semilla 42, desviación estándar 1.5

#graficar los datos
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm') #graficar los puntos con colores según su etiqueta
plt.title('Datos generados') 
plt.show()


#k-NN (Clasificación)

#crear el modelo k-NN
k = 3 #número de vecinos más cercanos
modelo_knn = KNeighborsClassifier(n_neighbors=k) #k=3 vecinos más cercanos

#entrenar el modelo con los datos generados
modelo_knn.fit(X, y) #ajustar el modelo a los datos

#crear un nuevo punto no etiquetado
nuevo_punto = np.array([[0, 5]]) #nuevo punto a clasificar (coordenadas x=0, y=5)

#predecir su clase usando k-NN
prediccion = modelo_knn.predict(nuevo_punto) #predecir la clase del nuevo punto

#Mostramos el resultado
print(f"El nuevo punto {nuevo_punto} pertenece a la clase: {prediccion[0]}") #imprimir la clase predicha

#graficar el nuevo punto junto con los datos
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm') #graficar los puntos con colores según su etiqueta
plt.scatter(nuevo_punto[:, 0], nuevo_punto[:, 1], c='black', marker='x', s=100) #coordenadas del nuevo punto
plt.title('Clasificación k-NN')
plt.show()


#k-Means (Clustering)

#crear el modelo k-Means
modelo_kmeans = KMeans(n_clusters=2, random_state=42, n_init=10) #n_clusters=2 (dos grupos), random_state=42 (semilla para reproducibilidad), n_init=10 (inicializaciones aleatorias)

#entrenar el modelo (sin usar etiquetas reales)
modelo_kmeans.fit(X) #ajustar el modelo a los datos

#obtener las etiquetas predichas por k-Means
etiquetas_kmeans = modelo_kmeans.labels_ #etiquetas asignadas a cada punto por k-Means

#graficar los clusters encontrados
plt.scatter(X[:, 0], X[:, 1], c=etiquetas_kmeans, cmap='coolwarm') #graficar los puntos con colores según su etiqueta
plt.scatter(modelo_kmeans.cluster_centers_[:, 0], modelo_kmeans.cluster_centers_[:, 1],  
            c='yellow', marker='*', s=200, label='Centros') #coordenadas de los centros de los clusters
plt.title('Clusters encontrados por k-Means')
plt.legend()
plt.show()

#Ejemplo de salida:
#El nuevo punto [[0 5]] pertenece a la clase: 0
#El nuevo punto ha sido clasificado como perteneciente a la clase 0 por el modelo k-NN.
#Los clusters encontrados por k-Means son visualizados en la gráfica, donde los puntos están coloreados según su etiqueta asignada por el algoritmo.
#Primera grafica: Los puntos estarán coloreados según su etiqueta verdadera (azul y rojo). Sin el nuevo punto todavía.
#Segundo grafico: Incluye el nuevo punto ([[0,5]]) marcado con una cruz negra x. se ubica en alguna de las zonas coloreadas.
#Tercer grafico: Los datos agrupados en dos colores (según cluster detectado). Dos centros de cluster marcados con estrellas amarillas *.
