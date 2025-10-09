# Hands-on 3 — Self-Assessment (OpenRefine)

**Group:** 03  
**Goal:** Clean and prepare CSV data in OpenRefine to facilitate RDF generation.

## What we did (validated)
- **Import & parsing:** Loaded the selected dataset; checked encoding, separator and headers.  
- **Text normalization:** Trimmed and standardized values in core columns (e.g., station/code/address/type).  
- **Dates:** Applied `toDate()` to `Fecha alta` and converted back to string for a normalized date representation.  
- **Numbers:** Replaced decimal commas with dots in `COORDENADA_*_ETRS89`, then cast `COORDENADA_*_ETRS89`, `LONGITUD`, `LATITUD`, `ALTITUD` to numbers.  
- **Identifiers:** Added `ID_ESTACION` from `CODIGO_CORTO` using GREL.  
- **Column order:** Minor column moves to keep schema tidy.

> Note: No aggregated pollutant columns or IRI helper columns were added in this pass; the updated CSV keeps the original pollutant flags and the original `Fecha alta` column name.

## Deliverables
- **Operations JSON:** `openrefine/history.json` — full sequence of edits/transforms.  
- **Updated CSV:** `csv/informacion-estaciones-red-calidad-aire-updated.csv`.  
- **This document:** `selfAssessmentHandsOn3.md` — in the repo root.

## Reproducibility
OpenRefine → **Undo/Redo → Apply** `openrefine/history.json` → export `csv/*-updated.csv`.

