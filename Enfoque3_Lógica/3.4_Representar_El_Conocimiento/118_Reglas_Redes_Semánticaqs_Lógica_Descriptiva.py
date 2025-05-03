#Reglas, Redes Semánticas y Lógica Descriptiva
# Las reglas son expresiones lógicas que conectan hechos y condiciones para derivar conclusiones
#Forma tipica: SI (condición) ENTONCES (acción/conclusión)
#Una red semántica representa conocimiento en forma de nodos (conceptos) y enlaces (relaciones):
#Estas redes son útiles para representar jerarquías y propiedades.
#la logica descriptiva Es una familia de lenguajes formales utilizados para:
# Definir conceptos, roles y relaciones.
# Realizar razonamiento automático sobre ontologías.
# Se usa en OWL (Web Ontology Language).
#Aplicaciones: sistemas expertos, ontologías, clasificadores, etc. 

#Ejemplo de red semántica: 

# Definimos una clase para representar una red semántica
class RedSemantica:
    # Método de inicialización que define la estructura de la red
    def __init__(self):
        self.nodos = {}  # Diccionario para almacenar los nodos (conceptos) de la red semántica
        self.reglas = []  # Lista para almacenar las reglas de inferencia

    # Método para agregar conceptos (nodos) a la red
    #Agrega un nodo con atributos opcionales. Si no se proporcionan atributos, se inicializa con un diccionario vacío.
    def agregar_concepto(self, nombre, atributos=None):
        if atributos is None:  #Si no se pasan atributos, se crea un diccionario vacío
            atributos = {}
        self.nodos[nombre] = atributos  #Se guarda el concepto en el diccionario de nodos

    # Método para establecer relaciones entre conceptos
    # Agrega una relación entre dos nodos en la red.
    #     origen: nombre del nodo de inicio.
    #     relacion: tipo de vínculo entre los nodos.
    #     destino: nodo de destino.
    def agregar_relacion(self, origen, relacion, destino):
        if origen in self.nodos:  # Verifica que el nodo de origen exista en la red
            self.nodos[origen][relacion] = destino  # Establece la relación en el nodo origen

    # Método para definir reglas de inferencia
    # Agrega una regla de inferencia a la red.
    #     - condicion: Función que evalúa si la regla se aplica a un nodo.
    #     - conclusion: Acción a ejecutar si la condición se cumple.
    def agregar_regla(self, condicion, conclusion):
        self.reglas.append((condicion, conclusion))  # Se almacena la regla como una tupla

    # Método para aplicar las reglas sobre los nodos existentes
    # Evalúa cada nodo de la red aplicando las reglas de inferencia almacenadas.
    # Si una condición se cumple, ejecuta la acción correspondiente.
    def inferir(self):
        for nodo, atributos in self.nodos.items():  # Itera sobre los nodos y sus atributos
            for condicion, conclusion in self.reglas:  # Itera sobre las reglas almacenadas
                if condicion(nodo, atributos):  # Evalúa si la condición de la regla se cumple
                    conclusion(nodo, atributos)  # Ejecuta la conclusión asociada

    # Método para imprimir la estructura actual de la red semántica
    #Muestra de manera organizada los nodos y sus atributos en la red.
    def mostrar(self):
        print("\n Red Semántica:")
        for nombre, atributos in self.nodos.items():  # Itera sobre los nodos
            print(f"• {nombre}:")  # Imprime el nombre del nodo
            for clave, valor in atributos.items():  # Itera sobre los atributos del nodo
                print(f"   - {clave} → {valor}")  # Muestra cada atributo y su valor asociado


#Ejemplo
#crear una instancia de la red semántica
red = RedSemantica()

#agregar conceptos (nodos) con atributos específicos
red.agregar_concepto("Gato", {"tiene_pelo": True, "maulla": True})  # definir que el gato tiene pelo y maúlla
red.agregar_concepto("Loro", {"tiene_plumas": True, "habla": True})  # El loro tiene plumas y puede hablar
red.agregar_concepto("Perro", {"tiene_pelo": True, "ladra": True})  # El perro tiene pelo y ladra

#agregar relaciones jerárquicas entre los conceptos
red.agregar_relacion("Gato", "es_un", "Mamífero")  # El gato pertenece a la categoría de mamíferos
red.agregar_relacion("Loro", "es_un", "Ave")  # El loro pertenece a la categoría de aves
red.agregar_relacion("Perro", "es_un", "Mamífero")  # El perro también pertenece a los mamíferos

#definir una regla de inferencia para identificar aves
#    Condición: Verifica si un nodo tiene plumas.
# es así, la regla aplicará una conclusión.
def regla_es_ave(nodo, atributos):
    return atributos.get("tiene_plumas", False)  # Retorna True si el atributo "tiene_plumas" está presente y es True

# Acción asociada a la regla anterior
#    Conclusión: Si el nodo cumple la condición de tener plumas, se clasifica como ave.
#    Además, se imprime un mensaje indicando la inferencia realizada.
def conclusion_es_ave(nodo, atributos):
    atributos["es_ave"] = True  # Se asigna un nuevo atributo que indica que el nodo es un ave
    print(f" Inferencia: {nodo} es un ave")  # Se muestra la inferencia realizada

#agregar la regla a la red semántica
red.agregar_regla(regla_es_ave, conclusion_es_ave)

#ejecutar el proceso de inferencia para deducir nuevas características
red.inferir()

# mostar el estado final de la red después de aplicar inferencias
red.mostrar()

#Ejemplo de salida: 
#  Inferencia: Loro es un ave

#  Red Semántica:
# • Gato:
#    - tiene_pelo → True
#    - maulla → True
#    - es_un → Mamífero
# • Loro:
#    - tiene_plumas → True
#    - habla → True
#    - es_un → Ave
#    - es_ave → True
# • Perro:
#    - tiene_pelo → True
#    - ladra → True
#    - es_un → Mamífero

# El ejemplo de salida nos muestra cómo funciona la red semántica y el proceso de inferencia:
# 1. Se realiza una inferencia basada en las reglas definidas. En este caso, se identifica que el "Loro" es un ave
#    porque tiene el atributo "tiene_plumas".
# 2. Se imprime la estructura final de la red semántica, mostrando los nodos (conceptos) y sus atributos.
#    - Cada nodo tiene sus atributos iniciales y, si se aplicaron reglas, también los atributos inferidos.
# 3. En el caso del "Loro", se añadió el atributo "es_ave" como resultado de la inferencia.
# 4. Los demás nodos ("Gato" y "Perro") permanecen sin cambios porque no cumplen con la condición de la regla.