__author__ = 'Italo'

from tkinter import *

class TelaMenu():

    escolha = None

    def __init__(self,janela_principal, controle):


        janela_principal.title("Age of Simulator")
        frameG = Frame(janela_principal)
        frameG.place(x=0,y=0,relwidth=1,relheight=1)

        imagem_fundo = PhotoImage(file='imagens\menu.gif')
        label1 = Label(frameG, image=imagem_fundo)
        label1.place(x=0,y=0,relwidth=1,relheight=1)

        botaoSair = Button(frameG, text = 'SAIR', height='0', width='10', command=lambda:controle.sair_simulador())
        botaoSair.pack(side = BOTTOM)

        botaoAbout = Button(frameG, text = 'INSTRUCOES', height='0', width='10', command = lambda:controle.ir_janelaInstrucoes())
        botaoAbout.pack(side = BOTTOM)

        botaoHistorico = Button(frameG, text = 'HISTORICO', height='0', width='10', command=lambda:controle.ir_janelaHistorico())
        botaoHistorico.pack(side = BOTTOM)

        botaoSimular = Button(frameG, text = 'SIMULADOR', height='0', width='10', command=lambda:controle.ir_janelaSimulacao())
        botaoSimular.pack(side = BOTTOM)

        frameG.mainloop()



