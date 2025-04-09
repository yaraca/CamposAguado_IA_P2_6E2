#Aprendizaje por refuerzo activo
#El agente no solo evalua una politica fija, sino que explora el entorno y mejora su politica de accion con el tiempo
#Aprende qué hacer y dónde hacerlo para maximizar su recompensa total
#Se compone de: exploración, explotación, modelo del entorno, actualización de la política, convergencia
#Se aplica en: robótica, juegos, sistemas de recomendación, etc.

#ejemplo de Aprendizaje por Refuerzo Activo
#LLegar al objetivo en una rejilla 3x3. Hay una recompensa de 1 al llegar al objetivo

#librerias necesarias
import random

#definir el entorno (rejilla 3x3)
estados = [(x, y) for x in range(3) for y in range(3)] 
acciones = ['arriba', 'abajo', 'izquierda', 'derecha'] #acciones posibles
estado_objetivo = (2, 2)  #estado que da recompensa

#Inicializar la Q-table (valores Q para cada par estado-acción)
Q = {}
for estado in estados:
    Q[estado] = {accion: 0.0 for accion in acciones} #inicializar Q(s,a) a 0 para cada acción en cada estado

#parámetros de aprendizaje
alpha = 0.1      #tasa de aprendizaje
gamma = 0.9      #factor de descuento
epsilon = 0.2    #probabilidad de explorar
episodios = 500  #número de episodios de entrenamiento

#función que aplica una acción y devuelve el nuevo estado y recompensa
def realizar_accion(estado, accion):
    x, y = estado
    if accion == 'arriba' and y > 0: #mover hacia arriba
        y -= 1 #si no está en el borde superior
    elif accion == 'abajo' and y < 2: #bajar
        y += 1 #si no está en el borde inferior
    elif accion == 'izquierda' and x > 0: #mover a la izquierda
        x -= 1 #si no está en el borde izquierdo
    elif accion == 'derecha' and x < 2: #mover a la derecha
        x += 1 #si no está en el borde derecho
    nuevo_estado = (x, y) #nuevo estado después de la acción
    recompensa = 1 if nuevo_estado == estado_objetivo else 0 #recompensa de 1 si se llega al objetivo, 0 en caso contrario
    return nuevo_estado, recompensa #devolver nuevo estado y recompensa

#entrenamiento del agente con Q-learning
for ep in range(episodios):
    estado = random.choice(estados)  #estado inicial aleatorio
    
    while estado != estado_objetivo:
        #selección de acción: exploración (aleatoria) o explotación (mejor acción conocida)
        if random.uniform(0, 1) < epsilon: #si se decide explorar
            accion = random.choice(acciones)    #seleccionar acción aleatoria
        else:
            #tomar la acción con mayor valor Q en ese estado
            accion = max(Q[estado], key=Q[estado].get) 
        
        #ejecutar acción y observar nuevo estado y recompensa
        nuevo_estado, recompensa = realizar_accion(estado, accion)

        #regla de actualización Q-learning:
        # Q(s,a) ← Q(s,a) + α [r + γ max_a' Q(s',a') - Q(s,a)]
        mejor_q_nuevo_estado = max(Q[nuevo_estado].values())
        Q[estado][accion] += alpha * (recompensa + gamma * mejor_q_nuevo_estado - Q[estado][accion])

        #avanzar al nuevo estado
        estado = nuevo_estado

#mostrar política aprendida
print("Política aprendida:")
for y in range(3):
    for x in range(3):
        estado = (x, y) #obtener la mejor acción para cada estado
        mejor_accion = max(Q[estado], key=Q[estado].get) #seleccionar la acción con mayor valor Q
        print(f"Estado {estado}: {mejor_accion}") #imprimir la mejor acción para cada estado

#Ejemplo de salida:
# Política aprendida:
# Estado (0, 0): derecha
# Estado (1, 0): abajo
# Estado (2, 0): abajo
# Estado (0, 1): abajo
# Estado (1, 1): abajo
# Estado (2, 1): abajo
# Estado (0, 2): derecha
# Estado (1, 2): derecha
# Estado (2, 2): arriba