from cdp.Guerreiro import Guerreiro
from cdp.Ninja import Ninja
from cdp.Defensor import Defensor

class TanTan(Defensor):

    def __init__ (self):
        Guerreiro.__init__(self,'Japao')
        self.tipo = 'Tantan'

    def defender(self, guerreiro, defensores, ofensores, ofensoresAdversarios):
        energia = self.getEnergia()

        if energia <=0:
            ninja = Ninja(self.nome,self.idade,self.peso)
            ofensores.append(ninja)


