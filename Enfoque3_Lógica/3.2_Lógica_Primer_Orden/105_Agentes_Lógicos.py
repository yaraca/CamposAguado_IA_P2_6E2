#Agentes lógicos 
#es un sistema que toma decisiones y realiza acciones basadas en un razonamiento lógico
#Utiliza una base de conocimiento para almacenar hechos y reglas, y un motor de inferencia para deducir nueva información.
#Componentes clave: 
# Base de conocimiento (KB): Hechos y reglas en lógica de primer orden.
# Motor de inferencia: Realiza inferencias lógicas (como resolución o encadenamiento).
# Percepción: Información que recibe del entorno.
# Función de decisión: Selecciona acciones basadas en lo que "sabe".
#Funcionamiento: 
# El agente observa el entorno (percepción).
# Agrega hechos nuevos a la base de conocimiento.
# Usa inferencias para deducir conocimiento adicional.
# Decide una acción en base a su razonamiento lógico.
#Aplicaciones: robótica, sistemas expertos, diagnóstico médico, etc.

#Ejemplo de un agente lógico simple 
#un agente quiere saber si debe salir a la calle. Su decisión se basa en si está lloviendo y si tiene paraguas.

#Clase de Agente Lógico
class AgenteLogico:
    #Función de inicialización
    def __init__(self):
        # Base de conocimiento: hechos iniciales
        self.base_conocimiento = set()

    #Función para agregar hechos a la base de conocimiento
    def decir(self, hecho):
        self.base_conocimiento.add(hecho) # Agrega el hecho a la base de conocimiento
        print(f"[KB] Añadido: {hecho}") # Imprime el hecho añadido

    #Función para verificar si el agente conoce un hecho
    def sabe(self, hecho):
        return hecho in self.base_conocimiento # Devuelve True si el hecho está en la base de conocimiento

    #Función para inferir nuevos hechos basados en reglas lógicas
    def inferir(self):
        #Aplica reglas lógicas simples para inferir nuevos hechos
        if 'llueve' in self.base_conocimiento and 'tiene_paraguas' in self.base_conocimiento: #si llueve y tiene paraguas
            self.base_conocimiento.add('puede_salir') # Agrega el hecho de que puede salir
            print("[Inferencia] Si llueve y tiene paraguas → puede salir")  
        elif 'llueve' in self.base_conocimiento and 'tiene_paraguas' not in self.base_conocimiento: #si llueve y no tiene paraguas
            self.base_conocimiento.add('no_puede_salir') # Agrega el hecho de que no puede salir
            print("[Inferencia] Si llueve y no tiene paraguas → no puede salir")
        elif 'no_llueve' in self.base_conocimiento: #si no llueve
            self.base_conocimiento.add('puede_salir') # Agrega el hecho de que puede salir
            print("[Inferencia] Si no llueve → puede salir")

    #Función para decidir la acción del agente
    def decidir_accion(self):
        if 'puede_salir' in self.base_conocimiento: #si puede salir
            return "El agente decide salir." # Devuelve la acción de salir
        elif 'no_puede_salir' in self.base_conocimiento: #si no puede salir
            return "El agente decide quedarse en casa." # Devuelve la acción de quedarse en casa
        else: #si no tiene suficiente información
            return "El agente no tiene suficiente información para decidir." # Devuelve que no tiene suficiente información


#Ejemplos de uso del agente lógico
print("== Escenario 1: Llueve y tiene paraguas ==")
agente = AgenteLogico()
agente.decir('llueve')
agente.decir('tiene_paraguas')
agente.inferir()
print(agente.decidir_accion())

print("\n== Escenario 2: Llueve y no tiene paraguas ==")
agente2 = AgenteLogico()
agente2.decir('llueve')
agente2.inferir()
print(agente2.decidir_accion())

print("\n== Escenario 3: No llueve ==")
agente3 = AgenteLogico()
agente3.decir('no_llueve')
agente3.inferir()
print(agente3.decidir_accion())

#Ejemplo de salida: 
# == Escenario 1: Llueve y tiene paraguas ==
# [KB] Añadido: llueve
# [KB] Añadido: tiene_paraguas
# [Inferencia] Si llueve y tiene paraguas → puede salir
# El agente decide salir.

# == Escenario 2: Llueve y no tiene paraguas ==
# [KB] Añadido: llueve
# [Inferencia] Si llueve y no tiene paraguas → no puede salir
# El agente decide quedarse en casa.

# == Escenario 3: No llueve ==
# [KB] Añadido: no_llueve
# [Inferencia] Si no llueve → puede salir
# El agente decide salir.

#Como se puede ver, el agente lógico toma decisiones basadas en la información que tiene y las reglas lógicas que aplica.
#En los ejemplos, el agente evalúa si puede salir o no, dependiendo de si está lloviendo y si tiene un paraguas.

