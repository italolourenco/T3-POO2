__author__ = 'Italo'


__author__ = 'Italo'

from tkinter import *
import tkMessageBox
import tkFont

class TelaResultado():

    def __init__(self, janela_principal, controle, nacao1, nacao2, resultado, codicaoVitoria):


        janela_principal.title("Tela de Resultado")
        janela_principal.resizable(0,0)
        frameG = Frame(janela_principal)
        frameG.place(x=0,y=0,relwidth=1,relheight=1)

        frameN1 = Frame(frameG)
        frameN1.grid(row = 0, column = 1, pady='50')
        labelTxt = Label(frameN1, text = "Nacao 1")
        labelTxt.pack()
        labelTxtN1 = Label(frameN1, text = nacao1)
        labelTxtN1.pack()

        frameN2 = Frame(frameG)
        frameN2.grid(row=1,column=1, pady='50')
        labelTxt2 = Label(frameN2,text = "Nacao 2")
        labelTxt2.pack()
        labelTxtN2 = Label(frameN2, text = nacao2)
        labelTxtN2.pack()

        frameResultado = Frame(frameG)
        frameResultado.grid(row = 2, column = 1, pady='50')
        labelTxt3 = Label(frameResultado, text = "  Resultado:")
        labelTxt3.pack()
        labelTxtResultado = Label(frameResultado, text ="  " + resultado + codicaoVitoria)
        labelTxtResultado.pack(side = RIGHT)

        frameBotoes = Frame(frameG)
        frameBotoes.grid(row = 3, column=50, padx = '100')
        botaoSair = Button(frameBotoes, text = 'SAIR', height='0', width='10', command=lambda: controle.sair())
        botaoSair.pack(side = RIGHT)

        botaoSalvar = Button(frameBotoes, text = 'SALVAR', height='0', width='10',command=lambda:controle.salvar())
        botaoSalvar.pack(side = LEFT)

        frameG.mainloop()

