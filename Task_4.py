from googletrans import Translator
translator = Translator()

content = []
line = ""

with open("text_4.txt", "r", encoding="utf-8") as f_obj:
    string = f_obj.readline()
    while string != "":
        string = string.split("-")
        string[0] = translator.translate(string[0], dest='ru').text + " "
        line = "-".join(string)
        content.append(line)
        string = f_obj.readline()

with open("text_4_russian.txt", "w", encoding="utf-8") as f_obj:
    f_obj.writelines(content)


