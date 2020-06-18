class MatrixStructureError(BaseException):
    pass


class MatrixDimensionsError(BaseException):
    pass


class Matrix:

    def __init__(self, matrix):
        self.__width = len(matrix)
        self.__length = 0
        if self.__width > 0:
            if not(isinstance(matrix[0], list)):
                self.__width = 0
                self.__length = 0
                self.__matrix = []
                raise MatrixStructureError
            self.__length = len(matrix[0])
            for i in range(1, self.__width):
                if len(matrix[i]) != self.__length:
                    self.__width = 0
                    self.__length = 0
                    self.__matrix = []
                    raise MatrixStructureError
        self.__matrix = matrix

    def __str__(self):
        result = '\n'
        for i in range(self.__width):
            for j in range(self.__length):
                result += f"{self.__matrix[i][j]:8}"
            result += '\n'
        return result

    def __add__(self, other):
        if type(self) != type(other):
            raise MatrixDimensionsError
        else:
            if (self.__width != other.__width) or (self.__length != other.__length):
                raise MatrixDimensionsError
        res_matrix = []
        for i in range(self.__width):
            string = []
            for j in range(self.__length):
                string.append(self.__matrix[i][j] + other.__matrix[i][j])
            res_matrix.append(string)
        return Matrix(res_matrix)


m1 = Matrix([[0, 1, 2], [10, 11, 12], [20, 21, 22]])
print(m1)
m2 = Matrix([])
print(m2)
try:
    m3 = Matrix([1])
    print(m3)
except MatrixStructureError:
    print("It wasn't a matrix!")
m4 = Matrix([[1, 2]])
print(m4)
try:
    m5 = Matrix([[1, 2], [3]])
    print(m5)
except MatrixStructureError:
    print("It wasn't a matrix!")
m6 = Matrix([[]])
print(m6)
m7 = Matrix([[1]])
print(m7)

m8 = Matrix([[1, 1456, 10895], [23, 167, 49], [45678, 0, 17]])
m9 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m8 + m9)
