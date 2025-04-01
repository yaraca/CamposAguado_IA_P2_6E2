#Comprobación hacia delante (Forward Checking)
#Es una técnica utilizada en algoritmos de búsqueda para resolver problemas de satisfacción de restricciones (CSP).
#Esta mejora la eficiencia de la busqueda de vuelta atras (backtracking) al reducir el espacio de busqueda
#SU objetivo es reducir el espacio de busqueda eliminando valores de los dominios de variables futuras, antes de llegar a ellas 
#se pueden aplicar en sudokus, coloreo de grafos, asignacion de horarios, planificacion de rutas.
#La idea es que al asignar un valor a una variable, se eliminan los valores incompatibles de las variables futuras


#Implementacion del forward checking en un problema de coloreo de mapas
#Librerias necesarias
import copy #para hacer copias profundas de objetos

#Funcion es_valido: veridicar si un color puede asignarse aun nodo sin romper las restricciones
def es_valido(nodo, color, asignacion, grafo): 
    for vecino in grafo[nodo]: #revisa los vecinos del nodo
        if vecino in asignacion and asignacion[vecino] == color: #si el vecino ya tiene un color asignado y es igual al que se quiere asignar a la variable 
            return False #retorna False si hay conflicto
    return True #si no hay conflictos, retorna True

#funcion forward_checking: comprueba si la asignacion de un color a un nodo es valida y elimina los colores incompatibles de los nodos vecinos
def forward_checking(nodo, color, dominios, grafo): 
    #crear una copia de los dominios para no modificar el original 
    dominios_copia = copy.deepcopy(dominios)

    #asignar el color al nodo 
    for vecino in grafo[nodo]:
        if color in dominios_copia[vecino]: #si el color es valido para el vecino
            dominios_copia[vecino].remove(color) #eliminar el color del dominio del vecino
            if not dominios_copia[vecino]: #si un vecino se queda sin opciones, la asignacion es inválida 
                return None
    return dominios_copia #retornar los dominios actualizados

#funcion resolver_coloreo: algoritmo de busqueda con comprobacion hacia delante 
def resolver_coloreo(grafo, colores, asignacion = {}, dominios = None): 
    if dominios is None: # inicializar los dominios con todos los colores posibles 
        dominios = {nodo: list(colores) for nodo in grafo} #crear un diccionario con los nodos y los colores posibles
    
    #si todas las variables estan asignadas,se encuentra la solucion 
    if len(asignacion) == len(grafo): 
        return asignacion #retornar la asignacion completa
    
    #seleccionar la siguiente variable sin asignar
    nodo = min([n for n in grafo if n not in asignacion], key = lambda x: len(dominios[x])) #seleccionar el nodo con menos opciones (heuristica de la menor restriccion)
    for color in dominios[nodo]: #probar cada color en el dominio
        if es_valido(nodo, color, asignacion, grafo): #si el color es valido 
            asignacion[nodo] = color #asignar el color al nodo
            nuevos_dominios = forward_checking(nodo, color, dominios, grafo) #llamar a la funcion forward_checking para eliminar los colores incompatibles de los nodos vecinos

            if nuevos_dominios is not None: #si la asignacion es valida
                resultado = resolver_coloreo(grafo, colores, asignacion, nuevos_dominios) #llamar a la funcion recursivamente
                if resultado: #si se encuentra una solucion 
                    return resultado
            del asignacion[nodo] #si no se encuentra una solucion, eliminar la asignacion (backtrack)
    return None #si no se encuentra una solucion, retornar None

#Ejemplo del problema de coloreo de mapas
if __name__ =="__main__":
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }

    colores = ['Rojo', 'Verde', 'Azul'] #colores disponibles

    solucion = resolver_coloreo(grafo, colores) #llamar a la funcion resolver_coloreo para encontrar una solucion

    if solucion: #si se encuentra una solucion
        print("Solucion encontrada:")
        for nodo, color in solucion.items():#recorrer la asignacion de nodos a colores 
            print(f"Nodo {nodo}: Color {color}")
    else: #si no se encuentra una solucion
        print("No se encontro una solucion.")

#Ejemplo de salida: Solucion encontrada:
#                                       Nodo A: Color Rojo
#                                       Nodo B: Color Verde
#                                       Nodo C: Color Azul
#                                       Nodo D: Color Rojo