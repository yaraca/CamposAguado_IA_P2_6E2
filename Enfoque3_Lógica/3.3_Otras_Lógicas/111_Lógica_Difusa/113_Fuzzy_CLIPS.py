#Fuzzy CLIPS
#Fuzzy CLIPS es una extensión del lenguaje CLIPS (C Language Integrated Production System) que permite incorporar conjuntos difusos en sistemas basados en reglas.
#Fuzzy CLIPS permite manejar incertidumbre y aproximaciones, esenciales en situaciones del mundo real.
#Funcionamiento: 
# Hechos difusos: se definen con grados de verdad entre 0 y 1.
# Reglas difusas: permiten inferencias en función del grado de pertenencia.
# Inferencia: se hace usando encadenamiento hacia adelante.
# Defuzzificación: opcional, si se requiere una salida crisp (numérica concreta).
#Aplicaciones: diagnóstico médico, control de procesos, sistemas de recomendación, etc.

#Ejemplo de Lógica Difusa con Fuzzy CLIPS
#Diagnóstico difuso de humedad del suelo.

# Simulación de reglas difusas tipo Fuzzy CLIPS
#Función de huedad baja
def humedad_baja(x):
    if x <= 30: #si la humedad es menor o igual a 30
        return 1 #la humedad es baja
    elif 30 < x < 50: #si la humedad es mayor a 30 y menor a 50
        return (50 - x) / 20 #la humedad es media
    else: #si la humedad es mayor a 50
        return 0 #la humedad es alta

#función de humedad media
def humedad_media(x):
    if 30 < x < 50: #si la humedad es mayor a 30 y menor a 50
        return (x - 30) / 20 #la humedad es media
    elif 50 <= x <= 70: #si la humedad es mayor o igual a 50 y menor o igual a 70
        return (70 - x) / 20 #la humedad es alta
    else: #si la humedad es menor a 30 o mayor a 70
        return 0 #la humedad es baja

#función de humedad alta
def humedad_alta(x):
    if x <= 50: #si la humedad es menor o igual a 50
        return 0 #la humedad es baja
    elif 50 < x < 70: #si la humedad es mayor a 50 y menor a 70
        return (x - 50) / 20 #la humedad es media
    else: #si la humedad es mayor o igual a 70
        return 1 #la humedad es alta

# Salidas esperadas
acciones = {
    'riego_bajo': 20, 
    'riego_medio': 50,
    'riego_alto': 80
}

#Función de motor de inferencia difusa para el diagnóstico de humedad del suelo
def motor_inferencia(humedad):
    # Fuzzificación
    mu_baja = humedad_baja(humedad) #grados de pertenencia a baja
    mu_media = humedad_media(humedad) #grados de pertenencia a media
    mu_alta = humedad_alta(humedad) #grados de pertenencia a alta

    # Reglas difusas tipo CLIPS:
    r1 = mu_baja * acciones['riego_alto']     # SI humedad es baja, ENTONCES riego alto
    r2 = mu_media * acciones['riego_medio']   # SI humedad es media, ENTONCES riego medio
    r3 = mu_alta * acciones['riego_bajo']     # SI humedad es alta, ENTONCES riego bajo

    suma_mu = mu_baja + mu_media + mu_alta #suma de los grados de pertenencia
    if suma_mu == 0: #si la suma de los grados de perten
        return 0  # Evita división por cero

    # Defuzzificación: promedio ponderado
    resultado = (r1 + r2 + r3) / suma_mu #promedio ponderado de los grados de pertenencia
    return resultado #devuelve el resultado de la defuzzificación

# Pruebas
niveles_humedad = [20, 40, 60, 80] #niveles de humedad a probar
for h in niveles_humedad: #para cada nivel de humedad
    riego = motor_inferencia(h) #llama a la función de motor de inferencia
    print(f"Humedad: {h}% → Nivel de riego recomendado: {riego:.2f}%") 

#Ejemplo de salida:
# Humedad: 20% → Nivel de riego recomendado: 80.00%
# Humedad: 40% → Nivel de riego recomendado: 65.00%
# Humedad: 60% → Nivel de riego recomendado: 35.00%
# Humedad: 80% → Nivel de riego recomendado: 20.00%
# El resultado muestra el nivel de riego recomendado según el nivel de humedad del suelo.
# A medida que la humedad aumenta, el nivel de riego recomendado disminuye.
# Esto es típico en sistemas de riego automatizados, donde se busca optimizar el uso del agua.
# En un sistema real, se podrían usar sensores para medir la humedad y ajustar el riego automáticamente.
