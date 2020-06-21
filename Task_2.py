class MyClassDateZDE(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


class MyNumData:

    def __init__(self, num):
        try:
            self.__num = float(num)
        except ValueError:
            self.__num = 0

    def __truediv__(self, other):
        if not(isinstance(other, type(MyNumData(0)))):
            other = MyNumData(other)

        if other.__num == 0:
            raise MyClassDateZDE("Devision by zero!")

        return self.__num / other.__num


first = MyNumData(1000)
second = MyNumData("5")
print(first / second)

try:
    second = MyNumData(0)
    print(first / second)
except MyClassDateZDE as zde:
    print(zde)
