#Búsqueda de Vuelta Atrás (Backtracking)
#Es un algoritmo utilizado para resolver problemas de satisfacción de restricciones (CSP) y otros problemas combinatorios.
#se basa en la exploracion sistemática y recursiva de las posibles asignaciones de valores a variables 
#asegurandose de que cada asginacion respete las restricciones del problema
# el algoritmo retrocede (backtrack) cuando se encuentra una asignacion que no satisface las restricciones
# el objetivo es encontrar una solucion valida o todas las soluciones posibles
#su aplicacion se puede ver en el sudoku, N-Reinas, problemas de coloreado de grafos, entre otros

#implementacion en un problema de coloreo de mapas 
#en este caso, el objetivo es colorear un mapa de manera que no haya dos regiones adyacentes del mismo color
#Librerias necesarias
from typing import Dict, List, Optional #para definir tipos de datos

#Clase de backtracking para resolver el problema de coloreo de mapas
class Backtracking:
    #funcion para inicializar el problema 
    #variables: lista de nombres de variables 
    #dominios: diccionario con valores posibles para cada variable.
    #restricciones:  iccionario con vecinos de cada variable 
    def __init__(self, variables: List[str], dominios: Dict[str, List[str]], restricciones: Dict[str, List[str]]): #__init__ es el constructor de la clase que se ejecuta al crear una instancia de la clase
        self.variables = variables #asignar variables a la instancia de la clase
        self.dominios = dominios #asignar dominios a la instancia de la clase
        self.restricciones = restricciones #asignar restricciones a la instancia de la clase
        self.asignaciones = {} #diccionario que almacenna la asignacion de variables a valores
    
    #funcion es_valido: Verifica si la asignación de 'valor' a 'variable' es válida según las restricciones
    def es_valido(self, variable: str, valor: str) -> bool: ##verifica si la asignacion es valida
        for vecino in self.restricciones.get(variable, []): #revisa los vecinos de la variable 
            if vecino in self.asignaciones and self.asignaciones[vecino] == valor: #si el vecino ya tiene un valor asignado y es igual al que se quiere asignar a la variable 
                return False #retorna False si hay conflicto
        return True #si no hay conflictos, retorna True
    
    #funcion resolver: inicia el algoritmo de backtracking para encontrar una solucion
    def resolver(self) -> Optional[Dict[str, str]]: #inicia el algoritmo de backtracking
        return self.backtrack() #llama a la funcion backtrack para resolver el problema
    
    #funcion backtrack: implementa el algoritmo de backtracking para encontrar una solucion
    def backtrack(self) -> Optional[Dict[str, str]]: #inicia el algoritmo de backtracking
        if len(self.asignaciones) == len(self.variables): #si todas las variables tienen asignacion 
            return self.asignaciones #retorna la asignacion completa
        
        variable = next(var for var in self.variables if var not in self.asignaciones) #selecciona la siguiente variable sin asignacion

        for valor in self.dominios[variable]: #probar cada valor en el dominio
            if self.es_valido(variable, valor): #si el valor cumple con las restricciones 
                self.asignaciones[variable] = valor #asigna el valor a la variable
                resultado = self.backtrack() #llama a la funcion backtrack recursivamente
                if resultado: 
                    return resultado #si se encuentra una solucion, retorna la asignacion
                del self.asignaciones[variable] #si no se encuentra una solucion, elimina la asignacion (backtrack)
        return None #si no se encuentra una solucion, retorna None
    

#Ejemplo del problema de coloreo de mapas
if __name__ == "__main__": 
    variables = ["A", "B", "C", "D"] #nombres de las variables (regiones del mapa)
    dominios = { var: ['Rojo', 'Verde', 'Azul'] for var in variables } #valores posibles para cada variable (colores)
    restricciones = { #restricciones entre las variables (regiones adyacentes)
        'A': ['B', 'C'],  #A no puede tener el mismo color que B o C
        'B': ['A', 'C', 'D'], #B no puede tener el mismo color que A, C o D
        'C': ['A', 'B', 'D'], #C no puede tener el mismo color que A, B o D
        'D': ['B', 'C'] #D no puede tener el mismo color que B o C

    }

    #Crear una instancia de la clase Backtracking 
    problema = Backtracking(variables, dominios, restricciones) #crear una instancia de la clase Backtracking con las variables, dominios y restricciones
    solucion = problema.resolver() #llamar a la funcion resolver para encontrar una solucion

    if solucion: #si se encuentra una solucion
        print("Solucion encontrada:")
        for variable, color in solucion.items(): #recorrer la asignacion de variables a colores
            print(f"{variable}: {color}") #imprimir la asignacion de cada variable
    else: #si no se encuentra una solucion
        print("No se encontro una solucion.")

#Ejemplo de salida: Solucion encontrada:
#                   A: Rojo
#                   B: Verde
#                   C: Azul
#                   D: Rojo
