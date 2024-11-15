from Aventurero import Aventurero
from Mascota import Mascota

class Ranger(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, mascota=None):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.__mascota = mascota

    @property
    def mascota(self):
        return self.__mascota

    @mascota.setter
    def mascota(self, mascota):
        self.__mascota = mascota

    def calcular_habilidad(self):
        if self.__mascota is not None:
            return self.puntos_habilidad + self.__mascota.puntos_habilidad
        else:
            return self.puntos_habilidad
       

    