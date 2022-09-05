#임의의 숫자를 발생시켜, 숫자를 맞추는 게임을 만들어 보기

from random import *


cnt = 0
num = randrange(1,101)

print(num)
print("1부터 100까지의 숫자를 맞춰보세요")

while cnt < 10 :
    guess= int(input("숫자를 입력하세요"))
    cnt += 1
    
    if guess < num :
        print("입력한 수가 난수보다 낮습니다.")
    elif guess > num :
        print("입력한 수가 난수가 큽니다:")
    elif guess == num :
        print("정답입니다.시도횟수{:_>3}".format(cnt))



