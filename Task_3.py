class CellError(BaseException):
    pass


class Cell:
    def __init__(self, num_of_nuc):
        self.__nuf_of_nucleus = num_of_nuc

    def __add__(self, other):
        if type(self) != type(other):
            raise CellError
        return Cell(self.__nuf_of_nucleus + other.__nuf_of_nucleus)

    def __sub__(self, other):
        if type(self) != type(other):
            raise CellError
        return Cell(max(self.__nuf_of_nucleus, other.__nuf_of_nucleus) - min(self.__nuf_of_nucleus, other.__nuf_of_nucleus))

    def __mul__(self, other):
        if type(self) != type(other):
            raise CellError
        return Cell(self.__nuf_of_nucleus * other.__nuf_of_nucleus)

    def __truediv__(self, other):
        if type(self) != type(other):
            raise CellError
        return Cell(self.__nuf_of_nucleus // other.__nuf_of_nucleus)

    def make_order(self, order):
        result = '\n'
        for i in range(self.__nuf_of_nucleus // order):
            string = ''
            for _ in range(order):
                string += '*'
            result += string + '\n'
        string = ''
        for _ in range(self.__nuf_of_nucleus % order):
            string += '*'
        result += string + '\n'
        return result


cell_1 = Cell(100)
print(cell_1.make_order(10))

cell_2 = Cell(1)
print(cell_2.make_order(10))

cell_3 = Cell(0)
print(cell_3.make_order(10))

cell_4 = Cell(3)
print(cell_4.make_order(2))

print((cell_1 + cell_4).make_order(20))
print((cell_1 - cell_4).make_order(15))
print((cell_4 - cell_1).make_order(15))
print((cell_1 * cell_4).make_order(50))
print((cell_1 / cell_4).make_order(50))
print((cell_4 / cell_1).make_order(50))
