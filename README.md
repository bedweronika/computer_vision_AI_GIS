# Concept:
### EN: Digitization of scans of basic raster maps using AI in accordance with applicable legal regulations in Poland
### PL: Digitalizacja skanów zasadniczych map rastrowych przy uzyciu AI zgodnie z obowiazujacymi przepisami prawa w Polsce
project started : 06.02.2026\
\
**raw map example**:\
<img width="30%%" height="30%" alt="obraz" src="https://github.com/user-attachments/assets/b5b90ec2-969a-4b64-b204-87f779f2b82e" />

**goal**: 
based on the legal regulation crate geospatial data base which can automaticaly convert ovject from raster to correct kind of data base object with metadata




---

## 1. START: 06.02.2026
   * create virtual envitoment using: '''python -m venv venv
   * acctivate tge enviroment: source .venv/bin/activate (Windows:  .\venv\Scripts\activate)
   * open terminal and install file requrements.txt with quiery: pip install -r .\requrements.txt

## 2. Files 
use file paths.py to set up the folders with files

## 3. Get cross-points for local coordinate system for the picture
Scale the map to get the map in correct proportions (keep the map content in the same size for diffrent type of objects in pixels). For that should be used file MapScaler.py


