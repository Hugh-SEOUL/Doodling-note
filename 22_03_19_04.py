

from tkinter.tix import InputOnly
from typing import Tuple


dognames = []
while True:
    name = input("강아지의 이름을 입력하시오(종료시에는 엔터키):")
    if name == "":
        break
    else : 
        dognames.append(name)

print("강아지의 이름은 {0}입니다. ".format(dognames))