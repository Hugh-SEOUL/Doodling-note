
import math

def sp(radius):
    volume = (4.0/3.0) * math.pi * math.pow(radius,3)
    return volume

radius = float(input("구의 반지름을 입력:"))

print("반지름이",radius,"인 구의 부피:",round(sp(radius),2))



