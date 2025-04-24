#Incertidumbre 
#La incertidumbre es cuando no se tiene informacion completa o segura sobre lo que ocurre
#Se refiere a la falta de certeza o conocimiento sobre un evento o resultado
#Es una parte fundamental de que la IA debe aprende a manejar para tomar decisiones inteligente s
#Se usa probabilidad para modelar la incertidumbre. Se representar eventos inciertos como variables aleatorias, teorema de Bayes, distribuciones de probabilidad, etc.
#Se puede utilizar en el diagnostico médico, reconocimiento de voz, clasificacion de objetos en vision artifical, agentes autonomos, etc.
#Teorema de Bayes: es una regla que permite actualizar la probabilidad de un evento a medida que se obtiene nueva información. Se basa en la regla de Bayes, que establece que la probabilidad de un evento A dado un evento B es igual a la probabilidad de B dado A multiplicada por la probabilidad de A, dividido por la probabilidad de B.
#P(A|B) = P(B|A) * P(A) / P(B)
#Donde: numerador = probabilidad conjunta de A y B, denominador = probabilidad de B

#Ejemplo de Incertidumbre
#Un paciente puede o no tener gripe, tiene sintomas de fiebre, tos y fatiga, se sabe la probabilidad de que pasen esos sintomas si tiene gripe y si no tiene gripe.

#Proabilidad inicial
p_gripe = 0.1 #probabilidad de que el paciente tenga gripe 10%
p_no_gripe = 1 - p_gripe #probabilidad de que el paciente no tenga gripe 90%

#Probabilidades condicionales 
# P(Síntoma | Gripe) y P(Síntoma | No Gripe)
prob_sintomas_dado_gripe = { 
    "fiebre": 0.9, #probabilidad de fiebre dado que tiene gripe
    "tos": 0.8, #probabilidad de tos dado que tiene gripe
    "fatiga": 0.7 #probabilidad de fatiga dado que tiene gripe
}

prob_sintomas_dado_no_gripe = {
    "fiebre": 0.2, #probabilidad de fiebre dado que no tiene gripe
    "tos": 0.3, #probabilidad de tos dado que no tiene gripe
    "fatiga": 0.1 #probabilidad de fatiga dado que no tiene gripe
}

#Sintomas observados
sintomas_observados = ["fiebre", "tos"]  #Sintomas que tiene el paciente

#Calcular la probabilidad conjunta de los sintomas dados los dos casos (gripe y no gripe)
#Usar la regla del producto para sintomas independientes
#P(Sintomas | Gripe)
prob_sintomas_si_gripe = 1.0 #probabilidad de los sintomas dado que tiene gripe
for sintoma in sintomas_observados:
    prob_sintomas_si_gripe *= prob_sintomas_dado_gripe[sintoma] #probabilidad de fiebre y tos dado que tiene gripe

#P(Sintomas | No Gripe)
prob_sintomas_si_no_gripe = 1.0 #probabilidad de los sintomas dado que no tiene gripe
for sintoma in sintomas_observados:
    prob_sintomas_si_no_gripe *= prob_sintomas_dado_no_gripe[sintoma] #probabilidad de fiebre y tos dado que no tiene gripe

#Proabilidad total de los sintomas (teorema de la probabilidad total)
p_sintomas = (prob_sintomas_si_gripe * p_gripe) + (prob_sintomas_si_no_gripe * p_no_gripe) 
#probabilidad de los sintomas dados los dos casos (gripe y no gripe)

#Teorema de Bayes para calcular la probabilidad de que el paciente tenga gripe dado los sintomas P(gripe | sintomas)
p_gripe_dado_sintomas = (prob_sintomas_si_gripe * p_gripe) / p_sintomas #probabilidad de que el paciente tenga gripe dado los sintomas

#mostrar resultados
print("'Diagnostico de gripe'")
print(f"Síntomas observados: {sintomas_observados}") #Sintomas que tiene el paciente
print(f"Probabilidad de tener gripe dado los síntomas: {p_gripe_dado_sintomas:.2f} (o {p_gripe_dado_sintomas*100:.1f}%)") #probabilidad de que el paciente tenga gripe dado los sintomas

#Ejemplo de salida:
# 'Diagnostico de gripe'
# Síntomas observados: ['fiebre', 'tos']
# Probabilidad de tener gripe dado los síntomas: 0.57 (o 57.1%)