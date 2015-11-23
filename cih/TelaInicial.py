__author__ = 'Italo'

from tkinter import *

class TelaInicial():

    def __init__(self):


        root = Tk()
        root.geometry("300x300")
        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack()
        frame3 = Frame(root)
        frame3.pack()

        botaoEntrar = Button(frame1, text = 'Entrar')
        botaoEntrar.pack()

        botaoAbout = Button(frame2, text = 'About')
        botaoAbout.pack(side = LEFT)

        botaoCadastro = Button(frame3, text = 'Cadastro')
        botaoCadastro.pack(side = LEFT)

        root.mainloop()
