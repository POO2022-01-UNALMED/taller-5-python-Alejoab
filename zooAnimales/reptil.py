from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, color, largo):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = color
        self._largoCola = largo
        Reptil._listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas

    def getLargoCola(self):
        return self._largoCola

    def setColorEscamas(self, color):
        self._colorEscamas = color

    def setLargoCola(self, largo):
        self._largoCola = largo

    

    @staticmethod
    def movimiento():
        return ""

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        a1 = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        cls.iguanas += 1
        return a1

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        a1 = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        cls.serpientes += 1
        return a1