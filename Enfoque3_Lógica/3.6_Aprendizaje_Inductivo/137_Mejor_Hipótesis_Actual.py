#Mejor Hipotesis Actual
#busca aprender un concepto general a partir de ejemplos positivos y negativos, manteniendo un conjunto de hipótesis consistentes con los datos vistos hasta ahora.
#Es una técnica basada en lógica que permite acotar el espacio de hipótesis, manteniendo solo las que no contradicen ningún ejemplo visto.
#Funcionamiento:
# Este algoritmo mantiene dos conjuntos:
# S (específica): la hipótesis más específica que concuerda con todos los ejemplos positivos.
# G (general): las hipótesis más generales que también concuerdan con los ejemplos positivos y no con los negativos.
# Si el ejemplo es positivo:
# Generaliza S para incluir el nuevo ejemplo. Elimina hipótesis de G que no lo cubran.
# Si el ejemplo es negativo:
# Especializa G para excluir ese ejemplo. Elimina hipótesis de S que lo cubran.
#Aplicaciones: Reconocimiento de patrones, clasificación, aprendizaje automático.

#Ejemplo de mejor hipótesis actual

#definir el dataset de entrenamiento con ejemplos clasificados por color, forma y superficie
datos_entrenamiento=[
    (['Rojo', 'Circular', 'Liso'], 'Sí'),      #positivo
    (['Rojo', 'Cuadrado', 'Liso'], 'Sí'),      #positivo
    (['Verde', 'Circular', 'Rugoso'], 'No'),   #negativo
    (['Rojo', 'Circular', 'Rugoso'], 'Sí'),    #positivo
]

#definir una función para inicializar las hipótesis más específica y más general
def inicializar_hipotesis(longitud):
    S=['Ø']*longitud  #hipótesis más específica inicializada con valores neutros
    G=[['?']*longitud]  #hipótesis más general inicializada con valores desconocidos
    return S, G  #retornar las hipótesis iniciales

#definir una función para verificar si una hipótesis cubre un ejemplo dado
def cubre(h, x):
    return all(h[i]=='?' or h[i]==x[i] for i in range(len(h)))  #verificar coincidencias

#definir una función para especializar una hipótesis general cuando se encuentra un ejemplo negativo
def especializar(h, x):
    resultado=[]  #lista para almacenar hipótesis especializadas
    for i in range(len(h)):  #recorrer los atributos de la hipótesis
        if h[i]=='?':  #si el atributo es desconocido, probar valores específicos
            for valor in ['Rojo', 'Verde', 'Azul', 'Circular', 'Cuadrado', 'Rugoso', 'Liso']:
                if valor!=x[i]:  #descartar el valor negativo en la especialización
                    nueva=h[:]  #crear una copia de la hipótesis
                    nueva[i]=valor  #asignar el nuevo valor al atributo
                    resultado.append(nueva)  #agregar la hipótesis especializada a la lista
    return resultado  #retornar la lista de hipótesis especializadas

#definir la función principal del algoritmo para encontrar la mejor hipótesis actual
def mejor_hipotesis_actual(datos):
    S, G=inicializar_hipotesis(len(datos[0][0]))  #inicializar hipótesis específicas y generales

    for x, resultado in datos:  #recorrer cada ejemplo en el conjunto de datos
        if resultado=='Sí':  #si el ejemplo es positivo
            for i in range(len(S)):  #generalizar la hipótesis específica
                if S[i]=='Ø':  #si el atributo es vacío, asignar el valor del ejemplo
                    S[i]=x[i]
                elif S[i]!=x[i]:  #si hay conflicto, asignar un valor desconocido
                    S[i]='?'
            G=[g for g in G if cubre(g, x)]  #eliminar hipótesis generales que no cubren el positivo
        else:  #si el ejemplo es negativo
            nuevas_G=[]  #crear una nueva lista de hipótesis generales
            for g in G:  #recorrer cada hipótesis en G
                if cubre(g, x):  #si la hipótesis cubre el negativo, especializarla
                    nuevas_G.extend(especializar(g, x))
                else:
                    nuevas_G.append(g)  #mantener la hipótesis si no cubre el negativo
            G=nuevas_G  #actualizar la lista de hipótesis generales
        print(f"Ejemplo: {x} -> {resultado}")  #mostrar el ejemplo procesado
        print(f"S (específica): {S}")  #mostrar la hipótesis específica actualizada
        print(f"G (general): {G}\n")  #mostrar la hipótesis general actualizada

    return S, G  #retornar las hipótesis finales obtenidas

#ejecutar el algoritmo para encontrar las hipótesis finales
S_final, G_final=mejor_hipotesis_actual(datos_entrenamiento)

#mostrar los resultados finales de las hipótesis específicas y generales
print("Hipótesis final específica:", S_final)
print("Hipótesis final general:", G_final)

#Ejemplo de salida: 
# Ejemplo: ['Rojo', 'Circular', 'Liso'] -> Sí
# S (específica): ['Rojo', 'Circular', 'Liso']
# G (general): [['?', '?', '?']]

# Ejemplo: ['Rojo', 'Cuadrado', 'Liso'] -> Sí
# S (específica): ['Rojo', '?', 'Liso']
# G (general): [['?', '?', '?']]

# Ejemplo: ['Verde', 'Circular', 'Rugoso'] -> No
# S (específica): ['Rojo', '?', 'Liso']
# G (general): [['Rojo', '?', '?'], ['Azul', '?', '?'], ['Circular', '?', '?'], ['Cuadrado', '?', '?'], ['Rugoso', '?', '?'], ['Liso', '?', '?'], ['?', 'Rojo', '?'], ['?', 'Verde', '?'], ['?', 'Azul', '?'], ['?', 'Cuadrado', '?'], ['?', 'Rugoso', '?'], ['?', 'Liso', '?'], ['?', '?', 'Rojo'], ['?', '?', 'Verde'], ['?', '?', 'Azul'], ['?', '?', 'Circular'], ['?', '?', 'Cuadrado'], ['?', '?', 'Liso']]

# Ejemplo: ['Rojo', 'Circular', 'Rugoso'] -> Sí
# S (específica): ['Rojo', '?', '?']
# G (general): [['Rojo', '?', '?']]

# Hipótesis final específica: ['Rojo', '?', '?']
# Hipótesis final general: [['Rojo', '?', '?']]

# El ejemplo de salida nos demuestra cómo el algoritmo ajusta las hipótesis específicas (S) y generales (G) 
# a medida que procesa cada ejemplo del conjunto de datos de entrenamiento.
# Para cada ejemplo positivo, S se generaliza para incluir el ejemplo, mientras que G se filtra para eliminar 
# hipótesis que no cubren el ejemplo.
# Para cada ejemplo negativo, G se especializa para excluir el ejemplo, mientras que S permanece sin cambios 
# si ya no cubre el ejemplo negativo.
# Al final, las hipótesis específicas y generales reflejan el conocimiento aprendido del conjunto de datos, 
# con S representando la hipótesis más específica y G las hipótesis más generales consistentes con los datos.
