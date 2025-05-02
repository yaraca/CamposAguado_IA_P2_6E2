#Resolución: Skolem
#Es un procedimiento para demostrar si una fórmula es válida o insatisfacible. 
#la resolución se utiliza para simplificar o eliminar cuantificadores universales y existenciales, con el fin de encontrar una contradicción o modelo que satisfaga una proposición lógica.
#la resolución trata de combinar dos cláusulas que contienen un literal complementario (por ejemplo, P(x) y ¬P(x)), eliminando dichos literales para producir una nueva cláusula
# El proceso continúa hasta que no se pueden generar más cláusulas, y si una cláusula vacía es generada, la fórmula es insatisfacible.
#La Skolemización es un proceso que se aplica en la lógica de primer orden para eliminar los cuantificadores existenciales de una fórmula.
#Este proceso se lleva a cabo sustituyendo las variables existenciales por funciones o constantes específicas.
#es una transformación importante porque facilita la resolución al convertir una fórmula lógica en una forma que es más fácil de manejar y analizar.
#Funcionamiento: 
#Quantificación Universal: Si un cuantificador universal ∀x está presente, se mantiene tal como está.
#Quantificación Existencial: Si un cuantificador existencial ∃x está presente, se reemplaza la variable existencial x por una función de Skolem que depende de las variables universales anteriores, 
# o por una constante de Skolem si no depende de ninguna variable universal.
#Aplicaciones: teoría de resolución, demostración automática de teoremas, inteligencia artificial, sistemas expertos y verificación formal.

#Ejemplo de Skolemización
#El objetivo es convertir una fórmula que contiene cuantificadores existenciales y universales en una forma de Skolem.

#librerias necesarias
import re #para expresiones regulares

#función para skolemizar una fórmula lógica	
def skolemizar(formula):
    print("Fórmula original:", formula)
    
    #Identificar cuantificadores
    #suponer la forma: ∀x ∃y (P(x, y) ∧ Q(x, y))
    universal_vars = re.findall(r'∀(\w)', formula) #encontrar variables universales
    existencial_vars = re.findall(r'∃(\w)', formula) #encontrar variables existenciales
    
    #Obtener el cuerpo de la fórmula
    cuerpo = re.findall(r'\((.*)\)', formula)[0] #extraer el cuerpo de la fórmula
    
    #Reemplazar variables existenciales por funciones de Skolem
    for var in existencial_vars: 
        if universal_vars: #si hay variables universales
            f_skolem = f"f({', '.join(universal_vars)})" #función de Skolem que depende de las variables universales
        else:
            f_skolem = "c"  # constante si no hay cuantificadores universales
        cuerpo = cuerpo.replace(var, f_skolem) #reemplazar la variable existencial por la función de Skolem
    
    #Reconstruir la fórmula sin el ∃
    if universal_vars: #si hay variables universales
        skolemizada = f"∀{''.join(universal_vars)} ({cuerpo})" #reconstruir la fórmula con los cuantificadores universales
    else: #si no hay variables universales
        skolemizada = cuerpo  # solo si no hay cuantificadores
    
    print("Fórmula Skolemizada:", skolemizada) #imprimir la fórmula skolemizada
    return skolemizada

# Prueba
formula = "∀x ∃y (P(x, y) ∧ Q(x, y))"
skolemizada = skolemizar(formula) #llamar a la función para skolemizar la fórmula

#Ejemplo de salida: 
# Fórmula original: ∀x ∃y (P(x, y) ∧ Q(x, y))
# Fórmula Skolemizada: ∀x (P(x, f(x)) ∧ Q(x, f(x)))
#Como se puede observar, la variable existencial y ha sido reemplazada por una función de Skolem f(x), que depende de la variable universal x.
#Esto permite eliminar el cuantificador existencial y convertir la fórmula en una forma más manejable para la resolución.
#La fórmula resultante es ∀x (P(x, f(x)) ∧ Q(x, f(x))), donde f(x) es una función de Skolem que representa la relación entre x e y.
