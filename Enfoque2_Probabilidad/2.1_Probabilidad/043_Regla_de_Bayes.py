#Regla de Bayes
#Nos permite actualizar nuestras creencias sobre un evento A dado que ocurrio otro evento B
#Formula: P(A|B) = P(B|A) * P(A) / P(B)
#P(A|B) = Probabilidad posterior (probabilidad de A dado B) lo que se quiere calcular
#P(B|A) = Probabilidad verosimil (que tan probable es B si A es cierto)
#P(A) = Probabilidad a priori (previa) (probabilidad de A antes de ver B) lo que se conoce
#P(B) = Probabilidad evidencia (probabilidad total de B) lo que se conoce
#se puede aplicar en medicina para diagnosticar enfermedades, en finanzas para evaluar riesgos, en marketing para segmentar clientes, y en muchas otras áreas.

#Ejemplo de regla de Bayes
#probabilidad de que una persona tenga una enfermedad dado que ha dado positivo en una prueba
#Se supone: P(enfermedad) = 0.01 (1% de la poblacion tiene la enfermedad)
#P(prueba positiva|enfermedad) = 0.99 (99% de los enfermos dan positivo en la prueba)
#P(prueba positiva|no enfermedad) = 0.05 (5% de los sanos dan positivo en la prueba)

#funcion de la regla de Bayes
def regla_de_bayes(p_enfermedad, p_positivo_dado_enfermedad, p_positivo_dado_no_enfermedad):
    #P(No enfermedad) = 1 - P(Enfermedad)
    p_no_enfermedad = 1 - p_enfermedad #probabilidad de no tener la enfermedad

    #P(Prueba positiva) total (teorema de la probabilidad total)
    p_positivo = (p_positivo_dado_enfermedad * p_enfermedad) + \
                 (p_positivo_dado_no_enfermedad * p_no_enfermedad) #probabilidad total de dar positivo en la prueba

    #aplicar la fórmula de Bayes
    p_enfermedad_dado_positivo = (p_positivo_dado_enfermedad * p_enfermedad) / p_positivo #probabilidad de tener la enfermedad dado que ha dado positivo en la prueba

    #mostrar los resultados
    print("Cálculo de la probabilidad posterior:")
    print(f"P(Enfermedad | Prueba positiva) = {p_enfermedad_dado_positivo:.4f}") #probabilidad de tener la enfermedad dado que ha dado positivo en la prueba
    print(f"P(Prueba positiva)              = {p_positivo:.4f}") #probabilidad total de dar positivo en la prueba

    return p_enfermedad_dado_positivo #devolver la probabilidad de tener la enfermedad dado que ha dado positivo en la prueba

#llamar a la funcion con los valores de probabilidad
regla_de_bayes(
    p_enfermedad=0.01,
    p_positivo_dado_enfermedad=0.99,
    p_positivo_dado_no_enfermedad=0.05
)

#Ejemplo de salida:
# Cálculo de la probabilidad posterior:
# P(Enfermedad | Prueba positiva) = 0.1667
# P(Prueba positiva)              = 0.0594
#Aunque la prueba es positiva, la probabilidad real de tener la enfermedad es solo 16.67%, porque la enfermedad es rara (1%) y hay falsos positivos.
#esta es la esencia de la Regla de bayes, ajustar creencias con evidencia.