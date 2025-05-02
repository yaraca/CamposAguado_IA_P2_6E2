#Equivalencia, Validez y Satisfacibilidad
#Equivalencia: Dos proposiciones son lógicamente equivalentes si tienen el mismo valor de verdad en todas las interpretaciones posibles.
#Validez: Una fórmula es válida si es verdadera en todas las interpretaciones posibles. Es una tautología.
#Satisfacibilidad: Una fórmula es satisfacible si existe al menos una interpretación en la que sea verdadera.
#Aplicaciones: verificacion de software, circuitos digitales, inteligencia artificial, etc.

#Ejemplo de equivalencia, validez y satisfacibilidad
#Evaluarexpresiones lógicas usando tablas de verdad para comprobar si son:Equivalentes, Válidas, Satisfacibles

#librerías necesarias
import itertools # Para combinaciones de verdad

#Funcion para Evaluar una expresión lógica con p y q
def evaluar_expr(expr, p, q): 
    return eval(expr) #usamos eval para evaluar la expresión lógica

#Función para Generar tabla de verdad y analizar la lógica
def analizar_logica(expr1, expr2=None): 
    combinaciones = list(itertools.product([True, False], repeat=2)) # Genera todas las combinaciones de verdad para p y q
    valores_expr1 = [] #lista para almacenar los valores de la expresión 1
    valores_expr2 = [] #lista para almacenar los valores de la expresión 2

    print(f"\nEvaluando expresión: {expr1}") #imprime la expresión 1
    if expr2: #si hay una segunda expresión
        print(f"Comparando con expresión: {expr2}") #imprime la expresión 2
    print(" P      Q      Expr1", end="") 
    if expr2: #si hay una segunda expresión
        print("    Expr2") #imprime la expresión 2
    else:
        print()

    for p, q in combinaciones: # Itera sobre todas las combinaciones de verdad
        val1 = evaluar_expr(expr1, p, q) #evalua la expresión 1
        valores_expr1.append(val1) #almacena el valor de la expresión 1
        print(f"{p:<6}{q:<6}{val1!s:<8}", end="") #imprime los valores de p, q y la expresión 1
        if expr2: #si hay una segunda expresión
            val2 = evaluar_expr(expr2, p, q) #evalua la expresión 2
            valores_expr2.append(val2) #almacena el valor de la expresión 2
            print(f"{val2!s:<8}") #imprime el valor de la expresión 2
        else: #si no hay una segunda expresión
            print() #imprime un salto de línea

    # Verificación
    print("\nResultado del análisis:")
    if expr2: #si hay una segunda expresión
        equivalentes = valores_expr1 == valores_expr2 #compara los valores de las dos expresiones
        print(f"¿Son equivalentes? {'Sí' if equivalentes else 'No'}") #imprime si son equivalentes

    valida = all(valores_expr1) #verifica si la expresión 1 es válida
    satisfacible = any(valores_expr1) #verifica si la expresión 1 es satisfacible

    print(f"¿Es válida? {'Sí' if valida else 'No'}") #imprime si es válida
    print(f"¿Es satisfacible? {'Sí' if satisfacible else 'No'}") #imprime si es satisfacible

# Ejemplo de uso
# Usamos 'not', 'and', 'or' porque eval entiende sintaxis de Python
expr1 = "not (p and q)"
expr2 = "not p or not q"

analizar_logica(expr1, expr2) #Ejemplo de equivalencia

#Ejemplo de salida: 
# Evaluando expresión: not (p and q)
# Comparando con expresión: not p or not q
#  P      Q      Expr1    Expr2
# 1     1     False   False
# 1     0     True    True
# 0     1     True    True
# 0     0     True    True

# Resultado del análisis:
# ¿Son equivalentes? Sí
# ¿Es válida? No
# ¿Es satisfacible? Sí

#Podemos ver que ambas expresiones son equivalentes, no son válidas (no son verdaderas en todas las combinaciones) pero sí son satisfacibles (hay combinaciones que las hacen verdaderas).
#esto nos ayuda a entender la lógica detrás de las proposiciones y su validez.