import numpy as np

class Pose2D:
    def __init__(self,x,y,theta):
        self.x = x
        self.y = y
        self.theta = theta
    
    def convert_to_deg(self):
        return np.degrees(self.theta)
    
    def __str__(self):
        return f"Position: {self.x}, {self.y}, Ori: {self.theta}"