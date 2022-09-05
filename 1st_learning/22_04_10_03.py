
class ANIMAL:
    def __init__(self,name,age,weight,instance):
        self.__name= name
        self.__age = age
        self.__weight = weight
        self.__instance = instance
        
    def show(self):
        print("이름:", self.__name)
        print("종류:",self.__instance.d_name)
        print("나이 :" ,self.__age)
        print("몸무게:", self.__weight)
        self.__instance.sound()
        print("------------------------------")

        
class TIGHER():
    d_name="호랑이"
    
    def sound(self):
        print("어흥")
        
class DOG():
    d_name="개"
    def __init__(self):
        super().__init__("",0,0,None)
    
    def sound(self):
        print("멍멍")        
        
        
if __name__== "__main__":
    ani1 = ANIMAL("호돌이",8,180,TIGHER())
    ani1.show()
    