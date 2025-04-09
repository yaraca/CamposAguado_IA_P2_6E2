#Q-Learning 
#Es un algoritmo que no necesita conocer cómo funciona el entorno, aprende directamente qué accion tomar en cada estado.
#para maximizar la recompensa total esperada
#Se compone de: agente(quien aprende), entorno(donde actua), estado(situacion actual), accion(que hace el agente)
#recompensa(retroalimentacion de la accion), Q(s,a) (valor esperado de tomar accion a en estado s)
#Se aplica en: juegos, robots, finanzas, asistentes inteligentes, etc.

#Ejemplo de Q-Learning
#Laberinto 4x4 donde se debe de llegar al objetivo
#Librerias necesarias
import random

#definir el entorno
filas, columnas = 4, 4
estados = [(x, y) for x in range(filas) for y in range(columnas)] #todos los estados posibles en la rejilla
acciones = ['arriba', 'abajo', 'izquierda', 'derecha'] #acciones posibles
objetivo = (3, 3) #estado objetivo donde se recibe recompensa

#inicializar la tabla Q con valores 0
Q = {}
for estado in estados:
    Q[estado] = {accion: 0.0 for accion in acciones} #inicializar Q(s,a) a 0 para cada acción en cada estado

#definir parámetros de aprendizaje
alpha = 0.1      #tasa de aprendizaje
gamma = 0.9      #factor de descuento
epsilon = 0.2    #probabilidad de exploración
episodios = 1000 #cantidad de episodios

#función para mover al agente en el entorno
def realizar_accion(estado, accion):
    x, y = estado
    if accion == 'arriba': #mover hacia arriba
        y = max(y - 1, 0) #si no está en el borde superior
    elif accion == 'abajo': #bajar
        y = min(y + 1, filas - 1) #si no está en el borde inferior
    elif accion == 'izquierda': #mover a la izquierda
        x = max(x - 1, 0) #si no está en el borde izquierdo
    elif accion == 'derecha': #mover a la derecha
        x = min(x + 1, columnas - 1) #si no está en el borde derecho
    
    nuevo_estado = (x, y) #nuevo estado después de la acción
    recompensa = 1 if nuevo_estado == objetivo else 0 #recompensa de 1 si se llega al objetivo, 0 en caso contrario
    return nuevo_estado, recompensa #devolver nuevo estado y recompensa

#entrenamiento con Q-Learning
for ep in range(episodios):
    estado = random.choice(estados)  #estado inicial aleatorio
    
    while estado != objetivo:
        #selección de acción: exploración o explotación
        if random.uniform(0, 1) < epsilon:  #decidir si explorar o explotar
            accion = random.choice(acciones)  #seleccionar acción aleatoria (exploración)
        else:
            accion = max(Q[estado], key=Q[estado].get)  #explotación (mejor acción conocida)
        
        #ejecutar la acción
        nuevo_estado, recompensa = realizar_accion(estado, accion) #obtener nuevo estado y recompensa

        #Q-Learning: actualizar la tabla Q
        max_q_nuevo = max(Q[nuevo_estado].values()) #valor máximo Q del nuevo estado
        #regla de actualización Q-learning:
        # Q(s,a) ← Q(s,a) + α [r + γ max_a' Q(s',a') - Q(s,a)]
        Q[estado][accion] += alpha * (recompensa + gamma * max_q_nuevo - Q[estado][accion]) #actualizar Q(s,a)

        #pasamos al nuevo estado
        estado = nuevo_estado

#mostrar la política aprendida
print("\nPolítica aprendida:")
for y in range(filas):
    for x in range(columnas):
        estado = (x, y)
        mejor_accion = max(Q[estado], key=Q[estado].get) #obtener la mejor acción para cada estado
        print(f"{estado}: {mejor_accion}") #imprimir la mejor acción para cada estado

#Ejemplo de salida:

# Política aprendida:
# (0, 0): derecha
# (1, 0): abajo
# (2, 0): abajo
# (3, 0): abajo
# (0, 1): arriba
# (1, 1): derecha
# (2, 1): abajo
# (3, 1): abajo
# (0, 2): derecha
# (1, 2): derecha
# (2, 2): derecha
# (3, 2): abajo
# (0, 3): arriba
# (1, 3): arriba
# (2, 3): arriba
# (3, 3): arriba