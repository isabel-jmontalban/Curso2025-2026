
from rdflib import Graph, Namespace, Literal, XSD
from rdflib.plugins.sparql import prepareQuery

# map, PONER AQUI LA RUTA DONDE ESTE EL parkings.ttl
DATA_FILE = "C:/Users/jzaba/OneDrive/Documentos/UPM/4 CURSO/1 Web Semantica/PROYECT/rdf/parkings.ttl"

# namespaces
NS  = Namespace("http://www.owl-ontologies.com/ns#")
EX  = Namespace("http://group20.linkeddata.es/parkings/resource/")
XSD_NS = Namespace("http://www.w3.org/2001/XMLSchema#")

g = Graph()

n = g.parse(DATA_FILE, format="turtle")

print("parkings.ttl parseado")

g.bind("ns", NS)
g.bind("ex", EX)
g.bind("xsd", XSD_NS)


#print(query 1, dame los primeros 10 parkings(id,nombre,calle))

q1 = prepareQuery('''SELECT ?id ?name ?address WHERE
                  {   ?s a ns:Parking .
                      ?s ns:hasId ?id .
                      ?s ns:hasName ?name .
                      ?s ns:hasAddress ?address .
                  } ORDER BY xsd:integer(?id)
                  LIMIT 20   
                  ''', initNs={"ns":NS})

for r in g.query(q1):
    print(r.id,"    ",r.name, "    ", r.address)
    
print() 
#print(query 2, parkings emt y zona postal)

q2 = prepareQuery('''SELECT ?id ?name ?pc ?emtParking WHERE
                  {
                   ?s a ns:Parking .
                   ?s ns:hasId ?id .
                   ?s ns:hasName ?name .
                   ?s ns:hasAreaCode ?pc .
                   ?s ns:hasLocation ?loc .
                   ?loc ns:isEMTParking ?emtParking .
                   FILTER(?emtParking = true) 
                  }ORDER BY xsd:integer(?id)
                  LIMIT 20  
                  ''', initNs={"ns":NS})

for r in g.query(q2):
    print(r.name,"    ",r.pc,"  ",r.emtParking)
    
print()

#print(query 3, nº de parkings en madrid)

q3 = prepareQuery('''
                  SELECT (COUNT(*) AS ?nParkings) WHERE 
                  { ?p a ns:Parking . }
                ''', initNs={"ns": NS})

for r in g.query(q3):
    print(r.nParkings)
    
#print(query 4, nº de parkings en plazas)
print()

q4 = prepareQuery('''
                  SELECT (COUNT(*) AS ?nParkings) WHERE 
                  { ?s a ns:Parking .
                    ?s ns:hasAddress ?address
                    FILTER(CONTAINS(LCASE(STR(?address)), "plaza"))
                    }
                ''', initNs={"ns": NS})

for r in g.query(q4):
    print(r.nParkings)
    
