__author__ = 'Italo'
from tkinter import *

class TelaInstrucoes():

    def __init__(self, janela_principal, controle):

        janela_principal.title("INSTRUCOES")
        janela_principal.resizable(0,0)
        frameG = Frame(janela_principal)
        frameG.place(x=0,y=0,relwidth=1,relheight=1)


        labelTxt = Label(frameG, text = "Siga as instrucoes abaixo para obter sucesso com Age of Simulator",pady = '10')
        labelTxt.pack()

        labelTxt = Label(frameG, text = "OPCAO SIMULAR:",pady = '20')
        labelTxt.pack()

        labelTxt = Label(frameG, text = "Nos campos de Nacao1 e Nacao2 - Deve ser informado o endereco para os arquivos" ,pady = '5')
        labelTxt.pack()

        labelTxt = Label(frameG, text = "- CUIDADO COM O \ n NO FINAL DO ENDERECO" ,pady = '5')
        labelTxt.pack()

        labelTxt = Label(frameG, text = "OPCAO HISTORICO" ,pady = '20')
        labelTxt.pack()

        labelTxt = Label(frameG, text = "Exibe o historico de jogadas salvas; Informa o nome das nacoes e o resultado da batalha" ,pady = '5')
        labelTxt.pack()

        labelTxt = Label(frameG, text = "ARQUIVOS" ,pady = '20')
        labelTxt.pack()

        labelTxt = Label(frameG, text = "Siga o exemplo de formatacao do arquivo que esta na pasta do simulador - EXEMPLO.TXT" ,pady = '5')
        labelTxt.pack()

        botaoVoltar = Button(frameG, text = 'VOLTAR', height='0', width='10', command = lambda : controle.ir_menu())
        botaoVoltar.pack(side = BOTTOM)
