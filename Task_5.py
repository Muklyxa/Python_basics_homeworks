class Stationery:
    def __init__(self, title):
        self.__title = title

    def draw(self):
        print("Start drawing!")

    def get_title(self):
        return self.__title


class Pen(Stationery):
    def __init__(self):
        super().__init__("Pen")

    def draw(self):
        print(f"{self.get_title()} is drawing now.")


class Pencil(Stationery):
    def __init__(self):
        super().__init__("Pencil")

    def draw(self):
        print(f"{self.get_title()} is drawing now.")


class Handle(Stationery):
    def __init__(self):
        super().__init__("Handle")

    def draw(self):
        print(f"{self.get_title()} is drawing now.")


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
