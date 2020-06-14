class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


manager = Position("Rob", "Jones", "manager", 10000, 5000)
accountant = Position("Alina", "Markovich", "accountant", 8000, 4000)
engineer = Position("Ran", "Ben", "engineer", 5000, 8000)

print(manager.get_full_name() + " " + str(manager.get_total_income()))
print(accountant.get_full_name() + " " + str(accountant.get_total_income()))
print(engineer.get_full_name() + " " + str(engineer.get_total_income()))
