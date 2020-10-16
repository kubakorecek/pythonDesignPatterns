"""
   Factory pattern
   Author: Jakub Koreček

"""


from abc import ABCMeta, abstractmethod


class ShapeInterface(metaclass=ABCMeta):

    @classmethod
    def __subclasscheck__(cls, subclass):

        return (hasattr(subclass, 'draw') and callable(subclass.draw)
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


if __name__ == '__main__':
    square = Square()
    circle = Circle()