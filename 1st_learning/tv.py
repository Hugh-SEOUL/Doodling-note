
class Tv:
    color = ""
    power = False
    channel = 0
    volume = 0

    def powertv(self, power):
        self.power = power
        if self.power == True:
            print("tv의 전원이 켜졌습니다.")
        else :
            print("tv의 전원이 꺼졌습니다.")
            
    def channelup(self, channel):
        if channel < 0 :
            print("채널은 음수일 수 없습니다.")
            return
        if self.power == False :
            print("tv의 전원부터 켜십시오.")
            return
        self.channel += channel
        
    def channeldown(self, channel):
        if channel < 0 :
            print("채널은 음수일 수 없습니다.")
            return
        if self.power == False :
            print("tv의 전원부터 켜십시오.")
            return
        self.channel -= channel
        
    def volumeup(self, volume):
        if volume < 0 :
            print("볼륨은 음수일 수 없습니다.")
            return
        if self.power == False :
            print("tv의 전원부터 켜십시오.")
            return
        self.volume += volume
        
    def volumedown(self, volume):
        if volume < 0 :
            print("볼륨은 음수일 수 없습니다.")
            return
        if self.power == False :
            print("tv의 전원부터 켜십시오.")
            return
        self.volume -= volume
        
    def printtv(self):
        print("tv의 색상:%s" % self.color)
        print("tv의 볼륨:%s"  %self.volume)
        print("tv의 채널:%s" % self.channel)
    
if __name__ =="__main__":
    tv1 = tv()
    tv2 = tv()

    tv1.color = "검정색"
    tv1.powertv(True)
    tv1.channelup(9)
        