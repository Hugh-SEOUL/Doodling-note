
# for y in range(5):
#     for x in range(10):
#         print("*",end="")
# print("")



for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(1,i*2):
        print("x", end="")     
    print("")

for i in range(5):
    for j in range(i):
        print(" ",end="")
    for j in range(10,i*2+1,-1):
        print("x", end="")     
    print("")
    




# for i in range(1,11,2):
#     print("{:^10}".format("*"*i))
    
    
