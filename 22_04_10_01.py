
from typing_extensions import Self


class CAR:
    value = "조상클래스 필드값"

    def carmethod(self):
        print("조상클래스 메서드")

class SEDAN(CAR):
    value = "자손클래스 필드값"
    def carmethod(self):
        super().carmethod()
        print("자손클래스 메서드 호출")
        print("조상클랙스의 value:", super().value)
        print("자손클랙스의 value:", Self.value)
        
        
        
        