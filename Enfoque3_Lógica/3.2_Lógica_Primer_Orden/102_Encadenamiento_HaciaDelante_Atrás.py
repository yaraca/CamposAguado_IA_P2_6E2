#Encadenamiento: Hacia Delante y Atrás
#es un algoritmo de inferencia lógica utilizado para derivar conclusiones a partir de una base de hechos y reglas
#Tipos de encadenamiento:
#Encadenamiento Hacia Atrás (Backward Chaining):
# Comienza con una meta (lo que queremos demostrar) y busca si hay reglas que puedan derivar esta meta a partir de hechos.
# Este enfoque es más adecuado para consultas, ya que comienza con la pregunta y busca las respuestas.
#Funcionamiento:
# Comienza con la meta (lo que quieres saber).
# Busca reglas que permitan derivar la meta.
# Recurre hacia atrás para encontrar hechos que respalden las reglas
#Encadenamiento Hacia Adelante (Forward Chaining):
# Comienza con los hechos conocidos y aplica reglas para generar nuevos hechos, hasta que se alcanza la meta o no se pueden hacer más inferencias.
# Este enfoque es más adecuado para sistemas que necesitan progresar a partir de hechos conocidos.
#Funcionamiento: 
# Comienza con los hechos conocidos.
# Aplica reglas para generar nuevos hechos.
# Repite el proceso hasta alcanzar la meta
#aplicaciones: sistemas expertos, diagnóstico médico, etc.

#Ejemplo de Encadenamiento Hacia Delante y Atrás 

#definir los hechos y reglas en un diccionario
hechos = {
    'juan_es_hombre': True, 
    'maria_es_mujer': True
}

reglas = [
    # Regla: Si alguien es hombre, entonces es adulto
    ('hombre', 'adulto', lambda hechos: hechos.get('juan_es_hombre', False)), #si juan es hombre, entonces es adulto
    
    # Regla: Si alguien es mujer, entonces es adulta
    ('mujer', 'adulta', lambda hechos: hechos.get('maria_es_mujer', False)) #si maria es mujer, entonces es adulta
]

#Función de Encadenamiento hacia atrás (Backwards Chaining)
def encadenamiento_hacia_atras(meta, hechos, reglas):
    # Si la meta ya es un hecho, devolver True
    if meta in hechos:
        return hechos[meta]
    
    # Si la meta no es un hecho directo, intentar encontrarla en las reglas
    for antecedente, consecuente, regla in reglas:
        if consecuente == meta and regla(hechos): ##si la regla se cumple
            hechos[meta] = True #añadir la meta a los hechos
            return True #si la meta se cumple
    return False

#Función de Encadenamiento hacia adelante (Forward Chaining)
def encadenamiento_hacia_adelante(hechos, reglas):
    #recorrer todas las reglas y aplicamos aquellas que se puedan derivar
    cambio = True #inicializamos el cambio a True
    while cambio: #mientras haya cambios en los hechos
        cambio = False #inicializamos el cambio a False
        for antecedente, consecuente, regla in reglas: #recorrer las reglas
            if consecuente not in hechos and regla(hechos): #si el consecuente no está en los hechos y la regla se cumple
                hechos[consecuente] = True #añadir el consecuente a los hechos
                cambio = True #actualizar el cambio a True
    return hechos

#Probar Encadenamiento Hacia Atrás
meta = 'adulto' #meta que se quiere demostrar
resultado_atras = encadenamiento_hacia_atras(meta, hechos, reglas) #llamar a la función de encadenamiento hacia atrás
print(f"Resultado de encadenamiento hacia atrás para '{meta}': {resultado_atras}") #imprimir el resultado

# Probar Encadenamiento Hacia Adelante
resultado_adelante = encadenamiento_hacia_adelante(hechos, reglas) #llamar a la función de encadenamiento hacia adelante
print("Hechos después de encadenamiento hacia adelante:", hechos) #imprimir los hechos después del encadenamiento hacia adelante

#Ejemplo de salida: 
# Resultado de encadenamiento hacia atrás para 'adulto': True
# Hechos después de encadenamiento hacia adelante: {'juan_es_hombre': True, 'maria_es_mujer': True, 'adulto': True, 'adulta': True}
# En este ejemplo, el encadenamiento hacia atrás verifica si 'juan' es adulto basándose en la regla de que si es hombre, entonces es adulto.
# El encadenamiento hacia adelante aplica las reglas para derivar nuevos hechos a partir de los hechos iniciales.
# En este caso, se infiere que 'juan' es adulto y 'maria' es adulta.
# Ambos enfoques son útiles en diferentes contextos y pueden complementarse entre sí.