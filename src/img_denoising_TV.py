# Created by Shahrokh Hamidi
# PhD., Electrical & Computer Engineering, University of Waterloo
# Waterloo, ON., Canada



from readimage import readImage
from denoising import Denoising 
import os
import matplotlib.pyplot as plt



    
if __name__ == "__main__":


    os.getcwd()
    os.chdir("../image")
    path = os.path.join('AE_noisy.png')
    
    img = readImage.read_image(path)
    
    #figManager = plt.get_current_fig_manager()
    #figManager.window.showMaximized()
    
    u = Denoising.denoise_img(img)