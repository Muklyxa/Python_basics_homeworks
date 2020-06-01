test_list = []
new_el = ''

while new_el != 'q':
    new_el = input("Enter new element ('q' for quit): ")
    if new_el != 'q':
        test_list.append(new_el)

print(test_list)

for i in range(len(test_list)//2):
    temp = test_list[2*i]
    test_list[2*i] = test_list[2*i + 1]
    test_list[2*i + 1] = temp

print(test_list)
