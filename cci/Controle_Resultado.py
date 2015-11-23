from cci.AbstractControle import AbstractControle
from cih.TelaResultado import TelaResultado

__author__ = 'Italo'


class Controle_Resultado(AbstractControle):

    def __init__(self, janela, controle):
        self.janela_principal = janela
        self.controle_geral = controle

    def carregar_tela(self):
        TelaResultado(self.janela_principal,self,self.controle_geral.batalha.getNacaoNome1(),self.controle_geral.batalha.getNacaoNome2(),self.controle_geral.batalha.resultado,self.controle_geral.batalha.condicaoVitoria)

    def sair(self):
        self.controle_geral.sair_simulador()

    def salvar(self):
        self.controle_geral.salvar_resultado()