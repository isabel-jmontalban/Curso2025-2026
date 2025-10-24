# Checklist
## Assignment 5
### 📁 `lodrefine` directory

#### 📄 `operations-with-links.json`
- [x] Includes the operations performed over the data for linking them
> [Open operations-with-links.json]()
---
### 📁 `csv` directory

#### 📄 `updated-parkings-with-links.csv`
- [x] Includes the updated version of the dataset
> [Open updated-parkings-with-links.csv]()
---
### 📁 `mappings` directory

#### 📄 `updated-mappings-with-links.rml`
- [x] Includes the updated versions of the mappings
> [Open updated-mappings-with-links.rml]()
---
### 📁 `rdf` directory

#### 📄 `parkings-with-links.ttl`
- [x] Includes the data transformed into RDF
- [x] Contains at least one `owl:sameAs` property
- [x] Has every `owl:sameAs` property linking a resource in the dataset with another resource in an external dataset
> [Open parkings-with-links.ttl]()

#### 📄 `queries-with-links.sparql`
- [x] Includes at least 1 query
- [x] Contains queries that retrieve the data that would be needed in the application
- [x] Has every SPARQL query making use of the ontology, returning a non-empty result and making use of the `owl:sameAs` links
> [Open queries-with-links.sparql]()
