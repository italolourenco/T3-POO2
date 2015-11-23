__author__ = 'Italo'


class Guerreiro (object):
    __energia = 100
    __tipo = None
    __nacao = None

    def __init__(self, nacao):
        self.__nacao = nacao

    def getEnergia(self):
        return self.__energia

    def setEnergia(self, energia):
         self.__energia = energia

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
         self.tipo = tipo

    def getNomeNacao(self):
        return self.__nacao







