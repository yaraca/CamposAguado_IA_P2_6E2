# Valor de la información (VOI)
#Este algoritmo mide cuánto vale obtener informacion adicionak antes de tomar una decisión 
#Se basa en el principio de que tener más información puede ayudar a tomar mejores decisiones, 
#si y solo si esa informacion cambia lo que haríamos 
#En este caso, el valor de la información se mide como la diferencia entre el valor esperado de la decisión con información y el valor esperado de la decisión sin información.
#VOI = EVw/oI - EVw/I donde: EVw/oI es el valor esperado de la decisión sin información y EVw/I es el valor esperado de la decisión con información.
#El valor esperado de la decisión sin información se calcula como la suma de los valores de cada acción multiplicados por su probabilidad de ocurrencia.
#El valor esperado de la decisión con información se calcula como la suma de los valores de cada acción multiplicados por su probabilidad de ocurrencia, dado que se tiene información adicional.
#Se puede aplicar en diagnostico médico, estrategias de marketing, robotica y planificacion 

#Ejemplo de valor de la informacion 
#Invertir en un proyecto o no 
#En el estado del mundo incierto hay: Mercado bueno o Mercado malo
#Pagar para obtener un informe predictivo, cuánto vale tener ese informe?

#estados del mundo
estados = ['Bueno', 'Malo'] 
probabilidades = [0.6, 0.4] #probabilidades de cada estado del mundo 60% bueno y 40% malo

#utilidades sin informacion, decisiones fijas
utilidades = {
    'Invertir': {'Bueno': 100, 'Malo': -50}, 
    'No Invertir': {'Bueno': 0, 'Malo': 0} 
}

#funcion para alcular la utilidad esperada SIN informacion 
def sin_informacion(): 
    mejores_utilidades = {} #almacena la mejor utilidad para cada decision
    estados_indices = {estado: i for i, estado in enumerate(estados)} #mapeo de estados a indices
    for decision in utilidades:
        ev = sum(probabilidades[estados_indices[estado]] * utilidades[decision][estado] for estado in estados) #calcula la utilidad esperada
        mejores_utilidades[decision] = ev #almacena la utilidad esperada
    mejor_decision = max(mejores_utilidades, key=mejores_utilidades.get) #decisión con mayor utilidad esperada
    return mejores_utilidades[mejor_decision] #retorna la mejor utilidad esperada

#funcion para calcular la utilidad esperada CON informacion
def con_informacion(): 
    utilidad_con_info = 0 #almacena la utilidad esperada con informacion
    estado_indices = {estado: i for i, estado in enumerate(estados)}  #mapea de estados a indices
    for estado in estados: #iteramos sobre los estados del mundo 
        #si se supiera el estado, se elegiria la mejor decision para ese caso
        mejor_utilidad = max(utilidades[decision][estado] for decision in utilidades) #mejor utilidad para el estado
        utilidad_con_info += probabilidades[estado_indices[estado]] * mejor_utilidad #suma de las utilidades esperadas para cada estado
    return utilidad_con_info #retorna la utilidad esperada con informacion

#calcular el valor de la informacion 
sin_info = sin_informacion() #utilidad esperada sin informacion
con_info = con_informacion() #utilidad esperada con informacion
voi = con_info - sin_info #valor de la informacion

print(f"Utilidad esperada SIN informacion: {sin_info}") #imprime la utilidad esperada sin informacion
print(f"Utilidad esperada CON informacion: {con_info}") #imprime la utilidad esperada con informacion
print(f"Valor de la informacion: {voi}") #imprime el valor de la informacion

#Ejemplo salida:
# Utilidad esperada SIN informacion: 40.0
# Utilidad esperada CON informacion: 60.0
# Valor de la informacion: 20.0