from cci.AbstractControle import AbstractControle
from cci.Controle_Historico import Controle_Historico
from cci.Controle_Simulador import Controle_Simulador
from cci.Controle_Instrucoes import Controle_Instrucoes
from cih.TelaMenu import TelaMenu

__author__ = 'Italo'

class Controle_Menu(AbstractControle):

    def __init__(self, janela, controle):
        self.janela_principal = janela
        self.controle_geral = controle

    def carregar_tela(self):
        TelaMenu(self.janela_principal,self)

    def sair_simulador(self):
        self.janela_principal.destroy()

    def ir_janelaSimulacao(self):
        self.controle_geral.tela_simulador()

    def ir_janelaHistorico(self):
        ctrl_historico = Controle_Historico(self.janela_principal)
        ctrl_historico.carregar_tela()

    def ir_janelaInstrucoes(self):
        self.controle_geral.tela_instrucoes()




