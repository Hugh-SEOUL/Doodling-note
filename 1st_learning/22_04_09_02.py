
from tokenize import Number


class card:
    kind = ""
    number = 0
    width = 100
    height = 250
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number
        
    def __str__(self):
        print("kind : ", self.kind)
        print("number : ", self.number)
        print("width : ", card.width)
        print("height : ", card.height)
        
if __name__=="__main__":
    card1 = card("다이아몬드",10)
    card1.__str__()
        
    card2= card("스페이드", 11)
    card2.__str__()