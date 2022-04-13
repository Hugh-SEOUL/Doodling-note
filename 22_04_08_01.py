

from multiprocessing.sharedctypes import Value
from this import d

import math
class circle :
    __radius = 0
    
    
    def __init__(self,radius):
        self.__radius = radius
        
    
    def getradius(self):
        return self.__radius
    def setradius(self, radius):
        self.__radius = radius
        
    def calcarea(self):
        area = math.pi * self.__radius * self.__radius
        return area
    
    def calccircum(self):
        values = 2 * math.pi *self.__radius
        return values
    
if __name__ == "__main__":
    circles = circle(10)
    print("원의 반지름 : ", circles.getradius())
    print("원의 넓이:", round(circles.calcarea(),2))
    print("원의 둘레 :", circles.calccircum())
