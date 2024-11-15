from abc import ABC , abstractmethod

class Mision(ABC):
    def __init__(self, nombre, rango, recompensa, tipo_de_mision, completado=False, minimo_de_miembros=1):
        self.__nombre = nombre
        self.__rango = rango
        self.__recompensa = recompensa
        self.__completado = completado
        self.__tipo_de_mision = tipo_de_mision
        self.cantidad_minima_miembros = minimo_de_miembros

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def rango(self):
        return self.__rango

    @rango.setter
    def rango(self, rango):
        self.__rango = rango

    @property
    def recompensa(self):
        return self.__recompensa

    @recompensa.setter
    def recompensa(self, recompensa):
        self.__recompensa = recompensa

    @property
    def completado(self):
        return self.__completado

    @completado.setter
    def completado(self, completado):
        self.__completado = completado

    @property
    def tipo_de_mision(self):
        return self.__tipo_de_mision

    @tipo_de_mision.setter
    def tipo_de_mision(self, tipo_de_mision):
        self.__tipo_de_mision = tipo_de_mision

    @property
    def minimo_de_miembros(self):
        return self.__cantidad_minima_miembros

    @minimo_de_miembros.setter
    def minimo_de_miembros(self, minimo_de_miembros):
        self.__cantidad_minima_miembros = minimo_de_miembros

    def __str__(self):
        estado = "Completada" if self.completado else "Pendiente"
        return f"{self.__nombre} (Rango: {self.__rango}) - Recompensa: {self.__recompensa} - Estado: {estado}"

    
    