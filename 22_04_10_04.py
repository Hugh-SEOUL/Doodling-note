

class PRODUCT:
    price = 0
    bonus = 0
    def __init__(self,price):
        self.price=price
        self.bonus = int(self.price / 10.0)
    
class TV(PRODUCT):
    def __init__(self, price):
        super().__init__(price)
    def __str__ (self):
        return "TV"
    
class COMPUTER(PRODUCT):
    def __init__(self, price):
        super().__init__(price)
    def __str__ (self):
        return "COMPUTER"

class AUDIO(PRODUCT):
    def __init__(self, price):
        super().__init__(price)
    def __str__ (self):
        return "AUDIO"

class BUYER :
    money = 1000
    bonus = 0
    def buy(self,product):
        if self.money < product.price:
            Print("잔액이 부족하여 물건 구입 x")
            return
        self.money -= product.price
        self.bonus = product.bonus
        print(product.__str__() + "를 구매하셨습니다")
        
        
if __name__ =="__main__":
    buyer = BUYER()
    tv = TV(300)
    computer = COMPUTER(100)
    audio = AUDIO(50)
    
    buyer.buy(tv)
    
        
        