#Regla de la cadena 
#es una forma de descomponer una probabilidad conjunta en un producto de probabilidades condicioneles.
#la probabilidad conjunta se puede escribir como:
#P(X1, X2, ..., Xn) = P(X1) * P(X2|X1) * P(X3|X1, X2) * ... * P(Xn|X1, X2, ..., Xn-1)
#donde P(X1) es la probabilidad de X1, P(X2|X1) es la probabilidad de X2 dado X1, y así sucesivamente.
#Con esto podemos calcular la probabilidad conjunta de muchas variables, multiplicando sus probabilidades condicionales una tras otra
#se usa para modelar sistemas complejos, evaluar modelos probabilísiticos, entrenamiento de modelos de IA, etc.

#ejemplo de la regla de la cadena
#supongamos que tenemos tres variables aleatorias: A, B y C.
#A = tormenta (Si o No), B = tráfico (Si o No) y C = llegar tarde al trabajo (Si o No)
#se tienen las siguientes probabilidades:
#P(A), P(B|A), P(C|A, B)
#Calcular la probabilidad conjunta P(A, B, C) usando la regla de la cadena

#definir las probabilidad basicas 
#probabilidad de tormenta
P_A = {
    'si': 0.3, #probabilidad de tormenta
    'no': 0.7 #probabilidad de no tormenta
}

#probabilidad de tráfico dado que hay tormenta
P_B_dado_A = {
    'si': {'si': 0.8, 'no': 0.2},   #P(B='si' | A='si') = 0.8 # probabilidad de tráfico dado que hay tormenta
    'no': {'si': 0.3, 'no': 0.7}    #P(B='si' | A='no') = 0.3 # probabilidad de tráfico dado que no hay tormenta
}

#probabilidad de llegar tarde dado que hay tormenta y tráfico
P_C_dado_AB = {
    'si': {
        'si': {'si': 0.9, 'no': 0.1},  # P(C='si' | A='si', B='si') = 0.9 # probabilidad de llegar tarde dado que hay tormenta y tráfico
        'no': {'si': 0.5, 'no': 0.5} # P(C='si' | A='si', B='no') = 0.5 # probabilidad de llegar tarde dado que hay tormenta y no hay tráfico
    },
    'no': {
        'si': {'si': 0.6, 'no': 0.4}, # P(C='si' | A='no', B='si') = 0.6 # probabilidad de llegar tarde dado que no hay tormenta y tráfico
        'no': {'si': 0.1, 'no': 0.9} # P(C='si' | A='no', B='no') = 0.1 # probabilidad de llegar tarde dado que no hay tormenta y no hay tráfico
    }
}

#regla de la cadena: P(A, B, C) = P(A) * P(B|A) * P(C|A, B)
#funcion para calcular la probabilidad conjunta P(A, B, C) para A='si', B='si', C='si'
def calcular_probabilidad_conjunta(a, b, c):
    p_a = P_A[a] # P(A)
    p_b_dado_a = P_B_dado_A[a][b] # P(B|A)
    p_c_dado_ab = P_C_dado_AB[a][b][c] # P(C|A, B)

    probabilidad = p_a * p_b_dado_a * p_c_dado_ab # P(A, B, C) = P(A) * P(B|A) * P(C|A, B)
    return probabilidad #probabilidad conjunta

#probabilidad de que haya tormenta, tráfico y llegar tarde al trabajo
prob = calcular_probabilidad_conjunta('si', 'si', 'si') #probabilidad de que haya tormenta, tráfico y llegar tarde al trabajo
print("P(A='si', B='si', C='si') =", prob) 

#probabilidad de que no haya tormenta, tráfico y llegar tarde al trabajo
print("P(A='no', B='si', C='no') =", calcular_probabilidad_conjunta('no', 'si', 'no')) 

#ejemplo de salida:
# P(A='si', B='si', C='si') = 0.216
# P(A='no', B='si', C='no') = 0.084
#en este ejemplo, la probabilidad de que haya tormenta, tráfico y llegar tarde al trabajo es 0.216
#y la probabilidad de que no haya tormenta, tráfico y llegar tarde al trabajo es 0.084
#esto significa que es más probable que haya tormenta, tráfico y llegar tarde al trabajo que no haya tormenta, tráfico y llegar tarde al trabajo