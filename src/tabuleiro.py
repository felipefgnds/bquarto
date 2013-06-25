"""
############################################################
Quarto - Tabuleiro
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

class Tabuleiro:
    """Lugar com casas onde se jogam as pecas."""
    def __init__(self, gui):
        tabuleiro_visual=gui.build_tabuleiro()
        """Constroi as partes do Jogo. """
        self.casas = [Casa(casa_v)
            for casa_v in gui.build_tabuleiro()]
        
    #: TODO - put all the rest

