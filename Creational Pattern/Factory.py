"""
   Factory pattern
   Author: Jakub Koreček

"""


from abc import ABCMeta, abstractmethod


class ShapeInterface(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'draw') and callable(subclass.draw)
                and hasattr(subclass, 'sides') and callable(subclass.sides)
                or NotImplemented
                )

    @abstractmethod
    def draw(self):
        raise NotImplementedError


class Circle(ShapeInterface):

    pass


class Square(ShapeInterface):

    def draw(self):
        pass


class Rectangle(ShapeInterface):
    def draw(self):
        pass

    def sides(self):
        pass


if __name__ == '__main__':

    s = Square()

    print(issubclass(Square, ShapeInterface))
    print(issubclass(Rectangle, ShapeInterface))
    circle = Circle()
