#Incertidumbre y Factores de Certeza
#Estos conceptos se utilizan para manejar la imprecisión y la falta de certeza en el conocimiento y las inferencias.
#La incertidumbre se refiere a la falta de certeza o precisión en el conocimiento.
#En muchos casos, la información disponible puede ser incompleta, ambigua o contradictoria
#Los factores de certeza son valores que cuantifican el grado de confianza en una afirmación o regla
#Estos valores pueden ser utilizados para ponderar la importancia de diferentes piezas de información en el proceso de toma de decisiones.
#Funcionamiento. 
# Representación del Conocimiento: El conocimiento se representa utilizando reglas o afirmaciones que incluyen factores de certeza.
# Propagación de la Incertidumbre: Durante el proceso de inferencia, la incertidumbre se propaga a través de las reglas y afirmaciones.
# Combinación de Factores de Certeza: Cuando se combinan múltiples fuentes de información, los factores de certeza se combinan utilizando reglas matemáticas específicas.
# Toma de Decisiones: Las decisiones se toman en función de los factores de certeza combinados, permitiendo manejar la incertidumbre de manera efectiva.
#Aplicaciones: sistemas expertos, diagnostico médico, sistemas de recomendación,etc. 

#Ejemplo de Manejo de Incertidumbre y Factores de Certeza


#Definir una clase para representar una regla con antecedente, consecuente y factor de certeza
class Rule:
    def __init__(self, antecedent, consequent, certainty_factor):
        #Inicializar los atributos de la regla
        self.antecedent = antecedent #antecedente
        self.consequent = consequent #conseciencia
        self.certainty_factor = certainty_factor #factor de certeza

    #Aplicar la regla sobre un conjunto de hechos
    def apply(self, facts):
        #Verificar si el antecedente está presente en los hechos
        if self.antecedent in facts:
            #Si el consecuente no está en los hechos, asignar el factor de certeza directamente
            if self.consequent not in facts:
                facts[self.consequent] = self.certainty_factor
            else:
                #Combinar factores de certeza utilizando un promedio simple
                facts[self.consequent] = (facts[self.consequent] + self.certainty_factor) / 2
        return facts

#Definir una función para imprimir los hechos almacenados con su factor de certeza
def print_facts(facts):
    print("Facts:")
    #Iterar sobre los hechos e imprimir cada uno con su factor de certeza formateado
    for fact, certainty in facts.items():
        print(f"{fact}: {certainty:.2f}")

#Definir un conjunto de reglas con factores de certeza
rules = [
    Rule("síntoma_A", "enfermedad_X", 0.8),
    Rule("síntoma_B", "enfermedad_X", 0.6),
    Rule("síntoma_C", "enfermedad_Y", 0.7),
    Rule("enfermedad_X", "tratamiento_Z", 0.9)
]

#Definir los hechos iniciales con sus respectivos factores de certeza
facts = {
    "síntoma_A": 1.0,
    "síntoma_B": 0.9,
    "síntoma_C": 0.8
}

#Aplicar cada regla sobre el conjunto de hechos inicial
for rule in rules:
    facts = rule.apply(facts)

#Imprimir los hechos resultantes después de aplicar las reglas
print_facts(facts)

#Ejemplo de salida: 
# Facts:
# síntoma_A: 1.00
# síntoma_B: 0.90
# síntoma_C: 0.80
# enfermedad_X: 0.70
# enfermedad_Y: 0.70
# tratamiento_Z: 0.90

# El ejemplo de salida muestra los hechos finales después de aplicar las reglas definidas.
# Cada hecho está acompañado por su factor de certeza actualizado, que refleja cómo las reglas
# han propagado y combinado la incertidumbre a través del sistema.