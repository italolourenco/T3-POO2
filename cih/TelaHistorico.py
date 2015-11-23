__author__ = 'Italo'

from tkinter import *

class TelaHistorico():

    def __init__(self, janela_principal, list):

        janela_principal.title("Historico")
        janela_principal.resizable(0,0)
        frameG = Frame(janela_principal)
        frameG.place(x=0,y=0,relwidth=1,relheight=1)

        frameN1 = Frame(frameG)
        frameN1.grid(row = 2, column = 1, padx='80', pady='20')
        labelTxt = Label(frameN1, text = "Nacao 1")
        labelTxt.pack()

        frameN2 = Frame(frameG)
        frameN2.grid(row = 2, column = 2, padx='80')
        labelTxt = Label(frameN2, text = "Nacao 2")
        labelTxt.pack()

        frameN3 = Frame(frameG)
        frameN3.grid(row = 2, column = 3, padx='0',pady='18')
        labelTxt = Label(frameN3, text = "Resultado")
        labelTxt.pack()

        i=0
        while(len(list)>i):
            labelTxt1 = Label(frameN1,text = list[i][0])
            labelTxt1.pack()
            labelTxt2 = Label(frameN2,text = list[i][1])
            labelTxt2.pack()
            labelTxt3 = Label(frameN3,text = list[i][2])
            labelTxt3.pack()
            labelTxt3 = Label(frameN3,text = "")
            labelTxt3.pack()
            i+=1


