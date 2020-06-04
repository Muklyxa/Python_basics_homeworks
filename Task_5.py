def sum_of_elements(el_list):
    """
    The function returns sum of elements. And status.
    :param el_list:
    :return: sum of el
    """
    sum_of_el = 0
    need_to_quit = False
    for i in range(len(el_list)):
        if el_list[i] == 'q':
            need_to_quit = True
            break
        try:
            sum_of_el += float(el_list[i])
        except ValueError:
            print(f"The element {el_list[i]} is not a number!")
    return need_to_quit, sum_of_el


need_to_quit = False
sum_of_el = 0
sum_of_new_el = 0
while not need_to_quit:
    need_to_quit, sum_of_new_el = sum_of_elements(input("Enter numbers (q for quit): ").split())
    sum_of_el += sum_of_new_el
    print(sum_of_el)
