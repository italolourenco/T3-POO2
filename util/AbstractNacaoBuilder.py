from cdp.Defensor import Defensor
from cdp.Nacao import Nacao
from cdp.Ofensor import Ofensor
from util.NacaoBuilder import NacaoBuilder
from util.FactoryReflection import FactoryReflection

class AbstractNacaoBuilder(NacaoBuilder):

    nacao = None
    fabrica = FactoryReflection()

    def criarNacao(self, nome):

        self.nacao = Nacao()
        self.nacao.setNome(nome)

    def fazerDefensores(self, listDefensores):

        num = len(listDefensores)
        cont = 0
        dados = []
        listDefensoresProntos = []

        while cont < num:

            dados = listDefensores[cont]

            defensor = self.fabrica.criar_guerreiro(dados[0])
            listDefensoresProntos.append(defensor)
            cont+=1

        self.nacao.setDefensores(listDefensoresProntos)

    def fazerOfensores(self, listOfensores):

        num = len(listOfensores)
        cont = 0
        dados = []
        listOfensoresProntos = []

        while cont < num:

            dados = listOfensores[cont]
            ofensor = self.fabrica.criar_guerreiro(dados[0])
            listOfensoresProntos.append(ofensor)
            cont+=1

        self.nacao.setOfensores(listOfensoresProntos)


    def getNacao(self):
        return self.nacao








