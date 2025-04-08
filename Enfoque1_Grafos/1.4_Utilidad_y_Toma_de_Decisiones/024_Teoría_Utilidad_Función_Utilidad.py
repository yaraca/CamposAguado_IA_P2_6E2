#Teoría de la Utilidad: Función Utilidad
#Este es un modelo matemático que representa las preferencias de un indiivido frente a diversas alternativas o decisiones
#Se usa para elegir la mejor opcion basandose en las consecuencias, la probabilidad y la utilidad de cada resultado
#Cada posible accion tiene varias consecuencias, cada consecuencia tiene una probabilidad, cada consecuencia tiene una utilidad numérica
#El agente elige la acción que maximiza la utilidad esperada UE = P(consecuencias) * U(consecuencias), probabilidad de la consecuencias * utilidad 
#Se aplica en la toma de decisiones en IA, sistemas expertos, planificación bajo incertidumbre, economía y teoría de juegos

#Ejemplo de la función de utilidad
#Un agente tiene tiene 3 acciones posibles: A=lanzar campaña, B= reducir precios, C= mejorar producto
#Cada accion puede tener distintas consecuencias con probabilidades y utilidades
#diccionario de acciones y consecuencias
acciones = { 
    'Campaña Publicitaria': [
        {'probabilidad': 0.6, 'utilidad': 80},  #exito en ventas
        {'probabilidad': 0.4, 'utilidad': 20}   #poco impacto
    ],
    'Reducir Precios': [
        {'probabilidad': 0.7, 'utilidad': 60},  #aumento en ventas
        {'probabilidad': 0.3, 'utilidad': 10}   #margen reducido
    ],
    'Mejorar Producto': [
        {'probabilidad': 0.5, 'utilidad': 90},  #fidelidad del cliente
        {'probabilidad': 0.5, 'utilidad': 30}   #retraso en el lanzamiento
    ]
}

#Función para calcular la utilidad esperada de cada acción
def utilidad_esperada(consecuencias): 
    utilidad_esperada = 0 #inicializa la utilidad esperada en 0
    for c in consecuencias: #itera sobre las consecuencias
        utilidad_esperada += c['probabilidad'] * c['utilidad'] #suma la probabilidad por la utilidad de cada consecuencia
    return utilidad_esperada #devuelve la utilidad esperada total

#calcular la utilidad esperada de cada acción
utilidades = {} #inicializa un diccionario para almacenar las utilidades esperadas
for accion, consecuencias in acciones.items(): #itera sobre las acciones y sus consecuencias 
    UEsperada = utilidad_esperada(consecuencias) #calcula la utilidad esperada de cada acción
    utilidades[accion] = UEsperada #almacena la utilidad esperada en el diccionario
    print(f"Utilidad esperada de {accion}: {UEsperada}") #imprime la utilidad esperada de cada acción

#seleccionar la mejor acción con mayor utilidad esperada
mejor_accion = max(utilidades, key=utilidades.get) #obtiene la acción con la mayor utilidad esperada
print(f"\nLa mejor acción es: {mejor_accion} con una utilidad esperada de {utilidades[mejor_accion]}") #imprime la mejor acción y su utilidad esperada

#Ejemplo de salida:
# Utilidad esperada de Campaña Publicitaria: 56.0
# Utilidad esperada de Reducir Precios: 45.0
# Utilidad esperada de Mejorar Producto: 60.0

# La mejor acción es: Mejorar Producto con una utilidad esperada de 60.0