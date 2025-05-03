#Taxonomías: Categorías y Objetos
#es una estructura jerárquica que organiza conceptos u objetos en categorías de forma ordenada. 
#Se utiliza para representar el conocimiento de un dominio, facilitando la clasificación y el razonamiento.
#Componentes:
# Categorías (Clases): Agrupaciones generales (Ej. "Animal", "Vehículo").
# Subcategorías: Más específicas (Ej. "Mamífero", "Reptil").
# Objetos (Instancias): Elementos concretos (Ej. "León", "Tigre").
#Función: 
# Representar conocimiento de forma estructurada.
# Facilitar inferencias (ej: Si "Perro" es un "Mamífero", entonces respira aire).
# Base de sistemas expertos, motores de búsqueda y clasificadores.
#Aplicaciones: cladsificación biológica, organización de información, sistemas de recomendación.

#Ejemplo de Taxonomía: Categorías y Objetos

# Clase base para representar una categoría general
class Categoria:
    def __init__(self, nombre, padre=None):
        self.nombre = nombre       # Nombre de la categoría
        self.padre = padre         # Categoría padre (si existe)
        self.subcategorias = []   # Lista de subcategorías
        self.objetos = []         # Lista de objetos (instancias)

        # Si hay categoría padre, se agrega esta como subcategoría
        if padre:
            padre.subcategorias.append(self)

    #función para agregar un objeto a la categoría
    def agregar_objeto(self, objeto):
        self.objetos.append(objeto) #agrega el objeto a la lista de objetos

    #función para imprimir toda la jerarquía de categorías
    def imprimir(self, nivel=0): #imprime la jerarquía de categorías
        print("  " * nivel + f"📂 {self.nombre}") 
        for objeto in self.objetos: #imprime los objetos de la categoría
            print("  " * (nivel + 1) + f"🔹 {objeto}")
        for sub in self.subcategorias: #recorre las subcategorías
            sub.imprimir(nivel + 1) #llama a la función imprimir de la subcategoría

#crear la taxonomía para representar animales
raiz = Categoria("Animal")

#subcategorías
mamifero = Categoria("Mamífero", raiz) #subcategoría de Animal
ave = Categoria("Ave", raiz) #subcategoría de Animal

#Sub-subcategorías
felino = Categoria("Felino", mamifero) #subcategoría de Mamífero
canino = Categoria("Canino", mamifero) #subcategoría de Mamífero

#Objetos (instancias)
felino.agregar_objeto("León") #agrega el objeto León a la subcategoría Felino
felino.agregar_objeto("Tigre") #agrega el objeto Tigre a la subcategoría Felino
canino.agregar_objeto("Perro") #agrega el objeto Perro a la subcategoría Canino
ave.agregar_objeto("Águila") #agrega el objeto Águila a la subcategoría Ave
ave.agregar_objeto("Paloma") #agrega el objeto Paloma a la subcategoría Ave

#Mostrar la taxonomía
print("Taxonomía generada:")
raiz.imprimir()

#Ejemplo de salida:
# Taxonomía generada:
# 📂 Animal
#   📂 Mamífero
#     📂 Felino
#       🔹 León
#       🔹 Tigre
#     📂 Canino
#       🔹 Perro
#   📂 Ave
#     🔹 Águila
#     🔹 Paloma
#En este ejemplo, la clase Categoria representa una categoría general, que puede tener subcategorías y objetos.
# La función imprimir muestra la jerarquía de categorías y objetos de forma estructurada.
# La taxonomía generada representa una jerarquía de animales, donde cada categoría puede tener subcategorías y objetos específicos.
# Esta estructura permite organizar y clasificar el conocimiento de manera eficiente, facilitando la comprensión y el razonamiento sobre los objetos y sus relaciones.
