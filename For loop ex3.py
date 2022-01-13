
# num_input = int(input("pick a number : "))

# for i in range(1,10):
#     if (num_input < 2) or (num_input > 9):
#         print("invaild muliplication table") 
#         break
#     print(num_input,"*",i," = ",num_input*i)


n1 = int(input("Frist number: "))
n2 = int(input("Second number: "))


for i in range(n1,n2+1):
    if (i % 3 == 0) and (i % 4 == 0):
         continue 
   