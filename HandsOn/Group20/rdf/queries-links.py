

from rdflib import Graph, Namespace, Literal, XSD
from rdflib.plugins.sparql import prepareQuery

# map, PONER AQUI LA RUTA DONDE ESTE EL parkings-with-links.ttl
DATA_FILE = "C:/Users/jzaba/OneDrive/Documentos/UPM/4 CURSO/1 Web Semantica/PROYECT/rdf/parkings-with-links.ttl"

# namespaces
NS  = Namespace("http://www.owl-ontologies.com/ns#")
EX  = Namespace("http://group20.linkeddata.es/parkings/resource/")
XSD_NS = Namespace("http://www.w3.org/2001/XMLSchema#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")

g = Graph()

n = g.parse(DATA_FILE, format="turtle")

print("parkings.ttl parseado")

g.bind("ns", NS)
g.bind("ex", EX)
g.bind("xsd", XSD_NS)

#print("#Query 5: imprime uris del csv de la parte Location, pero como no tienen su propia propiedad no se puede individual

q5 = prepareQuery('''
SELECT ?name ?uri WHERE {
  ?p a ns:Parking ;
     ns:hasName ?name ;
     ns:hasLocation ?loc .
  ?loc owl:sameAs ?uri .
  FILTER(CONTAINS(STR(?uri), "wikidata.org/entity/"))
} LIMIT 20
''', initNs={"ns": NS, "owl": OWL})

for r in g.query(q5):
    print(r.name, " -> ", r.uri)
    
    
print()
#query con links de parkings y no locations
q6 = prepareQuery('''
SELECT ?name ?uri WHERE {
  ?p a ns:Parking ;
     ns:hasName ?name ;
     owl:sameAs ?uri .
} LIMIT 20
''', initNs={"ns": NS, "owl": OWL})

for r in g.query(q6):
    print(r.name, " -> ", r.uri)
    
