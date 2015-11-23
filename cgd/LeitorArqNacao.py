class LeitorArqNacao(object):

    def leituraAtacantes(self,arquivo):

        listOfensores = []

        ARQ = open(arquivo, 'r')
        nacao = ARQ.readline()
        linha = ARQ.readline()
        linha = ARQ.readline()
        while (linha != 'Defensores\n'):

                dados = linha.split('\n')
                listOfensores.append(dados)

                linha = ARQ.readline()
        return listOfensores

    def leituraDefensores(self, arquivo):

        listDefensores = []

        ARQ = open(arquivo, 'r')
        nacao = ARQ.readline()
        linha = ARQ.readline()
        linha = ARQ.readline()
        while (linha != 'Defensores\n'):
            linha = ARQ.readline()

        linha = ARQ.readline()
        while linha!= '\n' and linha!= '':

            dados = linha.split('\n')
            listDefensores.append(dados)

            linha = ARQ.readline()

        return listDefensores

    def leituraNome(self, arquivo):

        ARQ = open(arquivo, 'r')
        nacao = ARQ.readline()
        ARQ.close()
        return nacao