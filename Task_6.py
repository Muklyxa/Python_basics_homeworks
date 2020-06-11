discipline = []
num_of_h = []

with open("text_6.txt", "r", encoding="utf-8") as f_obj:
    content = f_obj.readlines()
    for i in range(len(content)):
        string = content[i].split()
        discipline.append(string[0][0:-1])
        summ = 0
        for j in range(1, len(string)):
            if string[j] != "-":
                line = string[j].split("(")
                summ += int(line[0])
        num_of_h.append(summ)

result = dict(zip(discipline, num_of_h))
print(result)

