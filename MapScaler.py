import paths

import matplotlib.pyplot as plt
from PIL import Image
from mpl_interactions import zoom_factory

plt.rcParams["figure.figsize"] = (17, 10)
new_line = "\n"

show_cords = True
cords_float_round = 3

class MapScaler:
    """
    MapScaler scale the image file  wiht the map and create new file which will always have the same proportion 
    """
    def __init__(self, raw_file_name: str):
        self.raw_file_name = raw_file_name
        self.raw_map = Image.open(paths.raw_maps+raw_file_name)


    def get_cross_point_ccordinates_from_raw_map(self) -> list:
       
        """
        get_cross_point_ccordinates_from_raw_map
        load and show file for map from foder with raw maps. User should mark the cross points from the map using scrolling with the mouse
        
        :return points: list of points in the tuple format with X, Y of local pixel coordinates
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
        cords = f"{round(float(coord_tuple[0]), cords_float_round)}, {round(float(coord_tuple[1]), cords_float_round)}"
        if show_cords:
            print(cords)
        return cords




    
    
    def save_points_to_file(self):
        """
        save_points_to_file 
        use method get_cross_point_ccordinates_from_raw_map to mark the crod-points from raw map and save them to the csv file with the name of raw_file_name without image file format
        """
        points = self.get_cross_point_ccordinates_from_raw_map()
        with open(f"{paths.raw_map_cross_points}{self.raw_file_name.split(".")[0]}.csv", "w") as file:
            for cords in points:
                if show_cords:
                    print(cords) # to check np.float64 with python float after save to file
                file.write(self._convert_tuple_np_float_to_touple_float(cords)+new_line)


    def get_the_scale_from_file(self):

        # read the points from file
        points_list = []
        with open(paths.raw_map_cross_points + self.raw_file_name.split(".")[0]+".csv", "r") as file:
            for line in file:
                points_list.append(line.replace(new_line, ""))

        # raise the error when file has only 1 corrdiante or is empty 
        if len(points_list) < 1:
            raise "The files should not be empty or have more then 1 cross-point coordinate"

        # calcululate the scales
        scale_list=[]
        for cord_index in points_list:
            points_list[cord_index]

        # clauclate the 

    

        print(points_list)






    def get_the_scale_with_pillow(self):
        # not when adual-d > 2CALCULATEDd
        pass

    def get_the_scale_with_CV2(self):
        pass

    


    

if __name__=="__main__":
    #mymap = MapScaler("map.jpg")
    mymap = MapScaler("map2.png") # to tests
    #mymap = MapScaler("map3.jpg")
# crl + K + C    comment
# crl + K + U    uncomment

    # points = mymap.get_cross_point_ccordinates_from_raw_map()
    # print(points)
    # print(type(points))
    # print(points[0])
    # print(type(points[0]))

# the coords are saved into csv file
    mymap.save_points_to_file()


# get the scale from file with points
    #mymap.get_the_scale_from_file()




   