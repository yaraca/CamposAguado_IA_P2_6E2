#Probabilidad Condicionada y Normalizacion 
#La probabilidad condicionada es la probabilidad de que ocurra un evento dado que otro evento ya ha ocurrido. Se denota como P(A|B), que se lee como "la probabilidad de A dado B".
#P(A|B) = P(A y B) / P(B)
#La normalización es el proceso de ajustar los valores de una función de probabilidad para que sumen 1. Esto es importante porque las probabilidades deben ser proporcionales y la suma total de todas las probabilidades debe ser igual a 1.
#La normalización se utiliza para convertir una distribución de probabilidad no normalizada en una distribución de probabilidad válida.
#P(Ai/B) = α * P(B|Ai) * P(Ai) #la probabilidad de Ai dado B es proporcional a la probabilidad de B dado Ai multiplicada por la probabilidad de Ai.
#Donde: P(B|Ai) * P(Ai) es la probabilidad no normalizada y α es un factor de normalización que asegura que la suma total de las probabilidades sea 1.
#       α = 1 / P(B) = 1 / Σ P(B|Ai) * P(Ai)  #alpha es el inverso de la probabilidad total de B, que se obtiene sumando las probabilidades no normalizadas de todos los eventos Ai.
#Se puede usar en clasificadores bayesianos, diagnostico medico, deteccion de fallas, etc.

#Ejemplo de probabilidad condicionada y normalización
#Diagnostico de enfermad segun un test
#Saber la probabilidad de que un paciente tenga una enfermedad dado que el test ha dado positivo

#definir las probabiliadades a priori (previas)
P_enfermo = 0.01 # 1% de la población tiene la enfermedad
P_sano = 0.99 # 99% no la tiene

#definir la probabilidad condicional de que el test de positivo 
P_positivo_dado_enfermo = 0.99 #alta sensibilidad: si estás enfermo, 99% de dar positivo
P_positivo_dado_sano = 0.05 #falsos positivos: 5% de los sanos dan positivo

#probabilidad no normalizada
#usar regla de bayes sin normalizar para calcular la probabilidad de estar enfermo dado un resultado positivo en el test
no_norm_enfermo = P_positivo_dado_enfermo * P_enfermo #probabilidad de que el test sea positivo dado que el paciente está enfermo multiplicada por la probabilidad de estar enfermo
no_norm_sano = P_positivo_dado_sano * P_sano #probabilidad de que el test sea positivo dado que el paciente está sano multiplicada por la probabilidad de estar sano

#noralizar la probabilidad para que sumen 1
#α = 1 / suma de las probabilidades no normalizadas
alpha = 1 / (no_norm_enfermo + no_norm_sano)

#aplicar alfa para normalizar las probabilidades
P_enfermo_dado_positivo = alpha * no_norm_enfermo #probabilidad de estar enfermo dado que el test ha dado positivo
P_sano_dado_positivo = alpha * no_norm_sano #probabilidad de estar sano dado que el test ha dado positivo

#mostrar resultados
print("Probabilidad Condicionada (dado resultado positivo):")
print(f"  - P(Enfermo | Positivo) = {P_enfermo_dado_positivo:.4f}") #probabilidad de estar enfermo dado que el test ha dado positivo
print(f"  - P(Sano | Positivo)    = {P_sano_dado_positivo:.4f}") #probabilidad de estar sano dado que el test ha dado positivo

#Ejemplo de salida: 
# Probabilidad Condicionada (dado resultado positivo):
#   - P(Enfermo | Positivo) = 0.1667
#   - P(Sano | Positivo)    = 0.8333
