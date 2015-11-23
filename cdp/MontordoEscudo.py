from cdp.Guerreiro import Guerreiro
from cdp.Defensor import Defensor

class MontordoEscudo(Defensor):

    def __init__ (self):
        Guerreiro.__init__(self,'China')
        self.tipo = 'MontordoEscudo'
        self.setEnergia(150)

    def defender(self, guerreiro, defensores, ofensores, ofensoresAdversarios):
        guerreiro.setEnergia(0)