import paths

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from mpl_interactions import zoom_factory

plt.rcParams["figure.figsize"] = (17, 10)   # set up the sife of figure
new_line = "\n"


show_cords = True   # if True determine the prining of cords
round_value = 3   # deermine the value for round method
precision = 0.01 # %

class MapScaler:
    """
    Docstring for MapScaler 
    scale the image file  wiht the map and create new file which will always have the same proportion 
    """


    def __init__(self, raw_file_name: str, raster_scale: str):
        self.raw_file_name = raw_file_name
        self.raw_map = Image.open(paths.raw_maps+raw_file_name)
        self.raster_scale = raster_scale


    def get_cross_point_ccordinates_from_raw_map(self) -> list:
       
        """
        Docstring for get_cross_point_ccordinates_from_raw_map
        load and show file for map from foder with raw maps. User should mark the cross points from the map using scrolling with the mouse
        
        :return: list of points in the tuple format with X, Y of local pixel coordinates
        :rtype: list
        """
        # check if the map is loaded
        if not self.raw_map:
            raise ValueError("The file with raw map does not exist")
        
        # show raw map
        fig, ax = plt.subplots()
        ax.imshow(self.raw_map)
        ax.set_title("Click into the cross-points on the map")

        # scroll with the mouse during getting the points from cross-points
        disconnect_zoom = zoom_factory(ax, base_scale=1.5)
 
        # get voordinated from crosspoints from the map
        print(f"Click into the crodd-points on the map")
        points = plt.ginput(-1, timeout=0, show_clicks=True)

        plt.show()

        # raise the erro when the points are empty
        if len(points)==0:
            raise("The points are not marked")
        
        return points
    

    def _convert_tuple_np_float_to_touple_float(self, coord_tuple: tuple) -> str:
        """
        Docstring for _convert_tuple_np_float_to_touple_float
        convert touple with points in format np.float64 to float and round the velues to the decimal places in set up in the variable round_value. 
        based on the value of show_cords it print of not the orignal coordinates 
        
        :param coord_tuple: tuple with 2 values (x, y) in format np.float
        :type coord_tuple: tuple
        :return: return converted touple with x, y in format np.float to string in format 'x, y' rouded based on global value round_value
        :rtype: str
        """
        cords = f"{round(float(coord_tuple[0]), round_value)}, {round(float(coord_tuple[1]), round_value)}"
        if show_cords:
            print(cords)
        return cords

    
    def save_points_to_file(self):
        """
        Docstring for save_points_to_file 
        use method get_cross_point_ccordinates_from_raw_map to mark the crod-points from raw map and save them to the csv file with the name of raw_file_name without image file format
        """
        points = self.get_cross_point_ccordinates_from_raw_map()
        with open(f"{paths.raw_map_cross_points}{self.raw_file_name.split(".")[0]}.csv", "w") as file:
            for cords in points:
                if show_cords:
                    print(cords) # to check np.float64 with python float after save to file
                file.write(self._convert_tuple_np_float_to_touple_float(cords)+new_line)


    def _calculate_lengths_from_file(self) -> list:
        """
        Docstring for calculate_lengths_from_file
        Calculate the lengths between points from file with cross-points and dicide the length for side and diagonal lengths
        
        :return: list with 2 elementes, where first element is list with side lengths and secound element is list with diagonal lenghts list
        :rtype: list[side_lengths_list, diagonal_lengths_list]
        """

        # read the points from file
        points_list = []
        with open(paths.raw_map_cross_points + self.raw_file_name.split(".")[0]+".csv", "r") as file:
            for line in file:
                points_list.append(line.replace(new_line, ""))

        # raise the error when file has only 1 corrdiante or is empty 
        if len(points_list) < 1:
            raise "The files should not be empty or have more then 1 cross-point coordinate"

        # calcululate the lenght between the points
        length_list=[]
        for base_coord_index in range(len(points_list)):

            # base coordinate in current calculation
            base_coord = points_list[base_coord_index].split(", ")
            for coord_index in range(base_coord_index + 1, len(points_list)):
                coord = points_list[coord_index].split(", ")
                # calculate the lenght between base coord and the rest of coords from the list and append to list
                length_list.append(round(float(np.sqrt( (float(base_coord[0]) - float(coord[0]))**2 + (float(base_coord[1]) - float(coord[1]))**2 ) ), round_value))

        # side and diagonal length
        side_length = []
        diagonal_length = []
        max_value = np.max(length_list)
        min_value = np.min(length_list)

        for length in length_list:
            
            if  np.logical_and(min_value>=length*(1-precision), min_value<length*(1+precision)): 
                side_length.append(length)
            elif np.logical_and( max_value>=length*0.99, max_value<length*1.01 ):
                diagonal_length.append(length)
            else:
                answer = input("The value of the length s above the precision, do you want to check? [Y/N] ")
                if answer.lower() == "y":
                    print("current length: " + str(length))
                    print("\nAll lengths: \n" + "".join( f"{lengthc}, " for lengthc in length_list) )
                    print("Side length: \n" + "".join( f"{lengthc}, " for lengthc in side_length) )
                    print("Diagonal length: \n" + "".join( f"{lengthc}, " for lengthc in diagonal_length) )
                raise ValueError(f"The length schould be in precision {int(precision*100)}%")
        
        return [side_length, diagonal_length]
            

    def get_scale(self) -> float:
        """
        Docstring for get_scale
        calculate scale for the raw_mapbased on raster scale like 1:500
        
        :return: scale value 
        :rtype: float
        """
        
        # calculate the lenght in pixels
        lengths = self._calculate_lengths_from_file()
        mean_leanght_px = round(np.mean([np.mean(lengths[0]), np.mean(lengths[1])/np.sqrt(2)]), round_value)

        # calculate meters to pixel
        if (self.raster_scale == "1:500"):
            # for map scale 1:500 the distance between cross-points is 10cm on the map = 50m in the field
            real_distance_m = 50
            current_px = real_distance_m/mean_leanght_px # [m/px]
            goal_px = 0.1
            
            scale = current_px/goal_px
        else:
            raise ValueError(f"The scale {self.raster_scale} does not have impmented logic")
        
        return scale


    def scale_map_with_pillow(self):
        # not when adual-d > 2CALCULATEDd
        pass
    def get_the_scale_with_CV2(self):
        pass

    


    

if __name__=="__main__":
    mymap = MapScaler("map.jpg", "1:500")
    #mymap = MapScaler("map2.png") # to tests
    #mymap = MapScaler("map3.jpg")
# crl + K + C    comment
# crl + K + U    uncomment

    # points = mymap.get_cross_point_ccordinates_from_raw_map()
    # print(points)
    # print(type(points))
    # print(points[0])
    # print(type(points[0]))

# the coords are saved into csv file
    #mymap.save_points_to_file()


# get the scale from file with points
    #mymap._calculate_lengths_from_file()

# caltulate the cale
    mymap.get_scale()




   