from itertools import count

stop = 15
try:
    start = int(input("Enter a number between 0 and 10: "))
    for i in count(start):
        if i > stop:
            break
        print(i)
except:
    print("It's not a number!")
