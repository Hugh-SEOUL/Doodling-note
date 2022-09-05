import turtle
import operator

total = 0
price = ""

while True:
    price = input("상품 금액을 입력하세요.(\"끝\"을 입력하면 종료됨)")
    if operator.eq(price,"끝"):
        print("상품의 총 가격:" + str(total) + "원!")
        break
    
    total += int(price)
    
