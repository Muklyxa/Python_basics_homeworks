class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self._color = color
        self._name = name
        self.__is_police = is_police

    def go(self):
        print(f"{self._name} start moving with speed {self.speed}.")
        return

    def stop(self):
        self.speed = 0
        print(f"{self._name} stopped!")
        return

    def turn(self, direction):
        if (direction == "left") or (direction == "right"):
            print(f"{self._name} was turned {direction}")
        return

    def show_speed(self):
        print(f"{self._name} is moving with speed: {self.speed}")
        return


class TownCar(Car):
    __speed_limit = 60

    def __init__(self, speed, color, name):
        is_police = False
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.__speed_limit:
            print(f"{self._name}, caution! Current speed {self.speed} is higher than spee limit {self.__speed_limit}")
        else:
            print(f"{self._name} is moving with speed: {self.speed}")


class SportCar(Car):
    def __init__(self, speed, color, name):
        is_police = False
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    __speed_limit = 40

    def __init__(self, speed, color, name):
        is_police = False
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.__speed_limit:
            print(f"{self._name}, caution! Current speed {self.speed} is higher than spee limit {self.__speed_limit}")
        else:
            print(f"{self._name} is moving with speed: {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        is_police = True
        super().__init__(speed, color, name, is_police)


tc = TownCar(60, "white", "Citizen")
wc = WorkCar(40, "yellow", "Worker")
sc = SportCar(200, "red", "Racer")
pc = PoliceCar(100, "black and white", "Police")

tc.go()
wc.go()
sc.go()
pc.go()

tc.turn("left")
wc.turn("right")
tc.turn("right")
sc.turn("left")
pc.turn("right")

tc.show_speed()
wc.show_speed()
sc.show_speed()
pc.show_speed()

tc.speed = 80
wc.speed = 90
sc.speed = 120
pc.speed = 150

tc.show_speed()
wc.show_speed()
sc.show_speed()
pc.show_speed()

tc.stop()
wc.stop()
sc.stop()
pc.stop()

tc.show_speed()
wc.show_speed()
sc.show_speed()
pc.show_speed()
