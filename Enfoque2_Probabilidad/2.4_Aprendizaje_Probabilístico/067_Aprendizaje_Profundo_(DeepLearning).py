#Aprendizaje Profundo (Deep Learning)
#es una rama del Aprendizaje Automático (Machine Learning) que utiliza redes neuronales profundas.
#Una red neuronal profunda tiene varias capas ocultas entre la entrada y la salida.
#Estas capas permiten que el sistema aprenda representaciones complejas de los datos, especialmente cuando los datos son masivos, como imágenes, audio o texto.
#Funcionamiento: 
#Cada capa transforma los datos y los pasa a la siguiente.
#Introducen no linealidad  para aprender patrones complejos.
#Los datos fluyen desde la entrada hacia la salida, calculando una predicción.
#Mide qué tan mal está el modelo
#El error se propaga hacia atrás para ajustar los pesos de la red usando algoritmos de optimización como Descenso del Gradiente.
#El proceso se repite hasta que el modelo aprende a hacer buenas predicciones.
#Aplicaciones: reconocimiento de imagenes, traducción automática, procesamiento de lenguaje natural, juegos, etc.

#Ejemplo de Aprendizaje Profundo con Keras y TensorFlow
#keras es una API de alto nivel para construir y entrenar modelos de aprendizaje profundo.
#tensorflow es una biblioteca de código abierto para computación numérica y aprendizaje automático.
#clasificador de dígitos (0-9) usando la base de datos MNIST.
#MNIST es un conjunto de datos de imágenes de dígitos escritos a mano, comúnmente usado para entrenar modelos de aprendizaje automático.

# Importar las librerías necesarias
import tensorflow as tf #para computación numérica y aprendizaje automático
from keras import layers, models #para construir y entrenar modelos de aprendizaje profundo
import matplotlib.pyplot as plt #para graficar

#Cargar el conjunto de datos MNIST
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data() #Cargar el conjunto de datos MNIST (imágenes y etiquetas)
# x_train: imágenes de entrenamiento (60,000 imágenes de 28x28 píxeles)
# y_train: etiquetas de entrenamiento (0-9, dígitos correspondientes a las imágenes)
# x_test: imágenes de prueba (10,000 imágenes de 28x28 píxeles)
# y_test: etiquetas de prueba (0-9, dígitos correspondientes a las imágenes)

#Normalizar los datos (de 0-255 a 0-1)
x_train = x_train / 255.0 #Dividir entre 255 para normalizar los valores de píxeles (0-255) a un rango de 0-1
x_test = x_test / 255.0 #hacer lo mismo para los datos de prueba

#Definir el modelo
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  #Aplanar la imagen 28x28 en un vector de 784
    layers.Dense(128, activation='relu'),   #Capa oculta con 128 neuronas y función de activación ReLU(sirve para introducir no linealidad)
    layers.Dense(64, activation='relu'),    #Otra capa oculta
    layers.Dense(10, activation='softmax')  #Capa de salida con 10 neuronas (una por dígito)
])

#Compilar el modelo
model.compile(optimizer='adam', #Optimizador Adam (adaptativo y eficiente) para ajustar los pesos
              loss='sparse_categorical_crossentropy',  # Pérdida para clasificación multiclase
              metrics=['accuracy']) #Métrica de evaluación: precisión (accuracy) para medir el rendimiento del modelo

#Entrenar el modelo
history = model.fit(x_train, y_train, epochs=5, validation_split=0.2) #Entrenar el modelo con 5 épocas y 20% de los datos para validación
# epochs: número de veces que el modelo ve todo el conjunto de entrenamiento

#Evaluar el modelo
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)  #Evaluar el modelo con los datos de prueba (10,000 imágenes)
# test_loss: pérdida en los datos de prueba
# test_acc: precisión en los datos de prueba
# verbose=2: imprime el progreso de la evaluación

print('\nPrecisión en datos de prueba:', test_acc) #Imprimir la precisión en los datos de prueba

#Graficar precisión y pérdida
plt.plot(history.history['accuracy'], label='Precisión entrenamiento') #Graficar la precisión del entrenamiento
plt.plot(history.history['val_accuracy'], label='Precisión validación') #Graficar la precisión de la validación
plt.xlabel('Época')
plt.ylabel('Precisión')
plt.legend()
plt.show()

#ejemplo de salida:
#Precisión en datos de prueba: 0.9764999747276306
#La precisión en los datos de prueba es de aproximadamente 97.65%.
#La gráfica muestra cómo sube la precisión y baja la pérdida.
#El modelo aprende a clasificar dígitos escritos a mano con alta precisión.
#El aprendizaje profundo es útil para tareas complejas como reconocimiento de imágenes, procesamiento de lenguaje natural y más.

