
from threading import get_ident


def std_wright(height,gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
    
height = 175
gender = "남자"
weight = round(std_wright(height / 100, gender),2)



print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height,gender,weight))