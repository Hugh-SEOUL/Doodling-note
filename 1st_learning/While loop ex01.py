

cnt = 0
hap = 0
score = 0
avr =0.0

print("종료하시려면 음수를 입력하세요(예 : -1)")

while score >=0 :
    score = int(input(str(cnt+1) + "번째 학생의 성적을 입력: "))
    if score >= 0 :
        hap += score
        cnt += 1
        
if cnt > 0 :
    avr = hap / cnt
    
    
print(str(cnt) + "학생의 평균은 %.1f 입니다." % avr)
    
