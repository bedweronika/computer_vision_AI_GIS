#path to folder with files
files_folder="./files/" 
folder_maps = f"{files_folder}maps/"

#paths to folder with maps
raw_maps=f"{folder_maps}raw_maps/"    # folder with images with maps
scalled_maps=f"{folder_maps}scalled_maps/"   # folder with images with maps in local scale
maps_for_processing =f"{folder_maps}maps_for_processing/"   # folder with maps choosen the best from all maps -> the base AI
proccesed_maps=f"{folder_maps}proccesed_maps/"    # folder with images with maps after AI proccessing

# csv files
raw_map_cross_points = f"{folder_maps}raw_map_cross_points/" 

# scalled maps
scalled_maps_pillow = f"{folder_maps}pillow/"
scalled_maps_cv2 = f"{folder_maps}cv2/"