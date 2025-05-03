#Programación Lógica Inductiva: FOIL
#FOIL es un algoritmo de aprendizaje inductivo que aprende reglas lógicas de primer orden (basadas en predicados) a partir de ejemplos positivos y negativos. 
#FOIL puede trabajar con relaciones complejas entre objetos y generaliza mejor estructuras del tipo padre(X, Y) o mayor_que(X, Y).
#Funcionamiento: 
# Entrada:
# Ejemplos positivos (E⁺)
# Ejemplos negativos (E⁻)
# Conjunto de predicados posibles (literales)
# Proceso:
# Comienza con una regla vacía y busca añadir literales que maximicen la ganancia de información (FOIL Gain).
# Añade condiciones hasta que la regla cubre solo ejemplos positivos.
# Una vez creada una regla válida, elimina los ejemplos cubiertos y repite.
# Salida: Conjunto de reglas lógicas que cubren todos los positivos y excluyen los negativos.
#Aplicaciones: Aprendizaje de relaciones complejas, como jerarquías familiares, relaciones espaciales, etc.

#Ejemplo de FOil:Abuelo(X, Y)" basado en relaciones padre(X, Y)

#definir los hechos base que indican relaciones de paternidad entre individuos
padres={
    "juan": "carlos",
    "carlos": "pedro",
    "luis": "miguel",
    "miguel": "andres",
    "tomas": "ricardo"
}

#definir ejemplos positivos donde x es abuelo de y
ejemplos_positivos=[("juan", "pedro"), ("luis", "andres")]

#definir ejemplos negativos donde no hay relación de abuelo entre x y y
ejemplos_negativos=[("juan", "ricardo"), ("carlos", "pedro"), ("luis", "miguel")]

#definir una función para verificar si x es padre de y
def padre(x, y):
    return padres.get(x)==y  #buscar en el diccionario de padres si x tiene como hijo a y

#definir una función para verificar si existe un "z" tal que padre(x, z) y padre(z, y)
def cubre_abuelo(x, y):
    for z in padres:  #recorrer todos los individuos en la base de hechos
        if padre(x, z) and padre(z, y):  #verificar si existe una relación de abuelo
            return True  #si se cumple, retornar verdadero
    return False  #si no se encuentra una relación válida, retornar falso

#definir una versión simplificada del algoritmo foil para construir la regla abuelo(x, y) <- padre(x, z), padre(z, y)
def foil_aprender():
    reglas=[]  #lista para almacenar reglas de abuelo aprendidas
    for (x, y) in ejemplos_positivos:  #recorrer los ejemplos positivos
        if cubre_abuelo(x, y):  #verificar si x es abuelo de y basado en la función de cobertura
            reglas.append((x, y))  #agregar la regla a la lista

    return reglas  #retornar las reglas aprendidas

#ejecutar el algoritmo para aprender reglas de abuelo
reglas_aprendidas=foil_aprender()

#evaluar las reglas aprendidas y mostrarlas en pantalla
print("Reglas aprendidas (ejemplos cubiertos por la regla lógica):")
for (x, y) in reglas_aprendidas:
    print(f"abuelo({x}, {y})")

#verificar la cobertura sobre los ejemplos negativos para detectar falsos positivos
print("\n Verificando falsos positivos (no deben aparecer):")
for (x, y) in ejemplos_negativos:
    if cubre_abuelo(x, y):  #si la función cubre_abuelo detecta una relación en un negativo, es un falso positivo
        print(f" Falso positivo detectado: abuelo({x}, {y})")
    else:
        print(f"Correcto: abuelo({x}, {y}) no detectado.")

#Ejemplo de salida: 
# Reglas aprendidas (ejemplos cubiertos por la regla lógica):
# abuelo(juan, pedro)
# abuelo(luis, andres)

#  Verificando falsos positivos (no deben aparecer):
# Correcto: abuelo(juan, ricardo) no detectado.
# Correcto: abuelo(carlos, pedro) no detectado.
# Correcto: abuelo(luis, miguel) no detectado.

# El ejemplo de salida nos demuestra que el algoritmo FOIL es capaz de aprender reglas lógicas
# que cubren los ejemplos positivos dados (relaciones de abuelo en este caso).
# Además, verifica que no se produzcan falsos positivos al evaluar los ejemplos negativos,
# lo que indica que las reglas aprendidas son consistentes con los datos proporcionados.