#Inferencia Lógica Proposicional
#es el proceso de derivar conclusiones lógicas a partir de un conjunto de proposiciones conocidas (base de conocimiento o KB).
#Dado un conjunto de proposiciones verdaderas (hechos y reglas), y una consulta, la inferencia determina si esa consulta puede deducirse lógicamente.
#Metodos comunes: 
# Modus Ponens:Si p y p → q son verdaderos, entonces q es verdadero.
# Resolución:Reglas de inferencia aplicadas a cláusulas en forma normal conjuntiva (FNC).
# Encadenamiento hacia adelante (Forward chaining):Aplica reglas desde los hechos conocidos hasta derivar una conclusión.
# Encadenamiento hacia atrás (Backward chaining):Parte de la meta o consulta y busca hechos que puedan justificarla.
#Aplicaciones: Sistemas expertos, motores de inferencia, agentes inteligentes.

#Ejemplo de Inferencia Lógica Proposicional

# Base de conocimiento: hechos y reglas
hechos = {
    "llueve": True, # Hecho conocido
    "tiene_paraguas": False # Hecho conocido
}

# Reglas como tuplas (condición, consecuencia)
reglas = [
    (["llueve"], "suelo_mojado"), #si llueve, entonces el suelo está mojado
    (["llueve", "no tiene_paraguas"], "se_moja") ,#si llueve y no tiene paraguas, entonces se moja
]

# Función para aplicar inferencia
def inferencia_logica(hechos, reglas):
    nuevas_conclusiones = set() # Conjuntos para almacenar nuevas conclusiones
    
    for condiciones, consecuencia in reglas: #recorrer las reglas
        cumple = True # Variable para verificar si se cumplen las condiciones
        for condicion in condiciones: #recorrer las condiciones
            if condicion.startswith("no "): # Si la condición es negativa
                hecho = condicion[3:] #extraer el hecho
                if hechos.get(hecho, False): # Si el hecho es verdadero, la condición no se cumple
                    cumple = False #cumple es falso
                    break #salir del bucle
            else: # Si la condición es positiva
                if not hechos.get(condicion, False): # Si el hecho no es verdadero, la condición no se cumple
                    cumple = False #cumple es falso
                    break 
        if cumple: # Si todas las condiciones se cumplen
            nuevas_conclusiones.add(consecuencia) # Agregar la consecuencia a las nuevas conclusiones
    
    return nuevas_conclusiones # Devolver las nuevas conclusiones

# Aplicar inferencia
conclusiones = inferencia_logica(hechos, reglas)

# Mostrar resultados
print("Hechos conocidos:")
for k, v in hechos.items(): #iterar sobre los hechos
    print(f"- {k}: {v}") # Mostrar los hechos conocidos

print("\nConclusiones inferidas:")
if conclusiones:
    for c in conclusiones: #iterar sobre las conclusiones
        print(f"- {c}") # Mostrar las conclusiones inferidas
else:
    print("No se pudo inferir nada.")

#Ejemplo de salida: 
# Hechos conocidos:
# - llueve: True
# - tiene_paraguas: False

# Conclusiones inferidas:
# - suelo_mojado
# - se_moja
#como podemos ver, el agente ha inferido que si llueve y no tiene paraguas, entonces se moja.
