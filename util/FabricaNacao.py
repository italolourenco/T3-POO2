from cgd.LeitorArqNacao import LeitorArqNacao
from util.AbstractNacaoBuilder import AbstractNacaoBuilder
from util.Deus import Deus
from util.ImpBrigdeBuilder import ImpBrigeBuilder

__author__ = 'Italo'


class FabricaNacao():

    def prepararNacao(self, arquivo):

        leitor = LeitorArqNacao()
        nomeNacao = leitor.leituraNome(arquivo)
        listOfensores = leitor.leituraAtacantes(arquivo)
        listDefensores = leitor.leituraDefensores(arquivo)
        deus = Deus()
        build = AbstractNacaoBuilder()
        ponte = ImpBrigeBuilder(build)
        return deus.criarNacao(ponte,nomeNacao,listDefensores,listOfensores)




