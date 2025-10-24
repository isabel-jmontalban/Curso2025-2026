# Hands-on Assignment 3 – Self Assessment

## Checklist

**The data cleaning process:**
- [x] Imported the dataset into OpenRefine.
- [x] Removed empty or irrelevant rows.
- [x] Normalized park and species names (removed extra spaces, fixed casing and special characters).
- [x] Ensured that all text columns are trimmed.
- [x] Ensured that numeric columns (e.g., "UNIDADES 2024") are properly typed as numbers.
- [x] Removed unnecessary columns.
- [x] Created unique identifiers combining park and species names.
- [x] Exported the cleaned CSV dataset.
- [x] Exported the JSON file with the cleaning operations.

**Dataset–Ontology consistency:**
- [x] Every resource described in the CSV file has a unique identifier (not auto-incremented).
- [x] Every resource is related to a class in the ontology (`TreeCount`, `Park`, or `Species`).
- [x] Every class in the ontology is related to a resource in the CSV file.
- [x] Every column in the CSV is trimmed, properly typed, and related to a property in the ontology.
- [x] Every property in the ontology is related to a column in the CSV.

**Deliverables uploaded to GitHub:**
- [x] `openrefine/cleaning-operations.json`
- [x] `csv/arbolado-updated.csv`
- [x] `selfAssessmentHandsOn3.md`

---

## Comments

In this assignment, we cleaned and normalized the dataset *“Arbolado – Parques históricos, singulares y forestales (2024)”* using **OpenRefine**.  
We removed empty rows, trimmed all text fields, converted numeric fields, and unified park and species names.  
We also ensured that each resource (row) has a unique identifier combining the park and the species name.  

The cleaned dataset is now consistent with the ontology defined in the previous assignment (`ontology_arbolado.ttl`), and ready to be converted to RDF.  
All deliverables have been exported and included in the group repository structure:


