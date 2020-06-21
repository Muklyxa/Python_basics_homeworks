class DateException(Exception):
    pass


class Date:

    def __init__(self, date):
        self.__day, self.__month, self.__year = Date.check_date_is_number(date)
        if not(Date.date_validation(self.__day, self.__month, self.__year)):
            self.__day, self.__month, self.__year = 0, 0, 0
            raise DateException

    @classmethod
    def check_date_is_number(cls, date):
        if isinstance(date, type(str())):
            date_list = date.split('-')
            if len(date_list) == 3:
                try:
                    day = int(date_list[0])
                    month = int(date_list[1])
                    year = int(date_list[2])
                except ValueError:
                    raise DateException
            else:
                raise DateException
        else:
            raise DateException
        return day, month, year

    @staticmethod
    def date_validation(day, month, year):
        date_is_valid = True
        if (year < 1) or (year > 2020):
            date_is_valid = False
        else:
            if (month < 1) or (month > 12):
                date_is_valid = False
            else:
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    last_date = 31
                elif month in [4, 6, 9, 11]:
                    last_date = 30
                elif (year % 4) == 0:
                    last_date = 29
                else:
                    last_date = 28

                if (day < 1) or (day > last_date):
                    date_is_valid = False

        return date_is_valid


try:
    day_of_birth = Date(123456)
except DateException:
    print("Incorrect date")

try:
    day_of_birth = Date("123456")
except DateException:
    print("Incorrect date")

try:
    day_of_birth = Date("1b-34-56")
except DateException:
    print("Incorrect date")

try:
    day_of_birth = Date("15-15-2015")
except DateException:
    print("Incorrect date")

try:
    day_of_birth = Date("11-06-1991")
except DateException:
    print("Incorrect date")
