# 임의의 숫자를 발생시켜 숫자를 맞추는 게임을 만들어 보기


import random


cnt = 0
num = random.randint(1, 100)
print("발생한 난수의 값 : " , num)


print("1부터 100사이의 숫자를 맞추어 보세요")
print("기회는 10번 입니다.")

while cnt < 10:
    guess = int(input("숫자를 입력하세요 : "))
    cnt += 1
    
    if guess < num :
        print("입력한 수가 난수 보다 낮습니다.")
    elif guess > num:
        print("입력한 수가 난수보다 높습니다.")
    elif guess == num:
        print("정답입니다. 시도횟수 :", cnt)
        code = input("게임을 계속 하시겠습니까?(Y,N)")
        if code == "n":
            print("게임을 종료합니다.")
            break
        else:
            print("게임을 재시작 합니다.")
            num = random.randint(1, 100)
            print("발생한 난수의 값 : " , num)
            cnt = 0
print("기회 10번이 다 소진 되었습니다. 게임을 종료합니다.")