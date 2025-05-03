#Lógica No Monotónica
#es un tipo de lógica en la que añadir nueva información puede cambiar las conclusiones anteriores. Esto contrasta con la lógica clásica (monotónica),
#donde si una conclusión se deriva de una base de conocimiento, seguirá siendo válida incluso si se añade más información.
#Funcionamiento: 
# En lógica clásica: Si B ⊨ φ, entonces B ∪ {ψ} ⊨ φ (la conclusión no cambia al agregar más conocimiento).
# En lógica no monotónica, agregar un nuevo hecho puede invalidar inferencias anteriores.
#Aplicaciones: Inteligencia artificial, sistemas expertos, razonamiento bajo incertidumbre, etc.

#Ejemplo de Lógica No Monotónica
#Los pájaros normalmente vuelan
#representar conocimiento como: Todos los pájaros vuelan por defecto. Si se sabe que un pájaro es un pingüino, no vuela.

# Base de conocimiento no monotónica
class ConocimientoNoMonotonico:
    #Función que inicializa la base de conocimiento
    def __init__(self):
        self.hechos = set() #conjunto de hechos conocidos
        self.excepciones = set() #conjunto de excepciones (ej. pingüinos)

    #Función que agrega un hecho a la base de conocimiento
    def agregar_hecho(self, hecho):
        self.hechos.add(hecho) 

    #Función que agrega una excepción a la base de conocimiento
    def agregar_excepcion(self, hecho):
        self.excepciones.add(hecho)

    #Función que evalúa si un animal vuela o no
    def vuela(self, animal):
        # Si está en excepciones (por ejemplo, es pingüino), no vuela
        if animal in self.excepciones: ## Si es una excepción, no vuela
            return False # No vuela (excepción)
        #Si se sabe que es pájaro y no hay excepción, vuela
        if "pajaro_" + animal in self.hechos:
            return True #vuela (por defecto)
        return None  #si no se tiene información sobre el animal, devolvemos None

#Crear sistema de conocimiento
kb = ConocimientoNoMonotonico()

#Agregar algunos hechos
kb.agregar_hecho("pajaro_tweety")  #tweety es un pájaro
kb.agregar_hecho("pajaro_penguin") 

#Agregar una excepción: los pingüinos no vuelan
kb.agregar_excepcion("penguin")

#evaluar si cada animal vuela
print("¿Tweety vuela?", kb.vuela("tweety"))       #True (es pájaro y no es pingüino)
print("¿Penguin vuela?", kb.vuela("penguin"))     #False (excepción)
print("¿Flamingo vuela?", kb.vuela("flamingo"))   #None (no se tiene información)

#Ejemplo de salida: 
# ¿Tweety vuela? True
# ¿Penguin vuela? False
# ¿Flamingo vuela? None
#En este ejemplo, la lógica no monotónica permite que la base de conocimiento cambie su conclusión sobre si un animal vuela o no al agregar excepciones.
# Esto es útil en situaciones donde el conocimiento puede ser incompleto o cambiar con el tiempo.
#como se puede ver nos dice que tweety vuela, pero penguin no vuela porque es una excepción y flamingo es None porque no tenemos información sobre él.