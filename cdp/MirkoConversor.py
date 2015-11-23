from cdp.Guerreiro import Guerreiro
from cdp.Defensor import Defensor
from cdp import Gunte


class MirkoConversor(Defensor):

    def __init__ (self):
        Guerreiro.__init__(self,'China')
        self.tipo = 'MirkoConversor'

    def defender(self, guerreiro, defensores, ofensores, ofensoresAdversarios):

        if guerreiro.getTipo() == "Samurai":
            gunte = Gunte(guerreiro.getNome(), guerreiro.getIdade(), guerreiro.getPeso());
            ofensores.append(gunte)
            ofensoresAdversarios.remove(guerreiro)