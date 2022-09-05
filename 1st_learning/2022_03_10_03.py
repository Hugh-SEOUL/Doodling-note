

total = 0
price = ""

while True :
    price = input("상품 금액을 입력하세요\"끝\"을 입력하면 종료됨) : ")
    if price == "끝":
        print("상품의 총가격 : {:.210}원".format(total))
        break
    total += float(price)

