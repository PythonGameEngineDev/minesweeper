import PyGine
from clock import clock
from textInfo import textInfo
class info(PyGine.Overlay) :
    def start(self) :
        PyGine.Game.game.instanciate(textInfo("Press S to start", PyGine.Vector3(250, 200,0), (255,255,255), 64))
        