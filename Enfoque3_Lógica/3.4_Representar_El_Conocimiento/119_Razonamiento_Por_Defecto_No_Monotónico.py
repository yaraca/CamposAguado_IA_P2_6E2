#Razonamiento por Defecto y No Monotónico
#Es un tipo de razonamiento que permite asumir cosas por defecto, es decir, en ausencia de información que diga lo contrario.
# Es no monotónico porque nuevas evidencias pueden invalidar inferencias previas.
# Características:
# A diferencia del razonamiento lógico clásico (monotónico), en el no monotónico las conclusiones pueden cambiar cuando se agregan nuevos hechos.
# Se utiliza en IA para modelar el sentido común y tomar decisiones en situaciones incompletas o inciertas.
#Aplicaciones: sistemas expertos, diagnostico medico, agentes inteligentes, etc.

#Ejemplo de razonamiento por defecto 
#un sistema de razonamiento por defecto sobre animales que vuelan, con excepciones como los pingüinos.

#Definir una clase para manejar hechos y reglas por defecto
class RazonamientoDefecto:
    def __init__(self):
        #Inicializar un diccionario para almacenar los hechos conocidos
        self.hechos = {}  #Diccionario de hechos: {animal: tipo}
        #Inicializar un conjunto para registrar excepciones a la regla general
        self.excepciones = set()  #Animales que no cumplen la regla por defecto

    #Agregar un hecho al diccionario de hechos
    def agregar_hecho(self, animal, tipo):
        self.hechos[animal] = tipo

    #Registrar una excepción en el conjunto de excepciones
    def agregar_excepcion(self, animal):
        self.excepciones.add(animal)

    #Determinar si un animal puede volar según los hechos y excepciones
    def puede_volar(self, animal):
        #Verificar si el animal está en el conjunto de excepciones, en cuyo caso no vuela
        if animal in self.excepciones:
            return False
        #Verificar si el animal es un pájaro y no está en excepciones, en cuyo caso se asume que vuela
        if self.hechos.get(animal) == "pajaro":
            return True
        #Si el animal no es un pájaro, devolver False
        return False

#Crear una instancia del sistema de razonamiento
sistema = RazonamientoDefecto()

#Agregar animales al sistema con sus respectivos tipos
sistema.agregar_hecho("canario", "pajaro")
sistema.agregar_hecho("aguila", "pajaro")
sistema.agregar_hecho("pingüino", "pajaro")
sistema.agregar_hecho("murcielago", "mamifero")

#Agregar una excepción: el pingüino no vuela
sistema.agregar_excepcion("pingüino")

#Definir una lista de animales para probar inferencias
animales = ["canario", "aguila", "pingüino", "murcielago"]

#Iterar sobre la lista de animales y determinar si pueden volar
for animal in animales:
    resultado = sistema.puede_volar(animal)
    print(f"{animal.capitalize()} puede volar: {resultado}")

#Ejemplo de salida:
# Canario puede volar: True
# Aguila puede volar: True
# Pingüino puede volar: False
# Murcielago puede volar: False

# Este ejemplo de salida demuestra cómo funciona el razonamiento por defecto y no monotónico.
# En este caso, se asume que los pájaros pueden volar por defecto, a menos que haya una excepción explícita.
# Por ejemplo:
# - El canario y el águila son pájaros y no están en la lista de excepciones, por lo que se concluye que pueden volar.
# - El pingüino, aunque es un pájaro, está registrado como una excepción, por lo que no puede volar.
# - El murciélago no es un pájaro, por lo que no se aplica la regla por defecto y se concluye que no puede volar.
# Esto ilustra cómo el razonamiento no monotónico permite manejar excepciones y ajustar conclusiones
# en función de nueva información o reglas específicas.
