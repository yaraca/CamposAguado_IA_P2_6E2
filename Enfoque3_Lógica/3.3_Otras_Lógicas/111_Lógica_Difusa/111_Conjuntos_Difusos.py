#Logica Difusa: Conjuntos Difusos
#La lógica difusa (Fuzzy Logic) es una extensión de la lógica clásica que permite manejar la incertidumbre y el razonamiento aproximado. 
#En lugar de trabajar solo con valores verdadero (1) o falso (0), trabaja con grados de verdad, que pueden ser cualquier valor entre 0 y 1.
#Los conjuntos difusos: 
#permiten que un elemento pertenezca a un conjunto con cierto grado, llamado función de membresía.
#Ejemplo: Para un conjunto difuso "temperatura caliente", una temperatura de 30°C puede tener una pertenencia de 0.8, y una de 40°C una pertenencia de 1.0.
#Aplicaciones: control difuso(aires acondicionados, lavadoras), sistemas de recomendación, procesamiento de imágenes, etc.

#Ejemplo de conjunto difuso: temperatura caliente
#En este ejemplo, definimos un conjunto difuso para la temperatura "caliente" y graficamos su función de membresía.

#librerías necesarias
import matplotlib.pyplot as plt #para graficar
import numpy as np #para cálculos numéricos

#función para definir la función de membresía para "caliente"
def membresia_caliente(temperatura):
    if temperatura <= 25: #si la temperatura es menor o igual a 25°C, el grado de pertenencia es 0
        return 0.0 #no pertenece al conjunto difuso
    elif 25 < temperatura < 35: #si la temperatura está entre 25°C y 35°C, el grado de pertenencia aumenta linealmente
        return (temperatura - 25) / (35 - 25) #de 0 a 1
    else: #si la temperatura es mayor o igual a 35°C, el grado de pertenencia es 1
        return 1.0 #pertenece completamente al conjunto difuso

#crear un rango de temperaturas
temperaturas = np.linspace(20, 45, 100) #de 20°C a 45°C, 100 puntos
grados_membresia = [membresia_caliente(t) for t in temperaturas] #calcular el grado de pertenencia para cada temperatura

#graficar la función de membresía
plt.plot(temperaturas, grados_membresia, label='Caliente', color='red') 
plt.title('Conjunto Difuso: Temperatura Caliente')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Grado de pertenencia')
plt.grid(True)
plt.legend()
plt.show()

#evaluar algunos valores
pruebas = [22, 28, 35, 40] #temperaturas a evaluar
for t in pruebas: #para cada temperatura
    grado = membresia_caliente(t) #calcular el grado de pertenencia
    print(f"Temperatura: {t}°C -> Grado de membresía a 'caliente': {grado:.2f}") #imprimir el resultado

#Ejemplo de salida: 
# Temperatura: 22°C -> Grado de membresía a 'caliente': 0.00
# Temperatura: 28°C -> Grado de membresía a 'caliente': 0.30
# Temperatura: 35°C -> Grado de membresía a 'caliente': 1.00
# Temperatura: 40°C -> Grado de membresía a 'caliente': 1.00
#Grafica donde se observa la función de membresía para el conjunto difuso "caliente".
#La función de membresía es una representación gráfica que muestra cómo varía el grado de pertenencia al conjunto difuso "caliente" en función de la temperatura.
#Como se observa, a temperaturas menores a 25°C, el grado de pertenencia es 0. 
# A medida que la temperatura aumenta, el grado de pertenencia también aumenta, alcanzando un valor máximo de 1 a partir de 35°C.
#Esto significa que a 35°C y temperaturas superiores, la temperatura se considera completamente "caliente".
#A temperaturas entre 25°C y 35°C, el grado de pertenencia varía linealmente entre 0 y 1, lo que indica que la temperatura se considera "caliente" en un grado intermedio.
#Este enfoque permite manejar la incertidumbre y la vaguedad en la definición de conjuntos, lo que es útil en muchas aplicaciones prácticas.
