"""
    This Design, construct the complex object from its representation so same construction proccess will have           different representations
"""


class Ship(object):

    def __init__(self):
        self.__color = None
        self.__engine = None
        self.__body = None

    def setColor(self, color):
        self.__color = color

    def setEngine(self, engine):
        self.__engine = engine

    def setBody(self, body):
        self.__body = body

    def specification(self):
        out = "Body: {} \nEngine: {}\n Color: {}".format(
            self.__body.length,self.__engine.horsepower,self.__color.color
        )
        print(out)

class Engine:
    horsepower = None


class Color:
    color = None


class Body:
    length = None


class BuilderInterFace:
    def getColor(self): pass

    def getEngine(self): pass

    def getBody(self): pass


class TitanicBuilder(BuilderInterFace):
    def getBody(self):
        body = Body()
        body.length = 275
        return body

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 50000
        return engine

    def getColor(self):
        color = Color()
        color.color = 'Black'
        return color





class OlympicBuilder(BuilderInterFace):
    def getBody(self):
        body = Body()
        body.length = 275
        return body

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 30000
        return engine

    def getColor(self):
        color = Color()
        color.color = 'BLUE'
        return color


class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getShip(self):
        ship = Ship()

        color = self.__builder.getColor()
        ship.setColor(color)

        body = self.__builder.getBody()
        ship.setBody(body)

        engine = self.__builder.getEngine()
        ship.setEngine(engine)

        return ship

if __name__ =='__main__':

    d = Director()
    d.setBuilder(TitanicBuilder())
    ship_1 = d.getShip()


    d = Director()
    d.setBuilder(OlympicBuilder())
    ship_2 = d.getShip()

    ship_1.specification()
    ship_2.specification()