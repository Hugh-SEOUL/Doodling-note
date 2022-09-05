

# i = 0
# while i < 10 :
#     print( i , end="")
#     i+=1


# i = 1
# hap = 0

# while i <= 10 :
#     hap += i
#     i += 1
# print("1~10까지의 누계함 : ", hap)


# i = 1

# while i <= 9 :
#     print("3 * {} = {}".format(i, 3*i))
#     i+=1
    
    
    
# i = 1
# hap = 0

# while 1 <= 100 : 
#     if i % 3 == 0 :
#         hap += i
#     i+= 1
# print("1부터 100 사이의 모든 3의 배수의 합은 {}".format(hap))

num = 1234
hap = 0

while num > 0 : 
    digit = num % 10 
    hap += digit
    num = num // 10

print("1234정수의 자리 수의 합은 {0}".format(hap))