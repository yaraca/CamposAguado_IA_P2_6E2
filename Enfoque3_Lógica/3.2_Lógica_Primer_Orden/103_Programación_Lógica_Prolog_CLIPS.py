#Programación Lógica: Prolog y CLIPS
#es un paradigma de programación basado en la lógica formal.
#En este paradigma, los programas se escriben en forma de hechos y reglas lógicas, y la resolución de problemas se realiza a través de un proceso de inferencias
#Hechos: Son afirmaciones que siempre son verdaderas (por ejemplo, "Juan es hombre").
#Reglas: Son reglas condicionales que se aplican para deducir nuevos hechos (por ejemplo, "Si una persona es hombre, entonces es adulto").
#Prolog: un programa se compone de hechos y reglas, y la ejecución se basa en hacer consultas a la base de hechos y reglas. 
#CLIPS: CLIPS permite programar de manera declarativa y también realiza inferencias utilizando un conjunto de reglas.
#Aplicaciones: sistemas expertos, procesamiento de lenguaje natural, inteligencia artificial, etc.

#Ejemplo de programación lógica
#simular cómo funciona un sistema básico de inferencia lógico similar a Prolog.

# Definición de hechos en forma de diccionario
hechos = {
    'hombre': ['juan', 'pedro'], # Lista de hombres
    'mujer': ['maria'], # Lista de mujeres
    'edad': {'juan': 25, 'pedro': 30, 'maria': 22} # Edades de las personas
}

#Función de Definición de reglas
#Regla: Una persona es adulta si es hombre y su edad es mayor o igual a 18.
def es_adulto(persona):
    if persona in hechos['hombre']: #si la persona es hombre
        edad = hechos['edad'].get(persona, 0) #obtener la edad de la persona
        return edad >= 18 #si la edad es mayor o igual a 18
    return False #si no es hombre, no es adulto

#función para consultar si una persona es adulta
def consulta_adulto(persona):
    if es_adulto(persona): #si la persona es adulta
        print(f"{persona} es adulto.")
    else: #si no es adulta
        print(f"{persona} no es adulto.")

#realizar consultas
consulta_adulto('juan')  #esperar que sea adulto
consulta_adulto('maria')  #esperar que no sea adulto, porque no tiene la regla aplicada

# Mostrar edad de personas
print("\nEdades de las personas:")
for persona in hechos['edad']: #iterar sobre la lista de personas
    print(f"{persona}: {hechos['edad'][persona]} años") #imprimir la edad de cada persona

#Ejemplo de salida: 
# juan es adulto.
# maria no es adulto.

# Edades de las personas:
# juan: 25 años
# pedro: 30 años
# maria: 22 años
#Como se puede ver, el sistema infiere que Juan es adulto y María no lo es, basándose en la regla definida.
# También muestra las edades de las personas definidas en los hechos.
