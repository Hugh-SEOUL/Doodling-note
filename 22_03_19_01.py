



from pickle import FALSE


def readlist():
    score_list = []
    flag = True
    
    while flag:
        score = int(input("성적을 입력하세요 (종료를 하시려면 음수를 입력):"))
        if  score < 0 :
            flag = False
        else:
            score_list.append(score)
        
        
    return score_list

def sorting_list(score_list):
    score_list.sort()
    return score_list

def show_score(score_list):
    j = 0
    for i in score_list:
        print((j+1),"번쨰 성적", i)
        j += 1
        
    
    