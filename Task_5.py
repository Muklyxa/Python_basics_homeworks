from random import random, randint

num = randint(1, 101)
num_list = [str(((random() * 255) - 128)) for _ in range(num)]
string = " ".join(num_list)

with open("task_5.txt", "w", encoding="utf-8") as f_obj:
    f_obj.write(string)

with open("task_5.txt", "r", encoding="utf-8") as f_obj:
    content = f_obj.read()
    content = content.split()
    total_sum = 0
    for i in range(len(content)):
        total_sum += float(content[i])

print(f"The sum of the elements from file is: {total_sum:.2f}")
