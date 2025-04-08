#Redes de decisión
#Esta es una extensión de las Redes Bayesianas que incluye decisiones y utilidades.
#Es una herramienta gráfica para representar y resolver problemas de toma de deicisiones bajo incertidumbre.
#Se compone de 3 tipos de nodos:
#- nodo aleatorio: representa variables inciertas 
#- nodo de decisión: representa decisiones a tomar
#- nodo de utilidad: representa la utilidad o valor asociado a un resultado
#El objetivo es maximizar la utilidad esperada al tomar decisiones.
#La red de decisión se resuelve utilizando el algoritmo de programación dinámica.
#Se definen las variables aleatorias con sus probabilidades, las decisiones posibles, y las utilidades asociadas a cada resultado.
#Luego se calcula la utilidad esperada para cada decisión y se elige la que maximiza la utilidad.

#Ejemplo de red de decisión
#Decidir si llevar paraguas o no 

# Probabilidad de lluvia
prob_lluvia = 0.4  # 40% de probabilidad de lluvia
prob_no_lluvia = 1 - prob_lluvia

# Opciones de decisión
decisiones = ['Llevar paraguas', 'No llevar paraguas']

# Utilidades asociadas a cada resultado
# (llueve, decisión) : utilidad
utilidades = {
    ('Lluvia', 'Llevar paraguas'): 80,
    ('Lluvia', 'No llevar paraguas'): 10,
    ('No Lluvia', 'Llevar paraguas'): 30,
    ('No Lluvia', 'No llevar paraguas'): 90
}

# Función para calcular la utilidad esperada de cada decisión
def utilidad_esperada(decision):
    utilidad = 0  # Inicializar utilidad
    # Lluvia
    utilidad += prob_lluvia * utilidades[('Lluvia', decision)]
    # No lluvia
    utilidad += prob_no_lluvia * utilidades[('No Lluvia', decision)]
    return utilidad

# Evaluar cada decisión
mejor_utilidad = float('-inf')  # Inicializar mejor utilidad
mejor_decision = None  # Inicializar mejor decisión
for decision in decisiones:  # Iterar sobre decisiones
    utilidad = utilidad_esperada(decision)  # Calcular utilidad esperada
    print(f"Utilidad esperada de '{decision}': {utilidad}")  # Imprimir utilidad esperada
    if utilidad > mejor_utilidad:  # Si la utilidad es mejor que la mejor utilidad
        mejor_utilidad = utilidad  # Actualizar mejor utilidad
        mejor_decision = decision  # Actualizar mejor decisión

print(f"\nLa mejor decisión es '{mejor_decision}' con una utilidad esperada de {mejor_utilidad}.")  # Imprimir mejor decisión y utilidad esperada

#Ejemplo de salida:
# Utilidad esperada de 'Llevar paraguas': 50.0
# Utilidad esperada de 'No llevar paraguas': 58.0

# La mejor decisión es 'No llevar paraguas' con una utilidad esperada de 58.0.

