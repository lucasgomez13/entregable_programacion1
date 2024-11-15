from .Aventurero import Aventurero

class Guerrero(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, fuerza):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.__fuerza = fuerza

    @property
    def fuerza(self):
        return self.__fuerza

    @fuerza.setter
    def fuerza(self, fuerza):
        self.__fuerza = fuerza

    def calcular_habilidad(self):
        return self.puntos_habilidad + self.__fuerza / 2