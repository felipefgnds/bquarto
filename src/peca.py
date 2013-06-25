"""
############################################################
Quarto - Peca
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

class Peca:
    """Representa uma peca do jogo"""
    def __init__(self, peca_visual):
        """Constroi uma peca"""
        self.peca = peca_visual
        
    def selecionou(self, pecas, campo):
        campo.peca = pecas[0]
        pecas.remove(campo.peca)
        
    #: TODO - put all the rest

