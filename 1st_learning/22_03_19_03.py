
# li1 = list()
# print(li1)

# li2 = list("안녕")
# print(li2)


student = 5
scores = []
scores_sum = 0
score_aver = 0.0
cnt_80 = 0
for i in range(student): 
    score = int(input("성적을 입력하세요 :"))
    scores.append(score)
    scores_sum += score
    if score >= 80 :
        cnt_80 +=1
    
score_aver = scores_sum / len(scores)

print("성적평균은", score_aver,"입니다.")
print("80점 이상 성적을 받은 학생은",cnt_80 ,"명입니다.")