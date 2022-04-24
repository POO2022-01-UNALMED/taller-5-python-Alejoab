from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, color):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = color
        Ave._listado.append(self)

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, color):
        self._colorPlumas = color



    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    @staticmethod
    def movimiento():
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        a1 = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        cls.halcones += 1
        return a1

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        a1 = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls.aguilas += 1
        return a1