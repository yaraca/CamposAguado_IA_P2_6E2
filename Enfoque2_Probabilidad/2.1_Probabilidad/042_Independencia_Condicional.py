#Independencia Condicional
#significa que dos eventos A y B son independientes dado un tercer evento C. Es decir, saber C es irrelevante para la probabilidad de A dado B, y viceversa.
#Se denota como P(A|B,C) = P(A|C) #la probabilidad de A dado B y C es igual a la probabilidad de A dado C.
#esta reduce la complejidad de los modelos probabilísticos y permite simplificar cálculos en inferencia bayesiana.
#mejora el rendimiento y escalabilidad de los algoritmos de aprendizaje automático.
#se utiliza en el diagnostico medico (sintomas independientes dado una enfermedad), procesamiento de lenguaje natural (palabras independientes dado un tema), sistemas de recomendacion (productos independientes dado un usuario), etc.

#Ejemplo de independencia condicional
#C = lluvia, A = pasto mojado, B = paraguas
#la probabilidad de que el césped esté mojado depende de la lluvia o del aspersor. Pero si se sabe que llovió, la activación del aspersor puede ser irrelevante.

#librerias necesarias
import pandas as pd #para simular el concepto de independencia condicional que se refiere a la dependencia entre variables aleatorias

#tabla de probabilidades conjuntas
#lluvia (C), aspersor (B), pasto mojado (A)
#base de daros simulada
datos = pd.DataFrame([ 
    {"lluvia": True,  "aspersor": True,  "mojado": True},
    {"lluvia": True,  "aspersor": False, "mojado": True},
    {"lluvia": False, "aspersor": True,  "mojado": True},
    {"lluvia": False, "aspersor": False, "mojado": False},
    {"lluvia": True,  "aspersor": True,  "mojado": True},
    {"lluvia": True,  "aspersor": False, "mojado": True},
    {"lluvia": False, "aspersor": True,  "mojado": True},
    {"lluvia": False, "aspersor": False, "mojado": False},
])

#funcion para estimar P(A|B,C) la probabilidad de A dado B y C
def prob_condicional(df, A, B=None, C=None): #probabilidad de A dado B y C
    df_filtrado = df.copy() #crear una copia del dataframe para no modificar el original

    if B is not None: #si B no es None, filtrar el dataframe por B
        for var, val in B.items(): #iterar sobre las variables y valores de B
            df_filtrado = df_filtrado[df_filtrado[var] == val] #filtrar el dataframe por la variable y su valor

    if C is not None: #si C no es None, filtrar el dataframe por C
        for var, val in C.items(): #iterar sobre las variables y valores de C
            df_filtrado = df_filtrado[df_filtrado[var] == val] #filtrar el dataframe por la variable y su valor

    total = len(df_filtrado) #contar el total de filas en el dataframe filtrado
    if total == 0: #si el total es 0, no se puede calcular la probabilidad
        return 0

    positivos = len(df_filtrado[df_filtrado[A] == True]) #contar el total de filas donde A es True en el dataframe filtrado
    return positivos / total #calcular la probabilidad de A dado B y C

#funcion para comprobar la independencia condicional
def verificar_independencia_condicional():
    print("Probabilidades condicionales:")

    #sin condicionamiento
    p1 = prob_condicional(datos, "mojado", B={"aspersor": True}, C={"lluvia": True}) #probabilidad de mojado dado aspersor (True) y lluvia (True)
    p2 = prob_condicional(datos, "mojado", B={"aspersor": False}, C={"lluvia": True})  #probabilidad de mojado dado aspersor (False) y lluvia (True)
    p3 = prob_condicional(datos, "mojado", C={"lluvia": True})  #probabilidad de mojado dado lluvia (True)

    #imprimir resultados
    print(f"P(mojado | aspersor=Sí, lluvia=Sí)  = {p1:.2f}") #probabilidad de mojado dado aspersor (True) y lluvia (True)
    print(f"P(mojado | aspersor=No, lluvia=Sí)  = {p2:.2f}") #probabilidad de mojado dado aspersor (False) y lluvia (True)
    print(f"P(mojado | lluvia=Sí)               = {p3:.2f}") #probabilidad de mojado dado lluvia (True)

    #verificar si P(mojado | aspersor, lluvia) ≈ P(mojado | lluvia)
    if abs(p1 - p3) < 0.05 and abs(p2 - p3) < 0.05: #si la diferencia entre las probabilidades es menor a 0.05, se cumple la independencia condicional
        print("\nConclusión: Aspersor ⊥ Césped Mojado | Lluvia -> (Independencia condicional)") 
    else:
        print("\nNo se cumple la independencia condicional") #si no se cumple la independencia condicional, imprimir mensaje

#llamar a la funcion para verificar la independencia condicional
verificar_independencia_condicional() #llamar a la funcion para verificar la independencia condicional

#Ejemplo de salida:
# Probabilidades condicionales:
# P(mojado | aspersor=Sí, lluvia=Sí)  = 1.00
# P(mojado | aspersor=No, lluvia=Sí)  = 1.00
# P(mojado | lluvia=Sí)               = 1.00

# Conclusión: Aspersor ⊥ Césped Mojado | Lluvia -> (Independencia condicional) 
#una vez que sabemos que llovió, el hecho de que se haya encendido el aspersor no cambia la probabilidad de que el césped esté mojado.


