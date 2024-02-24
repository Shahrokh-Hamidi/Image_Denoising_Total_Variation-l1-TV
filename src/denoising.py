# Created by Shahrokh Hamidi
# PhD., Electrical & Computer Engineering, University of Waterloo
# Waterloo, ON., Canada



from gradient import Gradient
from copy import deepcopy
import matplotlib.pyplot as plt
from config import Config
import matplotlib as mpl




class Denoising(Gradient):
    
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def denoise_img(img):
        
        u = deepcopy(img)
        for i in range(Config.iter_):
            
            u_x = Gradient.gradient_x(u)
            u_y = Gradient.gradient_y(u)
            u_xx = Gradient.gradient_xx(u)
            u_xy = Gradient.gradient_xy(u)
            u_yy = Gradient.gradient_yy(u)
            A = (u_xx*(u_y**2) + u_yy*(u_x**2) - 2*u_x*u_y*u_xy)/((Config.epsilon + u_x**2+u_y**2)**1.5)
            u = u + Config.dt*(img - u + Config.lambda_*A)
        
            Denoising.Display(u, img, i)
            
        return u
    
    
    @staticmethod
    def Display(u, img, i):

        mpl.rcParams['toolbar'] = 'None'
        plt.subplot(121)
        plt.imshow(img, cmap = 'gray')
        plt.axis('off')
        plt.title('Noisy Image \n', fontsize = 16)
        plt.subplot(122)
        plt.imshow(u, cmap = 'gray')
        plt.title(f'Denoised Image \n iter. No.: {i}', fontsize = 16)
        plt.axis('off')
        plt.draw()
        plt.pause(0.01)
        if i < Config.iter_ - 1:
           plt.clf()
        else: 
            plt.show()

