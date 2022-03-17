



# def ftoc(temp_f):
#     temp_c = (5.0*(temp_f-32.0))/9.0
#     return temp_c

# temp = float(input("화씨 온도를 입력"))
# print("화씨 온도",temp_f,"섭씨 온도로 변환한 값  ")

def is_prime(num):
    for i in range(2,num):
        temp = True
        if num % i == 0:
            temp = False
        else:
            temp= True
        return temp 
    
prime = int(input("정수를 입력하세요 : "))


print(is_prime(prime))
        
    