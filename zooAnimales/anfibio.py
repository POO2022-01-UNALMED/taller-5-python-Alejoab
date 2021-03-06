from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, color, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = color
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    def getColorPiel(self):
        return self._colorPiel

    def isVenenoso(self):
        return self._venenoso

    def setColorPiel(self, color):
        self._colorPiel = color

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    

    @staticmethod
    def movimiento():
        return ""

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        a1 = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1
        return a1

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        a1 = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1
        return a1