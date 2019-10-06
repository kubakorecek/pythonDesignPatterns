"""
    This pattern will create deferred object, the main use is to creation of object after its initialization


"""

from abc import ABC, abstractmethod

class CarInterface(ABC):
    """
        Car interface

    """
    @abstractmethod
    def get_color(self): pass


class RedCar(CarInterface):

    def get_color(self):
        print("painting car to RED")

class BlueCar(CarInterface):

    def get_color(self):
        print("painting car to BLUE")


class CarColorFactory:
    @staticmethod
    def paint(type):
        if type == 'red':
            return  RedCar()
        elif type == 'blue':
            return  BlueCar()
        else:
            assert 0, "NOT IN THE STORAGE " + str(type)


if __name__ == '__main__':
    CarColorFactory.paint('red').get_color()
    CarColorFactory.paint('blue').get_color()
    CarColorFactory.paint('orange').get_color()


