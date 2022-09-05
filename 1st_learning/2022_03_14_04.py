from unicodedata import digit


statement = input("문자열을 입력하세요(영문자, 숫자, 공백)")

alpha_cnt = 0
digit_cnt = 0
spaces = 0

for ch in statement:
    if ch.isalpha():
        alpha_cnt +=1
    elif ch.isdigit():
        digit_cnt +=1
    elif ch.isspace():
        spaces += 1
    else : 
        print("해당하는 문자는 알파벳, 숫자, 공백이 아닙니다.")

print("알파벳의 갯수 : {}".format(alpha_cnt))
print("숫자의 갯수 : {}".format(digit_cnt))
print("공백의 갯수 : {}".format(spaces))