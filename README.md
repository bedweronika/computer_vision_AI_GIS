# Concept:
### EN: Vectorization of scanned fundamental raster maps using artificial intelligence in compliance with current legal regulations in Poland.
### PL: Wektoryzacja skanów zasadniczych map rastrowych przy uzyciu AI zgodnie z obowiazujacymi przepisami prawa w Polsce.
project started : 06.02.2026\
\
**raw map example:**\
<img width="20%%" height="20%" alt="obraz" src="https://github.com/user-attachments/assets/b5b90ec2-969a-4b64-b204-87f779f2b82e" />


### **GOAL**: 
based on the legal regulation create geospatial data base which can automaticaly convert object from raster to correct kind of geospatial data base object with metadata from the raster map\
\
**example of the final result:**\
geospatial data base where each object contains georeferences and metadata\
<img width="20%" height="20%" alt="obraz" src="https://github.com/user-attachments/assets/7e03fb85-6c50-4862-afab-8bbb7bdc4470" /> 


---

## 1. START: 
   * create virtual envitoment using: ```python -m venv venv```
   * acctivate tge enviroment: ```source .venv/bin/activate``` (Windows:  ```.\venv\Scripts\activate```)
   * open terminal and install file requrements.txt with quiery: ```pip install -r .\requrements.txt```

## 2. Files 
use file paths.py to set up the folders with files

## 3. Get cross-points for local coordinate system for the picture
Scale the map to get the map in correct proportions (keep the map content in the same size for diffrent type of objects in pixels). For that should be used file MapScaler.py. 
Scalling the map is doing throught library Pillow and OpenCV using different method and file formats. 
All files are saved in scalled_map folder

## 4. Choose the best map and clean
Choose the best map from scalled_map folder and clean the noises. The file is saved in folder maps_for_processing

The proccess and analysis are provided in jupiter notebook ```analysis_scalled_raster_map.ipynb```.

**Compare result of cleaned maps_for_processing and choosen scalled_map**
<img width="1888" height="686" alt="obraz" src="https://github.com/user-attachments/assets/14c61f24-011e-4528-8bab-1dca695addbd" />



