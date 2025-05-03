#Logica Temporal 
#es una extensión de la lógica proposicional y de primer orden que permite razonar sobre proposiciones con respecto al tiempo.
# Introduce operadores que indican cuándo una proposición es verdadera, como:
# F (Future / Finalmente): Algo será verdadero en algún momento futuro.
# G (Globally / Siempre): Algo será siempre verdadero en el futuro.
# X (neXt): Algo será verdadero en el siguiente estado.
# U (Until / Hasta que): Una condición se mantiene hasta que otra se cumple.
#Funcionamiento: 
#En lógica temporal se usa un modelo de tiempo representado como una secuencia de estados (línea temporal). 
#Cada estado representa un momento en el tiempo, con sus proposiciones verdaderas.
#Aplicaciones: Verificación de sistemas, planificación, inteligencia artificial, etc.

#Ejemplo de Lógica Temporal
#Simular una línea de tiempo de 5 estados, cada uno con proposiciones verdaderas o falsas, y evaluar los operadores F, G, X, y U.

#Línea temporal: lista de conjuntos de proposiciones verdaderas en cada estado
linea_tiempo = [
    {"P"},           # t0
    {"Q"},           # t1
    {"P", "Q"},      # t2
    set(),           # t3
    {"P"}            # t4
]

#Funciones para evaluar los operadores de lógica temporal
#Función F (Finalmente): ¿La proposición será verdadera en algún punto desde t?
def F(prop, t):
    return any(prop in estado for estado in linea_tiempo[t:]) # Evaluar desde el tiempo t

#Función G (Siempre): ¿La proposición es siempre verdadera desde t?
def G(prop, t):
    return all(prop in estado for estado in linea_tiempo[t:]) #evaluar desde el tiempo t

#Función X (neXt): ¿La proposición será verdadera en el siguiente estado?
def X(prop, t):
    if t + 1 < len(linea_tiempo): #verificar que no se salga de la línea temporal
        return prop in linea_tiempo[t + 1] #evaluar el siguiente estado
    return False #si no hay siguiente estado

#función U (Hasta que): ¿La proposición p es verdadera hasta que q se cumpla?
#p U q es verdadero si existe un tiempo futuro j ≥ t tal que:
#- q es verdadera en j
#- p es verdadera en todos los pasos desde t hasta j-1
def U(p, q, t):
    for j in range(t, len(linea_tiempo)): #recorrer la línea temporal desde t
        if q in linea_tiempo[j]: #verificar si q es verdadera en j
            if all(p in linea_tiempo[k] for k in range(t, j)): #verificar si p es verdadera desde t hasta j-1
                return True #si se cumple la condición
    return False #si no se cumple la condición

#evaluar desde el tiempo t=0
print("Desde t=0:") 
print("¿F Q? (Finalmente Q):", F("Q", 0)) #evaluar si Q es verdadero en algún momento futuro
print("¿G P? (Siempre P):", G("P", 0)) #evaluar si P es verdadero siempre desde t=0
print("¿X Q? (Siguiente Q):", X("Q", 0)) #evaluar si Q es verdadero en el siguiente estado
print("¿P U Q? (P hasta que Q):", U("P", "Q", 0)) #evaluar si P es verdadero hasta que

#Ejemplo de salida: 
# Desde t=0:
# ¿F Q? (Finalmente Q): True #Q es verdadero en t=1
# ¿G P? (Siempre P): False #P no es verdadero siempre desde t=0 (t=1 no es verdadero)
# ¿X Q? (Siguiente Q): True #Q es verdadero en el siguiente estado (t=1)
# ¿P U Q? (P hasta que Q): True #P es verdadero en t=0 y Q es verdadero en t=1

#como se observa en el ejemplo, la lógica temporal permite razonar sobre el comportamiento de las proposiciones a lo largo del tiempo, 
# lo que es útil en diversas aplicaciones como la verificación de sistemas y la planificación.
#En este caso, se ha simulado una línea temporal de 5 estados y se han evaluado los operadores F, G, X y U para las proposiciones P y Q.
#Los resultados muestran cómo se puede razonar sobre el futuro y el comportamiento de las proposiciones a lo largo del tiempo.