from cci.AbstractControle import AbstractControle
from cgd.DAOBatalha import DAOBatalha
from cih.TelaHistorico import TelaHistorico

__author__ = 'Italo'


class Controle_Historico(AbstractControle):

    def __init__(self, janela):
        self.janela_principal = janela

    def carregar_tela(self):
        dao = DAOBatalha()
        list = dao.get_batalhas()
        TelaHistorico(self.janela_principal,list)
