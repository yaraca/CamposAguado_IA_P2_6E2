#Planificación Continua y Multiagente
# Planificación Continua:
# El entorno y los objetivos pueden cambiar constantemente, por lo que los agentes deben replanificar de forma dinámica y constante, incluso mientras ejecutan acciones.
# Planificación Multiagente:
# Involucra varios agentes que:
# Colaboran para lograr metas comunes.
# Coordinan acciones para evitar conflictos (como colisiones).
# Pueden actuar de forma paralela o distribuida.
#Funcionamiento;
# Cada agente tiene: Su propio estado, objetivo y plan.
# Hay un coordinador (explícito o implícito) que ayuda a: Evitar conflictos. Coordinar tareas compartidas.
# Si algún evento imprevisto ocurre, cada agente puede: Actualizar su plan individual. Comunicar cambios a los demás agentes.
#Aplicaciones: robots autónomos, vehículos autónomos, drones, sistemas de producción industrial, etc.

#Ejemplo de Planificación Continua y Multiagente
#Dos robots quieren llegar a diferentes objetivos en una misma cuadrícula, evitando colisionar entre ellos y adaptándose si uno cambia de objetivo.

#librerías necesarias
import random #para generar números aleatorios

#definir el tamaño del mapa como una matriz 5x5 inicializada con valores de 0 (espacios libres)
TAM=5
mapa=[[0 for _ in range(TAM)] for _ in range(TAM)]

#definir los agentes con sus posiciones iniciales y objetivos
agentes={
    "R1": {"pos": [0, 0], "objetivo": [4, 4]},  #el agente R1 empieza en la esquina superior izquierda y su objetivo es la esquina inferior derecha
    "R2": {"pos": [4, 0], "objetivo": [0, 4]},  #el agente R2 empieza en la esquina inferior izquierda y su objetivo es la esquina superior derecha
}

#definir una función para calcular un plan de movimiento en línea recta hacia el objetivo
def planear(agente):
    x, y=agente["pos"]  #obtener la posición inicial del agente
    gx, gy=agente["objetivo"]  #obtener la meta del agente
    plan=[]  #crear una lista para almacenar los movimientos
    while x!=gx or y!=gy:  #repetir mientras no se alcance el objetivo
        if x<gx: x+=1  #moverse hacia abajo si es posible
        elif x>gx: x-=1  #moverse hacia arriba si es posible
        elif y<gy: y+=1  #moverse hacia la derecha si es posible
        elif y>gy: y-=1  #moverse hacia la izquierda si es posible
        plan.append([x, y])  #guardar la nueva posición en el plan
    return plan  #retornar el plan generado

#definir una función para ejecutar el movimiento de múltiples agentes de forma continua
def simular_movimiento():
    pasos=0  #contador de pasos en la simulación
    planes={a: planear(agentes[a]) for a in agentes}  #generar planes individuales para cada agente

    while any(planes[a] for a in agentes):  #mientras haya movimientos pendientes
        pasos+=1
        print(f"\n Paso {pasos}")  #mostrar el número de paso actual
        ocupados=[]  #lista para evitar colisiones entre agentes

        #recorrer cada agente y ejecutar su movimiento
        for nombre, agente in agentes.items():
            if planes[nombre]:  #verificar si el agente tiene movimientos pendientes
                siguiente=planes[nombre][0]  #obtener el siguiente paso en el plan

                #verificar si el espacio está ocupado por otro agente
                if siguiente not in ocupados:
                    ocupados.append(siguiente)  #marcar el espacio como ocupado
                    agente["pos"]=siguiente  #actualizar la posición del agente
                    planes[nombre].pop(0)  #eliminar el paso ya ejecutado
                    print(f" {nombre} se movió a {siguiente}")  #mostrar el movimiento exitoso
                else:
                    print(f" {nombre} esperó para evitar colisión")  #mostrar que el agente esperó para evitar una colisión

        #simular un cambio dinámico en el entorno (el agente R1 cambia su objetivo en el paso 3)
        if pasos==3:
            print(" R1 cambió su objetivo a [0,0]")  #mostrar el cambio de objetivo
            agentes["R1"]["objetivo"]=[0, 0]  #actualizar la meta de R1
            planes["R1"]=planear(agentes["R1"])  #generar un nuevo plan para R1

    print("\n Todos los agentes llegaron a sus destinos.")  #mensaje final cuando todos los agentes alcanzan sus metas

#ejecutar la simulación de movimiento multiagente
simular_movimiento()

#Ejemplo de salida:
#  Paso 1
#  R1 se movió a [1, 0]
#  R2 se movió a [3, 0]

#  Paso 2
#  R1 se movió a [2, 0]
#  R2 esperó para evitar colisión

#  Paso 3
#  R1 se movió a [3, 0]
#  R2 se movió a [2, 0]
#  R1 cambió su objetivo a [0,0]

#  Paso 4
#  R1 se movió a [2, 0]
#  R2 se movió a [1, 0]

#  Paso 5
#  R1 se movió a [1, 0]
#  R2 se movió a [0, 0]

#  Paso 6
#  R1 se movió a [0, 0]
#  R2 se movió a [0, 1]

#  Paso 7
#  R2 se movió a [0, 2]

#  Paso 8
#  R2 se movió a [0, 3]

#  Paso 9
#  R2 se movió a [0, 4]

#  Todos los agentes llegaron a sus destinos.

# El ejemplo de salida nos muestra cómo los agentes se mueven paso a paso hacia sus objetivos.
# También ilustra cómo los agentes evitan colisiones al esperar si otro agente ocupa la posición deseada.
# Además, demuestra cómo un agente puede adaptarse dinámicamente a un cambio en su objetivo durante la simulación.
# Finalmente, confirma que todos los agentes alcanzan sus destinos al finalizar la simulación.