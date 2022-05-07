
from UNIT import *

class TANK(UNIT):
    name = ""

    def move(self,x,y):
        self.x = x
        self.y = y
        print("탱크의 위치: ", self.x , ",", self.y, "로 이동함")
    
    def sizemose(self):
        self.mode = "공격모드 : 시즈모드 변환"
        print(self.mode)
        
        