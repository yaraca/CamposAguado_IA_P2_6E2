# Encadenamiento: Hacia Delante y Atrás
#es un método de inferencia lógica usado para deducir conclusiones a partir de hechos y reglas. Existen dos tipos principales:
#Encadenamiento hacia Adelante (Forward Chaining)
# Comienza con hechos conocidos.
# Aplica reglas para derivar nuevos hechos hasta que se alcance el objetivo o ya no haya más hechos nuevos.
#Encadenamiento hacia Atrás (Backward Chaining)
# Comienza con una meta.
# Busca reglas que puedan justificar la meta.
# Verifica si los antecedentes de esas reglas se pueden demostrar a partir de los hechos.
#Aplicaciones: sistemas expertos, inteligencia artificial, programación lógica, etc.

#Ejemplo de Encadenamiento Hacia Adelante y Atrás

# Reglas en forma de "SI condiciones → entonces conclusión"
reglas = [
    (['p'], 'q'),
    (['q'], 'r'),
    (['r', 's'], 't')
]

# Hechos conocidos
hechos_iniciales = {'p', 's'}


#Funcion para el encadenamiento hacia adelante
def encadenamiento_adelante(reglas, hechos): # hechos es un conjunto de hechos iniciales
    hechos = set(hechos)  # Copia local
    nuevas_inferencias = True # Inicializamos el ciclo
    print("Encadenamiento hacia Adelante:")
    while nuevas_inferencias:  # Mientras haya nuevas inferencias
        nuevas_inferencias = False #reiniciar la bandera
        for condiciones, conclusion in reglas: #recorrer las reglas
            if all(cond in hechos for cond in condiciones) and conclusion not in hechos: #si todas las condiciones son verdaderas y la conclusión no es un hecho
                hechos.add(conclusion) #agregar la conclusión a los hechos
                nuevas_inferencias = True #se encontró una nueva inferencia
                print(f"Se dedujo: {conclusion} a partir de {condiciones}") #imprimir la deducción
    return hechos #devolver los hechos finales

#funcion para el encadenamiento hacia atrás
def encadenamiento_atras(reglas, hechos, meta, visitados=None): # hechos es un conjunto de hechos iniciales
    if visitados is None: # Inicializar el conjunto de visitados si no se proporciona
        visitados = set() #inicializar el conjunto de visitados
    if meta in hechos: #si la meta ya es un hecho
        print(f"{meta} ya es un hecho.") #imprimir que la meta ya es un hecho
        return True #devolver verdadero
    if meta in visitados: #si la meta ya fue visitada
        return False #devolver falso

    visitados.add(meta) #agregar la meta a los visitados
    for condiciones, conclusion in reglas: #recorrer las reglas
        if conclusion == meta: #si la conclusión es la meta
            print(f"Para probar {meta}, necesito probar {condiciones}") #imprimir que se necesita probar las condiciones
            if all(encadenamiento_atras(reglas, hechos, cond, visitados) for cond in condiciones): #probar todas las condiciones
                hechos.add(meta) #agregar la meta a los hechos
                print(f"Se logró deducir: {meta}") #imprimir que se logró deducir la meta
                return True
    return False


# Ejemplo de uso
hechos_deducidos = encadenamiento_adelante(reglas, hechos_iniciales.copy()) # Copia de los hechos iniciales para no modificarlos
print("\nHechos al final del encadenamiento hacia adelante:", hechos_deducidos) #imprimir los hechos finales

print("\nEncadenamiento hacia Atrás para probar 't':") #imprimir que se va a probar la meta
es_deducible = encadenamiento_atras(reglas, hechos_iniciales.copy(), 't') # Copia de los hechos iniciales para no modificarlos
print(f"\n¿Se puede deducir 't' por encadenamiento hacia atrás?: {'Sí' if es_deducible else 'No'}") #imprimir si se puede deducir la meta

#Ejemplo de salida: 
# Encadenamiento hacia Adelante:
# Se dedujo: q a partir de ['p']
# Se dedujo: r a partir de ['q']
# Se dedujo: t a partir de ['r', 's']

# Hechos al final del encadenamiento hacia adelante: {'q', 't', 'p', 's', 'r'}

# Encadenamiento hacia Atrás para probar 't':
# Para probar t, necesito probar ['r', 's']
# Para probar r, necesito probar ['q']
# Para probar q, necesito probar ['p']
# p ya es un hecho.
# Se logró deducir: q
# Se logró deducir: r
# s ya es un hecho.
# Se logró deducir: t

# ¿Se puede deducir 't' por encadenamiento hacia atrás?: Sí

#Como se puede ver, el encadenamiento hacia adelante dedujo 't' a partir de los hechos iniciales 
# y el encadenamiento hacia atrás probó 't' a partir de los hechos iniciales. 
# Ambos métodos son útiles en diferentes contextos y pueden complementarse entre sí.
#El encadenamiento hacia adelante es útil cuando se tienen muchos hechos y se quiere deducir una conclusión,
# mientras que el encadenamiento hacia atrás es útil cuando se tiene una conclusión y se quiere probar si es verdadera a partir de los hechos.
