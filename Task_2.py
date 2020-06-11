file_name = "task_1.txt"
with open(file_name, "r", encoding="utf-8") as f_obj:
    content = f_obj.readlines()
    length = len(content)
    print(f"In {file_name} {length} strings.")
    for i in range(length):
        print(f"The string {i + 1} consist of {len(content[i].split())} words.")
