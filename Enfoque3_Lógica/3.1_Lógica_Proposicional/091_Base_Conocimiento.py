#Base de conocimiento 
#en lógica proposicional es un conjunto de proposiciones (hechos y reglas) que representan lo que un sistema sabe sobre un dominio.
#Se utiliza para razonar y derivar conclusiones mediante inferencia lógica.
#Componentes:
# Hechos: proposiciones básicas como llueve, tiene_paraguas.
# Reglas: proposiciones compuestas como si llueve entonces se moja.
# Motor de inferencia: aplica reglas para deducir nuevos hechos.
#Funcionamiento: 
# Se almacenan proposiciones en la KB.
# Se agrega una consulta que se quiere verificar, por ejemplo: ¿se moja?
# El sistema usa inferencia (como resolución o modus ponens) para verificar si la consulta es verdadera a partir de la KB.
#KB es un conjunto de proposiciones que representan el conocimiento del sistema.
#Aplicaciones: sistemas expertos, agentes inteligentes, diagnóstico médico, etc.

#Ejemplo de Base de Conocimiento en Lógica Proposicional

#definir la Base de Conocimiento
base_conocimiento = {
    "llueve": True,
    "tiene_paraguas": False,
    "si llueve entonces se moja": True
}

#Función para verificar si un hecho puede inferirse
def se_moja(kb):
    # Inferimos "se_moja" solo si "llueve" es verdadero y la regla también
    if kb.get("llueve", False) and kb.get("si llueve entonces se moja", False): #si llueve y la regla es verdadera
        return True #si se moja 
    return False #no se moja

#mostrar contenido de la base de conocimiento
print("Base de conocimiento:")
for hecho, valor in base_conocimiento.items(): ##iterar sobre los hechos y sus valores
    print(f"- {hecho}: {valor}") ##mostrar hechos y valores

# Inferencia
conclusion = se_moja(base_conocimiento) #llamar a la función para verificar si se moja

# Resultado
print("\n¿La persona se moja?")
print("Sí." if conclusion else "No.") #mostrar resultado de la inferencia

#Ejmeplo de Base de Conocimiento en Lógica Proposicional
# Base de conocimiento:
# - llueve: True
# - tiene_paraguas: False
# - si llueve entonces se moja: True

# ¿La persona se moja?
# Sí.

#como podemos ver, la base de conocimiento contiene hechos y reglas que nos permiten inferir si la persona se moja o no.
# En este caso, como llueve y la regla indica que si llueve entonces se moja, la conclusión es que la persona se moja.
