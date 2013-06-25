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
        self.build_tabuleiro(gui)
        self.build_mao(gui)
        
    def build_base(self,gui):
        """docs here"""
        base=self.gui.rect(x=0, y= 0, width=BASE, height=BASE,rx = RAIO,fill="navajowhite")
        self.canvas <= base
        
    def build_tabuleiro(self,gui):
        self.build_parte(ESPACO,LP+2*ESPACO,4,4)
    def build_mao(self,gui):
        """docs here"""
       # self.mao1 = Mao(gui)
        #gui.rect(x=10, y= 10, width=800, heigth=600)
        self.build_parte(ESPACO,ESPACO,4,2)
        self.build_parte(LG + 2 * ESPACO,LP+2*ESPACO,2,4)
        
    def build_campo(self,gui):
        """docs here"""
        #self.campo = Casa(gui)
        #self.build_parte(LG + 2 * ESPACO,ESPACO,1,1)
        
    def build_casa(self,lugar,x,y):
        """docs here"""
        #self.casa = Casa(gui)
        casa=self.gui.ellipse(cx=x , cy=y, ry=RAIO,rx = RAIO,fill="burlywood")
        lugar <= casa
    def build_parte(self,x,y,nch,ncv):
        rect=self.gui.rect(x=x,y=y, width=nch*PASSO+ESPACO, height=ncv*PASSO+ESPACO,rx = RAIO,fill="peru")
        self.canvas <= rect
        casas = [self.build_casa(self.canvas,
                                 ESPACO + RAIO + x +(c%nch)*PASSO,
                                 ESPACO+RAIO+y+(c//nch)*PASSO) for c in range(nch * ncv)]

