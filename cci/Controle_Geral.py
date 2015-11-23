from cgd.DAOBatalha import DAOBatalha
from cci.Controle_Batalha import Controle_Batalha

from tkinter import *
from util.FactoryFlyWeightControles import FactoryFlyWeightControles

__author__ = 'Italo'

import tkMessageBox

class Controle_Geral():

    def criar_tela(self):
        self.janela_principal = Tk()
        self.janela_principal.geometry("640x600")

    def iniciar_simulador(self):
        self.criar_tela()
        self.carregar_controles()
        self.carregar_menu()

    def carregar_controles(self):
        self.controle_factory = FactoryFlyWeightControles(self.janela_principal,self)

    def carregar_menu(self):
        ctrl_menu = self.controle_factory.get_controle('Menu')
        ctrl_menu.carregar_tela()

    def iniciar_luta(self, list):
        controleBatalha = Controle_Batalha()
        self.batalha = controleBatalha.iniciarBatalha(list[0], list[1])
        ctrl_resultado = self.controle_factory.get_controle('Resultado')
        ctrl_resultado.carregar_tela()

    def salvar_resultado(self):
        daoBatalha = DAOBatalha()
        daoBatalha.cria_conexao()
        daoBatalha.insere_batalha(self.batalha)
        daoBatalha.cancelar_conexao()
        self.mensagemSalvar()
        self.carregar_menu()

    def mensagemSalvar(self):
        tkMessageBox.showinfo("Mensagem", "Salvo Com Suceeso")

    def tela_instrucoes(self):
        ctrl_intrucoes = self.controle_factory.get_controle('Instrucoes')
        ctrl_intrucoes.carregar_tela()

    def tela_simulador(self):
        ctrl_simulador = self.controle_factory.get_controle('Simulador')
        ctrl_simulador.carregar_tela()

    def tela_historico(self):
        ctrl_historico = self.controle_factory.get_controle('Historico')
        ctrl_historico.carregar_tela()

    def sair_simulador(self):
        self.janela_principal.destroy()



