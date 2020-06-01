test_str = input("Enter a string: ")

for i, string in enumerate(test_str.split()):
    print(i, string[:10])
