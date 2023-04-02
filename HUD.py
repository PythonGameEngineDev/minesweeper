import PyGine
from clock import clock
from textInfo import textInfo
class HUD(PyGine.Overlay) :
    def start(self) :
        PyGine.Game.game.instanciate(clock(self))
        PyGine.Game.game.instanciate(textInfo("Press F to Flag", PyGine.Vector3(0, 40,0), (255,255,255),20))
        PyGine.Game.game.instanciate(textInfo("Press D to UnFlag", PyGine.Vector3(0, 80,0), (255,255,255),20))