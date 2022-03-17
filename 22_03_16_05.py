
from random import *


def get_pass():
    num_str = "0123456789" 
    password = ""

    for i in range(6):
        index = randrange(len(num_str))
        password += num_str[index]
    return password

print("발송한 숫자를 입력하세요 :",get_pass())