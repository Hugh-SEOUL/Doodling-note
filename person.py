

from traceback import print_tb


class person :
    name = ""
    age = 0
    height = 0
    weight = 0
    address = ""

    def __init__(self):
        self.name = "홍길동"
        self.age = 35
        self.height = 175
        self.weight = 70
        self.address = "경북"
        print("person의 기본 생성자 호출")
    
    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def getheight(self):
        return self.height
    def getweight(self):
        return self.weight
    def getaddress(self):
        return self.address
    
    
    def __str__(self):
        print(self.name)
        print(self.age)
        print(self.height)
        print(self.weight)
        print(self.address)