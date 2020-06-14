# pip install colorama - needed to be done before running
import time
from colorama import Fore


class TrafficLight:
    __time_for_red = 7
    __time_for_yellow = 2
    __time_for_green = 7

    def __init__(self):
        self.__color = Fore.RED

    def print_status_and_delay(self, delay):
        if self.__color == Fore.RED:
            text = "stop"
        elif self.__color == Fore.YELLOW:
            text = "ready"
        else:
            text = "go"

        for _ in range(delay):
            print(self.__color + text)
            time.sleep(1)

    def running(self):
        while True:
            self.__color = Fore.RED
            self.print_status_and_delay(self.__time_for_red)
            self.__color = Fore.YELLOW
            self.print_status_and_delay(self.__time_for_yellow)
            self.__color = Fore.GREEN
            self.print_status_and_delay(self.__time_for_green)
            self.__color = Fore.YELLOW
            self.print_status_and_delay(self.__time_for_yellow)


tf = TrafficLight()
tf.running()
