__author__ = 'Italo'

import sqlite3 as bd

class DAOBatalha():

    def __init__(self):
        self.con = bd.connect('agesimulator1.db')

    def cria_conexao(self):
        cur = self.con.cursor()
        cur.executescript("CREATE TABLE IF NOT EXISTS Batalha(Id_Batalha INTEGER PRIMARY KEY AUTOINCREMENT, Nacao1 TEXT, Nacao2 TEXT, Resultado TEXT);");
        self.con.commit()

    def insere_batalha(self, batalha):
        n1 = batalha.getNacaoNome1()
        n2 = batalha.getNacaoNome2()
        n3 = batalha.resultado
        cur = self.con.cursor()
        cur.execute("INSERT INTO Batalha (Nacao1, Nacao2, Resultado) VALUES (?, ?, ?)", (n1, n2, n3))
        self.con.commit()

    def get_batalhas(self):
        batalhas = []
        cur = self.con.cursor()
        cur.execute("""SELECT Nacao1, Nacao2, Resultado FROM Batalha""")
        for linha in cur.fetchall():
            batalhas.append(linha)
        return batalhas

    def cancelar_conexao(self):
        self.con.close()
