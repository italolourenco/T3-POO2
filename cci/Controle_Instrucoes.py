from cci.AbstractControle import AbstractControle
from cih.TelaInstrucoes import TelaInstrucoes

class Controle_Instrucoes(AbstractControle):

    def __init__(self, janela, controle):
        self.janela_principal = janela
        self.controle_geral = controle


    def carregar_tela(self):
        TelaInstrucoes(self.janela_principal,self)

    def ir_menu(self):
        self.controle_geral.carregar_menu()



