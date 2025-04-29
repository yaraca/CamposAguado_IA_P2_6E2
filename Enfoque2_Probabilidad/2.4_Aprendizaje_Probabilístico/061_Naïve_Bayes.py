#Naïve Bayes
#es un clasificador probabilístico basado en el Teorema de Bayes que asume que las características son independientes entre sí dadas la clase.
#Aunque esta suposición de independencia rara vez es cierta en la práctica, Naïve Bayes funciona muy bien en la mayoría de los problemas reales.
#El teorema de bayes es: P(θ|D) = P(D|θ) * P(θ) / P(D)
#Donde: θ= parametro o hipotesis, D= datos observados
#P(θ)=Distribucion a priori (creencias iniciales sobre θ)
#P(D|θ)=Verosimilitud (probabilidad de observar D dado θ)
#P(θ|D)=Distribucion a posteriori (creencias actualizadas sobre θ)
#P(D)=Evidencia (constante de normalizacion)
#Lo que se tiene que calcular es qué tan probable es que un conjunto de observaciones D pertenezca a una clase θ
#Pero Naïve Bayes asume:  P(D|θ) = P(x1|θ) * P(x2|θ) * ... * P(xn|θ)
#Donde xi es condicionalmente independiente entre si dado la clase θ
#Esto significa que la probabilidad de observar un conjunto de características D dado una clase θ es el producto de las probabilidades individuales de cada característica dado la clase θ.
#Funcionamiento: 
#Entrenamiento: calcular las probabilidades a priori P(θ) y las probabilidades condicionales P(xi|θ) para cada característica xi.
#Predicción: dado un nuevo conjunto de características, calcular la probabilidad de cada clase usando el Teorema de Bayes y elegir la clase con la mayor probabilidad posterior P(θ|D).
#Aplicaciones: deteccion de spam, clasificacion de texto, analisis de sentimientos, sistemas de recomendacion, etc.

#Ejemplo de Naïve Bayes
#Clasificar correos como 'spam' o 'no spam' basado en dos palabras: 'oferta' y 'gratis'.

#librerías necesarias
import numpy as np

#Datos de entrenamiento: cada fila representa [oferta, gratis]
# 1 = palabra presente, 0 = palabra ausente
#Labels: 1 = spam, 0 = no spam
X_train = np.array([
    [1, 1],  #oferta y gratis (spam)
    [1, 0],  #oferta pero no gratis (spam)
    [0, 1],  #gratis pero no oferta (spam)
    [0, 0],  #ni oferta ni gratis (no spam)
    [1, 1],  #oferta y gratis (spam)
    [0, 0],  #ni oferta ni gratis (no spam)
])

y_train = np.array([1, 1, 1, 0, 1, 0])  #etiquetas: spam o no spam

#FUncion para Calcular las probabilidades P(θ) de cada clase
def calcular_prior(y): 
    clases, conteos = np.unique(y, return_counts=True) #conteos de cada clase
    total = int(len(y)) #total de ejemplos
    prior = {clase: conteo / total for clase, conteo in zip(clases, conteos)} #probabilidad a priori
    return prior #probabilidad de cada clase

#FUncion para Calcular las probabilidades P(x_i|θ) para cada característica
def calcular_likelihood(X, y):
    n_features = X.shape[1] #número de características
    clases = np.unique(y) #clases únicas
    likelihood = {} #diccionario para almacenar las probabilidades de cada clase
    
    for clase in clases: ##iterar sobre cada clase
        X_clase = X[y == clase] #filtrar ejemplos de la clase actual
        #Probabilidad de que cada característica sea 1 dado la clase
        likelihood_clase = (np.sum(X_clase, axis=0) + 1) / (X_clase.shape[0] + 2)  #Suavizado de Laplace (+1 para evitar 0s), +2 para evitar división por cero
        likelihood[clase] = likelihood_clase #almacenar la probabilidad de cada característica dado la clase
        
    return likelihood #probabilidades de cada característica dado la clase

#Función de predicción
def predecir(X, prior, likelihood):
    predicciones = [] #lista para almacenar las predicciones
    for x in X: #iterar sobre cada ejemplo de prueba
        probs = {} #diccionario para almacenar las probabilidades de cada clase
        for clase in prior.keys(): #iterar sobre cada clase
            prob = float(np.log(prior[clase]))  #trabajar en logaritmos para evitar underflow, osea, multiplicar probabilidades muy pequeñas
            for i in range(len(x)): #iterar sobre cada característica
                if x[i] == 1: #si la característica está presente
                    prob += np.log(likelihood[clase][i]) #sumar logaritmo de la probabilidad de la característica dado la clase
                else: #si la característica no está presente
                    prob += int(np.log(1 - likelihood[clase][i])) #sumar logaritmo de la probabilidad de que la característica no esté presente dado la clase
            probs[clase] = prob #almacenar la probabilidad total para la clase actual
        predicciones.append(max(probs, key=probs.get)) #elegir la clase con la mayor probabilidad
    return np.array(predicciones) #devolver las predicciones como un array numpy

#Entrenamiento
prior = calcular_prior(y_train) #calcular la probabilidad a priori de cada clase
likelihood = calcular_likelihood(X_train, y_train) #calcular la probabilidad de cada característica dado la clase

print("Prior probabilities:", prior) #imprimir la probabilidad a priori de cada clase
print("Likelihoods:", likelihood) #imprimir la probabilidad de cada característica dado la clase

#Prueba
X_test = np.array([ 
    [1, 1],  # oferta y gratis
    [0, 0],  # ni oferta ni gratis
    [1, 0],  # solo oferta
])

predicciones = predecir(X_test, prior, likelihood) #predecir la clase para cada ejemplo de prueba

print("Predicciones:", predicciones) #imprimir las predicciones

#Ejemplo de salida:
# Prior probabilities: {0: 0.3333333333333333, 1: 0.6666666666666666}
# Likelihoods: {0: array([0.25, 0.25]), 1: array([0.66666667, 0.66666667])}  
# Predicciones: [1 0 1]
#El primer ejemplo es spam (oferta y gratis), el segundo no es spam (ni oferta ni gratis) y el tercero es spam (solo oferta).
#El clasificador Naïve Bayes ha predicho correctamente las clases para los ejemplos de prueba.
#Podemos ver como el clasificador Naïve Bayes ha aprendido a clasificar los correos como spam o no spam basado en la presencia o ausencia de las palabras "oferta" y "gratis".