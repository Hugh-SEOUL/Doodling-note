

from difflib import Differ
import math


score = [
    [100, 100, 100], [20, 20, 20], [30, 30, 30],
    [40, 40, 40], [50, 50, 50] ]

kortotal = 0
engtotal = 0
mathtotal = 0

totalsum = 0
avg = 0.0

print("번호 국어 영어 수학 총점 평균".replace(" ","\t"))


print("----------------------------------------------")

for i in range(len(score)):
    sum = 0
    average = 0.0
    
    kortotal += score[i][0]
    engtotal += score[i][1]
    mathtotal += score[i][2]

    print("{}".format(i+1),end="\t")
    
    for j in range(len(score[i])):
        sum += score[i][j] 
        print("{}".format(score[i][j]),end="\t")
    totalsum += sum
    average = sum / len(score[i])
    avg += average
    print("{} {}".format(sum,average).replace(" ","\t"))
print("총점 국어{} 영어{} 수학{} 전체총점{} 전체평균{}".format(kortotal,engtotal,mathtotal,totalsum,avg),end="\t")
    


