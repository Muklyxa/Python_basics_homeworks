def int_func(word):
    start_code = ord('a')
    stop_code = ord('z')
    result_str = word
    correct_word = True
    for i in range(len(word)):
        char_code = ord(word[i])
        if (char_code < start_code) or (char_code > stop_code):
            print(f"The '{word[i]}' is not latin character in lower case!")
            correct_word = False
            break

    if correct_word:
        result_str = word.title()

    return result_str


string = input("Enter a string in lower case (latin characters only): ").split()
new_list = []
result_string = ' '
for i in range(len(string)):
    new_list.append(int_func(string[i]))
print(result_string.join(new_list))
