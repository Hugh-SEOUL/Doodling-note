

from collections import *
import time 

deque_test = deque()
start = time.time()


for i in range(100000000):
    deque_test.append(i)

end = time.time()


print("deque append 시간:", end-start)

list = [] 

start = time.time()


for i in range(100000000):
    list.append(i)

end = time.time()

print("list 시간:", end-start)

    
    