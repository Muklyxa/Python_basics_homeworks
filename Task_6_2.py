from itertools import cycle
from random import randint

test_list = [randint(0, 10), randint(10, 100), randint(100, 1000)]
stop = 15
cnt = 0
for el in cycle(test_list):
    if cnt > stop:
        break
    print(el)
    cnt += 1
