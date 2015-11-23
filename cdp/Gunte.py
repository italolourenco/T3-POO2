from cdp.Guerreiro import Guerreiro
from cdp.Ofensor import Ofensor

class Gunte(Ofensor):

    def __init__ (self):
        Guerreiro.__init__(self,'China')
        self.tipo = 'Gunte'

    def atacar(self, guerreiro, ofensores, defensores, defensoresAdversarios):
        if guerreiro.getNomeNacao() == "Japao":
            guerreiro.setEnergia(guerreiro.getEnergia()-20)
        print guerreiro.getNomeNacao()
        if guerreiro.getNomeNacao() == "India":
            guerreiro.setEnergia(guerreiro.getEnergia()-1)
            self.setEnergia(0)
