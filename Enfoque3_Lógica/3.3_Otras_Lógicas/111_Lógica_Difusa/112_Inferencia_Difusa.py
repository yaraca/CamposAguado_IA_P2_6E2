#Lógica Difusa: Inferencia Difusa
#es el proceso mediante el cual un sistema toma decisiones o conclusiones basadas en reglas difusas y valores imprecisos.
#Se basa en: 
# Fuzzificación: Convertir datos numéricos en valores difusos.
# Evaluación de reglas: Aplicar reglas del tipo SI condición ENTONCES consecuencia.
# Agregación: Combinar resultados de todas las reglas.
# Defuzzificación: Convertir el resultado difuso a un valor numérico claro (crisp).
#Aplicaciones: control de sistemas, toma de decisiones, procesamiento de imágenes, etc.

#Ejemplo de Lógica difuda: Inferencia difusa
#Control de velocidad de un ventilador
# Reglas:
# SI temperatura es baja ENTONCES velocidad es baja
# SI temperatura es media ENTONCES velocidad es media
# SI temperatura es alta ENTONCES velocidad es alta

#librerías necesarias
import numpy as np #para operaciones numéricas y matrices

# Funciones de membresía para la entrada: temperatura
#Función de temperatura baja
def temperatura_baja(x): 
    if x <= 20: #si la temperatura es menor o igual a 20
        return 1 #pertenece completamente a la categoría baja
    elif 20 < x < 30: #si la temperatura está entre 20 y 30
        return (30 - x) / 10 #pertenencia parcial
    else: #si la temperatura es mayor o igual a 30
        return 0 #no pertenece a la categoría baja

#Función de temperatura media
def temperatura_media(x):
    if 20 < x < 30: #si la temperatura está entre 20 y 30
        return (x - 20) / 10 #pertenencia parcial
    elif 30 <= x <= 40: #si la temperatura está entre 30 y 40
        return (40 - x) / 10 #pertenencia parcial
    else: #si la temperatura es menor o igual a 20 o mayor a 40
        return 0 #no pertenece a la categoría media

#Función de temperatura alta
def temperatura_alta(x):
    if x <= 30: #si la temperatura es menor o igual a 30
        return 0 #no pertenece a la categoría alta
    elif 30 < x < 40: #si la temperatura está entre 30 y 40
        return (x - 30) / 10 #pertenencia parcial
    else: #si la temperatura es mayor o igual a 40
        return 1 #pertenece completamente a la categoría alta

# Valores difusos de salida: velocidad (crisp luego de defuzzificación)
valores_velocidad = {
    'baja': 20,
    'media': 50,
    'alta': 80
}

# Función de inferencia difusa
def inferencia_difusa(temperatura):
    # Fuzzificación: obtener grados de membresía, osea, qué tan baja, media o alta es la temperatura
    mu_baja = temperatura_baja(temperatura) #grado de pertenencia a baja
    mu_media = temperatura_media(temperatura) #grado de pertenencia a media
    mu_alta = temperatura_alta(temperatura) #grado de pertenencia a alta

    #Regla 1: SI temperatura es baja ENTONCES velocidad es baja
    r1 = mu_baja * valores_velocidad['baja']
    
    #Regla 2: SI temperatura es media ENTONCES velocidad es media
    r2 = mu_media * valores_velocidad['media']
    
    #Regla 3: SI temperatura es alta ENTONCES velocidad es alta
    r3 = mu_alta * valores_velocidad['alta']

    #Agregación y Defuzzificación (promedio ponderado)
    suma_pesos = mu_baja + mu_media + mu_alta #suma de los grados de pertenencia
    if suma_pesos == 0: #si la suma es cero, no hay pertenencia a ninguna categoría
        return 0 #evita división por cero
    velocidad_resultado = (r1 + r2 + r3) / suma_pesos #promedio ponderado de las velocidades
    return velocidad_resultado #retorna la velocidad resultante

#probar el sistema con diferentes temperaturas
temperaturas_prueba = [18, 25, 35, 42] #temperaturas de prueba
for t in temperaturas_prueba: #iterar sobre las temperaturas
    velocidad = inferencia_difusa(t) #calcular la velocidad usando la función de inferencia difusa
    print(f"Temperatura: {t}°C → Velocidad estimada del ventilador: {velocidad:.2f} %") 

#Ejemplo de salida: 
# Temperatura: 18°C → Velocidad estimada del ventilador: 20.00 %
# Temperatura: 25°C → Velocidad estimada del ventilador: 35.00 %
# Temperatura: 35°C → Velocidad estimada del ventilador: 65.00 %
# Temperatura: 42°C → Velocidad estimada del ventilador: 80.00 %
#El resultado muestra la velocidad estimada del ventilador para cada temperatura de entrada, utilizando la lógica difusa para inferir el resultado.
#como se puede ver, a medida que la temperatura aumenta, la velocidad del ventilador también aumenta, lo que es consistente con las reglas definidas.
#Este ejemplo ilustra cómo la lógica difusa puede ser utilizada para tomar decisiones basadas en condiciones imprecisas, como la temperatura ambiente.