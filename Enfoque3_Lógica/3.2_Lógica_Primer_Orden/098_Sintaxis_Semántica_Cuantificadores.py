#Sintaxis y Semántica: Cuantificadores
#Cuantificadores en Lógica de Primer Orden (FOL)
#La Lógica de Primer Orden (FOL por sus siglas en inglés: First-Order Logic) extiende la lógica proposicional añadiendo cuantificadores, predicados, y variables.
#Sintaxis básica:
# En FOL, se usan expresiones como:
# ∀x P(x) → "Para todo x, se cumple P(x)"
# ∃x P(x) → "Existe al menos un x tal que se cumple P(x)"
# Donde:
# ∀ (cuantificador universal), ∃ (cuantificador existencial), P(x) es un predicado, una función lógica que depende de la variable x.
#Semántica: 
#∀x P(x) es verdadera si P(x) es verdadera para todo x en el dominio.
# ∃x P(x) es verdadera si existe al menos un x en el dominio donde P(x) sea verdadera.
#Aplicaciones: sistemas expertos, inteligencia artificial, bases de datos, etc.

#Ejemplo práctico: Cuantificadores
# Definimos el dominio de variables (conjunto de posibles valores)
dominio = [1, 2, 3, 4, 5]

#Función para Definir el predicado: es_par
def es_par(x):
    return x % 2 == 0

#Función para Evaluar cuantificador universal: ∀x es_par(x)
def cuantificador_universal(predicado, dominio): # predicado: función que define el predicado
    for x in dominio: # dominio: lista de valores
        if not predicado(x): # Si hay al menos un valor que no cumple el predicado, es falso
            return False # Si no, es verdadero
    return True # Si todos los valores cumplen el predicado, es verdadero

#Función para Evaluar cuantificador existencial: ∃x es_par(x)
def cuantificador_existencial(predicado, dominio):
    for x in dominio: #para cada valor en el dominio
        if predicado(x): # Si hay al menos un valor que cumple el predicado, es verdadero
            return True
    return False

# Resultados
print("Dominio:", dominio)

resultado_universal = cuantificador_universal(es_par, dominio) #evaluar el predicado en el dominio
print("∀x es_par(x):", resultado_universal) #evaluar el predicado en el dominio

resultado_existencial = cuantificador_existencial(es_par, dominio) #evaluar el predicado en el dominio
print("∃x es_par(x):", resultado_existencial) #evaluar el predicado en el dominio

#Ejemplo de salida: 
# Dominio: [1, 2, 3, 4, 5]
# ∀x es_par(x): False
# ∃x es_par(x): True
#Como podemos ver, el resultado del cuantificador universal es falso porque no todos los números en el dominio son pares, 
#mientras que el cuantificador existencial es verdadero porque hay al menos un número par (2 y 4) en el dominio.