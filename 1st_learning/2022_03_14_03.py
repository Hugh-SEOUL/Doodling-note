#반복문으로 문자열 관련 처리하기 실습



# fruit = "apple"

# for letter in fruit:
#     print(letter,end=" ")

s = input("문자열을 입력하세요(영문자만) : ")
vowels = "aeiouAEIOU"
result = ""

for letter in s:
    if letter not in vowels:
        result += letter
print("자음만 출력됨 {}".format(result))


  