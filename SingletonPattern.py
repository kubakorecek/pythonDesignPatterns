"""
   Singleton pattern is type of design which will make sure only one object is created.

KEY points:
-----------


   ONLY ONE OBJECT CAN BE CREATE

   GLOBAL ACCESS POINT FOR PROGRAM

   CONTROL ACCESS TO SHARED RESOURCES

POSSIBLE VARIATIONS:
-------------------

    Monostate

    Borg


"""


class ClassicalSingleton(object):

    """Only one object is created!"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ClassicalSingleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, x=1):
        self.x = x



class ClassicalSingletonLazy(object):

    """Only one object is created with lazy
    loading!!!"""

    __instance = None

    def __init__(self):
        if not ClassicalSingletonLazy.__instance:
            print("Initialized!")
        else:
            print("Instance already created!!")

    @classmethod
    def setInstance(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = ClassicalSingletonLazy()
        return cls.__instance




def main():
    a = ClassicalSingleton()
    b = ClassicalSingleton()
    print(a, id(a))
    print(b, id(b))
    print(a.x)
    b.x=2

    print("a changed a since they share same space in memory!", a.x)

    c = ClassicalSingletonLazy()
    ClassicalSingletonLazy.setInstance()
    d = ClassicalSingletonLazy()

    print(c, id(c))
    print(d, id(d))


if __name__ == '__main__':

    main()