from config import paths
from ReadMapCV2 import ReadMapCV2
from datetime import datetime


"""
Default values
"""
# size of tile if 200 -> 200x200 px
tile_size_value = 200
# size of tile coverage for "20%"" -> 20
tile_cover_value = 20

class MapTileCutter(ReadMapCV2):
    def __init__(self, file_path: str, tile_size: int = tile_size_value, tile_cover: int = tile_cover_value):
        super().__init__(file_path)
        self.tile_size=tile_size
        self.tile_cover=tile_cover

    def caltualte_coordinates_for_cut(self):
        hight, width = self.img.shape[0], self.img.shape[1]



    def get_file_id(self, x_max, y_max, x_min, y_min):
        """
        Get tile id for new tile from the map
        """
        hash = f"{file_path.split(".")[0]}_{x_max}_{y_max}_{x_min}_{y_min}".relace(".", "-")
        print(hash)


    def save_tile():
        pass


if __name__=="__main__":
    file_path = f"{paths.maps_for_processing}map_nearrest.jpg"
    map_loaded = MapTileCutter(file_path)


    map_loaded.caltualte_coordinates_for_cut()
