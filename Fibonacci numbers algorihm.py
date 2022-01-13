n1 = 1
n2 = 1
n3 = 1

input_ = int(input("pick a number: "))

for i in range(1,input_):
    if i < 3:
        n3 = 1
    else :
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        
    if n3 < input_:
        print(n3, end= " ")
        