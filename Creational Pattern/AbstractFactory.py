from abc import ABCMeta, abstractmethod


class ShapeInterface2D(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'draw') and callable(subclass.draw) or NotImplemented
                )

    @abstractmethod
    def draw(self):
        pass


class ShapeInterface3D(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'build') and callable(subclass.draw)
                or NotImplemented

                )

    @abstractmethod
    def build(self):
        pass


class Circle(ShapeInterface2D):

    def draw(self):
        pass


class Square(ShapeInterface2D):

    def draw(self):
        pass


class Cube(ShapeInterface3D):
    def build(self):
        pass


class Sphere(ShapeInterface3D):
    def build(self):
        pass


class ShapeFactoryInterface(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'draw') and callable(subclass.draw) or NotImplemented
                )

    @staticmethod
    @abstractmethod
    def get_shape(sides):
        """Subclasses must implement this as a @staticmethod"""
        pass


class Shape2DFactory(ShapeFactoryInterface):

    @staticmethod
    def get_shape(sides):
        if sides == 1:
            return Circle()
        elif sides == 4:
            return Square()
        assert 0, " Bad shape " + sides + " sides"


class Shape3DFactory(ShapeFactoryInterface):

    @staticmethod
    def get_shape(sides):
        if sides == 1:
            return Sphere()
        elif sides == 6:
            return Cube()
        assert 0, " Bad shape " + sides + " sides"


if __name__ == '__main__':
    factory2d = Shape2DFactory()
    factory2d.get_shape(1)
    factory3d = Shape3DFactory()
