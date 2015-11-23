from util.Director import Director

class Deus(Director):

    def criarNacao(self, ajudante, nome, listDefensores, listOfensores):
        return ajudante.montar_nacao(nome, listDefensores, listOfensores)