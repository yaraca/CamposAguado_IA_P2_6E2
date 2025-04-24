#Distribución de Probabilidad
#Describe como se distribuyen los valores de una variable aleatoria.
#Asocia valores posibles con la probabilidad de que ocurran.
#Esta la distribución discreta y continua.
#la discreta se usa para variables que toman valores contables (como lanzar un dado) y la continua para variables con infinitos valoes posibles en un intervalo.
#la suma (o integral) de todas las probabilidades es 1  #discreta(suma) o continua (integral)
#representa incertidumbre sobre el valor real de una variable 
#Se puede aplizar en economia en el análisis de riesgos, en la medicina para evaluar la probabilidad de enfermedades, en la ingeniería para el control de calidad, en la meteorología para predecir el clima, y en muchas otras áreas.

#Ejemplo de distribucion de probabilidad
#2 ejemplos: discreta(lanzar dados) y continua (normal)

#librerias necesarias
import matplotlib.pyplot as plt #para graficar
import numpy as np #para operaciones matematicas
from scipy.stats import norm #para distribucion normal 

#Probabilidad Discreta: Lanzar un Dado
#funcion de distribucion discreta
def distribucion_discreta():
    print("Distribución Discreta: Lanzar un dado")
    #posibles valores al lanzar un dado
    valores = [1, 2, 3, 4, 5, 6]
    #probabilidad uniforme de cada valor (1/6)
    probabilidades = [1/6] * 6
    #mostrar resultados
    for val, prob in zip(valores, probabilidades): #probabilidad de cada valor
        print(f"P({val}) = {prob:.2f}") 
    #graficar
    plt.figure(figsize=(6, 4)) #tamaño de la figura
    plt.bar(valores, probabilidades, color='skyblue', edgecolor='black') #barra de colores
    plt.title('Distribución de Probabilidad - Dado Justo') 
    plt.xlabel('Valor')
    plt.ylabel('Probabilidad')
    plt.xticks(valores) #valores en el eje x
    plt.ylim(0, 0.25) #limite del eje y
    plt.grid(axis='y', linestyle='--', alpha=0.5) #cuadrícula en el eje y  
    plt.show()

#Probabilidad Continua: Distribución Normal
#funcion de distribucion continua
def distribucion_continua():
    print("Distribución Normal (Gaussiana)") #la distribucion normal es una distribucion continua que describe como se distribuyen los valores de una variable aleatoria
    #parametros de la distribucion normal
    media = 0 #media o promedio de la distribucion 
    desviacion = 1 #desviacion estandar de la distribucion
    #rango de valores para graficar
    x = np.linspace(-4, 4, 1000) #valores de -4 a 4 con 1000 puntos
    #calcular la funcion de densidad de probabilidad (PDF) para la distribucion normal
    y = norm.pdf(x, media, desviacion) #PDF de la distribucion normal
    #el PDF es la funcion que describe la probabilidad de que una variable aleatoria continua tome un valor especifico

    #mostrar una probabilidad especifica (ejemplo: P(X < 1))
    prob_menor_1 = norm.cdf(1, media, desviacion) #CDF de la distribucion normal
    #la CDF es la funcion que describe la probabilidad de que una variable aleatoria continua tome un valor menor o igual a un valor especifico
    print(f"P(X < 1) = {prob_menor_1:.4f}") #probabilidad de que X sea menor que 1

    #graficar la distribucion normal
    plt.figure(figsize=(8, 4)) #tamaño de la figura
    plt.plot(x, y, color='purple', label='f(x)') #graficar la PDF
    plt.title('Distribución Normal (μ=0, σ=1)') #distribucion normal con media 0 y desviacion estandar 1
    plt.xlabel('x') #etiqueta del eje x
    plt.ylabel('Densidad de Probabilidad') #etiqueta del eje y
    plt.fill_between(x, y, where=(x < 1), color='violet', alpha=0.3, label='P(X < 1)') #rellenar el area bajo la curva para P(X < 1)
    plt.legend() #leyenda de la grafica
    plt.grid(True, linestyle='--', alpha=0.5) #cuadrícula en la grafica
    plt.show()

#función principal
def main():
    #llamar a las funciones de distribucion discreta y continua
    distribucion_discreta() #distribucion discreta
    distribucion_continua() #distribucion continua

#ejecutar la funcion principal
if __name__ == "__main__":
    main() #ejecutar la funcion principal

#Ejemplo de salida:
# Distribución Discreta: Lanzar un dado
# P(1) = 0.17
# P(2) = 0.17
# P(3) = 0.17
# P(4) = 0.17
# P(5) = 0.17
# P(6) = 0.17
# Distribución Normal (Gaussiana)
# P(X < 1) = 0.8413