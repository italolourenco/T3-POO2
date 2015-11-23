# coding=utf-8
from cci.Controle_Menu import Controle_Menu
from cdp.Chunku import Chunku
from cdp.Defensor import Defensor
from cdp.TanTan import TanTan
from util.FactoryFlyWeightControles import FactoryFlyWeightControles
from util.FactoryReflection import FactoryReflection


class Testes(object):


    def testReflection(self):
        fabrica = FactoryReflection()
        guerreiro = fabrica.criar_guerreiro("TanTan")

        if type(guerreiro) == type(TanTan()):
            print 'True'

    def testAtacar(self):
        guerreiro = Chunku()
        defensor = TanTan()
        guerreiro.atacar(defensor,None,None,None)

        if defensor.getEnergia() == 90:
            print 'True'


    def testAtactReflection(self):
        fabrica = FactoryReflection()
        guerreiro = fabrica.criar_guerreiro("Seak")
        defensor = fabrica.criar_guerreiro("MongeBomb")
        guerreiro.atacar(defensor,None,None,None)

        if defensor.getEnergia() == 75:
            print 'True'

    def flyweight(self):
        fabrica = FactoryFlyWeightControles('teste','teste')
        controle = fabrica.get_controle("Menu")

        if(type(controle) == type(Controle_Menu('teste','teste'))):
            print 'True'







