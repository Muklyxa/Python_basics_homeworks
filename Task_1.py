test_list = [1, 2.1, 3+2j, "four", True, None, [7, 8], (9, 10), set([11, 12, 11]),
             frozenset([13, 14, 13]), {"key_1": 15, "key_2": 16}, bytes([17, 18]),
             bytearray(b"some text"), ZeroDivisionError]

for i, el in enumerate(test_list):
    print(i, el, type(el))
