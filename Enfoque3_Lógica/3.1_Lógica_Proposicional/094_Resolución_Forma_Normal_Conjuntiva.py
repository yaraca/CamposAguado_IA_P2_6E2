#Resolución y Forma Normal Conjuntiva (FNC)
# es una manera estándar de escribir fórmulas lógicas donde:
#La fórmula se representa como una conjunción (AND) de cláusulas.
#Cada cláusula es una disyunción (OR) de literales.
# La resolución es una técnica inferencial utilizada para verificar la satisfacibilidad de una fórmula en FNC:
# Se basa en eliminar literales opuestos entre cláusulas.
# Si se deriva la cláusula vacía (∅), significa que hay una contradicción ⇒ la fórmula es insatisfacible.
#Aplicaciones: verificacion de harware, sistemas expertos, deduccion automatica, etc.

#Ejemplo de Resolución en FNC

#Funciones para la resolución de cláusulas en FNC
#Si hay un literal opuesto en ambas, se eliminan y se combinan el resto de los literales.
def resolver(clausula1, clausula2):
    for literal in clausula1: ## Recorre los literales de la primera cláusula
        complemento = '¬' + literal if not literal.startswith('¬') else literal[1:] ## Complemento del literal
        if complemento in clausula2: #si el complemento está en la segunda cláusula
            nueva = (clausula1 - {literal}) | (clausula2 - {complemento}) #se eliminan los literales opuestos y se combinan el resto
            return nueva #devuelve la nueva cláusula
    return None

#Funcion principal de resolución
#Aplica el algoritmo de resolución sobre la base de conocimiento más la negación de la meta.
def resolucion_fnc(base_conocimiento, meta):
    clausulas = base_conocimiento + [set(('¬' + l if not l.startswith('¬') else l[1:] for l in meta))] #negación de la meta
    # Se convierte la meta a su forma negada y se agrega a la base de conocimiento
    nuevas = [] # Lista para almacenar nuevas cláusulas derivadas

    print("Inicio de resolución con clausulas:")
    for c in clausulas: # Se imprimen las cláusulas iniciales
        print(c) 

    while True: #mientras haya cláusulas para resolver
        n = len(clausulas) #número de cláusulas actuales
        for i in range(n): # Recorre las cláusulas
            for j in range(i+1, n): # Compara cada cláusula con las demás
                resolvente = resolver(clausulas[i], clausulas[j]) # Resuelve las cláusulas
                if resolvente is not None: # Si se obtuvo un resolvente
                    if not resolvente: # Si el resolvente es vacío, se encontró una contradicción
                        print("\nSe derivó la cláusula vacía ∅ ⇒ Contradicción encontrada.") # Se imprime la contradicción
                        return True # Se devuelve True si se encuentra la contradicción
                    if resolvente not in clausulas and resolvente not in nuevas: # Si el resolvente no está en las cláusulas actuales ni en las nuevas
                        nuevas.append(resolvente) # Se agrega a la lista de nuevas cláusulas

        if not nuevas: # Si no se generaron nuevas cláusulas, se termina el proceso
            print("\nNo se pudo derivar la cláusula vacía ⇒ No se puede demostrar la meta.")
            return False

        clausulas += nuevas # Se agregan las nuevas cláusulas a la lista de cláusulas
        nuevas = [] # Se reinicia la lista de nuevas cláusulas para la siguiente iteración

# Base de conocimiento en FNC
# (p ∨ q), (¬p ∨ r), (¬q ∨ r), (¬r)
base_conocimiento = [
    {'p', 'q'},
    {'¬p', 'r'},
    {'¬q', 'r'},
    {'¬r'}
]

# Meta a demostrar: r
meta = ['r']

#ejecutar el algoritmo
resultado = resolucion_fnc(base_conocimiento, meta) # Se llama a la función de resolución con la base de conocimiento y la meta
print("\n¿Se puede deducir la meta?:", "Sí" if resultado else "No") # Se imprime el resultado de la deducción

#Ejemplo de salida: 
# Inicio de resolución con clausulas:
# {'q', 'p'}
# {'¬p', 'r'}
# {'r', '¬q'}
# {'¬r'}
# {'¬r'}

# Se derivó la cláusula vacía ∅ ⇒ Contradicción encontrada.

# ¿Se puede deducir la meta?: Sí

#Como se puede observar, la resolución de la base de conocimiento y la negación de la meta derivó en una contradicción, 
# lo que indica que la meta es deducible a partir de la base de conocimiento.
