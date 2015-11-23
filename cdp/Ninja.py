from cdp.Guerreiro import Guerreiro
from cdp.Ofensor import Ofensor

class Ninja(Ofensor):

    def __init__ (self):
        Guerreiro.__init__(self,'Japao')
        self.tipo = 'Ninja'

    def atacar(self, guerreiro, ofensores, defensores, defensoresAdversarios):
        guerreiro.setEnergia(guerreiro.getEnergia()-20)
