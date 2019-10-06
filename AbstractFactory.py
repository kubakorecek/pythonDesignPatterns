"""
    This pattern will create family of deferred objects, the main use is to creation of object after its initialization.


"""

from abc import ABC, abstractmethod

class CarInterface(ABC):
    """
        Car interface

    """
    @abstractmethod
    def get_brand(self): pass

class MotocykleInterface(ABC):
    """
        Motocycle interface

    """
    @abstractmethod
    def get_brand(self): pass

class VW(CarInterface):
    def get_brand(self):
        print("VW")

class Skoda(CarInterface):
    def get_brand(self):
        print("Skoda")

class Harley(MotocykleInterface):
    def get_brand(self):
        print("Harley")

class Suzuki(MotocykleInterface):
    def get_brand(self):
        print("Suzuki")


class MotoFactory(ABC):
    """
        FACTORY
    """

    @abstractmethod
    def brand(self): pass

class CarFactory(MotoFactory):
    @staticmethod
    def brand(type):
        if type == 'VW':
            return  VW()
        elif type == 'Skoda':
            return  Skoda()
        else:
            assert 0, "NOT IN THE STORAGE " + str(type)


class MotorcycleFactory(MotoFactory):
    @staticmethod
    def brand(type):
        if type == 'Suzuki':
            return Suzuki()
        elif type == 'Harley':
            return Harley()
        else:
            assert 0, "NOT IN THE STORAGE " + str(type)



if __name__ == '__main__':
    bike = MotorcycleFactory()
    bike.brand('Suzuki').get_brand()