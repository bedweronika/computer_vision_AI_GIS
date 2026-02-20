import cv2

class ReadMapCV2:
    """
    ReadMapCV2 
    load file with map uwing CV2 library and create image object during initilization
    """
    def __init__(self, file_path, is_gray: bool = True):
        self.file_path = file_path
        self.is_gray = is_gray
        self.loaded_img = None

    @property
    def img(self):
        if self.loaded_img is None:
            if self.is_gray:
                self.loaded_img = cv2.imread(self.file_path, cv2.IMREAD_GRAYSCALE)
            else :
                self.loaded_img = cv2.imread(self.file_path)

            if self.loaded_img is None:
                raise ValueError("The image cannot be loaded: ", self.file_path)
            
            if len(self.loaded_img.shape)>2 and self.is_gray:
                raise ValueError("The image should be in gray scale, image shape: ", self.loaded_img.shape)

        return self.loaded_img