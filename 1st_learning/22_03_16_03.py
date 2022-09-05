

def printinfo(name,age):
    print("-----------------------")
    print("이름:", name)
    print("나이:",age)
    print("-----------------------")
    return
end_input = ""
print("이름과 나이를 입력하세요.(입력 종료 : q)")
while True :
    if end_input == "n":
        print("입력을 종료합니다.")
        
        break
    elif end_input == "y":
        name = input("회원명을 입력:")
        age = int(input("나이를 입력:"))
        printinfo(name,age)
    
    
    end_input = input("계속입력하시겠습니까?(y/n)")

