#Espacio de Versiones y AQ
#El espacio de versiones es una representación lógica de todas las hipótesis que son consistentes con los ejemplos vistos hasta un momento.
# Se construye a partir de dos fronteras:
# S (Specific boundary): la hipótesis más específica que cubre todos los ejemplos positivos.
# G (General boundary): la hipótesis más general que no contradice ningún ejemplo negativo.
#El algoritmo AQ es una técnica que genera reglas clasificadoras a partir de ejemplos positivos y negativos.
#Intenta crear una o más reglas que cubran todos los ejemplos positivos sin cubrir ninguno negativo.
#La idea es construir reglas si-entonces del tipo:
#SI (atributo1=valor1) Y (atributo2=valor2) ENTONCES clase=Positiva
#Aplicaciones: clasificación de datos, sistemas expertos, etc.

#Ejemplo de espacio de versiones y algoritmo AQ

#definir los datos de entrenamiento donde cada instancia contiene atributos y su clase
datos=[
    (['Rojo', 'Circular', 'Liso'], 'Sí'),
    (['Rojo', 'Cuadrado', 'Liso'], 'Sí'),
    (['Verde', 'Circular', 'Rugoso'], 'No'),
    (['Rojo', 'Circular', 'Rugoso'], 'Sí'),
    (['Azul', 'Cuadrado', 'Liso'], 'No')
]

#definir una función para verificar si una regla cubre un ejemplo dado
def cubre(regla, ejemplo):
    for i in range(len(regla)):  #recorrer cada atributo de la regla
        if regla[i]!='?' and regla[i]!=ejemplo[i]:  #verificar si hay una diferencia en los valores
            return False  #la regla no cubre el ejemplo
    return True  #la regla cubre el ejemplo

#definir una función para generalizar una regla con el objetivo de cubrir un ejemplo positivo
def generalizar(regla, ejemplo):
    nueva_regla=[]  #crear una lista para almacenar la nueva regla generalizada
    for i in range(len(regla)):  #recorrer cada atributo de la regla
        if regla[i]==ejemplo[i]:  #si el valor es igual, mantenerlo
            nueva_regla.append(regla[i])
        else:
            nueva_regla.append('?')  #si hay una diferencia, se generaliza con '?'
    return nueva_regla  #retornar la regla generalizada

#definir el algoritmo aq simplificado que genera reglas positivas consistentes
def AQ_algorithm(datos):
    reglas=[]  #lista para almacenar las reglas generadas

    positivos=[x for x, y in datos if y=='Sí']  #filtrar ejemplos positivos
    negativos=[x for x, y in datos if y=='No']  #filtrar ejemplos negativos

    for pos in positivos:  #recorrer cada ejemplo positivo
        regla_actual=pos[:]  #inicializar la regla con los valores del ejemplo positivo

        #refinar la regla para asegurarse de que no cubre ningún ejemplo negativo
        for neg in negativos:  #recorrer cada ejemplo negativo
            if cubre(regla_actual, neg):  #si la regla cubre un negativo, se debe generalizar
                regla_actual=generalizar(regla_actual, neg)

        reglas.append(regla_actual)  #agregar la regla refinada a la lista de reglas

    return reglas  #retornar el conjunto de reglas generadas

#ejecutar el algoritmo para generar reglas basadas en el conjunto de datos
reglas_resultado=AQ_algorithm(datos)

#imprimir los resultados obtenidos con las reglas generadas
print("Reglas generadas por el algoritmo AQ:\n")
for i, regla in enumerate(reglas_resultado):  #recorrer cada regla generada
    condiciones=' Y '.join(
        f"A{i+1}={valor}" if valor!='?' else f"A{i+1}=?" for i, valor in enumerate(regla)
    )  #formatear la condición de la regla
    print(f"Regla {i+1}: SI {condiciones} ENTONCES Clase = Sí")  #mostrar la regla en formato natural

 #Ejemplo de salida:
#  Reglas generadas por el algoritmo AQ:

# Regla 1: SI A1=Rojo Y A2=Circular Y A3=Liso ENTONCES Clase = Sí
# Regla 2: SI A1=Rojo Y A2=Cuadrado Y A3=Liso ENTONCES Clase = Sí
# Regla 3: SI A1=Rojo Y A2=Circular Y A3=Rugoso ENTONCES Clase = Sí

# El ejemplo de salida nos demuestra cómo el algoritmo AQ genera reglas clasificadoras
# a partir de ejemplos positivos y negativos. Cada regla describe una condición específica
# que cubre un conjunto de ejemplos positivos sin cubrir ejemplos negativos.
# Además, ilustra cómo el algoritmo generaliza las reglas para evitar conflictos con
# los ejemplos negativos, utilizando el carácter '?' para representar valores genéricos
# en los atributos donde no es posible especificar un valor exacto.