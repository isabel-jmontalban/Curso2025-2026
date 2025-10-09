# -*- coding: utf-8 -*-
"""
Task06_2025.ipynb – RDF(S) Modifying RDF(s)
Autora: Isabel Juárez (isabel-jmontalban)
Correo: Isabel.jmontalban@alumnos.upm.es
GitHub: isabel-jmontalban
"""

from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from rdflib.term import URIRef
from validation import Report

# ================================================================
# Inicialización
# ================================================================
g = Graph()
r = Report()

# 6.0 — Clase Researcher en un NS auxiliar (tal y como arranca el notebook)
ns_aux = Namespace("http://mydomain.org#")
g.add((ns_aux.Researcher, RDF.type, RDFS.Class))

# Namespaces oficiales del validador
PEOPLE = Namespace("http://oeg.fi.upm.es/def/people#")       # clases y propiedades
PERSON = Namespace("http://oeg.fi.upm.es/resource/person/")  # individuos
VCARD  = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")  # vCard 3.0 (Given, Family)

# Bind de prefijos
g.namespace_manager.bind("people", PEOPLE,  override=True)
g.namespace_manager.bind("person", PERSON,  override=True)
g.namespace_manager.bind("vcard",  VCARD,   override=True)
g.namespace_manager.bind("foaf",   FOAF,    override=True)

# ================================================================
# TASK 6.1 – Clases + etiquetas + jerarquía
# ================================================================
def add_class(uri, label):
    g.add((uri, RDF.type, RDFS.Class))
    g.add((uri, RDFS.label, Literal(label, datatype=XSD.string)))

add_class(PEOPLE.Person, "Person")
add_class(PEOPLE.Professor, "Professor")
add_class(PEOPLE.AssociateProfessor, "AssociateProfessor")
add_class(PEOPLE.InterimAssociateProfessor, "InterimAssociateProfessor")
add_class(PEOPLE.FullProfessor, "FullProfessor")

# Jerarquía
g.add((PEOPLE.Professor,                 RDFS.subClassOf, PEOPLE.Person))
g.add((PEOPLE.AssociateProfessor,        RDFS.subClassOf, PEOPLE.Professor))
g.add((PEOPLE.InterimAssociateProfessor, RDFS.subClassOf, PEOPLE.AssociateProfessor))
g.add((PEOPLE.FullProfessor,             RDFS.subClassOf, PEOPLE.Professor))

# Validación 6.1
r.validate_task_06_01(g)

# ================================================================
# TASK 6.2 – Propiedades + dominios y rangos
# ================================================================
def add_property(uri, label):
    g.add((uri, RDF.type, RDF.Property))
    g.add((uri, RDFS.label, Literal(label, datatype=XSD.string)))

add_property(PEOPLE.hasColleague, "hasColleague")
add_property(PEOPLE.hasName,      "hasName")
add_property(PEOPLE.hasHomePage,  "hasHomePage")

# Dominios y rangos
g.add((PEOPLE.hasColleague, RDFS.domain, PEOPLE.Person))
g.add((PEOPLE.hasColleague, RDFS.range,  PEOPLE.Person))

g.add((PEOPLE.hasName,      RDFS.domain, PEOPLE.Person))
g.add((PEOPLE.hasName,      RDFS.range,  RDFS.Literal))

g.add((PEOPLE.hasHomePage,  RDFS.domain, PEOPLE.FullProfessor))
g.add((PEOPLE.hasHomePage,  RDFS.range,  RDFS.Literal))

# Validación 6.2
r.validate_task_06_02(g)

# ================================================================
# TASK 6.3 – Individuos + relaciones
# ================================================================
def add_individual(uri, label, rdf_type):
    g.add((uri, RDF.type, rdf_type))
    g.add((uri, RDFS.label, Literal(label, datatype=XSD.string)))

# Individuos
add_individual(PERSON.Oscar, "Oscar", PEOPLE.Person)
add_individual(PERSON.Asun, "Asun", PEOPLE.FullProfessor)
add_individual(PERSON.Raul, "Raul", PEOPLE.Person)

# Relaciones
g.add((PERSON.Oscar, PEOPLE.hasColleague, PERSON.Asun))
g.add((PERSON.Asun,  PEOPLE.hasColleague, PERSON.Oscar))
g.add((PERSON.Oscar, PEOPLE.hasName,      Literal("Oscar", datatype=XSD.string)))
g.add((PERSON.Asun,  PEOPLE.hasHomePage,  Literal("https://asun.example.org", datatype=XSD.string)))

# Validación 6.3
r.validate_task_06_03(g)

# ================================================================
# TASK 6.4 – Datos adicionales de Oscar
# ================================================================

g.add((PERSON.Oscar, VCARD.Given,  Literal("Oscar", datatype=XSD.string)))
g.add((PERSON.Oscar, VCARD.Family, Literal("Orocho", datatype=XSD.string)))
g.add((PERSON.Oscar, FOAF.mbox,    URIRef("oro")))

# Validation. Do not remove
r.validate_task_06_04(g)
r.save_report("_Task_06")
