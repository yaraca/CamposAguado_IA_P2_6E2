#Perceptron, ADALINE y MADALINE
#Son modelos de redes neuronales artificiales muy básicos e históricos, fueron los primeros modelos que se usaron para aprender de los datos
#Perceptron: Neurona sencilla.
#            Clasificador lineal que usa una función escalón para la salida.
#ADELINE: Neurona con aprendizaje adaptativo. 
#         Similar al Perceptrón, pero en vez de usar el escalón para actualizar pesos, usa una función lineal y minimiza el error cuadrático.
#MADALINE: Red neuronal con múltiples capas.
#          Red neuronal de varias capas de ADALINEs, entrenada con un algoritmo llamado MADALINE Rule.


#Perceptron 
import numpy as np

#Clase del Perceptrón
class Perceptron:
    #función de inicialización
    def __init__(self, tasa_aprendizaje=0.1, iteraciones=1000): #inicializa la tasa de aprendizaje y el número de iteraciones
        self.tasa_aprendizaje = tasa_aprendizaje #tasa de aprendizaje
        self.iteraciones = iteraciones #número de iteraciones
        self.pesos = None #inicializa los pesos como None
        self.sesgo = None #inicializa el sesgo como None

    #función de activación escalón (step function)
    def activar(self, x):
        return 1 if x >= 0 else 0 #devuelve 1 si x es mayor o igual que 0, 0 en caso contrario

    #función de entrenamiento
    def entrenar(self, X, y):
        # Inicializa pesos y sesgo en 0
        n_caracteristicas = X.shape[1] #número de características (columnas) en X
        self.pesos = np.zeros(n_caracteristicas) #inicializa los pesos a cero
        self.sesgo = 0 #inicializa el sesgo a cero

        #entrenamiento iterativo
        for _ in range(self.iteraciones): #itera el número de veces especificado
            for xi, salida_real in zip(X, y): #itera sobre cada entrada y su salida real
                salida_predicha = self.activar(np.dot(xi, self.pesos) + self.sesgo) #predicción de la salida
                error = salida_real - salida_predicha #calcula el error (diferencia entre la salida real y la predicha)
                #actualización de pesos y sesgo
                self.pesos += self.tasa_aprendizaje * error * xi #actualiza los pesos multiplicando la tasa de aprendizaje, el error y la entrada
                self.sesgo += self.tasa_aprendizaje * error #actualiza el sesgo multiplicando la tasa de aprendizaje y el error
    
    #función de predicción
    def predecir(self, X):
        # Predicción para un conjunto de datos
        return [self.activar(np.dot(xi, self.pesos) + self.sesgo) for xi in X] #devuelve una lista de predicciones para cada entrada en X

#prueba con compuerta lógica AND
if __name__ == "__main__": 
    #entradas (x1, x2) y salidas correspondientes
    X = np.array([[0,0], [0,1], [1,0], [1,1]]) #entradas de la compuerta AND
    y = np.array([0, 0, 0, 1])  #salida de una compuerta AND

    perceptron = Perceptron(tasa_aprendizaje=0.1, iteraciones=10) #inicializa el perceptrón con una tasa de aprendizaje de 0.1 y 10 iteraciones
    perceptron.entrenar(X, y) #entrena el perceptrón con las entradas y salidas

    #Predicciones
    predicciones = perceptron.predecir(X) #realiza predicciones con el perceptrón entrenado
    print("Predicciones:", predicciones) #imprime las predicciones



#ADELINE
class ADALINE:
    #función de inicialización
    def __init__(self, tasa_aprendizaje=0.01, epocas=100): #inicializa la tasa de aprendizaje y el número de épocas
        self.tasa_aprendizaje = tasa_aprendizaje  #Tasa de aprendizaje
        self.epocas = epocas  #número de épocas de entrenamiento
        self.pesos = None  #pesos inicializados como None
        self.sesgo = None  #sesgo inicializado como None

    #función de activación lineal (función identidad)
    def activacion(self, X):
        return np.dot(X, self.pesos) + self.sesgo  #producto punto de X y pesos más sesgo

    #función de entrenamiento
    def entrenamiento(self, X, y):
        self.pesos = np.zeros(X.shape[1])  #inicializar los pesos a cero
        self.sesgo = 0  #inicializar el sesgo a 0

        #iterar por el número de épocas
        for _ in range(self.epocas):
            #calcular la salida de la activación
            salida = self.activacion(X) 

            #calcular el error (diferencia entre salida real y esperada)
            error = y - salida

            #actualizar los pesos y el sesgo usando el gradiente descendente
            self.pesos += self.tasa_aprendizaje * np.dot(X.T, error) #actualiza los pesos multiplicando la tasa de aprendizaje y el error
            self.sesgo += self.tasa_aprendizaje * error.sum() #actualiza el sesgo multiplicando la tasa de aprendizaje y la suma del error

    #función de predicción
    def predecir(self, X): #predicción para un conjunto de datos x
        salida_lineal = self.activacion(X) #calcula la salida lineal
        return np.where(salida_lineal >= 0.0, 1, -1)  #devuelve 1 si la salida es positiva, -1 si es negativa


#función para normalizar las entradas
def normalizar(X):
    return (X - X.mean()) / X.std() #normaliza las entradas restando la media y dividiendo por la desviación estándar

#datos de entrenamiento de la compuerta AND (con salidas en {-1, 1})
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  #Entradas
y = np.array([-1, -1, -1, 1])  #Salidas en {-1, 1}

#inicializar
adaline = ADALINE(tasa_aprendizaje=0.01, epocas=100) #inicializa el modelo ADALINE con una tasa de aprendizaje de 0.01 y 100 épocas

#entrenar el modelo
adaline.entrenamiento(X, y)

#mostrar los pesos finales y el sesgo
print("Pesos finales:", adaline.pesos)
print("Sesgo final:", adaline.sesgo)

#predicciones
predicciones = adaline.predecir(X) #realiza predicciones con el modelo ADALINE entrenado
print("Predicciones:", predicciones)


#Ejemplo de salida: 
#Perceptrón: 
#Predicciones: [0, 0, 0, 1]
#ADALINE:
# Pesos finales: [0.40918296 0.40918296]
# Sesgo final: -0.7987741943759272
# Predicciones: [-1 -1 -1  1]
#este resultado indica que el modelo ha aprendido a clasificar correctamente la compuerta AND, donde la salida es 1 solo cuando ambas entradas son 1.
#El modelo ADALINE ha ajustado sus pesos y sesgo para minimizar el error cuadrático entre la salida real y la esperada.
#El resultado de la predicción es -1 para las entradas (0,0), (0,1) y (1,0), y 1 para la entrada (1,1), lo que indica que el modelo ha aprendido correctamente la función AND.
#El modelo ADALINE es capaz de aprender funciones lineales y se basa en el principio de minimizar el error cuadrático medio (MSE) durante el entrenamiento.
#Esto lo hace diferente del Perceptrón, que utiliza una función escalón para la activación y no minimiza el error cuadrático.
#MADELINE combina muchas neuronas ADALINE para resolver problemas más complejos.