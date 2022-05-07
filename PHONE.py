
class PHONE:
    def __init__(self):
        self.model = ""
        self.color = ""

    def poweron(self):
        print("전원을 켭니다.")
    def poweroff(self):
        print("전원을 끕니다.")
    def bell(self):
        print("벨이 울립니다.")
    def sendvoice(self,message):
        print("자신:", message)
    def receivevoice(self,message):
        print("타인:", message)
    def hungup(self):
        print("전화를 끊습니다.")
        