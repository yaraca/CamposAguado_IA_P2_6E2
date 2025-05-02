#Sintaxis y Semántica Tablas Verdad
#es una herramienta utilizada en lógica proposicional para mostrar cómo cambia el valor de una expresión lógica en función de los valores de verdad de sus proposiciones atómicas (P, Q, R, etc.).
#Funcionamiento:
# Cada proposición puede ser verdadera (1/True) o falsa (0/False).
# Se calculan todas las combinaciones posibles de verdad/falsedad de las proposiciones.
# Se evalúa la expresión lógica bajo cada combinación.
#Conectores logicos más comunes:
# Negación	     ¬P	     Verdadero si P es falso
# Conjunción	P ∧ Q	Verdadero si P y Q lo son
# Disyunción	P ∨ Q	Verdadero si al menos uno lo es
# Condicional	P → Q	Falso solo si P es verdadero y Q falso
# Bicondicional	P ↔ Q	Verdadero si P y Q tienen el mismo valor
#Aplicaciones: validez de argumentos, simplificación de expresiones lógicas, diseño de circuitos digitales, etc.

#Ejemplo de sintaxis y semántica de tablas de verdad

#librerías necesarias
import itertools # Para combinaciones de verdad

#función del Evaluador lógico
def evaluar_expresion(p, q, expresion): #p y q son las variables proposicionales
    return eval(expresion) # eval evalúa la expresión lógica en Python

#funcion de Tabla de verdad para una expresión dada
def tabla_verdad(expresion): 
    valores = list(itertools.product([True, False], repeat=2))  # Combinaciones para P y Q
    
    print("P\tQ\tResultado") #encabecera de la tabla
    print("-"*30) 
    
    for p, q in valores: # Iterar sobre todas las combinaciones de verdad
        resultado = evaluar_expresion(p, q, expresion) # Evaluar la expresión
        print(f"{int(p)}\t{int(q)}\t{int(resultado)}") # Imprimir resultados como 1 (True) o 0 (False)

#Ejemplos de uso
# and = ∧, or = ∨, not = ¬, =>: usar (not P or Q), <=>: usar (P == Q)
# Ejemplo: "(not p or q)" para P → Q
print("Ejemplo: (not p or q) para P → Q")
expresion_logica = "(not p or q)"  # P → Q
tabla_verdad(expresion_logica)

print("\nEjemplo: (p and q) para P ∧ Q")
expresion_logica = "(p and q)"  # P ^ Q
tabla_verdad(expresion_logica)

print("\nEjemplo: (p or q) para P ∨ Q")
expresion_logica = "(p or q)"  # P ∨ Q
tabla_verdad(expresion_logica)

print("\nEjemplo: (p and not q) para P ¬ Q")
expresion_logica = "(p and not q)"  # P ¬ Q
tabla_verdad(expresion_logica)

print("\nEjemplo: (p == ) para P <=> Q")
expresion_logica = "(p == q)"  # P <=> Q
tabla_verdad(expresion_logica)

#Ejemplo de salida:
# Ejemplo: (not p or q) para P → Q
# P       Q       Resultado
# ------------------------------
# 1       1       1
# 1       0       0
# 0       1       1
# 0       0       1

# Ejemplo: (p and q) para P ∧ Q
# P       Q       Resultado
# ------------------------------
# 1       1       1
# 1       0       0
# 0       1       0
# 0       0       0

# Ejemplo: (p or q) para P ∨ Q
# P       Q       Resultado
# ------------------------------
# 1       1       1
# 1       0       1
# 0       1       1
# 0       0       0

# Ejemplo: (p and not q) para P ¬ Q
# P       Q       Resultado
# ------------------------------
# 1       1       0
# 1       0       1
# 0       1       0
# 0       0       0

# Ejemplo: (p == ) para P <=> Q
# P       Q       Resultado
# ------------------------------
# 1       1       1
# 1       0       0
# 0       1       0
# 0       0       1

#como podemos ver, la tabla de verdad nos permite analizar el comportamiento de las expresiones lógicas en función de los valores de verdad de las proposiciones atómicas.