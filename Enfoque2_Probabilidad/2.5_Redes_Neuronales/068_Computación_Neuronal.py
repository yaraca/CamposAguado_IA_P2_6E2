# Computación Neuronal
#es la simulación de la forma en que el cerebro procesa información utilizando modelos computacionales llamados neuronas artificiales.
#Cada neurona artificial imita el comportamiento de una neurona biológica: recibe señales, las procesa y genera una salida.
#La computación neuronal es la base de las redes neuronales artificiales que se usan hoy en día en Deep Learning.
#Cada neurona artificial realiza 3 pasos principales:
#Suma ponderada de entradas: Cada entrada se multiplica por un peso que representa su importancia.
#Suma total + sesgo: Se añade un término llamado bias que ajusta el resultado.
#Función de activación: Decide si la neurona debe activarse o no, introduciendo no linealidad.
#Formula basica de una neurona artificial: y=f(∑(wi*xi)+b)
#Donde: wi son los pesos, xi son las entradas, b es el sesgo, f es la función de activación, y es la salida.
#Aplicaciones: reconocimiento de patrones, predicción de series temporales, procesamiento de imágenes, procesamiento de lenguaje natural, etc.

#Ejemplo de una neurona artificial simple
#construir una neurona simple para clasificar datos básicos.

#librerías necesarias
import numpy as np #para operaciones matemáticas y matrices

#definir una función de activación (en este caso, la función escalón)
def step_function(x): ##Función de activación escalón (step function)
    return 1 if x >= 0 else 0 #Devuelve 1 si x es mayor o igual a 0, de lo contrario devuelve 0

#definir la clase de una neurona
class Neurona: 
    #funcion constructor 
    def __init__(self, pesos, sesgo):  #Inicializa la neurona con pesos y sesgo
        self.pesos = np.array(pesos)  # Los pesos (w)
        self.sesgo = sesgo            # El sesgo (b)

    #funcion activar
    def activar(self, entradas): # Activa la neurona con las entradas
        #Producto punto entre entradas y pesos + sesgo
        suma = np.dot(self.pesos, entradas) + self.sesgo
        
        #Aplicar función de activación
        salida = step_function(suma)
        
        return salida # Devuelve la salida (0 o 1)

#Datos de ejemplo
entradas = np.array([1, 0])  #dos entradas (por ejemplo, interruptores ON y OFF)

#Crear la neurona
#pesos = [0.6, 0.5], sesgo = -0.2
neurona = Neurona(pesos=[0.6, 0.5], sesgo=-0.2)

#activar la neurona con las entradas
salida = neurona.activar(entradas) #salida = 1 o 0 dependiendo de la activación

#Mostrar resultados
print(f"La salida de la neurona es: {salida}")

#Ejemplo de salida:
#La salida de la neurona es: 1
#Esto significa que la neurona se activó (salida 1) porque la suma ponderada de las entradas y el sesgo fue mayor o igual a 0.
#Si la salida hubiera sido 0, significaría que la neurona no se activó.
#Este ejemplo ilustra cómo funciona una neurona artificial simple y cómo se puede usar para clasificar datos básicos.
#En la práctica, las neuronas se combinan en capas para formar redes neuronales más complejas que pueden aprender patrones y realizar tareas más sofisticadas.



