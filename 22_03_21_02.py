


prices = [1000 , 3000, 500, 10000, 20000, 700]

lowprice =prices[0]

for i in range(1,len(prices)):
    if prices[i] < lowprice:
        lowprice = prices[i]
print("가장 싼 가격:",lowprice)