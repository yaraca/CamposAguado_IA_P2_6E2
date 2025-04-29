#Máquinas de Vectores de Soporte (Núcleo)-> SVM (Support Vector Machines)	
#Es un algoritmo de clasificación supervisada que encuentra la mejor frontera para separar dos clases de datos
#maximizando el margen entre los datos de diferentes clases.
#Su objetivo es encontrar un límite que divida los datos con el mayor margen posible.
#Soportes: Los puntos de datos más cercanos al hiperplano se llaman vectores de soporte.
#si los datos NO son linealmente separables, se usa un Núcleo (Kernel).
#El Kernel transforma los datos a un espacio de mayor dimensión donde sí son separables. Así, se pueden separar datos no lineales.
#Tipos de nucleos comunes: lineal, polinómico(relaciones polinomicas), RBF (Radial Basis Function) (datos complicados y no lineales), sigmoide(inspirado en redes neuronales).
#Aplicaciones: reconocimiento de patrones, clasificación de texto, detección de fraudes, etc.

#Ejemplo de SVM con Kernel RBF

 #librerías necesarias
import numpy as np #para operaciones matemáticas y matrices
import matplotlib.pyplot as plt #para graficar
from sklearn import datasets #para generar datos de ejemplo
from sklearn.svm import SVC #para SVM (Support Vector Classifier)

#generar un conjunto de datos NO linealmente separables
X, y = datasets.make_moons(n_samples=100, noise=0.1, random_state=42) #100 muestras, ruido 0.1, semilla 42

#crear un clasificador SVM con un núcleo RBF (Radial Basis Function)
clf = SVC(kernel='rbf', C=1.0) #C=1.0 es el parámetro de regularización (controla el margen y la complejidad del modelo)

#Entrenar el modelo con los datos
clf.fit(X, y)

#Crear una malla para visualizar mejor la frontera de decisión
xx, yy = np.meshgrid(np.linspace(X[:,0].min()-0.5, X[:,0].max()+0.5, 500),  # Crear una malla de puntos
                     np.linspace(X[:,1].min()-0.5, X[:,1].max()+0.5, 500))  #.min() y .max() para obtener los límites de la malla

#Predecir la clase para cada punto de la malla
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]) #np.c_ combina las coordenadas x e y de la malla en un solo array
Z = Z.reshape(xx.shape) #Reformatear Z para que tenga la misma forma que la malla

#Graficar
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8) # Frontera coloreada
plt.scatter(X[:,0], X[:,1], c=y, cmap=plt.cm.coolwarm, edgecolors='k') # Puntos originales
plt.title("SVM con Núcleo RBF")
plt.xlabel("X1")
plt.ylabel("X2")
plt.show()

#ejemplo de salida:
#Una grafica con dos medias lunas (una de cada clase).
#El espacio estará dividido por una frontera curva creada por el núcleo RBF.
#Cada lado estará coloreado diferente.
#Así el SVM logra separar dos clases no lineales correctamente.
#El modelo SVM con núcleo RBF es útil para datos no lineales, como imágenes, texto o datos biológicos.
