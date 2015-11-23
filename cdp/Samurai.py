from cdp.Guerreiro import Guerreiro

from cdp.Ofensor import Ofensor


class Samurai(Ofensor):

    def __init__ (self):
        Guerreiro.__init__(self,'Japao')
        self.tipo = 'Samurai'

    def atacar(self, guerreiro, ofensores, defensores, defensoresAdversarios):

        if not guerreiro.getTipo() == "MirkOConversor":
            guerreiro.setEnergia(guerreiro.getEnergia()-50)