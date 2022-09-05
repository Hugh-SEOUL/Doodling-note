

from hashlib import new


def menu_print():
    print("1. 친구리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")

menu_choice = 0
friends = []

while True :
    menu_print()
    menu_choice = int(input("메뉴를 선택하시오 : "))
    if menu_choice == 9:
        print("프로그램을 종료합니다.")
        break
    elif menu_choice == 1 :
        print("친구 리스트입니다.")
        print(friends)
    elif menu_choice == 2 :
        name = input("이름을 입력하시오 : ")
        friends.append(name)
    elif menu_choice == 3 :
        del_name = input("삭제하고싶은 이름을 입력하세요 : ")
        if del_name in friends:
            friends.remove(del_name)
            print("[]님이 삭제되었습니다.".format(del_name))
        else:
            print("[]님이 존재하지 않습니다.".format(del_name))
    elif menu_choice == 4 :
        old_name = input("변경하고 싶은 이름을 입력하세요 :")
        if old_name in friends:
            index = friends.index(old_name)
            new_name = input("변경하실 이름을 입력하세요:")
            friends[index] = new_name
        else : 
            print("[]님이 존재하지 않습니다".format(old_name))
            


            