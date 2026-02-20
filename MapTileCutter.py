from config import paths
from ReadMapCV2 import ReadMapCV2
import json
import cv2


"""
Default values
"""
# size of tile if 512 -> 512x512 px
tile_size_value = 512
# size of tile coverage for "20%"" -> 20
tile_cover_value = 20

class MapTileCutter(ReadMapCV2):
    def __init__(self, file_path: str, tile_size: int = tile_size_value, tile_cover: int = tile_cover_value):
        super().__init__(file_path)
        self.tile_size=tile_size
        self.tile_cover=tile_cover/100

    
    def generate_positions(self, size: int) -> list:
        """
        Generete list with positions
        :param size: max size od the file
        :type size: int

        :return: list with powision from top left corner to the edge
        :rtype: list
        """
        step = int(self.tile_size - self.tile_size * self.tile_cover)
        edge_positions = []
        pos = 0

        while pos + self.tile_size <= size:
            edge_positions.append(pos)
            pos += step

        # last tile on the edge
        last_pos = size - self.tile_size
        if edge_positions[-1] != last_pos:
            edge_positions.append(last_pos)

        return edge_positions
    

    def save_tile(self, tile_name: str, x_top: int, y_top: int):
        """
        save the tile from map
        :param tile_name: tile name using to named the file
        :type tile_name: str
        :param x_top: vertical coordinate of the top left corner
        :type x_top: int
        :param y_top: horizontal coordinate of the top left corner
        :type y_top: int
        """
        tile = self.loaded_img[x_top:x_top+self.tile_size, y_top:y_top+self.tile_size]
        cv2.imwrite(paths.folder_tiles + tile_name + "." + file_path.split(".")[-1], tile)


    def get_tiles(self: dict, X: int, Y: int, height: int, width: int) -> dict:
        """
        Get tiles

        :param X: X - vertical axis coordinate
        :type X: int
        :param Y: Y - horiznontal axis coordinate
        :type Y: int
        :param height: hight of the map
        :type height: int
        :param width: width size of the map
        :type width: int

        :return: dictionary where key is a name of the map + top left corner corrdinate + bottm left corner corrdinate, the value is a list with the top left coordinate of the corner
        :rtype: dict
        """
        temp_json_dict = {}
        x_positions = self.generate_positions(width)
        y_positions = self.generate_positions(height)

        # generate the tiles
        for X in x_positions:
            for Y in y_positions:
                x_bottom = X + self.tile_size
                y_bottom = Y + self.tile_size

                tile_name = f"{file_path.split("/")[-1].split(".")[0]}_{X}_{Y}_{x_bottom}_{y_bottom}".replace(".", "-")
                if (tile_name not in temp_json_dict.keys()):
                    temp_json_dict[tile_name] = str([X, Y])
                    self.save_tile(tile_name, X, Y)
                    with open(paths.folder_tiles_json+file_path.split("/")[-1].split(".")[0]+".json", 'a') as file:
                        json.dump({tile_name: str([X, Y])}, file, indent=4)
                else:
                    raise ValueError("the tile is already in the json temp dict")

        return temp_json_dict


    def cut_the_tiles(self):
        """
        cut the tiles from map
        """
        # get height and width of loaded image
        if len(self.img.shape) == 2:
            height, width = self.img.shape[0], self.img.shape[1]
        else:
            # TODO: in the future implement for color pictures
            raise ValueError("The picture is not loaded in grayscale")
        
        # initial coordinates for top left
        # FOR POLAND horizontal ax is Y and vertical ax is X
        # TODO: shuld be readed from geotiff file
        X, Y = 0, 0

        # horizontal jump
        temp_dict = self.get_tiles(X, Y, height, width)

        print(temp_dict)



if __name__=="__main__":
    file_path = f"{paths.maps_for_processing}map_nearrest.jpg"
    map_loaded = MapTileCutter(file_path)

    # map_loaded.cut_the_tiles()
