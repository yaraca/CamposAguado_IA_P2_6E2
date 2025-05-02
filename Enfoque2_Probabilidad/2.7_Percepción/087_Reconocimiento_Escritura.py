#Reconocimiento d#es el proceso mediante el cual una computadora identifica texto escrito a mano, ya sea:
# Online: capturado mientras se escribe (por ejemplo, en tabletas gráficas).
# Offline: detectado desde una imagen escaneada o fotografía.
#Funcionamiento: 
# Preprocesamiento: convertir la imagen a escala de grises, binarizar, eliminar ruido.
# Segmentación: separar palabras o caracteres.
# Extracción de características: extraer propiedades relevantes (por ejemplo, forma, contorno).
# Clasificación: usar modelos probabilísticos o de aprendizaje automático (como KNN, SVM, redes neuronales).
#Aplicaciones: lectura automática de formularios, reconocimiento de firmas, conversión de texto manuscrito a digital.

#Ejemplo de reconocimiento de escritura
#usar el conjunto de datos MNIST (70,000 imágenes de dígitos escritos a mano).

#librerías necesarias
from sklearn.datasets import load_digits #para cargar el conjunto de datos de dígitos escritos a mano
from sklearn.model_selection import train_test_split #para dividir el conjunto de datos en entrenamiento y prueba
from sklearn.linear_model import LogisticRegression #para crear un modelo de regresión logística
from sklearn.metrics import classification_report, accuracy_score #para evaluar el rendimiento del modelo
import matplotlib.pyplot as plt #para visualizar los dígitos

#Cargar el conjunto de datos de dígitos escritos a mano (8x8 píxeles)
digits = load_digits()

#Visualizar algunos dígitos
plt.figure(figsize=(8, 4)) #crear una figura de 8x4 pulgadas
for i in range(8): #mostrar 8 dígitos
    plt.subplot(2, 4, i+1) #crear una subgráfica
    plt.imshow(digits.images[i], cmap='gray') #mostrar la imagen en escala de grises
    plt.title(f'Dígito: {digits.target[i]}') 
    plt.axis('off')
plt.tight_layout() #ajustar el espaciado entre subgráficas
plt.show()

#Separar datos de entrada (imágenes) y etiquetas (números reales)
X = digits.data         # Imagen 8x8 convertida en un vector de 64 valores
y = digits.target       # Número al que corresponde cada imagen

#Dividir en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) #usar una semilla para reproducibilidad

#Crear un modelo de regresión logística (clasificador)
modelo = LogisticRegression(max_iter=2000) #aumentar el número de iteraciones para asegurar la convergencia

#Entrenar el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train) #ajustar el modelo a los datos

#Realizar predicciones sobre el conjunto de prueba
y_pred = modelo.predict(X_test) #predecir las etiquetas para los datos de prueba

#Medir precisión y mostrar informe de clasificación
print("Exactitud del modelo:", accuracy_score(y_test, y_pred)) #calcular la precisión del modelo
print("\nReporte de clasificación:\n") #mostrar un informe detallado de la clasificación
print(classification_report(y_test, y_pred)) #calcular métricas como precisión, recall y F1-score

#Ejemplo de salida:
# Exactitud del modelo: 0.975

# Reporte de clasificación:

#               precision    recall  f1-score   support

#            0       1.00      1.00      1.00        33
#            1       0.97      1.00      0.98        28
#            2       1.00      1.00      1.00        33
#            3       0.97      0.97      0.97        34
#            4       1.00      0.98      0.99        46
#            5       0.92      0.96      0.94        47
#            6       0.97      0.97      0.97        35
#            7       1.00      0.97      0.99        34
#            8       0.97      0.97      0.97        30
#            9       0.97      0.95      0.96        40

#     accuracy                           0.97       360
#    macro avg       0.98      0.98      0.98       360
# weighted avg       0.98      0.97      0.98       360
#Como se puede observar, el modelo tiene una alta precisión (97.5%) y un buen rendimiento en todas las clases.
#Esto indica que el modelo es capaz de reconocer dígitos escritos a mano con alta precisión.
#Y como se puede observar el modelo sí es capaz de reconocer dígitos escritos con alta precisión.
