class Road:
    __density = 0.025  # ton/(m^2*1cm)

    def __init__(self, length, width):
        self._length = length  # metres
        self._width = width  # metres

    def mass_calc(self, depth):
        return self.__density * self._length * self._width * depth


hw = Road(20, 5000)
mass = hw.mass_calc(5)
print(mass)
