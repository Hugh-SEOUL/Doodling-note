


class account :
    __balance = 0 
    __deposit = 0
    __withdwral = 0
    
    def __init__(self):
        self.__balance = 0
        
    def getbalance(self):
        return self.__balance
    
    def deposit(self,ammount):
        self.__balance += ammount
        print("통장에", format(ammount,",") ,"이 입금됨")
        print("현재잔액", self.__balance,"원")
    
    
    def withdraw(self,ammount):
        self.__balance -= ammount
        print("통장에", ammount,"가 출금됨")
        print("현재잔액", self.__balance,"원")
    
    
if __name__ == "__main__":
    accounts = account()
    accounts.deposit(100000)