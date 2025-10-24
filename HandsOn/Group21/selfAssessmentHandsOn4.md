# Assignment 4 – Self assessment

### Every RDF file
- [✔️] Uses the **.nt** or **.ttl** extension as required (Turtle serialization generated with RMLmapper).  
- [✔️] The RDF data is serialized in **N-Triples compatible Turtle format**, validated with RDFLib and YASGUI.  
- [✔️] Follows a consistent **resource naming strategy**:  
  - `http://example.org/wjh/accident/{num_expediente}` for accidents  
  - `http://example.org/wjh/district/{cod_distrito}` for districts  
  - `http://example.org/wjh/accident/{id}/participant` for participants  
  - `http://example.org/wjh/accident/{id}/place` for locations  
- [✔️] All **classes and properties** use URIs consistent with the ontology (`schema.org` and `example.org/traffic#`).  

---

### Every URI in the RDF files
- [✔️] Every URI is **human-readable** and meaningful (e.g., `/accident/2025S000056` instead of random IDs).  
- [✔️] No URI is incorrectly encoded as a string (all appear as IRIs).  
- [✔️] No URI contains double slashes (`//`) other than the initial protocol (`http://`).  

---

### Every individual in the RDF files
- [✔️] Every individual has a **label or name** (`schema:name`, `schema:streetAddress`, etc.) when applicable.  
- [✔️] Every individual has at least one **rdf:type** triple indicating its class (e.g., `schema:Event`, `schema:Place`, `schema:Person`).  

---

### Every value in the RDF files
- [✔️] All literal values are **trimmed** (no extra spaces).  
- [✔️] All values are **properly encoded**:
  - Dates as `xsd:date` or `xsd:dateTime` (e.g., `"2025-01-01T00:00:00Z"^^xsd:dateTime`).  
  - Booleans as `xsd:boolean` (e.g., `"true"` / `"false"`).  
  - Numeric coordinates as `xsd:integer` or `xsd:decimal`.  
- [✔️] Every literal includes its **datatype**.  
- [✔️] The correct datatypes are used (e.g., booleans for positive alcohol/drug tests, integers for UTM coordinates, strings for street names).  

---

## 💬 Comments on the self-assessment

- The transformation from CSV to RDF was performed using **RMLmapper**, based on the official templates provided in the course repository.  
- The mapping was verified with **RDFLib in Python**, confirming that all triples were generated correctly and that datatypes are consistent.  
- URIs were generated following a clear and hierarchical pattern to ensure readability and uniqueness.  
- SPARQL validation queries were executed successfully (see `rdf/queries.sparql` and Python validation script).  
- The RDF was validated with **YASGUI** and **RDF Validator**, confirming that serialization is valid and consistent with the ontology.  
- No missing types or malformed URIs were detected.  
- The assignment objectives — *transform data into RDF, ensure consistent URIs, correct datatypes, and validate mappings* — have been fully achieved.
