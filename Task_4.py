from abc import ABC


class Stock:
    def __init__(self):
        self.__number_of_units = 0
        self.lst = []
        self.dict = {"Printer": 0, "Scanner": 0, "Xerox": 0}

    @property
    def number_of_units(self):
        return self.__number_of_units

    def get(self, lst):
        for i in range(len(lst)):
            self.lst.append(lst[i])
            self.dict[lst[i].name] += 1
            self.__number_of_units += 1
            print(f"{lst[i].name} with serial number {lst[i].serial_number} was added in stock.")

    def transfer(self, sn_lst):
        for i in range(len(sn_lst)):
            for j in range(len(self.lst)):
                if sn_lst[i] == self.lst[j].serial_number:
                    print(f"{self.lst[j].name} with serial number {self.lst[j].serial_number} will be transfered to office.")
                    self.dict[self.lst[j].name] -= 1
                    self.lst.remove(self.lst[j])
                    self.__number_of_units -= 1
                    break

    def get_serial_numbers(self, name, numbers):
        result_list = []
        cnt = 0
        for i in range(len(self.lst)):
            if self.lst[i].name == name:
                result_list.append(self.lst[i].serial_number)
                cnt += 1
                if cnt == numbers:
                    break
        return result_list


class OfficeEquipment(ABC):
    def __init__(self, name, serial_number):
        self.__name = name
        self.__serial_number = serial_number

    @property
    def name(self):
        return self.__name

    @property
    def serial_number(self):
        return self.__serial_number


class Printer(OfficeEquipment):
    def __init__(self, serial_number):
        super().__init__("Printer", serial_number)


class Scanner(OfficeEquipment):
    def __init__(self, serial_number):
        super().__init__("Scanner", serial_number)


class Xerox(OfficeEquipment):
    def __init__(self, serial_number):
        super().__init__("Xerox", serial_number)


st = Stock()
command = input("Enter the command:\n\
1 - add the printer to the stock\n\
2 - add the scanner to the stock\n\
3 - add the xerox to the stock\n\
4 - show total number of office equipment in the stock\n\
5 - show total numbers of equipment\n\
6 - transfer to the office\n\
q - quit\n")
while command != 'q':
    if command == '1':
        try:
            serial_number = int(input("Print the serial number: "))
        except ValueError:
            print("Incorrect serial number!")
        else:
            st.get([Printer(serial_number)])
    elif command == '2':
        try:
            serial_number = int(input("Print the serial number: "))
        except ValueError:
            print("Incorrect serial number!")
        else:
            st.get([Scanner(serial_number)])
    elif command == '3':
        try:
            serial_number = int(input("Print the serial number: "))
        except ValueError:
            print("Incorrect serial number!")
        else:
            st.get([Xerox(serial_number)])
    elif command == '4':
        print(f"In the stock {st.number_of_units} numbers of units.")
    elif command == '5':
        print(f"In the stock:\n{st.dict['Printer']} - printers\n{st.dict['Scanner']} - scaners\n{st.dict['Xerox']} - xeroxes")
    elif command == '6':
        name = input("What do you want to transfer?\n\
                     1 - Printers\n\
                     2 - Scanners\n\
                     3 - Xeroxes\n")
        try:
            num_of_units = int(input("How many units do you want to transfer?\n"))
        except ValueError:
            print("Incorrect number!")
            num_of_units = 0
        if name == '1':
            name = "Printer"
        elif name == '2':
            name = "Scanner"
        elif name == '3':
            name = "Xerox"

        if (st.dict[name] < num_of_units):
            print(f"Only {st.dict[name]} units in the stock!")
            num_of_units = st.dict[name]

        sn_lst = st.get_serial_numbers(name, num_of_units)
        st.transfer(sn_lst)
    command = input("Enter the command:\n\
    1 - add the printer to the stock\n\
    2 - add the scanner to the stock\n\
    3 - add the xerox to the stock\n\
    4 - show total number of office equipment in the stock\n\
    5 - show total numbers of equipment\n\
    6 - transfer to the office\n\
    q - quit\n")
