#path to folder with files
files_folder="./files/" 

#paths to folder with maps
raw_maps=f"{files_folder}raw_maps/"    # folder with images with maps
scalled_maps=f"{files_folder}scalled_maps/"   # folder with images with maps in local scale
maps_for_processing =f"{files_folder}maps_for_processing/"   # folder with maps choosen the best from all maps -> the base AI
proccesed_maps=f"{files_folder}proccesed_maps/"    # folder with images with maps after AI proccessing

# csv files
raw_map_cross_points = f"{files_folder}raw_map_cross_points/" 

# scalled maps
scalled_maps_pillow = f"{scalled_maps}pillow/"
scalled_maps_cv2 = f"{scalled_maps}cv2/"