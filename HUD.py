import PyGine
from clock import clock
class HUD(PyGine.Overlay) :
    def start(self) :
        PyGine.Game.game.instanciate(clock(self))
