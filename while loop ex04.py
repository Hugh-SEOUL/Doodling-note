
from pickle import FALSE
from turtle import Turtle


run = True
speed = 0
keycode = 0

print(int(input("1.증속 , 2: 감속, 3.중지")))

while run :
    print("----------------------")
    print("1.증속 , 2: 감속, 3.중지: ")))
    keycode = int(input("선택 : "))
    
    if keycode == 1:
        speed += 10
        print("현재속도 : ",speed)
    elif keycode == 2:
        speed -= 10
        if speed < 0 :
            print("속도는 음수일수가 없습니다. 뒤로갈까요?")
            speed = 0
        else:
            print("현재속도 : ",speed)
    elif keycode == 0 :
        run = False
    else :
        print("잘못된 입력값입니다.")
print("프로그램 종료")
        