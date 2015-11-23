from util.NacaoBuilder import NacaoBuilder

__author__ = 'Italo'

class AbstractBrigdeBuilder():

    build = NacaoBuilder

    def __init__(self, builder):
        self.build = builder

    def montar_nacao(self,nomeNacao,listDefensores,listOfensores):

        self.build.criarNacao(nomeNacao)
        self.build.fazerDefensores(listDefensores)
        self.build.fazerOfensores(listOfensores)
        return self.build.getNacao()

