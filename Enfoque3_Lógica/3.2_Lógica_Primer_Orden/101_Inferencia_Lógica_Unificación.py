#Inferencia Lógica: Unificación
#La unificación es el proceso de hacer que dos expresiones lógicas sean iguales encontrando una sustitución (valores de variables) que las haga idénticas.
#Sirve para: 
#Motores de inferencia, Sistemas expertos, Prolog y otros lenguajes de lógica, Resolución y encadenamiento hacia delante/atrás
#Ejemplo de unificar: 
#Unificar: padre(X, juan)    y    padre(carlos, Y)
#sustituciones: {X: carlos, Y: juan}
#Quedan como: padre(carlos, juan)
#Aplicaciones: Sistemas expertos, Prolog, motores de inferencia, etc.

#Ejemplo de unificación de expresiones lógicas

# Función principal de unificación
def unificar(expr1, expr2, sustituciones={}):
    # Si ya hay una sustitución previa, se actualizan las expresiones
    if expr1 == expr2: 
        return sustituciones

    # Si expr1 es una variable
    if es_variable(expr1):
        return unificar_variable(expr1, expr2, sustituciones) #se retorna la unificación de expr1 con expr2

    # Si expr2 es una variable
    if es_variable(expr2):
        return unificar_variable(expr2, expr1, sustituciones) #se retorna la unificación de expr2 con expr1

    # Si ambos son listas o tuplas (funciones o predicados)
    if isinstance(expr1, (list, tuple)) and isinstance(expr2, (list, tuple)): ##se verifica si son listas o tuplas
        if len(expr1) != len(expr2): # Si tienen diferente longitud, no se pueden unificar
            return None  # No se pueden unificar
        for e1, e2 in zip(expr1, expr2): #recorrer los elementos de ambas expresiones
            sustituciones = unificar(e1, e2, sustituciones) #se llama a la función unificar para cada par de elementos
            if sustituciones is None: # Si alguna unificación falla, se retorna None
                return None # No se pueden unificar
        return sustituciones

    # En cualquier otro caso, no hay unificación posible
    return None

#Función que Detecta si una expresión es variable (por convención: empieza con mayúscula)
def es_variable(x):
    return isinstance(x, str) and x[0].isupper() #se verifica si es una cadena y si empieza con mayúscula

#Función qe Unifica una variable con una expresión, considerando las sustituciones ya existentes
def unificar_variable(var, expr, sustituciones):
    if var in sustituciones: # Si la variable ya tiene una sustitución
        return unificar(sustituciones[var], expr, sustituciones) #se llama a la función unificar con la sustitución existente y la nueva expresión
    elif expr in sustituciones: # Si la expresión ya tiene una sustitución
        return unificar(var, sustituciones[expr], sustituciones) #se llama a la función unificar con la variable y la sustitución existente
    else: # Si la variable no tiene sustitución, se agrega
        sustituciones[var] = expr #se agrega la variable y la expresión a las sustituciones
        return sustituciones #se retorna las sustituciones

# ---------- Ejemplo de uso ----------
# Dos predicados lógicos a unificar
expr1 = ("padre", "X", "juan") # Expresión con variable X
expr2 = ("padre", "carlos", "Y") # Expresión con variable Y

resultado = unificar(expr1, expr2) #llamar a la función unificar con las dos expresiones

# Mostrar resultado
print("Resultado de la unificación:")
if resultado: # Si hay un resultado, se muestran las sustituciones
    for variable, valor in resultado.items(): #recorrer las sustituciones
        print(f"{variable} = {valor}") #se imprime la variable y su valor
else:
    print("No se pudo unificar.")

#Ejemplo de salida: 
# Resultado de la unificación:
# X = carlos
# Y = juan
#Como se puede ver, se han unificado las variables X y Y con los valores correspondientes de la expresión.
#Esto es útil en motores de inferencia, sistemas expertos y lenguajes de programación lógica como Prolog.