#Red Bayesiana 
#Es un modelo probabilistico grafico que representa un conjunto de variables aleatorias y sus relaciones condicionales mediante un grafo dirigido acíclico (DAG).
#se compone de nodos (variables aleatorias), aristas dirigidas (dependencias condicionales), tablas de probabilidad condicional (CPT, cada nodo tiene una tabla que describe la probabilidad condicional dado sus padres en el grado)
#Este permite la inferencia probabilistica eficiente (cuál es la probabilidad de X dado Y)
#Permiten aprender la estructura y los parámetros de los datos 
#se pueden usar para tomar decisiones bajo incertidumbre 
#se puede aplicar en el diagnostico médico, reconocimiento de patrones, prediccion y clasificación, inteligencia artificial, etc.

#Ejemplo de Red Bayesiana
#Problema de alarma de robo 
#si ocurre un robo o un terremoto, se activa la alarma.
#si la alarma suena, Pancho y Pancha pueden llamar 

#librerias necesarias 
from pgmpy.models import DiscreteBayesianNetwork # para crear la red bayesiana discreta 
from pgmpy.factors.discrete import TabularCPD #para crear las tablas de probabilidad condicional
from pgmpy.inference import VariableElimination #para hacer inferencia en la red bayesiana

#definir la estructura del grafo (las relaciones entre las variables)
modelo = DiscreteBayesianNetwork([
    ('Robo', 'Alarma'),
    ('Terremoto', 'Alarma'),
    ('Alarma', 'PanchoLlama'),
    ('Alarma', 'PanchaLlama')
])

#definir las tablas de probabilidad condicional (CPT)
#robo tiene probabilidad a priori (antes de ver la alarma)
cpd_robo = TabularCPD(variable='Robo', variable_card=2, values=[[0.99], [0.01]]) #probabilidad de que no ocurra el robo y de que ocurra el robo
#el terremoto es una variable independiente
cpd_terremoto = TabularCPD(variable='Terremoto', variable_card=2, values=[[0.998], [0.002]]) #probabilidad de que no ocurra el terremoto y de que ocurra el terremoto

#la alarma depende del robo y el terremoto (2 pdres -> 4 combinaciones)
cpd_alarma = TabularCPD( #probabilidad de que suene la alarma dado el robo y el terremoto
    variable='Alarma', variable_card=2, #probabilidad de que no suene la alarma y de que suene la alarma
    values=[ # probabilidad de que suene la alarma dado el robo y el terremoto
        [0.999, 0.71, 0.06, 0.05],  #P(Alarma=F) 
        [0.001, 0.29, 0.94, 0.95]   #P(Alarma=T)
    ],
    evidence=['Robo', 'Terremoto'], # padres de la alarma
    evidence_card=[2, 2] #cardinalidad de los padres (2 valores: True o False)
) 

#pancho llama solo si escucha la alarma
cpd_pancho = TabularCPD( #probabilidad de que pancho llame dado la alarma
    variable='PanchoLlama', variable_card=2, #probabilidad de que no llame y de que llame
    values=[[0.1, 0.05], [0.9, 0.95]], #probabilidad de que llame dado la alarma
    evidence=['Alarma'], #padre de pancho
    evidence_card=[2] #cardinalidad del padre (2 valores: True o False)
)

#pancha llama solo si escucha la alarma
cpd_pancha = TabularCPD( #probabilidad de que pancha llame dado la alarma
    variable='PanchaLlama', variable_card=2,  #probabilidad de que no llame y de que llame
    values=[[0.3, 0.01], [0.7, 0.99]], #probabilidad de que llame dado la alarma
    evidence=['Alarma'], #padre de pancha
    evidence_card=[2] #cardinalidad del padre (2 valores: True o False)
)

#asociacion de las tablas de probabilidad condicional al modelo
modelo.add_cpds(cpd_robo, cpd_terremoto, cpd_alarma, cpd_pancho, cpd_pancha) # agregamos las tablas al modelo

#verificar la valizez del modelo
print("¿El modelo es válido?", modelo.check_model())

#hacer inferencias con eliminacion de variables
inferencia = VariableElimination(modelo) 

#ejemplo: ¿cuál es la probabilidad de que hay habido un robo si Pancho y Pancha llamaron?
resultado = inferencia.query(variables=['Robo'], evidence={'PanchoLlama': 1, 'PanchaLlama': 1}) #
print("\nProbabilidad de que haya habido un robo dado que ambos llamaron:") 
print(resultado)

#Ejemplo de salida: 
# ¿El modelo es válido? True

# Probabilidad de que haya habido un robo dado que ambos llamaron:
# +---------+-------------+
# | Robo    |   phi(Robo) |
# +=========+=============+
# | Robo(0) |      0.9854 |
# +---------+-------------+
# | Robo(1) |      0.0146 |
# +---------+-------------+
#Probabilidad de que haya habido un robo dado que ambos llamaron: 0.0146
#Probabilidad de que haya habido un robo dado que ambos llamaron: 0.9854
#esto significa que la probabilidad de que haya habido un robo dado que ambos llamaron es muy baja (0.0146) y la probabilidad de que no haya habido un robo dado que ambos llamaron es muy alta (0.9854)
#esto se debe a que la alarma suena con alta probabilidad si hay un robo o un terremoto

