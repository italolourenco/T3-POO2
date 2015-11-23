__author__ = 'Italo'

from tkinter import *
import tkMessageBox
import tkFont

class TelaSimulacao():


    def __init__(self, janela_principal, controle):

        self.nomeN1 = StringVar()
        self.nomeN2 = StringVar()

        janela_principal.title("Tela Simulador")

        frameG = Frame(janela_principal)
        frameG.place(x=0,y=0,relwidth=1,relheight=1)

        imagem_fundo = PhotoImage(file='imagens\simulador.gif')
        labelImagem = Label(frameG, image=imagem_fundo)
        labelImagem.place(x=0,y=0,relwidth=1,relheight=1)

        frameTOP = Frame(frameG)
        frameTOP.pack(side = TOP)

        frameMeio = Frame(frameG)
        frameMeio.pack(padx=10, pady=130)

        frameFim = Frame(frameG)
        frameFim.pack(side=BOTTOM)

        textTitle = Label(frameTOP, text = 'CARREGAR NACOES')
        textTitle.pack()

        frameN1 = Frame(frameMeio)
        frameN1.pack(side = BOTTOM)

        textNacao1 = Label(frameN1, text='Nacao 1:')
        textNacao1.pack(side = LEFT)

        campNacao1 = Entry(frameN1, textvar = self.nomeN1)
        campNacao1.pack()

        frameN2 = Frame(frameG)
        frameN2.pack()

        textNacao2 = Label(frameN2, text='Nacao 2:')
        textNacao2.pack(side = LEFT)

        campNacao2 = Entry(frameN2,textvar = self.nomeN2)
        campNacao2.pack()

        frameB = Frame(frameG)
        frameB.pack(side = BOTTOM)

        botaoEnviar = Button(frameB, text = 'SIMULAR', height='0', width='10', command = lambda : self.salve_nacao(self.nomeN1.get(),self.nomeN2.get(),controle))
        botaoEnviar.pack(side = LEFT)

        botaoVoltar = Button(frameB, text = 'VOLTAR', height='0', width='10', command = lambda : controle.ir_telaMenu())
        botaoVoltar.pack(side = RIGHT)

        frameG.mainloop()

    def salve_nacao(self, n1, n2,controle):
        list=[]
        list.append(n1)
        list.append(n2)
        controle.get_nacoes(list)
