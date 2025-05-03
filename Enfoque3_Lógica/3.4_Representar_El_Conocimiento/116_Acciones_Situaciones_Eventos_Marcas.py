#Acciones, Situaciones y Eventos: Marcos
#son una estructura de representación del conocimiento utilizada para modelar objetos, situaciones o eventos.
#se basan en la idea de representar información en "paquetes estructurados".
#Un marco (frame) tiene:
# Nombre del marco
# Slots (atributos): cada uno con un valor, regla, condición o procedimiento.
# Valores por defecto o valores dinámicos.
# Herencia: un marco puede heredar de otro.
#Función y aplicaciones: 
# Los marcos permiten representar:
# Objetos del mundo real (un coche, una persona).
# Escenarios (una visita al doctor).
# Situaciones cambiantes (un evento en el tiempo).

#Ejemplo de Marcos: 
#se representa la visita de una persona a un médico.

#clase Frame (Marco) para representar objetos, eventos o situaciones
class Frame:
    #función de inicialización
    def __init__(self, nombre, padre=None):
        self.nombre = nombre      # Nombre del marco (por ejemplo: "VisitaMédico")
        self.slots = {}           # Diccionario con atributos (slots)
        self.padre = padre        # Marco padre para herencia (si aplica)

    #función para agregar o actualizar un slot	
    def agregar_slot(self, nombre_slot, valor):
        self.slots[nombre_slot] = valor  # Agrega o actualiza un slot

    #función para obtener el valor de un slot
    def obtener_valor(self, nombre_slot):
        # Si el slot está definido en este marco
        if nombre_slot in self.slots: 
            return self.slots[nombre_slot] #retorna el valor del slot
        # Si el marco tiene un padre, buscar recursivamente
        elif self.padre:
            return self.padre.obtener_valor(nombre_slot) #retorna el valor del slot en el marco padre
        else: #retorna None si no se encuentra el slot
            return None

    #función para mostrar el marco y sus slots	
    def mostrar(self):
        print(f"Frame: {self.nombre}") 
        for slot, valor in self.slots.items(): #para cada slot y su valor en el marco
            print(f"   {slot}: {valor}") 

# Marco general: Evento
evento = Frame("Evento") # Marco base para eventos
evento.agregar_slot("fecha", "Desconocida") # Slot para fecha
evento.agregar_slot("lugar", "No especificado") # Slot para lugar

# Marco específico: Visita al Médico (hereda de Evento)
visita_medico = Frame("VisitaMédico", padre=evento) #marco específico que hereda de Evento
visita_medico.agregar_slot("paciente", "Juan Pérez") #slot para paciente
visita_medico.agregar_slot("doctor", "Dra. Rodríguez") #slot para doctor
visita_medico.agregar_slot("síntoma", "Dolor de cabeza") #slot para síntoma
visita_medico.agregar_slot("diagnóstico", "Migraña") #slot para diagnóstico

# Mostrar el marco específico y acceso a un valor heredado
visita_medico.mostrar()
print(f"\nFecha del evento (heredado): {visita_medico.obtener_valor('fecha')}")

#Ejemplo de salida: 
# Frame: VisitaMédico
#    paciente: Juan Pérez
#    doctor: Dra. Rodríguez
#    síntoma: Dolor de cabeza
#    diagnóstico: Migraña

# Fecha del evento (heredado): Desconocida
#El marco "VisitaMédico" hereda el slot "fecha" del marco "Evento", mostrando cómo los marcos pueden representar objetos
#  y situaciones complejas mediante la herencia y la organización jerárquica de información.
#Los marcos son útiles para representar conocimiento estructurado y permiten la herencia de propiedades, facilitando la organización y reutilización de información.
