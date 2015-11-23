from random import randint
from cdp.Nacao import Nacao
from util.FabricaNacao import FabricaNacao


class Batalha(object):
    nomePlayer = None
    resultado = None
    nacao1 = Nacao()
    nacao2 = Nacao()
    nacaoAtaque = None
    ofensor = None
    ofensoresAtacantes = None
    defensoresAtacantes = None
    ofesoresDefesa = None
    defensoresDefesa = None
    defensor = None
    condicaoVitoria = None

    def carregar(self, arquivo1, arquivo2):

        fabricaNacao = FabricaNacao()
        self.__nacao1 = fabricaNacao.prepararNacao(arquivo1)
        self.__nacao2 = fabricaNacao.prepararNacao(arquivo2)

    def setParamentros(self,nacaoAtaque, nacaoDefesa):

        self.nacaoAtaque = nacaoAtaque
        self.ofensor = nacaoAtaque.getLutador()
        self.ofensoresAtacantes = nacaoAtaque.getOfensores()
        self.defensoresAtacantes = nacaoAtaque.getDefensores()
        self.ofesoresDefesa = nacaoDefesa.getOfensores()
        self.defensoresDefesa = nacaoDefesa.getDefensores()
        self.defensor = nacaoDefesa.getDefensor()

    def lutar(self):

        vezAtaque = randint(1,2)

        print(self.defensor)

        while self.__nacao1.sizeOfensor()!= 0 and self.__nacao1.sizeDefensores()!=0 and self.__nacao2.sizeOfensor()!=0 and self.__nacao2.sizeDefensores()!=0:

            if vezAtaque == 1:
                self.setParamentros(self.__nacao1,self.__nacao2)
                proxAtaque = 2

            else:
                self.setParamentros(self.__nacao2,self.__nacao1)
                proxAtaque = 1

            while self.defensor.getEnergia() > 0 and len(self.ofensoresAtacantes) > 0:
                self.ofensor.atacar(self.defensor,self.ofensoresAtacantes,self.defensoresAtacantes,self.defensoresDefesa)
                self.defensor.defender(self.ofensor,self.defensoresDefesa,self.ofesoresDefesa,self.ofensoresAtacantes)

                if self.ofensor.getEnergia() > 0:
                    self.nacaoAtaque.adcionarOfensor(self.ofensor)

                self.ofensor = self.nacaoAtaque.getLutador()

            vezAtaque = proxAtaque

    def gerarResultados(self):

        empate = 0

        if self.__nacao1.sizeOfensor() == 0 and self.__nacao2.sizeDefensores() == 0 or self.__nacao2.sizeOfensor() == 0 and self.__nacao1.sizeDefensores() == 0:
            self.resultado = "Empate"
            empate = 1

        if self.__nacao1.sizeOfensor() == 0 and empate == 0:
            self.resultado = "Vitoria Nacao 2"
            self.condicaoVitoria =  "- Acabaram os Atacantes da Nacao 1"

        if self.__nacao1.sizeDefensores() == 0 and empate == 0:
            self.resultado = "Vitoria Nacao 2"
            self.condicaoVitoria = "- Acabaram os Defensores da Nacao 1"

        if self.__nacao2.sizeOfensor == 0 and empate == 0:
            self.resultado = "Vitoria Nacao 1"
            self.condicaoVitoria = "- Acabaram os Atacantes da Nacao 2"

        if self.__nacao2.sizeDefensores() == 0 and empate == 0:
            self.resultado = "Vitoria Nacao 1"
            self.condicaoVitoria = "- Acabaram os Defensores da Nacao 2"


    def getNacaoNome1(self):
        return self.__nacao1.getNome()

    def getNacaoNome2(self):
        return self.__nacao2.getNome()

