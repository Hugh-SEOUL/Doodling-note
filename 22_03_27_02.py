

eng_dict = {}

eng_dict["one"] = "하 나"
eng_dict["two"] = "두 개"
eng_dict["three"] = "세 개"
eng_dict["four"] = "네 개"
eng_dict["five"] = "다 개"

while True :
    word = input("단어를 입력하시오 (종료 하시려면 종료라고 치세요)")
    if word =="종료":
        break
    
    if word in eng_dict:
        print(eng_dict.get(word))
    else:
        print("해당하는 단어가 없습니다.")
        
        
