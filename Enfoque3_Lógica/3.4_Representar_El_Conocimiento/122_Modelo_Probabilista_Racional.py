#Modelo Probabilista Racional
#es un enfoque que combina la lógica y la teoría de la probabilidad para manejar la incertidumbre en la toma de decisiones.
#Este modelo se basa en la idea de que los agentes racionales toman decisiones que maximizan su utilidad esperada, considerando las probabilidades de diferentes eventos.
#Funcionamiento:
# Representación del Conocimiento: El conocimiento se representa utilizando reglas probabilísticas que describen las relaciones entre eventos y sus probabilidades.
# Cálculo de Probabilidades: Se utilizan técnicas de la teoría de la probabilidad para calcular las probabilidades de diferentes eventos.
# Toma de Decisiones: Las decisiones se toman maximizando la utilidad esperada, que es una función de las probabilidades de los eventos y sus consecuencias.
# Actualización de Creencias: Las creencias se actualizan utilizando el teorema de Bayes a medida que se obtiene nueva información.
#Aplicaciones: diagnostico medico, robotica, finanzas, sistemas de recomendación

# definir una clase para representar una regla probabilística con antecedente, consecuente y probabilidad
class ProbabilisticRule:
    def __init__(self, antecedent, consequent, probability):
        # inicializar el antecedente como el conjunto de condiciones necesarias
        self.antecedent = antecedent
        # inicializar el consecuente como el resultado esperado si se cumplen las condiciones
        self.consequent = consequent
        # establecer la probabilidad asociada a la regla
        self.probability = probability

    # aplicar la regla sobre un conjunto de hechos
    def apply(self, facts):
        # verificar si todos los elementos del antecedente están presentes en los hechos
        if all(fact in facts for fact in self.antecedent):
            # si el consecuente no está en los hechos, asignar la probabilidad directamente
            if self.consequent not in facts:
                facts[self.consequent] = self.probability
            else:
                # combinar probabilidades utilizando un promedio simple
                facts[self.consequent] = (facts[self.consequent] + self.probability) / 2
        # retornar el conjunto de hechos actualizado
        return facts

# definir una clase para representar un sistema experto probabilístico
class ProbabilisticExpertSystem:
    def __init__(self):
        # inicializar un diccionario para almacenar los hechos con su probabilidad
        self.facts = {}
        # inicializar una lista para almacenar las reglas del sistema experto
        self.rules = []

    # agregar una regla al sistema experto
    def add_rule(self, rule):
        self.rules.append(rule)

    # agregar un hecho al sistema experto con su probabilidad y activar el proceso de inferencia
    def add_fact(self, fact, probability):
        # añadir el hecho al conjunto de hechos conocidos con su probabilidad
        self.facts[fact] = probability
        # llamar al método de inferencia para derivar nuevos hechos basados en reglas
        self.infer()

    # aplicar todas las reglas sobre los hechos actuales
    def infer(self):
        # crear una copia del conjunto de hechos conocidos para aplicar reglas
        new_facts = self.facts.copy()
        # iterar sobre todas las reglas en el sistema experto
        for rule in self.rules:
            # aplicar cada regla sobre el conjunto de hechos actualizado
            new_facts = rule.apply(new_facts)
        # actualizar los hechos del sistema con los nuevos deducidos
        self.facts = new_facts

    # obtener el conjunto de hechos inferidos
    def get_facts(self):
        # retornar el conjunto de hechos actuales en el sistema
        return self.facts

# definir una función para imprimir los hechos con sus probabilidades
def print_facts(facts):
    print("Facts:")
    # iterar sobre los hechos e imprimir cada uno con su probabilidad formateada
    for fact, probability in facts.items():
        print(f"{fact}: {probability:.2f}")

# definir un conjunto de reglas probabilísticas
rules = [
    ProbabilisticRule({"síntoma_A"}, "enfermedad_X", 0.8), 
    ProbabilisticRule({"síntoma_B"}, "enfermedad_X", 0.6),
    ProbabilisticRule({"síntoma_C"}, "enfermedad_Y", 0.7),
    ProbabilisticRule({"enfermedad_X"}, "tratamiento_Z", 0.9)
]

# crear una instancia del sistema experto probabilístico
expert_system = ProbabilisticExpertSystem()

# añadir todas las reglas definidas al sistema experto
for rule in rules:
    expert_system.add_rule(rule)

# añadir hechos iniciales al sistema experto con sus respectivas probabilidades
expert_system.add_fact("síntoma_A", 1.0)  # registrar que el síntoma A está presente con probabilidad 1.0
expert_system.add_fact("síntoma_B", 0.9)  # registrar que el síntoma B está presente con probabilidad 0.9
expert_system.add_fact("síntoma_C", 0.8)  # registrar que el síntoma C está presente con probabilidad 0.8

# obtener el conjunto de hechos inferidos después de aplicar reglas
facts = expert_system.get_facts()

# imprimir los hechos inferidos por el sistema experto
print_facts(facts)

#Ejemplo de salida: 
# Facts:
# síntoma_A: 1.00
# enfermedad_X: 0.68
# tratamiento_Z: 0.90
# síntoma_B: 0.90
# síntoma_C: 0.80
# enfermedad_Y: 0.70

# El ejemplo de salida nos muestra los hechos inferidos por el sistema experto probabilístico
# después de aplicar las reglas definidas. Cada hecho está acompañado de su probabilidad
# actualizada, que refleja la certeza del sistema sobre la ocurrencia de ese hecho.
# 
# En este caso, se observa cómo los síntomas iniciales ("síntoma_A", "síntoma_B", "síntoma_C")
# llevan a la inferencia de enfermedades ("enfermedad_X", "enfermedad_Y") y un tratamiento
# ("tratamiento_Z") con probabilidades calculadas en función de las reglas y los hechos iniciales.