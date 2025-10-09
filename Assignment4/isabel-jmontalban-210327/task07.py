# -*- coding: utf-8 -*-
"""
Task07_2025.ipynb – Querying RDF(s)
Autora: Isabel Juárez (isabel-jmontalban)
Correo: Isabel.jmontalban@alumnos.upm.es
GitHub: isabel-jmontalban
"""

# =========================
# Carga de librerías y datos
# =========================
!pip -q install rdflib
!wget -q https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials/python/validation.py

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from validation import Report

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2025-2026/master/Assignment4/course_materials"

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.parse(github_storage + "/rdf/data06.ttl", format="turtle")

report = Report()

# Namespaces del curso
PPL   = Namespace("http://oeg.fi.upm.es/def/people#")
PER   = Namespace("http://oeg.fi.upm.es/resource/person/")
FOAF  = Namespace("http://xmlns.com/foaf/0.1/")
g.namespace_manager.bind("ppl", PPL, override=True)
g.namespace_manager.bind("person", PER, override=True)
g.namespace_manager.bind("foaf", FOAF, override=True)


# ==========================================================
# TASK 7.1a (RDFLib): Lista (clase, superclase|None) -> result
# ==========================================================
result = []
classes = set(g.subjects(RDF.type, RDFS.Class))
for c in sorted(classes):
    supers = list(g.objects(c, RDFS.subClassOf))
    if supers:
        for sc in supers:
            result.append((c, sc))
    else:
        result.append((c, None))

# Validación 7.1a
report.validate_07_1a(result)


# ==========================================================
# TASK 7.1b (SPARQL): ?c ?sc
# ==========================================================
query_71b = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?c ?sc
WHERE {
  ?c a rdfs:Class .
  OPTIONAL { ?c rdfs:subClassOf ?sc . }
}
ORDER BY ?c ?sc
"""
report.validate_07_1b(query_71b, g)


# ==========================================================
# TASK 7.2a (RDFLib): individuos de Person (incluye subclases)
# Devolver etiquetas en lista -> individuals
# ==========================================================
# Cerradura subClassOf* de ppl:Person
to_visit = [PPL.Person]
visited = set()
types_closure = set()
while to_visit:
    t = to_visit.pop()
    if t in visited:
        continue
    visited.add(t)
    types_closure.add(t)
    for sub in g.subjects(RDFS.subClassOf, t):
        to_visit.append(sub)

# Recolectar labels de instancias de cualquier tipo en la cerradura
individuals = []
seen = set()
for t in types_closure:
    for ind in g.subjects(RDF.type, t):
        for lbl in g.objects(ind, RDFS.label):
            s = str(lbl)
            if s not in seen:
                individuals.append(s)
                seen.add(s)
            break

# Validación 7.2a
report.validate_07_02a(individuals)


# ==========================================================
# TASK 7.2b (SPARQL): individuos de Person (incluye subclases) -> ?ind
# ==========================================================
query_72b = """
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ppl:  <http://oeg.fi.upm.es/def/people#>
SELECT DISTINCT ?ind
WHERE {
  ?ind rdf:type ?t .
  ?t rdfs:subClassOf* ppl:Person .
}
ORDER BY ?ind
"""
report.validate_07_02b(g, query_72b)


# ==========================================================
# TASK 7.3 (SPARQL): nombre y tipo de quienes conocen a Rocky
# Resultado: variables ?name ?type
# (soporta ppl:knows o foaf:knows; nombre via ppl:hasName/rdfs:label/foaf:name)
# ==========================================================
query_73 = """
PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
PREFIX ppl:   <http://oeg.fi.upm.es/def/people#>
PREFIX person:<http://oeg.fi.upm.es/resource/person/>

SELECT ?name ?type
WHERE {
  {
    SELECT ?s (COALESCE(?n1, ?n2, ?n3) AS ?name) (SAMPLE(?t) AS ?type)
    WHERE {
      { ?s ppl:knows person:Rocky . } UNION { ?s foaf:knows person:Rocky . }
      ?s rdf:type ?t .
      ?t rdfs:subClassOf* ppl:Person .
      OPTIONAL { ?s ppl:hasName ?n1 . }
      OPTIONAL { ?s rdfs:label   ?n2 . }
      OPTIONAL { ?s foaf:name    ?n3 . }
    }
    GROUP BY ?s ?n1 ?n2 ?n3
  }
}
ORDER BY ?name ?type
"""
report.validate_07_03(g, query_73)


# ==========================================================
# TASK 7.4 (SPARQL): nombre de quienes tienen un colega con un perro
# o un colega de colega con un perro (evitar duplicados)
# ==========================================================
query_74 = """
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ppl:  <http://oeg.fi.upm.es/def/people#>

SELECT ?name
WHERE {
  {
    SELECT (COALESCE(?n1, ?n2, ?n3) AS ?name)
    WHERE {
      ?s (ppl:hasColleague|ppl:hasColleague/ppl:hasColleague) ?col .
      ?col ppl:hasPet ?pet .
      ?pet rdf:type ppl:Dog .

      ?s rdf:type ?t .
      ?t rdfs:subClassOf* ppl:Person .

      OPTIONAL { ?s ppl:hasName ?n1 . }
      OPTIONAL { ?s rdfs:label   ?n2 . }
      OPTIONAL { ?s <http://xmlns.com/foaf/0.1/name> ?n3 . }
    }
    GROUP BY ?s ?n1 ?n2 ?n3
  }
}
ORDER BY ?name
"""
report.validate_07_04(g, query_74)

report.save_report("_Task_07")
