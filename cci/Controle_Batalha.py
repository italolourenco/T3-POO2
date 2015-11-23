from cdp.Batalha import Batalha


class Controle_Batalha(object):

    def iniciarBatalha(self, arquivo1, arquivo2):

        batalha = Batalha()
        batalha.carregar(arquivo1,arquivo2)
        batalha.lutar()
        batalha.gerarResultados()
        return batalha