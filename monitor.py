
class moniter:
    __company = ""
    __inch = 0
    __price = 0
    __color = ""
    
    
    def __init__(self,company,inch,price,color):
        self.__company = company
        self.__inch = inch
        self.__price = price
        self.__color = color
        
        
    def getcompany(self):
        return self.__company
    def getinch(self):
        return self.__inch
    def getprice(self):
        return self.__price
    def getcolor(self):
        return self.__color
    
    def setcompany(self, company):
        self.__company = company
    def setinch(self,inch):
        self.__inch = inch
    def setprice(self, price):
        self.__price = price
    def setcolor(self,color):
        self.__color = color
    
    def __str__(self):
        print("제조사:", __self.company)
        print("인치:", __self.inch)
        print("가격:",__self.price)
        print("색상:",__self.color)        