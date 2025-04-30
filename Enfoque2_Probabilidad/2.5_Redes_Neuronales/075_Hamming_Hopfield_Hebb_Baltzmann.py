#Hamming, Hopfield, Hebb, Boltzmann, ...
#HAMMING
#Se usa para reconocimiento de patrones binarios. 
#Tiene dos capas: Comparación (distancia Hamming). y Capa de competencia (neurona ganadora).
#Aplicación: Reconocimiento de patrones binarios con ruido.
#HOPFIELD
#Red recurrente totalmente conectada. Las conexiones son simétricas y sin auto-conexión.
#Guarda patrones como mínimos de energía. Capaz de recuperar un patrón completo a partir de una entrada parcial o ruidosa.
#Aplicación: Memoria asociativa, recuperación de patrones, optimización combinatoria.
#HEBB
#“Las neuronas que se disparan juntas, se conectan juntas”.
#Se usa para aprender patrones asociativos de forma no supervisada.
#Aplicación: Reconocimiento y asociación de patrones.
#BOLTZMANN
#Red estocástica (probabilística) con nodos visibles y ocultos. Puede aprender distribuciones de probabilidad de los datos.
#Usa una función de energía y probabilidades para el aprendizaje.
#Aplicación: Modelado generativo, reconocimiento de patrones complejos.



#Red de Hopfield para almacenar y recuperar patrones binarios
import numpy as np

#función de entrenamiento
def entrenar_hopfield(patrones):
    n = patrones.shape[1]  # número de neuronas
    W = np.zeros((n, n))   # matriz de pesos
    for p in patrones:
        W += np.outer(p, p)  # producto externo del patrón consigo mismo
    np.fill_diagonal(W, 0)  # no se permite autoconexión
    return W

#Definir función de recuperación
def recuperar(W, patron_inicial, pasos=5): # número de pasos de actualización
    patron = patron_inicial.copy() # copia del patrón inicial
    for _ in range(pasos): # iterar por el número de pasos
        for i in range(len(patron)): # para cada neurona
            suma = np.dot(W[i], patron) # producto punto con la fila i de W
            patron[i] = 1 if suma >= 0 else -1 # función de activación (escalón) 
    return patron # devuelve el patrón recuperado
 
#definir patrones de entrenamiento
#usar -1 y 1 en lugar de 0 y 1 (forma estándar en Hopfield)
patrones_entrenamiento = np.array([
    [1, -1, 1, -1],  #patrón A
    [-1, 1, -1, 1]   #patrón B
])

#entrenar la red
W = entrenar_hopfield(patrones_entrenamiento) # matriz de pesos

#prueba con un patrón ruidoso
patron_ruidoso = np.array([1, -1, -1, -1])  #se parece al patrón A

#recuperar el patrón
patron_recuperado = recuperar(W, patron_ruidoso) 

#mostrar resultados
print("PATRÓN DE HOPFIELD")
print("Patrón de entrada ruidoso:   ", patron_ruidoso)
print("Patrón recuperado por Hopfield:", patron_recuperado)


#--------------------------------------------------------------------
#Red de Hamming para almacenar y recuperar patrones binarios

#Patrones de entrenamiento binarios (0 y 1)
patrones = np.array([
    [1, 0, 1, 0],   # Patrón A
    [0, 1, 0, 1]    # Patrón B
])

#convertir a -1 y 1 (estilo neuronal)
patrones_convertidos = 2 * patrones - 1 # Convertir 0 a -1 y 1 a 1

#función de red de Hamming
def red_hamming(patrones_entrenamiento, patron_entrada):
    #convertir entrada
    entrada = 2 * np.array(patron_entrada) - 1 # Convertir 0 a -1 y 1 a 1

    #calcular similitud (producto punto con cada patrón)
    similitudes = patrones_entrenamiento @ entrada 

    #elegir el índice del patrón más similar
    indice_ganador = np.argmax(similitudes) 

    return indice_ganador, similitudes #devuelve el índice del patrón más similar y las similitudes

#Entrada con ruido
entrada_ruidosa = [1, 0, 0, 0]  #se parece más al patrón A

#ejecutar la red de Hamming
indice, similitudes = red_hamming(patrones_convertidos, entrada_ruidosa) 

#mostrar resultados
print("\nHAMMING")
print("Similitud con cada patrón:", similitudes)
print("El patrón más parecido es el número:", indice)
print("Patrón identificado:", patrones[indice])


#--------------------------------------------------------------------
#Regla de Hebb para aprender patrones

#definir los patrones de entrada (X) y salidas deseadas (Y)
X = np.array([
    [1, -1, 1],   # Patrón 1
    [-1, 1, -1],  # Patrón 2
    [1, 1, -1]    # Patrón 3
])

Y = np.array([1, -1, 1])  #salidas deseadas asociadas a cada patrón

#inicializar los pesos en cero
pesos = np.zeros(X.shape[1])  #vector de pesos del mismo tamaño que las entradas

#aplicar la Regla de Hebb para aprendizaje supervisado
for i in range(len(X)):
    pesos += X[i] * Y[i]  #Hebb: Δw = x * y (asociación entrada-salida)

print("\nHEBB")
print("Pesos entrenados con Hebb:")
print(pesos)

#fase de prueba: aplicar los pesos a los mismos patrones
def activar(x):
    return 1 if x >= 0 else -1  #función escalón binaria

print("Resultados de la red:")
for i in range(len(X)): # iterar por cada patrón
    salida = activar(np.dot(X[i], pesos))  #producto punto entrada · pesos
    print(f"Entrada: {X[i]} → Salida esperada: {Y[i]} → Salida obtenida: {salida}") # salida de la red

#ejemplo de salida:
# PATRÓN DE HOPFIELD
# Patrón de entrada ruidoso:    [ 1 -1 -1 -1]
# Patrón recuperado por Hopfield: [ 1 -1  1 -1]
#como se puede observar, el patrón recuperado es el patrón A, que es el más parecido al patrón ruidoso.
#esto indica que la red de Hopfield ha logrado recuperar el patrón original a partir de una entrada ruidosa.

# HAMMING
# Similitud con cada patrón: [ 2 -2]
# El patrón más parecido es el número: 0
# Patrón identificado: [1 0 1 0]
#como se puede observar, la red de Hamming ha identificado correctamente el patrón A como el más parecido al patrón ruidoso.
#esto indica que la red de Hamming ha logrado reconocer el patrón original a partir de una entrada ruidosa.

# HEBB
# Pesos entrenados con Hebb:
# [ 3. -1.  1.]
# Resultados de la red:
# Entrada: [ 1 -1  1] → Salida esperada: 1 → Salida obtenida: 1
# Entrada: [-1  1 -1] → Salida esperada: -1 → Salida obtenida: -1
# Entrada: [ 1  1 -1] → Salida esperada: 1 → Salida obtenida: 1
#como se puede observar, la red de Hebb ha logrado aprender los patrones de entrada y producir las salidas esperadas.
#esto indica que la regla de Hebb ha sido efectiva para aprender patrones asociativos a partir de ejemplos de entrada y salida.

