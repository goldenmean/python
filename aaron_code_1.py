class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def with_title(self, title):
        print(title + " {} {}".format(self.first, self.last))

peep = Person("Bob", "Smith")
peep.with_title("Mr.")