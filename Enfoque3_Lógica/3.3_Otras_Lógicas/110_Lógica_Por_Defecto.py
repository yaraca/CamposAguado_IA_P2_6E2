#Lógica por Defecto
#es un tipo de lógica no monotónica desarrollada por Raymond Reiter. 
#Permite razonar con supuestos por defecto, es decir, asumir ciertas cosas a falta de evidencia en contra.
#Se usa cuando: 
#El conocimiento es incompleto.
# Se desea hacer inferencias mientras se acepta que pueden tener excepciones.
#Ejemplo: (Regla por defecto) Si X es un pájaro : y no se sabe que no vuela => entonces X vuela
#(formato de la regla) Condición : Justificación / Conclusión
#(Ejemplo de la regla) pajaro(x) : puede_volar(x) / vuela(x)
#Aplicaciones: sistemas expertos, inteligencia artificial, razonamiento automático, etc. 

#Ejemplo de logica por defecto
#Pajaros y su capacidad de volar

#Clase de Base de Conocimiento
class BaseConocimiento:
    #Funcion para inicializar la base de conocimiento
    def __init__(self):
        self.hechos = set() #conjunto de hechos conocidos
        self.conocido_que_no_vuela = set() #conjunto de excepciones (animales que no vuelan)

    #Funcion para agregar hechos a la base de conocimiento
    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    #Funcion para agregar excepciones a la base de conocimiento
    def agregar_excepcion(self, animal):
        self.conocido_que_no_vuela.add(animal)

    #Funcion para aplicar la regla por defecto
    def aplicar_regla_por_defecto(self):
        resultados = {} #diccionario para almacenar los resultados
        for hecho in self.hechos: #iterar sobre los hechos conocidos
            if hecho.startswith("pajaro_"): #verificar si el hecho es un pájaro
                animal = hecho.replace("pajaro_", "") #extraer el nombre del animal
                if animal not in self.conocido_que_no_vuela: #verificar si no es una excepción
                    resultados[animal] = True  #si no es una excepción, asumimos que vuela
                else: #si es una excepción, asumimos que no vuela
                    resultados[animal] = False  #se asume que no vuela
        return resultados #devolver los resultados

#Crear la base de conocimiento
bc = BaseConocimiento()

# Agregar pájaros
bc.agregar_hecho("pajaro_tweety") #pajaro tweety
bc.agregar_hecho("pajaro_penguin") #pinguino
bc.agregar_hecho("pajaro_flappy") #pajaro flappy

#Excepción: se sabe que penguin no vuela
bc.agregar_excepcion("penguin")

#Aplicar regla por defecto
resultados = bc.aplicar_regla_por_defecto()

#Mostrar resultados
for animal, vuela in resultados.items(): ##iterar sobre los resultados
    print(f"¿{animal.capitalize()} vuela? {'Sí' if vuela else 'No'}") #imprime si vuela o no

#Ejemplo de salida:
# ¿Flappy vuela? Sí
# ¿Penguin vuela? No
# ¿Tweety vuela? Sí
#como se puede ver, el sistema asume que los pájaros que no son excepciones vuelan,
#mientras que los que son excepciones no vuelan. 
#esto demuestra cómo la lógica por defecto permite razonar con suposiciones y excepciones.