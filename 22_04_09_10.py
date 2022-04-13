

class CAR:
    __speed=0
    def upspeed(self,speed):
        self.speed += speed
        print("조상클랙스",self.speed)
        
    def downspeed(self,speed):
        self.speed -= speed
        print("조상클랙스",self.speed)

class SEDAN(CAR):
    def upspeed(self, speed):
        self.speed += speed
        if self.speed > 150:
            self.speed = 150
            print("150을 넘을 순 x")
        print("자손클랙스",self.speed)

class TRUCK(CAR):
    pass

        