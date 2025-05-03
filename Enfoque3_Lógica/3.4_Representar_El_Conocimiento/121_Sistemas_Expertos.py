#Sistemas Expertos
#es un programa de inteligencia artificial diseñado para emular la toma de decisiones de un experto humano.
# Estos sistemas utilizan una base de conocimientos y un motor de inferencia para resolver problemas complejos que normalmente requerirían la intervención de un experto humano.
#Componentes: 
# Base de Conocimientos: Contiene el conocimiento específico del dominio, representado en forma de reglas, hechos y relaciones.
# Motor de Inferencia: Utiliza la base de conocimientos para realizar inferencias y tomar decisiones.
# Interfaz de Usuario: Permite a los usuarios interactuar con el sistema, proporcionando entradas y recibiendo salidas.
# Módulo de Explicación: Proporciona explicaciones sobre cómo se llegó a una conclusión particular.
# Módulo de Adquisición de Conocimiento: Permite la actualización y expansión de la base de conocimientos.
#FUncionamiento: 
# Adquisición de Conocimiento: El conocimiento se adquiere de expertos humanos y se almacena en la base de conocimientos.
# Representación del Conocimiento: El conocimiento se representa en forma de reglas, hechos y relaciones.
# Inferencia: El motor de inferencia utiliza la base de conocimientos para realizar inferencias y tomar decisiones.
# Interacción con el Usuario: El usuario proporciona entradas y recibe salidas a través de la interfaz de usuario.
# Explicación: El módulo de explicación proporciona detalles sobre cómo se llegó a una conclusión particular.
#Aplicaciones: diagnostico médico, soporte tecnico, finanzas ingenieria,e tc. 

#Ejemplo de sistemas expertos

#Definir una clase para representar una regla con antecedente y consecuente
class Rule:
    def __init__(self, antecedent, consequent):
        #Inicializar el antecedente de la regla como un conjunto de condiciones necesarias
        self.antecedent = antecedent
        #Inicializar el consecuente de la regla como el resultado esperado si se cumplen las condiciones
        self.consequent = consequent

    #Definir un método para aplicar la regla sobre un conjunto de hechos
    def apply(self, facts):
        #Verificar si todos los hechos necesarios están en el conjunto de hechos conocidos
        if all(fact in facts for fact in self.antecedent):
            #Si la condición se cumple, agregar el consecuente a los hechos conocidos
            facts.add(self.consequent)
        #Retornar el conjunto de hechos actualizado
        return facts

#Definir una clase para representar un sistema experto
class ExpertSystem:
    def __init__(self):
        #Inicializar un conjunto para almacenar los hechos conocidos
        self.facts = set()
        #Inicializar una lista para almacenar las reglas del sistema experto
        self.rules = []

    #Definir un método para agregar reglas al sistema experto
    def add_rule(self, rule):
        #Añadir la regla a la lista de reglas del sistema
        self.rules.append(rule)

    #Definir un método para agregar hechos al sistema y activar el proceso de inferencia
    def add_fact(self, fact):
        #Añadir el nuevo hecho al conjunto de hechos conocidos
        self.facts.add(fact)
        #Llamar al método de inferencia para derivar nuevos hechos basados en reglas
        self.infer()

    #Definir un método para inferir nuevos hechos aplicando reglas existentes
    def infer(self):
        #Crear un conjunto de hechos actualizados para aplicar reglas
        new_facts = set(self.facts)
        #Iterar sobre todas las reglas en el sistema experto
        for rule in self.rules:
            #Aplicar cada regla sobre el conjunto de hechos actualizado
            new_facts = rule.apply(new_facts)
        #Actualizar los hechos del sistema con los nuevos deducidos
        self.facts = new_facts

    #Definir un método para obtener el conjunto de hechos inferidos
    def get_facts(self):
        #Retornar el conjunto de hechos actuales en el sistema
        return self.facts

#Definir un conjunto de reglas para diagnosticar problemas mecánicos
rules = [
    #Si el motor no arranca y la batería está descargada, el sistema recomienda reemplazar la batería
    Rule({"motor_no_arranca", "bateria_descargada"}, "reemplazar_bateria"),
    #Si el motor no arranca y hay poco combustible, el sistema recomienda llenar el tanque
    Rule({"motor_no_arranca", "combustible_insuficiente"}, "llenar_tanque"),
    #Si hay un ruido extraño y fuga de aceite, el sistema recomienda revisar el motor
    Rule({"ruido_extraño", "fuga_de_aceite"}, "revisar_motor"),
    #Si los frenos no funcionan y el nivel de líquido de frenos es bajo, el sistema recomienda revisar el sistema de frenos
    Rule({"frenos_no_funcionan", "nivel_de_liquido_de_frenos_bajo"}, "revisar_sistema_de_frenos")
]

#Crear una instancia del sistema experto
expert_system = ExpertSystem()

#Añadir todas las reglas definidas al sistema experto
for rule in rules:
    expert_system.add_rule(rule)

#Añadir hechos iniciales al sistema experto
expert_system.add_fact("motor_no_arranca")  #Registrar que el motor no arranca
expert_system.add_fact("bateria_descargada")  #Registrar que la batería está descargada

#Obtener el conjunto de hechos inferidos después de aplicar reglas
facts = expert_system.get_facts()

#Imprimir los hechos inferidos por el sistema experto
print("Hechos inferidos:")
#Iterar sobre cada hecho en el conjunto de hechos inferidos y mostrarlo en pantalla
for fact in facts:
    print(fact)

#Ejemplo de salida:
# Hechos inferidos:
# reemplazar_bateria
# bateria_descargada
# motor_no_arranca

#Esta salida muestra los hechos inferidos después de aplicar las reglas. 
# En este caso, el sistema experto ha inferido que se debe "reemplazar_bateria" 
# basado en los hechos iniciales "motor_no_arranca" y "bateria_descargada".