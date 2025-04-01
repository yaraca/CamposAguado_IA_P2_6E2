#Propagacion de restricciones
#Es una técnica utilizada en los problemas de satisfacción de restricciones (CSP) para reducir el espacio de búsqueda y mejorar la eficiencia de los algoritmos de búsqueda.
#Esto se logra propagando restricciones de una variable a otra mediante la eliminacion de valores inconsistentes de los dominios de las variables.
#La propagacion de restricciones se puede aplicar en problemas como el sudoku, coloreo de grafos, asignacion de horarios, entre otros.
#La idea es que al asignar un valor a una variable, se eliminan los valores incompatibles de las variables futuras.

##Implementacion con el algoritmo AC-3 (Arc Consistency 3)
#Este es un metodo eficiente de propagacion de restricciones que se usa en CPS para hacer que los dominios sean consistentes en arco 

#Librerias necesarias
from collections import deque #para usar colas (FIFO)

#funcion AC3: implementacion del algoritmo AC-3 para la propagacion de restricciones
def AC3(CSP):
    cola = deque() # Cola para almacenar los arcos (direccionales)
    #inicializar la  cola con todos los arcos del grafo
    for var1 in CSP['variables']: #iterar sobre todas las variables
        for var2 in CSP['vecinos'][var1]: #iterar sobre los vecinos de cada variable
            cola.append((var1, var2)) #agregar los arcos a la cola
    
    while cola:
        var1, var2 = cola.popleft() #sacar el primer arco de la cola
        if revisar_arco(var1, var2, CSP):  #si se modificó el dominio de var1
            if not CSP['dominios'][var1]:   #si el dominio de var1 está vacío, no hay solución
                return False
            #rvisar arcos de vuelta vecinos de var1, excepto var2
            for vecino in CSP['vecinos'][var1]:
                if vecino != var2: #si el vecino no es el mismo que var2
                    cola.append((vecino, var1)) #agregar restricciones afectadas de vuelta a la cola
    return True

#funcion revisar_arco: revisa si el arco (var1, var2) es consistente
def revisar_arco(var1, var2, CSP):
    dominio_reducido = False #inicializar la variable de dominio reducido
    valores_a_eliminar = set() #inicializar el conjunto de valores a eliminar
    
    for valor1 in list(CSP['dominios'][var1]):  #iterar sobre copia del dominio
        #verificar si hay minimo un valor en var2 que cumpla la restricción
        restriccion_valida = False
        for valor2 in CSP['dominios'][var2]: ##iterar sobre los valores del dominio de var2
            #aplicar la restricción específica entre var1 y var2
            if (var1, var2) in CSP['restricciones']: #si llega a haber una restricción explícita
                if CSP['restricciones'][(var1, var2)](valor1, valor2): #si la restricción se cumple
                    restriccion_valida = True #marcar que la restricción es válida
                    break
            else:  #restriccion por defecto (no explícita)
                if valor1 != valor2: #si los valores son diferentes
                    restriccion_valida = True #marcar que la restricción es válida
                    break
        
        if not restriccion_valida: #si no hay valores válidos en var2 para el valor1
            valores_a_eliminar.add(valor1) #agregar el valor1 a los valores a eliminar
    
    if valores_a_eliminar: #si hay valores a eliminar
        CSP['dominios'][var1] -= valores_a_eliminar #eliminar los valores inválidos del dominio de var1
        dominio_reducido = True #marcar que el dominio fue reducido
    
    return dominio_reducido #retornar si el dominio fue reducido o no

#Ejemplo de propagacion de restricciones con el algoritmo AC-3
if __name__ == "__main__":
    CSP = {
        'variables': ['A', 'B', 'C'], #nombres de las variables 
        'dominios': { #valores posibles para cada variable
            'A': {1, 2, 3, 4},
            'B': {2, 3, 4},
            'C': {3, 4, 5}
        },
        'vecinos': { #definir los vecinos de cada variable (arcos)
            'A': ['B', 'C'],
            'B': ['A', 'C'],
            'C': ['A', 'B']
        },
        'restricciones': { #definir las restricciones entre las variables
            ('A', 'B'): lambda x, y: x > y,    # A debe ser mayor que B
            ('B', 'C'): lambda x, y: x == y//2 # B debe ser la mitad de C 
        }
    }

    print("Dominios antesde AC3:")
    for variable, dominio in CSP['dominios'].items(): #imprimir los dominios antes de aplicar AC3
        print(f"{variable}: {dominio}")

    if AC3(CSP):
        print("\nDominios despues de AC3:") #imprimir los dominios después de aplicar AC3
        for variable, dominio in CSP['dominios'].items():
            print(f"{variable}: {dominio}")
    else:
        print("\nNo hay solución posible")