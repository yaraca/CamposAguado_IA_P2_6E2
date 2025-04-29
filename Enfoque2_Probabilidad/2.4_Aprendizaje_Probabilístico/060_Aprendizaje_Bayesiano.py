#Aprendizaje Bayesiano
# es un método de inferencia estadística donde actualizamos nuestras creencias sobre un modelo o hipótesis cada vez que obtenemos nueva información o datos.
#Se basa en el Teorema de Bayes, que permite calcular una distribución posterior combinando la información a priori con la evidencia nueva.
#El teorema de bayes es: P(θ|D) = P(D|θ) * P(θ) / P(D)
#Donde: θ= parametro o hipotesis, D= datos observados
#P(θ)=Distribucion a priori (creencias iniciales sobre θ)
#P(D|θ)=Verosimilitud (probabilidad de observar D dado θ)
#P(θ|D)=Distribucion a posteriori (creencias actualizadas sobre θ)
#P(D)=Evidencia (constante de normalizacion)
#Funcionamiento: Definir un prior(creencias inciales), observar datos(recopilar nueva información), Actualizar (aplicar teorema de bayes para obtener el posterior), iterar (continuar el proceso a medida que se obtienen más datos)
#Se puede aplicar en: sistemas de diagnostico médico, sistemas de recomendación, análisis de sentimientos, detección de fraudes, etc.

#Ejemplo de aprendizaje bayesiano
#aprender la probabilidad de éxito de un experimento (ej. lanzar una moneda)

#librerias necesarias
import numpy as np #para operaciones matematicas y matrices
import matplotlib.pyplot as plt #para graficar

#Definir un prior: distribución beta
#Beta(α, β) es la distribución conjugada para problemas Bernoulli (éxito/fracaso)
#Inicialmente se cree que es una moneda justa => α=1, β=1 (distribución uniforme)
alpha_prior = 1
beta_prior = 1

#Datos observados: 1 para exito->cara, 0 para fracaso->cruz
datos = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1]  #7 caras, 3 cruces

#Contar éxitos y fracasos
exitos = sum(datos) #suma de 1s (caras)
fracasos = len(datos) - exitos #total de lanzamientos - éxitos (caras)

#Actualizar el prior con los datos observados
#Fórmulas de actualización para la distribución Beta:
#α_posterior = α_prior + éxitos
#β_posterior = β_prior + fracasos
alpha_posterior = alpha_prior + exitos #suma de éxitos (caras)
beta_posterior = beta_prior + fracasos #suma de fracasos (cruces)

print(f"Prior Beta: α={alpha_prior}, β={beta_prior}") #imprimir el prior
print(f"Posterior Beta: α={alpha_posterior}, β={beta_posterior}") #imprimir el posterior

#Graficar el prior y posterior
x = np.linspace(0, 1, 100) #valores de 0 a 1 para la probabilidad de éxito (cara)

# Distribuciones
from scipy.stats import beta # importar beta de scipy.stats para calcular la distribución beta
prior_distribution = beta(alpha_prior, beta_prior) #distribución beta con parámetros α y β
posterior_distribution = beta(alpha_posterior, beta_posterior) #distribución beta posterior con parámetros α y β

plt.plot(x, prior_distribution.pdf(x), label="Prior", linestyle='--') #pdf=funcion de densidad de probabilidad
plt.plot(x, posterior_distribution.pdf(x), label="Posterior", color='red')  #pdf=funcion de densidad de probabilidad
plt.title('Aprendizaje Bayesiano de una moneda')
plt.xlabel('Probabilidad de éxito (cara)')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)
plt.show()

#ejemplo de salida
# Prior Beta: α=1, β=1
# Posterior Beta: α=8, β=4
#Al principio, creíamos que cualquier probabilidad era igual de probable (uniforme).
#Después de ver 7 éxitos y 3 fracasos, la distribución posterior se desplaza hacia 0.7, indicando que creemos más en una probabilidad alta de éxito.
#En la grafica La línea roja (posterior) estará concentrada alrededor de 0.7, lo que indica que después de observar los datos, nuestra creencia sobre la probabilidad de éxito ha cambiado.
#Y la línea punteada (prior) será plana (sin preferencia).

