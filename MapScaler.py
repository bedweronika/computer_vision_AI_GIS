import paths

import matplotlib.pyplot as plt
from PIL import Image
from mpl_interactions import zoom_factory


plt.rcParams["figure.figsize"] = (18, 10)


class MapScaler:
    """
    MapScaler scale the image file  wiht the map and create new file which will always have the same proportion 
    """
    def __init__(self, raw_file_name):
        self.raw_file_name = raw_file_name
        self.raw_map = Image.open(paths.raw_maps+raw_file_name)


    def get_cross_point_ccordinates_from_raw_map(self):
       
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
    
    
    def save_points_to_file(self):
        """
        save_points_to_file use method get_cross_point_ccordinates_from_raw_map to mark the crodd-points from raw map and save them to the csv file with the name of raw_file_name without image file format
        
        :param self: Description
        """
        points = self.get_cross_point_ccordinates_from_raw_map()
        with open(f"{paths.raw_map_cross_points}{self.raw_file_name.split(".")[0]}.csv", "w") as file:
            for cords in points:
                file.write(str(cords)+"\n")

    


    

if __name__=="__main__":
    mymap = MapScaler("map.jpg")
# crl + K + C    comment
# crl + K + U    uncomment

    # points = mymap.get_cross_point_ccordinates_from_raw_map()
    # print(points)
    # print(type(points))
    # print(points[0])
    # print(type(points[0]))

# the coords are saved into scv file
    #mymap.save_points_to_file()




