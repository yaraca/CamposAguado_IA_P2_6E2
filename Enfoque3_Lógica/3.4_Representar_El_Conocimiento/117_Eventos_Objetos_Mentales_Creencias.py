#Eventos y Objetos Mentales: Creencias
#son representaciones mentales que un agente (persona, robot, software) tiene sobre el mundo, que pueden ser verdaderas o falsas.
#En inteligencia artificial y lógica, las creencias forman parte de los sistemas cognitivos que toman decisiones, planean acciones o razonan sobre el entorno.
#En lógica modal, las creencias se representan como: B(a, φ) → "El agente a cree que φ es verdadero".
#Se pueden usar para modelar:
# Estados mentales de un agente.
# Cambio de creencias con nueva información.
# Razonamiento con conocimiento incompleto.

#Ejemplo de creencias: 
#modelar un agente que tiene ciertas creencias y puede actualizarlas con nueva información.

#Clase Agente 
class Agente:
    #función de inicialización
    def __init__(self, nombre):
        self.nombre = nombre  # Asignar el nombre del agente
        self.creencias = set()  #usarun conjunto para evitar duplicados

    #función agregar creencias
    #Agrega una nueva creencia al agente.
    def agregar_creencia(self, creencia):
        # Mostrar un mensaje indicando que se ha agregado una nueva creencia
        print(f" {self.nombre} ahora cree que: '{creencia}'")
        self.creencias.add(creencia)

    #función eliminar creencia
    #Elimina una creencia si el agente ya no la considera válida
    def eliminar_creencia(self, creencia):
        # Si la creencia está en el conjunto de creencias, eliminarla
            print(f" {self.nombre} ya no cree que: '{creencia}'")
            self.creencias.remove(creencia)

    #función mostrar creencias
    #Muestra todas las creencias actuales del agente
    def mostrar_creencias(self):
        print(f"\n Creencias actuales de {self.nombre}:")
         # Si no hay creencias, mostrar un mensaje indicando que no hay ninguna
        print("  (Ninguna creencia)")
        for c in self.creencias:  #para cada creencia 
            print(f"  • {c}")

    #funcion cree
    #Verifica si el agente cree en una proposición dada
    def cree(self, proposicion):
        return proposicion in self.creencias

#Crear un agente
ana = Agente("Ana")

#Agregar creencias iniciales
ana.agregar_creencia("El cielo está nublado")
ana.agregar_creencia("Puede que llueva")
ana.agregar_creencia("Traeré paraguas")

#Mostrar creencias actuales
ana.mostrar_creencias()

#Actualizar creencias con nueva información
ana.eliminar_creencia("Puede que llueva")
ana.agregar_creencia("Está lloviendo")

#Consultar si Ana aún cree en algo
print(f"\n¿Cree Ana que 'Está lloviendo'? {ana.cree('Está lloviendo')}")
print(f"¿Cree Ana que 'Puede que llueva'? {ana.cree('Puede que llueva')}")

#Mostrar creencias finales
ana.mostrar_creencias()

#Ejemplo de salida: 
#  Ana ahora cree que: 'El cielo está nublado'
#  Ana ahora cree que: 'Puede que llueva'
#  Ana ahora cree que: 'Traeré paraguas'

#  Creencias actuales de Ana:
#   (Ninguna creencia)
#   • Traeré paraguas
#   • Puede que llueva
#   • El cielo está nublado
#  Ana ya no cree que: 'Puede que llueva'
#  Ana ahora cree que: 'Está lloviendo'

# ¿Cree Ana que 'Está lloviendo'? True
# ¿Cree Ana que 'Puede que llueva'? False

#  Creencias actuales de Ana:
#   (Ninguna creencia)
#   • Traeré paraguas
#   • Está lloviendo
#   • El cielo está nublado


# El ejemplo de salida nos muestra cómo funciona la clase Agente para manejar creencias:
# 1. Se crean creencias iniciales para el agente "Ana" y se muestran.
# 2. Se actualizan las creencias eliminando una y agregando otra.
# 3. Se consulta si Ana cree en ciertas proposiciones específicas.
# 4. Finalmente, se muestran las creencias finales del agente.
# Esto ilustra cómo un agente puede gestionar y razonar sobre sus creencias de manera dinámica.