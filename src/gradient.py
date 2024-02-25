# Created by Shahrokh Hamidi
# PhD., Electrical & Computer Engineering




import numpy as np
        





class Gradient:
    
    def __init__(self):
        pass
    
    @staticmethod
    def gradient_x(u):
        
        return (np.roll(u,-1,axis=1) - np.roll(u,1,axis=1))/2.
    
    @staticmethod
    def gradient_y(u):
        
        return (np.roll(u,-1,axis=0) - np.roll(u,1,axis=0))/2.
    
    
    @staticmethod
    def gradient_xy(u):
        
        u_x = Gradient.gradient_x(u)
        return (np.roll(u_x,-1,axis=0) - np.roll(u_x,1,axis=0))/2.
    
    @staticmethod
    def gradient_xx(u):
        
        return np.roll(u,-1,axis=1) - 2*u + np.roll(u,1,axis=1)
    
    
    @staticmethod
    def gradient_yy(u):
        
        return np.roll(u,-1,axis=0) - 2*u + np.roll(u,1,axis=0)
    
    
