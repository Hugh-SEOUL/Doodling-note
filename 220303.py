

user_list = ["신은혁", "김연아", "손연재", "박길수", "지창우"]
pw = "1234"



id = input("id를 입력하세요: ")

if id in user_list:
    password = input("패스워드를 입력하세요")
    if password in pw:
        print("{}님이 로그인 하셨습니다.".format(id))
    else:
        print("패스워드가 틀렸습니다.")
else:
    print("회원가입이 하십시오.")