#Ingeniería del Conocimiento: Ontologías
#es una representación formal de un conjunto de conceptos dentro de un dominio y las relaciones entre esos conceptos
#Se usa para modelar el conocimiento y facilitar la comunicación entre humanos y máquinas.
#Componentes: 
# Clases (conceptos): categorías o tipos (por ejemplo, Animal, Persona).
# Individuos (instancias): objetos concretos (por ejemplo, "Juan" es una Persona).
# Propiedades (atributos o relaciones): conectan clases e individuos (por ejemplo, "es_amigo_de", "tiene_edad").
#Función: 
# Compartir conocimiento entre sistemas. Inferir nueva información usando razonadores. Crear sistemas más comprensibles y mantenibles.
#Aplicaciones: diagnóstico médico, búsqueda semántica, sistemas de recomendación, etc.

#Ejemplo de ingeniería del conocimiento: Ontologías
#usar la biblioteca rdflib para crear una pequeña ontología de animales.

#librerias necesarias
from rdflib import Graph, Literal, RDF, RDFS, Namespace, URIRef #para crear y manipular grafos RDF
#graph es para almacenar la ontología
#literal es para crear literales RDF (valores de texto, números, etc.)
#rdf es el vocabulario RDF estándar
#rdfs es el vocabulario RDF Schema, que proporciona vocabulario para describir propiedades y clases
#namespace es para definir un espacio de nombres para la ontología
#uriref es para crear referencias URI (identificadores únicos) para recursos en la ontología

#crear un grafo RDF para almacenar la ontología
g = Graph()

#definir un espacio de nombres (Namespace) para la ontología
EX = Namespace("http://example.org/")

#añadir el namespace al grafo
g.bind("ex", EX)

#crear las clases principales de la ontología
g.add((EX.Animal, RDF.type, RDFS.Class)) #definir la clase Animal como una clase RDF
g.add((EX.Mamifero, RDF.type, RDFS.Class)) #definir la clase Mamífero como una clase RDF
g.add((EX.Ave, RDF.type, RDFS.Class)) #definir la clase Ave como una clase RDF

#especificar jerarquía: Mamífero y Ave son subclases de Animal
g.add((EX.Mamifero, RDFS.subClassOf, EX.Animal)) #definir que Mamífero es una subclase de Animal
g.add((EX.Ave, RDFS.subClassOf, EX.Animal)) #definir que Ave es una subclase de Animal

#crear individuos
g.add((EX.Leon, RDF.type, EX.Mamifero)) #definir el individuo León como un Mamífero
g.add((EX.Aguila, RDF.type, EX.Ave)) #definir el individuo Águila como un Ave

#añadir propiedades (por ejemplo, "viveEn")
g.add((EX.viveEn, RDF.type, RDF.Property)) #definir la propiedad viveEn como una propiedad RDF
g.add((EX.viveEn, RDFS.domain, EX.Animal)) #definir el dominio de la propiedad viveEn como Animal
g.add((EX.viveEn, RDFS.range, EX.Habitat)) #definir el rango de la propiedad viveEn como Habitat

#definir instancias de hábitats
g.add((EX.Sabana, RDF.type, EX.Habitat)) #definir el hábitat Sabana como un tipo de hábitat
g.add((EX.Montaña, RDF.type, EX.Habitat)) #definir el hábitat Montaña como un tipo de hábitat

#relacionar los animales con su hábitat
g.add((EX.Leon, EX.viveEn, EX.Sabana)) #definir que el León vive en la Sabana
g.add((EX.Aguila, EX.viveEn, EX.Montaña)) #definir que el Águila vive en la Montaña

#imprimir todas las declaraciones del grafo
print("📚 Ontología generada:\n")
for subj, pred, obj in g:
    print(f"{subj} -- {pred} --> {obj}")

#Ejemplo de salida:
# 📚 Ontología generada:

# http://example.org/Montaña -- http://www.w3.org/1999/02/22-rdf-syntax-ns#type --> http://example.org/Habitat
# http://example.org/viveEn -- http://www.w3.org/1999/02/22-rdf-syntax-ns#type --> http://www.w3.org/1999/02/22-rdf-syntax-ns#Property
# http://example.org/Ave -- http://www.w3.org/1999/02/22-rdf-syntax-ns#type --> http://www.w3.org/2000/01/rdf-schema#Class
# http://example.org/Mamifero -- http://www.w3.org/1999/02/22-rdf-syntax-ns#type --> http://www.w3.org/2000/01/rdf-schema#Class
# http://example.org/Aguila -- http://www.w3.org/1999/02/22-rdf-syntax-ns#type --> http://example.org/Ave
# http://example.org/Leon -- http://www.w3.org/1999/02/22-rdf-syntax-ns#type --> http://example.org/Mamifero
# http://example.org/Aguila -- http://example.org/viveEn --> http://example.org/Montaña
# http://example.org/viveEn -- http://www.w3.org/2000/01/rdf-schema#domain --> http://example.org/Animal
# http://example.org/Ave -- http://www.w3.org/2000/01/rdf-schema#subClassOf --> http://example.org/Animal
# http://example.org/Sabana -- http://www.w3.org/1999/02/22-rdf-syntax-ns#type --> http://example.org/Habitat
# http://example.org/viveEn -- http://www.w3.org/2000/01/rdf-schema#range --> http://example.org/Habitat
# http://example.org/Animal -- http://www.w3.org/1999/02/22-rdf-syntax-ns#type --> http://www.w3.org/2000/01/rdf-schema#Class
# http://example.org/Mamifero -- http://www.w3.org/2000/01/rdf-schema#subClassOf --> http://example.org/Animal
# http://example.org/Leon -- http://example.org/viveEn --> http://example.org/Sabana
#Como se puede ver, la ontología describe una jerarquía de clases (Animal, Mamífero, Ave) y sus instancias (León, Águila), así como propiedades que conectan estas clases e individuos.
#Esta representación permite realizar inferencias y consultas sobre el conocimiento representado, facilitando la interoperabilidad entre sistemas.
#La ontología puede ser ampliada con más clases, individuos y propiedades según sea necesario.
