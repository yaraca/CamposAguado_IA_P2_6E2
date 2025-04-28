#Manto de Markov 
#El manto de Markov de una variable aleatoria es una red bayesiana es un conjunto minimo de nodos que hacen a esa variable condicionalmente independiente del resto de la red
#es decir, si conoces el manto de Markov de una variable, ya no necesitas conocer nada más de la red para inferir su valor.
#Contiene (para una variable X): Padres (nodos que apuntan a X), Hijos (nodos que apuntan desde X) y Padres de los Hijos (nodos que apuntan a los hijos de X)
#Se pueden aplicar en la reduccion del espacio de busqueda, en la seleccion de variables relevantes, pruebas de independecia condicional, etc.

#Ejemplo manto de Markov
#Red bayesiana con la relacion: A y B -> C -> D (C tiene como padres a A y B, y como hijo a D)
#El manto de Markov de C es: A, B y D

#crear una clase para representar la red bayesiana
class RedBayesiana:
    #funcion para inicializar la red bayesiana
    def __init__(self): 
        self.padres = {}  #Diccionario: nodo -> lista de padres
        self.hijos = {}   #diccionario: nodo -> lista de hijos

    #funcion para agregar un arco a la red bayesiana
    def agregar_arco(self, padre, hijo):
        # Agrega un arco de padre -> hijo
        if hijo not in self.padres: #si el hijo no tiene padres, lo inicializa como una lista vacia
            self.padres[hijo] = []
        if padre not in self.hijos: #si el padre no tiene hijos, lo inicializa como una lista vacia
            self.hijos[padre] = []
        self.padres[hijo].append(padre) #agrega el padre a la lista de padres del hijo
        self.hijos[padre].append(hijo) #agrega el hijo a la lista de hijos del padre

    #funcion para obtener el manto de Markov de un nodo
    def obtener_manto_markov(self, nodo):
        manto = set() #inicializa el manto como un conjunto vacio

        #agregar los padres
        padres = self.padres.get(nodo, []) #obtiene la lista de padres del nodo, si no tiene, devuelve una lista vacia
        manto.update(padres) #agrega los padres al manto

        #agregar los hijos
        hijos = self.hijos.get(nodo, []) #obtiene la lista de hijos del nodo, si no tiene, devuelve una lista vacia
        manto.update(hijos) #agrega los hijos al manto

        #agregar otros padres de los hijos
        for hijo in hijos: #para cada hijo del nodo
            otros_padres = self.padres.get(hijo, []) #obtiene la lista de padres del hijo, si no tiene, devuelve una lista vacia
            for p in otros_padres: #para cada padre del hijo
                if p != nodo: #si el padre no es el nodo
                    manto.add(p) #agrega el padre al manto (si no es el nodo)

        return manto #devuelve el manto de Markov como un conjunto

#Crear la red bayesiana del ejemplo: A -> C <- B ; C -> D
red = RedBayesiana() #inicializa la red bayesiana
red.agregar_arco("A", "C") #agrega el arco A -> C
red.agregar_arco("B", "C") #agrega el arco B -> C
red.agregar_arco("C", "D") #agrega el arco C -> D

#obtener el manto de Markov de C
manto_C = red.obtener_manto_markov("C") 
print("Manto de Markov de 'C':", manto_C) #imprime el manto de Markov de C

#ejemplo de salida:
#Manto de Markov de 'C': {'D', 'A', 'B'}
#El manto de Markov de C es: A, B y D (los padres, los hijos y los padres de los hijos)
