from cdp.Guerreiro import Guerreiro
from cdp.Defensor import Defensor

class MongeBomb(Defensor):

    def __init__ (self):
        Guerreiro.__init__(self,'India')
        self.tipo = 'MongeBomb'

    def defender(self, guerreiro, defensores, ofensores, ofensoresAdversarios):
        guerreiro.setEnergia(1)

