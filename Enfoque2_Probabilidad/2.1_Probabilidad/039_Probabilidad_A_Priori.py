#Probabilidad A Priori (probabilidad previa)
#Es la estimación inicial que hacemos sobre la probabilidad de que ocurra un evento antes de observar cualquier evidencia 
#Es lo que creemos que va a pasar basados en datos historicos, conocimiento previo o supociones, sin observar los datos actuales
#Primero se define los posibles eventos, se le asigna una probabilidad a cada evento y estas probabilidades pueden actualizarse a medida que se obtiene nueva información
#Sirve en IA para dar un valor inicial a las creencias de un modelo, en medician para estimar la probabilidad de una enfermedad antes de realizar pruebas, en finanzas para evaluar el riesgo de una inversión antes de analizar el mercado, etc.
#La suma de todas las probabilidades a priori debe ser igual a 1 (100%)

#Ejemplo probabilidad A Priori
#Un medico sabe que el 10% de la pobablacion tiene una enfermedad X, esa es su probabilidad a priori
#Solo se va a calcular y visualizar las probabilidades a priori
#Hay 3 posibles problemas: Enfermedad A, Enfermedad B y Sin enfermedad

#librerias necesarias
import matplotlib.pyplot as plt #libreria para graficar

#probabilidad a priori de cada enfermedad (antes de ver sintomas)
#estos valores pueden venir de estudios preivos, datos historicos, etc.
probabilidades_priori = {
    "Enfermedad A": 0.1,   # 10%
    "Enfermedad B": 0.05,  # 5%
    "Sin enfermedad": 0.85 # 85%
}

#verificar que la suma de las probabilidades a priori sea 1
suma_total = sum(probabilidades_priori.values()) #suma de todas las probabilidades

#mostrar resultados
print("Probabilidades a priori de cada enfermedad:")
for condicion, probabilidad in probabilidades_priori.items(): #probabilidad es un valor entre 0 y 1
    print(f" - {condicion}: {probabilidad*100:.1f}%") #multiplicamos por 100 para mostrar en porcentaje

#verificar que la suma de las probabilidades a priori sea 1
print(f"\nSuma total de probabilidades: {suma_total:.2f}")

#graficar las probabilidades a priori
etiquetas = list(probabilidades_priori.keys()) #obtener las etiquetas de los eventos
valores = list(probabilidades_priori.values()) #obtener los valores de las probabilidades

plt.figure(figsize=(6,6)) #crear una figura de 6x6 pulgadas
plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=140) #crear un grafico de pastel con los valores y etiquetas
plt.title("Distribución de Probabilidad A Priori")
plt.show()

#Ejemplo de salida:
# Probabilidades a priori de cada enfermedad:
#  - Enfermedad A: 10.0%
#  - Enfermedad B: 5.0%
#  - Sin enfermedad: 85.0%

# Suma total de probabilidades: 1.00