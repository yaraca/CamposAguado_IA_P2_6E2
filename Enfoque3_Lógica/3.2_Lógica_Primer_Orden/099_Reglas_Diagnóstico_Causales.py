# Reglas de Diagnóstico y Causales
#son estructuras lógicas utilizadas para razonar sobre causas y efectos dentro de un sistema
#estas reglas se usan para inferir causas a partir de efectos observados (diagnóstico) o para predecir efectos a partir de causas conocidas (razonamiento causal).
#Sintaxis causal: causa => efecto "Si x es una causa, entonces x produce un efecto".
#Sintaxis de diagnostico: Efecto(x) ∧ Regla(x) → Causa(x)  "Si veo un efecto y tengo una regla que lo relacione, puedo deducir la causa".
#Aplicaciones: medicina, ingeniería, sistemas expertos, etc.

#Ejemplo de reglas de diagnóstico y causales

# Base de conocimiento: reglas causales
# Cada regla indica: causa => efecto
reglas_causales = {
    "resfriado": "tos", #si hay resfriado, hay tos
    "gripe": "fiebre", #si hay gripe, hay fiebre
    "alergia": "estornudo" #si hay alergia, hay estornudo
}

#Función de Razonamiento causal: si conozco la causa, obtengo el efecto
def razonamiento_causal(causa):
    if causa in reglas_causales: # si la causa está en las reglas
        efecto = reglas_causales[causa] #obtener el efecto
        print(f"[CAUSAL] '{causa}' causa '{efecto}'") #imprimir la relación causa-efecto
        return efecto #devolver el efecto
    else:
        print(f"[CAUSAL] No hay información para la causa '{causa}'") #imprimir que no hay información
        return None

#Función de Diagnóstico: si observo un efecto, intento deducir la(s) causa(s)
def diagnostico(efecto_observado):
    causas_posibles = [causa for causa, efecto in reglas_causales.items() if efecto == efecto_observado] #buscar causas que produzcan el efecto observado
    if causas_posibles: #si hay causas posibles
        print(f"[DIAGNÓSTICO] El efecto '{efecto_observado}' puede ser causado por: {', '.join(causas_posibles)}") #imprimir las causas posibles
        return causas_posibles #devolver las causas posibles
    else:
        print(f"[DIAGNÓSTICO] No se encontró ninguna causa para el efecto '{efecto_observado}'") #imprimir que no se encontró ninguna causa
        return []

# Ejemplo de uso
print("----- Razonamiento Causal -----")
razonamiento_causal("gripe")
razonamiento_causal("hambre")

print("\n----- Diagnóstico -----")
diagnostico("fiebre")
diagnostico("dolor")

#Ejemplo de salida: 
# ----- Razonamiento Causal -----
# [CAUSAL] 'gripe' causa 'fiebre'
# [CAUSAL] No hay información para la causa 'hambre'

# ----- Diagnóstico -----
# [DIAGNÓSTICO] El efecto 'fiebre' puede ser causado por: gripe
# [DIAGNÓSTICO] No se encontró ninguna causa para el efecto 'dolor'
#Como podemos ver, el razonamiento causal nos permite deducir efectos a partir de causas conocidas, 
# mientras que el diagnóstico nos ayuda a identificar posibles causas a partir de efectos observados. 
# Estos conceptos son fundamentales en sistemas expertos y aplicaciones de inteligencia artificial.