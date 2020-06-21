class MyValueException(ValueError):
    def __init__(self, bad_list):
        self.list = bad_list

    @staticmethod
    def check_list(lst):
        bad_list = []
        for n in range(len(lst)):
            try:
                float(lst[n])
            except ValueError:
                bad_list.append(lst[n])

        if len(bad_list) != 0:
            raise MyValueException(bad_list)


result_list = []
line = input("Enter a numbers: ")
while line != 'q':
    line = line.split()
    try:
        MyValueException.check_list(line)
    except MyValueException as err:
        for i in range(len(err.list)):
            line.remove(err.list[i])
    finally:
        for i in range(len(line)):
            result_list.append(line[i])
    line = input("Enter a numbers: ")

print(result_list)
