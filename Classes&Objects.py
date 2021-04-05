class Car:
    """
    This is a car class
    """

    def __init__(self, name, colour, drive):
        self.name = name
        self.colour = colour
        self.drive = drive

    def accelerate(self):
        """
        This is a method for class Car
        """
        print("%s accelerates at 100MPH" %self.name)
        print(f"The {self.colour} {self.name} accelerates at 100MPH")
        

    pass

Car1 = Car("Audi","Red",4)
Car2 = Car("Limo","Red",4)
print(Car1)
#Car1.accelerate()

print(help(Car1))