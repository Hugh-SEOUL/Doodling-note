from collections import *
from email.mime import base


# deque_list = deque()
# print(deque_list)

# for i in range(5):
#     deque_list.append(i)
# print(deque_list)

# print(deque_list.popleft())

print("--------------------")

# deque_list = deque()

# print(deque_list)

# for i in range(5):
#     deque_list.extendleft(i)
# print(deque_list)




# print(deque_list)

# for i in range(5):
#     deque_list.extendleft(i)
# print(deque_list)

deque_list = deque()

basedate = ["a","b","c","d","e",]
deque_list = deque(basedate, maxlen= 3)
print(deque_list)