import tkMessageBox
from cci.AbstractControle import AbstractControle
from cih.TelaSimulacao import TelaSimulacao

__author__ = 'Italo'


class Controle_Simulador(AbstractControle):

    def __init__(self, janela, controle):
        self.janela_principal = janela
        self.controle_geral = controle

    def carregar_tela(self):
        TelaSimulacao(self.janela_principal,self)

    def get_nacoes(self,list):
        if(list[0]!='' and list[1]!= ''):
            self.controle_geral.iniciar_luta(list)
        else:
            self.mensagemAviso()

    def ir_telaMenu(self):
        self.controle_geral.carregar_menu()

    def mensagemAviso(self):
        tkMessageBox.showinfo("Mensagem", "Por favor - Informe os caminhos corretamente!")

