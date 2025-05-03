#Lógica Modal
#es una extensión de la lógica proposicional clásica que introduce modalidades como:
# Necesidad (□): “Es necesario que...”
# Posibilidad (◇): “Es posible que...”
#Por ejemplo: □P → “Siempre es cierto que P” (necesariamente P).
#             ◇P → “Puede ser cierto que P” (posiblemente P).
#Funcionamiento: La lógica modal trabaja sobre mundos posibles (semántica de Kripke), donde:
# Cada mundo tiene un conjunto de proposiciones verdaderas.
# Las relaciones entre mundos (accesibilidad) indican qué mundos son posibles desde otros.
#Aplicaciones: inteligencia artificial, filosofía, lingüística, teoría de juegos, etc.

#Ejemplo de logica modal:
#Simular agentes que creen en proposiciones dependiendo de los mundos posibles.

#Definir una clase para representar los mundos posibles
class Mundo:
    #Funcion para inicializar el mundo
    def __init__(self, nombre, proposiciones):
        self.nombre = nombre                      #Nombre del mundo
        self.proposiciones = set(proposiciones)   #Proposiciones verdaderas en ese mundo
        self.accesibles = []                      #Otros mundos posibles desde este

    #Funcion para agregar mundos accesibles
    def agregar_mundo_accesible(self, mundo):
        self.accesibles.append(mundo)             #Agregar mundo accesible

    #Función para evaluar si una proposición es necesaria 
    def es_necesario(self, proposicion):
        #La proposición debe ser verdadera en todos los mundos accesibles
        return all(proposicion in mundo.proposiciones for mundo in self.accesibles)  # Retorna True si la proposición es verdadera en todos los mundos accesibles

    #Función para evaluar si una proposición es posible
    def es_posible(self, proposicion):
        # La proposición debe ser verdadera en al menos un mundo accesible
        return any(proposicion in mundo.proposiciones for mundo in self.accesibles) # Retorna True si la proposición es verdadera en al menos un mundo accesible

#definir los mundos y qué proposiciones son verdaderas en cada uno
mundos = {
    "A": {"P"},            # En A, solo P es verdadera
    "B": {"P", "Q"},       # En B, P y Q son verdaderas
    "C": {"Q"}             # En C, solo Q es verdadera
}

#Relación de accesibilidad: desde A se puede ir a B y C
relaciones = {
    "A": ["B", "C"], #Desde A se puede acceder a B y C
    "B": [],        #Desde B no se puede acceder a ningún otro mundo
    "C": []       #Desde C no se puede acceder a ningún otro mundo
}

#Funciones para evaluar □P (necesariamente P) desde un mundo origen
def necesario(mundo_origen, proposicion):
    accesibles = relaciones[mundo_origen] #obtener mundos accesibles desde el mundo origen
    #Si no hay mundos accesibles, se considera vacuamente verdadero
    if not accesibles: 
        return True 
    return all(proposicion in mundos[m] for m in accesibles) #Retorna True si la proposición es verdadera en todos los mundos accesibles

#función para evaluar ◇P (posiblemente P) desde un mundo origen
def posible(mundo_origen, proposicion):
    accesibles = relaciones[mundo_origen] #obtener mundos accesibles desde el mundo origen
    return any(proposicion in mundos[m] for m in accesibles) #Retorna True si la proposición es verdadera en al menos un mundo accesible

#evaluar desde el mundo A
print("Desde el mundo A:")
print("¿Es necesario que P sea verdadera (□P)?", necesario("A", "P")) 
print("¿Es posible que Q sea verdadera (◇Q)?", posible("A", "Q")) 
print("¿Es necesario que Q sea verdadera (□Q)?", necesario("A", "Q")) 

#Ejemplo de salida: 
# Desde el mundo A:
# ¿Es necesario que P sea verdadera (□P)? False
# ¿Es posible que Q sea verdadera (◇Q)? True
# ¿Es necesario que Q sea verdadera (□Q)? True
#Como se puede ver, la lógica modal permite razonar sobre la necesidad y posibilidad de proposiciones en diferentes mundos posibles.
#en este caso, la proposición P es necesaria en el mundo A, pero Q no lo es. Sin embargo, Q es posible en el mundo A porque hay un mundo accesible (B) donde Q es verdadera.
#Esto ilustra cómo la lógica modal puede ser utilizada para razonar sobre la verdad de proposiciones en diferentes contextos o mundos posibles.