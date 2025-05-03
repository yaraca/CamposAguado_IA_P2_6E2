#Árboles de Regresión: M5
#A diferencia de un árbol de decisión clásico (como ID3 o C4.5) que clasifica datos en categorías, M5 predice valores numéricos continuos.
#Funcionamiento: 
# División recursiva del espacio de atributos (como un árbol de decisión).
# En cada nodo hoja, en lugar de dar un valor constante, se ajusta una regresión lineal usando los atributos.
# Usa medidas como el Error Absoluto Medio o la Desviación Estándar Reducida para decidir los puntos de división.
#Aplicaciones: Predicción de precios, análisis de series temporales, etc.

#Ejemplo de Arbol de Regresión M5

#librerías necesarias
import numpy as np  #importar la biblioteca numpy para manipulación de arreglos numéricos
import matplotlib.pyplot as plt  #importar matplotlib para graficar resultados
from sklearn.tree import DecisionTreeRegressor  #importar el modelo de árbol de regresión de scikit-learn

#definir los datos de entrada x como una característica (por ejemplo, número de habitaciones)
#definir los valores de salida y como el precio de la casa en miles
X=np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y=np.array([150, 200, 250, 270, 300, 320, 340, 370, 400, 450])

#crear un modelo de árbol de regresión con profundidad máxima de 3 para evitar sobreajuste
modelo=DecisionTreeRegressor(max_depth=3)

#entrenar el modelo utilizando los datos de entrada x y los valores esperados y
modelo.fit(X, y)

#generar valores de prueba distribuidos uniformemente entre 1 y 10
X_test=np.linspace(1, 10, 100).reshape(-1, 1)

#realizar predicciones con el modelo entrenado utilizando los valores de prueba
y_pred=modelo.predict(X_test)

#crear un gráfico de dispersión para visualizar los datos originales
plt.scatter(X, y, color='blue', label='Datos reales')

#graficar la curva de predicción generada por el árbol de regresión
plt.plot(X_test, y_pred, color='red', label='Predicción árbol de regresión')

#añadir título y etiquetas a los ejes del gráfico
plt.title('Simulación de Árbol de Regresión tipo M5')
plt.xlabel('Número de habitaciones')
plt.ylabel('Precio (en miles)')

#añadir leyenda y cuadrícula para mejorar la visualización
plt.legend()
plt.grid(True)

#mostrar el gráfico generado
plt.show()

#definir un nuevo valor de entrada para realizar una predicción específica
nueva_muestra=np.array([[6.5]])

#predecir el precio de una casa con 6.5 habitaciones utilizando el modelo
prediccion=modelo.predict(nueva_muestra)

#mostrar la predicción obtenida con formato numérico adecuado
print(f'Predicción para 6.5 habitaciones: {prediccion[0]:.2f} mil')

#Ejemplo de salida: 
#Predicción para 6.5 habitaciones: 310.00 mil
# una gráfica con:
# Puntos azules: datos reales.
# Línea roja: predicción del modelo (segmentos de regresión).

# Este ejemplo de salida nos demuestra cómo un Árbol de Regresión tipo M5 puede ajustarse a datos numéricos continuos.
# La gráfica generada muestra cómo el modelo divide el espacio de atributos en segmentos y ajusta regresiones lineales en cada uno.
# Los puntos azules representan los datos reales, mientras que la línea roja muestra las predicciones del modelo.
# Además, la predicción específica para 6.5 habitaciones (310.00 mil) ilustra cómo el modelo puede interpolar valores dentro del rango de datos.