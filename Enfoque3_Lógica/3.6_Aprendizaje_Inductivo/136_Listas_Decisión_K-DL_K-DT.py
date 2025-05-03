# Listas de Decisión: K-DL y K-DT
#Las Listas de Decisión son una representación lógica para funciones booleanas que se expresan como una secuencia ordenada de reglas condicionales ("si-entonces").
#Estas reglas se aplican una tras otra hasta que una condición se cumple. Existen dos variantes principales:
#Una k-Decision List (K-DL) es una lista ordenada de k-conjunciones (es decir, cada condición puede incluir hasta k literales como A ∧ ¬B, etc.) con una salida booleana
#Tiene la forma:
# if condición_1: salida_1
# elif condición_2: salida_2
# ...
# else: salida_defecto
#Un k-Decision Tree (K-DT) es un árbol donde cada nodo contiene una k-conjunción, lo que hace que pueda representar funciones más complejas que un árbol tradicional, manteniendo interpretabilidad.
#Aplicaciones: clasificación, diagnóstico médico, sistemas expertos, etc.

#Ejemplo de K-DL
#Simular una 2-DL (usa conjunciones de 2 condiciones como máximo) para clasificar datos simples.

#definir un conjunto de datos de entrada donde cada tupla contiene atributos y una etiqueta de clasificación
datos=[
    ({'A': True, 'B': True, 'C': False}, 1),
    ({'A': True, 'B': False, 'C': False}, 0),
    ({'A': False, 'B': True, 'C': True}, 1),
    ({'A': False, 'B': False, 'C': True}, 0),
]

#definir una lista de reglas de decisión utilizando conjunciones de hasta dos condiciones
#cada regla es una tupla que asocia condiciones con una salida esperada
reglas=[
    ({'A': True, 'B': True}, 1),  #si A=True y B=True entonces la salida es 1
    ({'B': True, 'C': True}, 1),  #si B=True y C=True entonces la salida es 1
    ({'C': True}, 0),  #si C=True entonces la salida es 0
]

#definir un valor por defecto si ninguna regla se cumple
salida_defecto=0

#definir una función para evaluar si una instancia cumple una condición específica
def cumple_condicion(instancia, condicion):
    for atributo, valor_esperado in condicion.items():  #recorrer cada atributo en la condición
        if instancia[atributo]!=valor_esperado:  #verificar si el valor real no coincide con el esperado
            return False
    return True  #retornar True si todos los atributos coinciden

print("K-DL")

#evaluar los datos utilizando la k-decision list
for instancia, etiqueta_real in datos:
    prediccion=salida_defecto  #asumir la salida por defecto inicialmente
    for condicion, salida in reglas:  #recorrer las reglas de decisión
        if cumple_condicion(instancia, condicion):  #si la instancia cumple una condición
            prediccion=salida  #asignar la salida correspondiente
            break  #detener la búsqueda en la primera condición verdadera
    print(f"Instancia: {instancia} → Predicción: {prediccion} (Real: {etiqueta_real})")

#------------------------------------------------------------------
#k-dt (k-decision tree)

#definir un nuevo conjunto de datos con diferentes instancias
datos=[
    ({'A': True, 'B': True, 'C': False}, 1),
    ({'A': False, 'B': True, 'C': False}, 0),
    ({'A': True, 'B': False, 'C': True}, 1),
    ({'A': False, 'B': False, 'C': False}, 0),
]

#definir las condiciones de cada nodo como funciones utilizando k=2 condiciones por nodo
def cond1(inst):  #a ∧ b
    return inst['A'] and inst['B']

def cond2(inst):  #¬a ∧ c
    return not inst['A'] and inst['C']

def cond3(inst):  #b ∨ c (no es conjunción, pero se incluye para extender el ejemplo)
    return inst['B'] or inst['C']

#definir el árbol k-dt como nodos anidados de condiciones y valores finales
k_dt=(cond1, 
            1,  #si A ∧ B entonces clase 1
            (cond2,
                1,  #si ¬A ∧ C entonces clase 1
                (cond3,
                    0,  #si B ∨ C entonces clase 0
                    0   #caso contrario entonces clase 0
                )
            )
       )

#definir una función para recorrer el árbol de decisión y obtener una predicción
def predecir_kdt(arbol, instancia):
    if isinstance(arbol, int):  #si el nodo es un número entero, es un nodo hoja
        return arbol  #retornar el valor final
    condicion, si_verdadero, si_falso=arbol  #extraer la condición y los nodos hijos
    if condicion(instancia):  #evaluar la condición en la instancia
        return predecir_kdt(si_verdadero, instancia)  #recorrer el nodo verdadero
    else:
        return predecir_kdt(si_falso, instancia)  #recorrer el nodo falso

print("K-DT")
#evaluar los datos utilizando el árbol de decisión k-dt
for instancia, etiqueta_real in datos:
    pred=predecir_kdt(k_dt, instancia)
    print(f"Instancia: {instancia} → Predicción: {pred} (Real: {etiqueta_real})")

#Ejemplo de salida: 

# Instancia: {'A': True, 'B': True, 'C': False} → Predicción: 1 (Real: 1)
# Instancia: {'A': True, 'B': False, 'C': False} → Predicción: 0 (Real: 0)
# Instancia: {'A': False, 'B': True, 'C': True} → Predicción: 1 (Real: 1)
# Instancia: {'A': False, 'B': False, 'C': True} → Predicción: 0 (Real: 0)
# K-DT
# Instancia: {'A': True, 'B': True, 'C': False} → Predicción: 1 (Real: 1)
# Instancia: {'A': False, 'B': True, 'C': False} → Predicción: 0 (Real: 0)
# Instancia: {'A': True, 'B': False, 'C': True} → Predicción: 0 (Real: 1)
# Instancia: {'A': False, 'B': False, 'C': False} → Predicción: 0 (Real: 0)

# El ejemplo de salida nos demuestra cómo funcionan las K-Decision Lists (K-DL) y los K-Decision Trees (K-DT) 
# para clasificar instancias basadas en reglas lógicas.
# En el caso de K-DL, se observa cómo las reglas se evalúan secuencialmente hasta encontrar una que se cumpla,
# asignando la predicción correspondiente o el valor por defecto si ninguna regla aplica.
# En el caso de K-DT, se muestra cómo las condiciones se evalúan de manera jerárquica en un árbol,
# siguiendo las ramas según las condiciones hasta llegar a un nodo hoja que contiene la predicción final.
# Esto ilustra las diferencias entre ambos enfoques y cómo pueden producir resultados distintos
# dependiendo de las reglas y la estructura del árbol.