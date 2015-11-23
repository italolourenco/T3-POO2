from cci.Controle_Historico import Controle_Historico
from cci.Controle_Instrucoes import Controle_Instrucoes
from cci.Controle_Menu import Controle_Menu
from cci.Controle_Simulador import Controle_Simulador
from cci.Controle_Resultado import Controle_Resultado
from util.Singleton import Singleton


class FactoryFlyWeightControles(Singleton):

    controles = {}
    __instance = None

    def __init__(self,janela,controle):

        self.controles = dict([('Menu',Controle_Menu(janela,controle)),('Instrucoes',Controle_Instrucoes(janela,controle)),('Historico',Controle_Historico(janela)),('Simulador',Controle_Simulador(janela,controle)),('Resultado',Controle_Resultado(janela,controle))])


    def get_controle(self, controle):
        return self.controles[controle]