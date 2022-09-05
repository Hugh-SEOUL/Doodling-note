




for Y in range(5):
     for x in range(10):
         print("*", end= "")
     print("")



 for i in range(5):
     for j in range(i+1):
         print("*", end="")
     print("")

#format함수

 print("정수값 :{}, string : {} , flaot : {}".format(10,"안녕하세요",10.10))

 print("숫자 '{:>5}'".format(300))
 print("숫자 '{:>5d}'".format(300))

 for i in range(5):
     print("{:<5}".format("*"*(i+1)))
 for i in range(5,0,-1):
     for j in range(i):
         print("*", end ="")
     print("")

for i in range(6,0,-1):
    print("{:<5}".format("*" * (i-1)))
$