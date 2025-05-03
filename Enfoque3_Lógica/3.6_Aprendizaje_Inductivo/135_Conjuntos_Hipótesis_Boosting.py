#COnjunto de hipotesis de Boosting
#es una técnica de aprendizaje conjunto (ensemble) que combina varios modelos débiles (por ejemplo, árboles pequeños o “stumps”) para crear un modelo fuerte.
#Funcionamiento: 
# Entrena varios modelos débiles de forma secuencial.
# Cada modelo se entrena prestando más atención a los errores cometidos por los modelos anteriores.
# Asigna un peso a cada modelo según su desempeño.
# La predicción final es una combinación ponderada de todos los modelos.
#Aplicaciones: Clasificación, regresión, detección de fraudes, análisis de sentimientos, etc.

#Ejemplo de Boosting con AdaBoost 

#librerias necesarias
from sklearn.ensemble import AdaBoostClassifier  #importar el clasificador AdaBoost para mejorar modelos débiles
from sklearn.tree import DecisionTreeClassifier  #importar árbol de decisión como modelo base
from sklearn.datasets import make_classification  #importar función para generar datos de clasificación
from sklearn.model_selection import train_test_split  #importar función para dividir datos en entrenamiento y prueba
from sklearn.metrics import accuracy_score  #importar métrica para evaluar la precisión del modelo

#generar un conjunto de datos de ejemplo para clasificación binaria con 100 muestras y 4 características
X, y=make_classification(n_samples=100, n_features=4, n_informative=2, 
                         n_redundant=0, random_state=42)

#dividir los datos en un conjunto de entrenamiento (70%) y otro de prueba (30%)
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.3, random_state=42)

#crear un modelo base débil usando un árbol de decisión con profundidad máxima de 1 (stump)
modelo_base=DecisionTreeClassifier(max_depth=1)

#crear el modelo adaboost usando el árbol de decisión como estimador base con 50 iteraciones
modelo_boosting=AdaBoostClassifier(estimator=modelo_base, n_estimators=50, random_state=42)

#entrenar el modelo adaboost usando el conjunto de entrenamiento
modelo_boosting.fit(X_train, y_train)

#realizar predicciones sobre el conjunto de prueba
y_pred=modelo_boosting.predict(X_test)

#evaluar la precisión del modelo comparando predicciones con los valores reales
precision=accuracy_score(y_test, y_pred)

#imprimir la precisión obtenida en porcentaje
print(f"Precisión del modelo AdaBoost: {precision * 100:.2f}%")

#Ejemplo de salida: 
#Precisión del modelo AdaBoost: 96.67%
# El ejemplo de salida nos demuestra que el modelo AdaBoost es capaz de combinar múltiples modelos débiles
# (en este caso, árboles de decisión con profundidad máxima de 1) para lograr un modelo fuerte con alta precisión.
# En este caso, la precisión obtenida (por ejemplo, 96.67%) indica que el modelo es efectivo para clasificar
# correctamente los datos de prueba en la mayoría de los casos.