from cdp.Guerreiro import Guerreiro
from cdp.Defensor import Defensor

class MangaldeDefesa(Defensor):

    def __init__ (self):
        Guerreiro.__init__(self,'China')
        self.tipo = 'MangaldeDefesa'

    def defender(self, guerreiro, defensores, ofensores, ofensoresAdversarios):
        guerreiro.setEnergia(guerreiro.getEnergia()-2)

