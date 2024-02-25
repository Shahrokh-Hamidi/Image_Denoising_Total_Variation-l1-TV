# Created by Shahrokh Hamidi
# PhD., Electrical & Computer Engineering




from skimage import io, color



class readImage:
    def __init__(self):
        pass
    
    @staticmethod
    def read_image(path):     
        img = io.imread(path)
        if img.shape[-1] == 4:
            img = img[:,:,0:3]
            return readImage.color_gray(img)
        
        if img.shape[-1] == 3:
            return readImage.color_gray(img)
        
        return img
    
    
    @staticmethod
    def color_gray(img):
        
        return color.rgb2gray(img)
        
        
