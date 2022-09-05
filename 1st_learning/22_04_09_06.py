



class CAR:
    speed = 0
    
    def __init__(self,speed):
        self.speed = speed
        
        
    
    def upspeed(self,speed):
        self.speed = speed
        print("조상클래스의 speed",self.speed)



class SEDAN(CAR):
    pass
    

if __name__ =="__main__":
    sedan = SEDAN()
    sedan.upspeed(100)
    
    