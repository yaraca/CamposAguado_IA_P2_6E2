#Planificación Lógica Proposicional: SATPLAN
# SATPLAN es un algoritmo de planificación que:
# Transforma un problema de planificación en una fórmula de lógica proposicional (SAT).
# Usa un solver SAT (algoritmo que decide si una fórmula proposicional es satisfacible) para encontrar un plan.
#Funcionamiento:
# Codificación: Se modela el problema como una serie de proposiciones lógicas:
# Estados en distintos tiempos.
# Acciones que ocurren en esos tiempos.
# Efectos y precondiciones.
# Traducción a SAT:
# Se genera una fórmula lógica (en CNF) que expresa todas las restricciones del problema.
# Se busca un plan de longitud 1, luego de 2, y así sucesivamente.
# Resolución:
# Un SAT solver evalúa si hay alguna combinación de acciones que satisface las restricciones y alcanza la meta.
# Si la fórmula es satisfacible, se extrae el plan a partir de los literales verdaderos.
#Aplicaciones: planificacion de entornos, verificación de sistemas, razonamiento automatico, etc. 

#Ejemplo de SATPLAN: Apagar una lámpara encendida
# Estado inicial: Lámpara Encendida
# Acción: Presionar Interruptor
# Precondición: Lámpara Encendida
# Efecto: ¬Lámpara Encendida
# Meta:¬Lámpara Encendida (La lámpara está apagada)

#librerias necesarias
from pysat.solvers import Glucose3

#definir un diccionario de variables proposicionales con identificadores numéricos
variables = {
    'lamp_on_0': 1,  #estado en el que la lámpara está encendida en t=0
    'press_switch_0': 2,  #acción de presionar el interruptor en t=0
    'lamp_off_1': 3  #estado en el que la lámpara está apagada en t=1
}

#crear una lista para almacenar las cláusulas en forma normal conjuntiva (cnf)
clauses = []

#definir el estado inicial en t=0 con la lámpara encendida
clauses.append([variables['lamp_on_0']])

#definir la acción: si se presiona el interruptor en t=0, la lámpara se apaga en t=1
clauses.append([-variables['press_switch_0'], variables['lamp_off_1']])

#definir la condición para presionar el interruptor: solo si la lámpara está encendida en t=0
clauses.append([-variables['press_switch_0'], variables['lamp_on_0']])

#definir la meta: lograr que la lámpara esté apagada en t=1
clauses.append([variables['lamp_off_1']])

#crear una instancia del solucionador glucose3
solver = Glucose3()

#agregar todas las cláusulas definidas al solucionador
for clause in clauses:
    solver.add_clause(clause)

#intentar resolver el problema utilizando el solucionador
if solver.solve():
    #obtener el modelo que satisface las cláusulas
    model = solver.get_model()
    print("Plan encontrado:")
    #recorrer las variables y verificar cuáles son verdaderas en la solución
    for name, idx in variables.items():
        if idx in model:
            print(f"{name} = True")  #la variable es verdadera en el modelo
        elif -idx in model:
            print(f"{name} = False")  #la variable es falsa en el modelo
else:
    #indicar que no se encontró un plan válido
    print("No hay plan posible.")

#Ejemplo de salida: 
# Plan encontrado:
# lamp_on_0 = True
# press_switch_0 = False
# lamp_off_1 = True

# El ejemplo de salida nos muestra el plan encontrado por el algoritmo SATPLAN.
# Indica el estado inicial de la lámpara (lamp_on_0 = True), 
# que la acción de presionar el interruptor no se realizó (press_switch_0 = False),
# y que se logró el objetivo de apagar la lámpara (lamp_off_1 = True).