import PyGine
from gridManager import gridManager
from HUD import HUD

class GameOverScene(PyGine.Scene) :
    def __init__(self) :
        super().__init__()
        PyGine.Game.game.setBgColor((100,10,10))

    def update(self, dt):
        if PyGine.KeyListener.getPressed(ord("r")) :
            PyGine.Game.game.setScene(3)
            print("goto start scene")
