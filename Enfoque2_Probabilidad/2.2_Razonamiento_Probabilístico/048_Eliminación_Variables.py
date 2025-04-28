#Eliminación de Variables
#es un algoritmo usado para realizar inferencia exacta en una Red Bayesiana.
#Su objetivo es calcular una pbabilidad condicional como:  P(Query | Evidencia)
#…sin evaluar toda la distribución conjunta completa, lo que ahorra mucho cálculo.
#Se identifican: Variables objetivo (query), Variables evidentes (observaciones conocidas), Variables ocultas (a eliminar)
#Se multiplican los factores (tablas de probabilidad condicional) relevantes.
#Se eliminan variables ocultas (suman sus valores en las tablas).
#por último, se normaliza el resultado para obtener la probabilidad condicional deseada.
#se usa en sistemas expertos, diagnóstico médico, análisis de datos y toma de decisiones.

#Ejemplo de Eliminación de Variables
#Red bayesiana: Burglary (allanamiento), Earthquake, Alarm, JohnCalls, MaryCalls
# Burglary->Alarm<-Earthquake, Alarm->JohnCalls, Alarm->MaryCalls
#En este ejemplo, se quiere calcular la probabilidad de que haya un allanamiento dado que Mary o John han llamado.

#librerias necesarias
from pgmpy.models import DiscreteBayesianNetwork #para crear la red bayesiana
from pgmpy.factors.discrete import TabularCPD #para crear las tablas de probabilidad condicional
from pgmpy.inference import VariableElimination #para realizar la inferencia

#definir la estructura de la red
modelo = DiscreteBayesianNetwork([
    ('Burglary', 'Alarm'), # Burglary -> Alarm
    ('Earthquake', 'Alarm'), # Earthquake -> Alarm
    ('Alarm', 'JohnCalls'), # Alarm -> JohnCalls
    ('Alarm', 'MaryCalls') # Alarm -> MaryCalls
])

#Definir las CPDs (tablas de probabilidad condicional)

#Robo: 0.001 de probabilidad de ocurrir
cpd_burglary = TabularCPD(variable='Burglary', variable_card=2, # 2 estados: True/False
                          values=[[0.999], [0.001]]) # 0.999 de probabilidad de no ocurrir, 0.001 de ocurrir

#Terremoto: 0.002 de probabilidad
cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2, # 2 estados: True/False
                            values=[[0.998], [0.002]]) # 0.998 de probabilidad de no ocurrir, 0.002 de ocurrir

#Alarma: depende de Robo y Terremoto
cpd_alarm = TabularCPD(variable='Alarm', variable_card=2, # 2 estados: True/False
                       values=[
                           # Alarm=False
                           [0.999, 0.71, 0.06, 0.05], #probabilidad de que no suene la alarma
                           # Alarm=True
                           [0.001, 0.29, 0.94, 0.95] #probabilidad de que suene la alarma
                       ],
                       evidence=['Burglary', 'Earthquake'], # depende de Burglary y Earthquake
                       evidence_card=[2, 2]) # 2 estados: True/False

#John llama si suena la alarma
cpd_john = TabularCPD(variable='JohnCalls', variable_card=2, # 2 estados: True/False
                      values=[
                          [0.95, 0.1],   #probabilidad John no llama
                          [0.05, 0.9]    #probabilidad John llama
                      ],
                      evidence=['Alarm'], evidence_card=[2]) # depende de Alarm

# Mary llama si suena la alarma
cpd_mary = TabularCPD(variable='MaryCalls', variable_card=2, # 2 estados: True/False
                      values=[
                          [0.99, 0.3], #probabilidad Mary no llama
                          [0.01, 0.7]   #probabilidad Mary llama
                      ],
                      evidence=['Alarm'], evidence_card=[2]) # depende de Alarm

#añadir las CPDs al modelo
modelo.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_john, cpd_mary) 

#verificar consistencia
assert modelo.check_model(), "¡La red bayesiana no es válida!" #verifica que el modelo es consistente

#Usar Eliminación de Variables
inferencia = VariableElimination(modelo) #inicializa el objeto de inferencia

#pregunta: ¿Cuál es la probabilidad de que haya un robo dado que John y Mary llamaron?
resultado = inferencia.query(variables=['Burglary'], #variables objetivo
                             evidence={'JohnCalls': 1, 'MaryCalls': 1}) #evidencia: John y Mary llamaron

#Mostrar resultados
print("P(Robo | John=True, Mary=True):") #imprime la pregunta
print(resultado) #imprime el resultado

#Ejemplo de salida:
# P(Robo | John=True, Mary=True):
# +-------------+-----------------+
# | Burglary    |   phi(Burglary) |
# +=============+=================+
# | Burglary(0) |          0.7158 |
# +-------------+-----------------+
# | Burglary(1) |          0.2842 |
# +-------------+-----------------+
#Esto significa que, dado que John y Mary llamaron, hay una probabilidad de 28.4% de que haya habido un robo, y 71.6% de que no lo hubo.
