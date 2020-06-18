from abc import ABC, abstractmethod


class Clothes(ABC):

    __total_tissue_consumption = 0

    @abstractmethod
    def get_tissue_consumption(self):
        pass

    @property
    def total_tissue_consumption(self):
        return Clothes.__total_tissue_consumption

    @total_tissue_consumption.setter
    def total_tissue_consumption(self, tissue_consumption):
        Clothes.__total_tissue_consumption = tissue_consumption


class Coat(Clothes):

    def __init__(self, size):
        self.__size = size
        self.total_tissue_consumption += self.get_tissue_consumption()

    def __del__(self):
        self.total_tissue_consumption -= self.get_tissue_consumption()

    def get_tissue_consumption(self):
        return (self.__size / 6.5) + 0.5


class Suit(Clothes):

    def __init__(self, height):
        self.__height = height
        self.total_tissue_consumption += self.get_tissue_consumption()

    def __del__(self):
        self.total_tissue_consumption -= self.get_tissue_consumption()

    def get_tissue_consumption(self):
        return (2 * self.__height) + 0.3


c_1 = Coat(84)
print(c_1.get_tissue_consumption())
print(c_1.total_tissue_consumption)
c_2 = Coat(48)
print(c_2.get_tissue_consumption())
print(c_2.total_tissue_consumption)
s_1 = Suit(1.86)
print(s_1.get_tissue_consumption())
print(s_1.total_tissue_consumption)
s_2 = Suit(1.56)
print(s_2.get_tissue_consumption())
print(s_2.total_tissue_consumption)
del c_1
print(c_2.total_tissue_consumption)
del s_1
print(s_2.total_tissue_consumption)
