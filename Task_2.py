test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [test_list[i] for i in range(len(test_list)) if (i > 0) and (test_list[i] > test_list[i - 1])]
print(result_list)
