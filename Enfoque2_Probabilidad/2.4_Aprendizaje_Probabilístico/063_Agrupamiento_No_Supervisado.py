#Agrupamiento no supervisado (K-means) 
#es una técnica de aprendizaje automático donde no tienes etiquetas (clases) en tus datos, pero quieres descubrir grupos naturales dentro de ellos.
#su objetivo es dividir los datos en grupos (clusters) de modo que:
#Los datos en el mismo grupo sean similares entre sí y os datos en grupos distintos sean diferentes.
#Funcionamiento: Inicialización (elecciona aleatoriamente "centros" o "prototipos" de los clusters.)
#Asignación (asigna cada dato al cluster cuyo centro esté más cerca de él.)
#Actualización (Calcula nuevos centros como el promedio de los puntos asignados.)
#Iteracion (Repite los pasos 2 y 3 hasta que los centros ya no cambien (o hasta un número máximo de iteraciones)
#Aplicaciones: segmentación de clientes, análisis de imágenes, compresión de datos, etc.

#Ejemplo de K-means

##librerías necesarias
import numpy as np #para operaciones matemáticas y matrices
import matplotlib.pyplot as plt #para graficar

#Crear datos de ejemplo (dos grupos separados)
np.random.seed(42) #para reproducibilidad
grupo1 = np.random.randn(100, 2) + np.array([0, 0])  # Grupo alrededor de (0,0)
grupo2 = np.random.randn(100, 2) + np.array([5, 5])  # Grupo alrededor de (5,5)
datos = np.vstack((grupo1, grupo2))  #unir los datos

#Parámetros del algoritmo
k = 2  #Número de clusters
n_iteraciones = 10 #Número de iteraciones

#Inicializar los centros (elegir k puntos aleatorios)
centros = datos[np.random.choice(len(datos), k, replace=False)] 

print(f"Centros iniciales:\n{centros}") #imprimir centros iniciales

#Algoritmo K-means
for iteracion in range(n_iteraciones): #Iterar para ajustar los centros
    #Paso de asignación
    etiquetas = [] #Lista para almacenar etiquetas de cada punto
    for punto in datos: #iterar sobre cada punto
        distancias = np.linalg.norm(punto - centros, axis=1)  # Distancia a cada centro
        etiqueta = np.argmin(distancias)  # Tomar el centro más cercano
        etiquetas.append(etiqueta) #almacenar la etiqueta del punto
    etiquetas = np.array(etiquetas) #convertir a array de numpy

    #Paso de actualización
    nuevos_centros = [] #Lista para almacenar nuevos centros
    for i in range(k): #iterar sobre cada cluster
        puntos_cluster = datos[etiquetas == i] #filtrar puntos del cluster i
        nuevo_centro = puntos_cluster.mean(axis=0) if len(puntos_cluster) > 0 else centros[i] #calcular nuevo centro como la media de los puntos asignados al cluster
        nuevos_centros.append(nuevo_centro) #almacenar el nuevo centro
    centros = np.array(nuevos_centros) #convertir a array de numpy

    print(f"Iteración {iteracion+1}: Centros actualizados:\n{centros}") #imprimir centros actualizados

#mostrar resultado
colores = ['red', 'blue'] #colores para los clusters
for i in range(k): #iterar sobre cada cluster
    plt.scatter(datos[etiquetas == i][:, 0], datos[etiquetas == i][:, 1],  
                color=colores[i], label=f'Cluster {i+1}') #graficar puntos del cluster i

plt.scatter(centros[:, 0], centros[:, 1], color='black', marker='x', s=100, label='Centros') #graficar centros
plt.title('Resultado del Agrupamiento No Supervisado (K-means)') 
plt.legend()
plt.show()

#Ejemplo de salida:
# Centros iniciales:
# [[ 1.40279431 -1.40185106]
#  [-0.19236096  0.30154734]]
# Iteración 1: Centros actualizados:
# [[3.07706858 0.91336764]
#  [2.40562582 2.82558805]]
# Iteración 2: Centros actualizados:
# [[ 0.08252383 -0.21667301]
#  [ 4.22580316  4.49346032]]
# Iteración 3: Centros actualizados:
# [[-0.11556425  0.03402232]
#  [ 5.12824872  5.04348765]]
# Iteración 4: Centros actualizados:
# [[-0.11556425  0.03402232]
#  [ 5.12824872  5.04348765]]
# Iteración 5: Centros actualizados:
# [[-0.11556425  0.03402232]
#  [ 5.12824872  5.04348765]]
# Iteración 6: Centros actualizados:
# [[-0.11556425  0.03402232]
#  [ 5.12824872  5.04348765]]
# Iteración 7: Centros actualizados:
# [[-0.11556425  0.03402232]
#  [ 5.12824872  5.04348765]]
# Iteración 8: Centros actualizados:
# [[-0.11556425  0.03402232]
#  [ 5.12824872  5.04348765]]
# Iteración 9: Centros actualizados:
# [[-0.11556425  0.03402232]
#  [ 5.12824872  5.04348765]]
# Iteración 10: Centros actualizados:
# [[-0.11556425  0.03402232]
#  [ 5.12824872  5.04348765]]

#En la grafica los datos rojos y azules separados claramente en dos grupos.
#Dos grandes manchas de puntos y los centros (en negro) marcados.
#Asi se puede ver cómo K-means aprendió los patrones sin saber a qué grupo pertenecían los datos.

