from cdp.Guerreiro import Guerreiro

from cdp.Ofensor import Ofensor

class Chunku(Ofensor):

    def __init__ (self):
        Guerreiro.__init__(self,'China')
        self.tipo = 'Chunku'

    def atacar(self, guerreiro, ofensores, defensores, defensoresAdversarios):

        if guerreiro.getNomeNacao() == "India":
            guerreiro.setEnergia(guerreiro.getEnergia()-5)
        if guerreiro.getNomeNacao() == "Japao":
            guerreiro.setEnergia(guerreiro.getEnergia()-10)



