from cdp.Guerreiro import Guerreiro

from cdp.Ofensor import Ofensor


class Seak(Ofensor):

    def __init__ (self):
        Guerreiro.__init__(self,'India')
        self.tipo = 'Seak'

    def atacar(self, guerreiro, ofensores, defensores, defensoresAdversarios):
        guerreiro.setEnergia(guerreiro.getEnergia()-25)

