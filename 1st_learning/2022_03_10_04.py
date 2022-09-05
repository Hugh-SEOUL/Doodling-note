


run = True 
speed = 0
keycode = 0 

while run :
    print("-----------------------------")
    print("1. 증속    2. 감속     3.중지")
    print("-----------------------------")
    keycode = int(input("선택 :"))
    
    if keycode == 1 :
        speed += 10
        print("현재 속도 {}".format(speed))
    elif keycode == 2:
        speed -= 10
        if speed < 0:
            print("속도는 음수일 수가 없습니다. 뒤로갈까요?")
            speed = 0
        else:
            print("현재 속도 {}".format(speed))
    elif keycode == 3:
        run = False
    else:
        print("잘못된 입력값입니다.")
print("프로그램 종료")