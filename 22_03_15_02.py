


# def square(num):
#     temp = num*num
#     return temp


# num = int(input("정수를 입력하세요"))

# print(result)

def get_max(x,y):
    temp = 0
    if x > y :
        temp = x
    else:
        temp =y
    return temp

x = int(input("수를 입력하세요"))
y = int(input("수를 입력하세요"))
 
print(get_max(x,y))   