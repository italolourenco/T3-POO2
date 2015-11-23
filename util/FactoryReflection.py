__author__ = 'Italo'


class FactoryReflection():

    def criar_guerreiro(self,nome):
        nomel = [nome]
        path = 'cdp.'+nome
        _mod = __import__(path,fromlist=nomel)
        teste = getattr(_mod,nome)
        guerreiro = teste()
        return guerreiro

