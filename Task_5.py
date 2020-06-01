my_list = [7, 5, 3, 3, 2]

new_pos = str("")
while new_pos != 'q':
    print(f"Rating: {my_list}.")
    new_pos = input("Enter new position (enter 'q' for quit): ")
    if new_pos.isnumeric():
        new_pos = int(new_pos)
        inserted = False
        for i, el in enumerate(my_list):
            if new_pos > el:
                my_list.insert(i, new_pos)
                inserted = True
                break

        if not inserted:
            my_list.append(new_pos)
