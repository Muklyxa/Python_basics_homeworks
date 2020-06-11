with open("task_1.txt", "w", encoding="utf-8") as f_obj:
    string = input("Enter a string: ")
    while string != "":
        string = string + '\n'
        f_obj.write(string)
        string = input("Enter a string: ")
