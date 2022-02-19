
# from traceback import print_tb


# url= "http://naver.com"
# my_str = url.replace("http://","")
# print(my_str)

# my_str = my_str[:my_str.find(".")]
# print(my_str)

# password = my_str[:my_str.index("e")]+str(len(my_str))+str(my_str.count("e"))+"!"

# print("%s에 생성된 비밀번호 : %s입니다." % (url, password))


from decimal import InvalidOperation
from traceback import print_tb


users = range(1,21)
users = list(users)

from random import *

winners = sample(users,4)

print("--당첨자 발표 --")
print("치킨당첨자 : %s" % winners[0])
print("커피당첨자 : %s" % winners[1:])
print("--축하합니다--")