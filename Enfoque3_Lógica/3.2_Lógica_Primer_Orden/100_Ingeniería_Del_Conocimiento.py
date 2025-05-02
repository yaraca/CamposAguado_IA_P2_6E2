#Ingeniería del Conocimiento
#Es el proceso de capturar, representar, organizar, y  Mantener el conocimiento experto en una base de conocimiento, para que un sistema inteligente pueda razonar, inferir y tomar decisiones.
#Se utilizan herramientas de la lógica de primer orden para representar:
#Hechos, reglas, relaciones entre objetos, inferencias basadas en hechos conocidos, etc. 
#Componentes principales: 
# Base de Conocimiento (KB): Conjunto de hechos y reglas.
# Motor de Inferencia: Algoritmo que deduce nuevo conocimiento a partir del existente.
# Interfaz de Usuario: Para consulta o retroalimentación
#Aplicaciones: Diagnóstico médico, sistemas de recomendación, control de procesos industriales, etc.

#Ejemplo de ingeniería del conocimiento: Diagnóstico de plantas

# Base de conocimiento (hechos y reglas)
conocimiento = {
    "falta_agua": False,
    "hojas_amarillas": True,
    "flores_marchitas": True,
    "raices_sanas": True
}

#Función para detectar falta de agua
def detectar_falta_agua(facts):
    return facts["hojas_amarillas"] and facts["flores_marchitas"] #regresa True si hay falta de agua

#Función para determinar si la planta está sana
def planta_sana(facts):
    return facts["raices_sanas"] and not detectar_falta_agua(facts) #regresa True si la planta está sana

#Función de Motor de inferencia 
def sistema_experto(facts):
    print("Análisis de planta...\n")

    if detectar_falta_agua(facts): #si hay falta de agua
        print("Diagnóstico: La planta podría tener falta de agua.")
    else: #si no hay falta de agua
        print("Diagnóstico: No hay señales claras de deshidratación.")

    if planta_sana(facts): #si la planta está sana
        print("Estado general: La planta parece estar sana.")
    else: #si la planta no está sana
        print("Estado general: La planta muestra signos de problema.")

# Ejecutar el sistema experto
sistema_experto(conocimiento) 

#Ejemplo de salida: 
# Análisis de planta...

# Diagnóstico: La planta podría tener falta de agua.
# Estado general: La planta muestra signos de problema.
#Como se puede ver, el sistema experto analiza los hechos y proporciona un diagnóstico basado en reglas predefinidas.
#en este caso, la planta tiene hojas amarillas y flores marchitas, lo que indica un posible problema de falta de agua.
#El sistema también evalúa el estado general de la planta, considerando si las raíces están sanas o no.
