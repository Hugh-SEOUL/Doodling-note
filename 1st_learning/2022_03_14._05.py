from unittest import result


phone_num = input("당신의 전화번호를 입력하세요 (-포함)")
new_phone = ""

for ch in phone_num:
    if ch != "-":
        new_phone += ch
        
        
        
statements = input("원하는 문자열을 입력하세요 : ")
result = ""

for ch in statements :
    if ch !=" " :
        result += ch