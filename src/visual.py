"""
############################################################
Visual
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/04/09
:Status: This is a "work in progress"
:Revision: 0.1.1
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
RAIO = 45
RAIOP=1.618 * 45 / 2
ESPACO = 10
PASSO = 2 * RAIO + ESPACO
LP = ESPACO + 2 * PASSO
LG = ESPACO + 4 * PASSO
BASE = LP + LG + 3 * ESPACO

from tabuleiro import Tabuleiro
from mao import Mao
from casa import Casa
def main(doc):
  print('Quarto 0.1.0')

class Visual:
    """Base do jogo com tabuleiro e duas maos."""
    def __init__(self,doc,gui):
        """Constroi as partes do Jogo. """
        self.gui = gui
        self.canvas=gui.svg(width=BASE,height=BASE)
        doc["main"] <= self.canvas
        self.build_base()
        self.build_campo(gui)
        #self.build_tabuleiro(gui)
        #self.build_mao(gui)
        
    def build_base(self,gui):
        """docs here"""
        base=self.gui.rect(x=0, y= 0, width=BASE, height=BASE,rx = RAIO,fill="navajowhite")
        self.canvas <= base
        
    def build_tabuleiro(self,gui):
        return self.build_parte(ESPACO,LP+2*ESPACO,4,4)
    def build_mao(self,gui):
        """docs here"""
       # self.mao1 = Mao(gui)
        #gui.rect(x=10, y= 10, width=800, heigth=600)
        mao1 = self.build_parte(ESPACO,ESPACO,4,2)
        mao2 = self.build_parte(LG + 2 * ESPACO,LP+2*ESPACO,2,4)
        return (mao1 + mao2)
        
    def build_campo(self,gui):
        """docs here"""
        #self.campo = Casa(gui)
        #self.build_parte(LG + 2 * ESPACO,ESPACO,1,1)
        
    def build_casa(self,lugar,x,y):
        """docs here"""
        #self.casa = Casa(gui)
        elipse=self.gui.ellipse(cx=0 , cy=0, ry=RAIO,rx = RAIO,fill="burlywood")
        casa=self.gui.g(transform = "translate(%d %d)"%(x,y))
        casa <= elipse
        lugar<= casa
        return casa
    def build_pecas(self,lugar):
      print('build pecas')
      return[self.build_peca(umlugar,tipo)
             for tipo,umlugar in enumerate(lugar)]
    def build_peca(self,lugar,tipo):
        #self.casa = Casa(gui)
        cores =("sandybrown" , "saddlebrown")
        elipse=self.gui.ellipse(cx=0 , cy=0, ry=RAIOP,rx = RAIOP,fill=(cores[tipo %2]))
        peca=self.gui.g()
        peca <= elipse
        lugar<= peca
        return peca
    def build_parte(self,x,y,nch,ncv):
        rect=self.gui.rect(x=x,y=y, width=nch*PASSO+ESPACO, height=ncv*PASSO+ESPACO,rx = RAIO,fill="peru")
        self.canvas <= rect
        casas = [self.build_casa(self.canvas,
                                 ESPACO + RAIO + x +(c%nch)*PASSO,
                                 ESPACO+RAIO+y+(c//nch)*PASSO) for c in range(nch * ncv)]
        return casas 

