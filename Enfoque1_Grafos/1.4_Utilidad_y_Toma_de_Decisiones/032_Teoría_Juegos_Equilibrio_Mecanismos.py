#Teoría de Juegos
#Es un marco matemático que se utiliza para analizar decisiones estratégicas entre múltiples agentes (jugadores)
#Donde el resultado para cada uno depende no solo de sus acciones, sino también de las acciones de los demás.
#Se compone de: jugadores, estrategias, pagos(utilidades), equilibrio de Nash(ningun jugador puede mejorar su resultado cambiando su estrategia si los demás no cambian la suya)
#se aplica en: economía, IA, ciberseguridad, negociación automática, toma de decisiones distribuidas.

#Ejemplo de teoria de juegos 
#Dilema del Prisionero. 
#2 jugadores, cada uno puede Cooperar (C) o Traicionar (T).
#Tabla de pagos:
#                        Jugador B Coopera   Jugador B Traiciona
#JUgador A Coopera            (3, 3)               (0, 5)
#Jugador A Traiciona          (5, 0)               (1, 1)

#librerias necesarias 
import itertools #para combinaciones y permutaciones

#definir estrategias
estrategias = ['C', 'T']  # C = Cooperar, T = Traicionar

#definir matriz de pagos
#las tuplas representan (pago A, pago B)
pagos = {
    ('C', 'C'): (3, 3),
    ('C', 'T'): (0, 5),
    ('T', 'C'): (5, 0),
    ('T', 'T'): (1, 1)
}

#función para encontrar el Equilibrio de Nash
def encontrar_equilibrios(pagos):
    equilibrios = [] #lista para almacenar los equilibrios de Nash
    for estrategia_A, estrategia_B in pagos: #iterar sobre las estrategias de A y B
        pago_A, pago_B = pagos[(estrategia_A, estrategia_B)] #obtener los pagos de A y B

        #verificar si A no puede mejorar unilaterialmente
        mejor_respuesta_A = True 
        for otra_estrategia_A in estrategias: #iterar sobre las estrategias de A
            if otra_estrategia_A != estrategia_A: #si no es la misma estrategia
                if pagos[(otra_estrategia_A, estrategia_B)][0] > pago_A: #si el pago de otra estrategia A es mayor que el pago actual
                    mejor_respuesta_A = False #no es mejor respuesta
                    break

        #verificar si B no puede mejorar unilaterialmente
        mejor_respuesta_B = True
        for otra_estrategia_B in estrategias: #iterar sobre las estrategias de B
            if otra_estrategia_B != estrategia_B: #si no es la misma estrategia
                if pagos[(estrategia_A, otra_estrategia_B)][1] > pago_B: #si el pago de otra estrategia B es mayor que el pago actual
                    mejor_respuesta_B = False #no es mejor respuesta
                    break

        if mejor_respuesta_A and mejor_respuesta_B: #si ambas son mejores respuestas
            equilibrios.append((estrategia_A, estrategia_B)) #agregar al equilibrio
    return equilibrios 

#ejecutar y mostrar resultados
print("Estrategias posibles:")
for s in pagos: #iterar sobre las estrategias
    print(f"{s}: Pago A = {pagos[s][0]}, Pago B = {pagos[s][1]}")  #imprimir estrategias y pagos

equilibrios = encontrar_equilibrios(pagos) #encontrar los equilibrios de Nash
print("\nEquilibrio(s) de Nash encontrado(s):")
for e in equilibrios:
    print(f"Estrategia A: {e[0]}, Estrategia B: {e[1]} → Pagos: {pagos[e]}") #imprimir los equilibrios de Nash encontrados


#Ejemplo de Salida:
# Estrategias posibles:
# ('C', 'C'): Pago A = 3, Pago B = 3
# ('C', 'T'): Pago A = 0, Pago B = 5
# ('T', 'C'): Pago A = 5, Pago B = 0
# ('T', 'T'): Pago A = 1, Pago B = 1

# Equilibrio(s) de Nash encontrado(s):
# Estrategia A: T, Estrategia B: T → Pagos: (1, 1)
#Aunque ambos estarían mejor cooperando (3,3), el miedo a ser traicionado los lleva a un equilibrio subóptimo (1,1).