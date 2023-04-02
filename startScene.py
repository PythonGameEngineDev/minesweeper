import PyGine
from gridManager import gridManager
from HUD import HUD

class startScene(PyGine.Scene) :
    def __init__(self) :
        super().__init__()
        

    def update(self, dt):
        PyGine.Game.game.setBgColor((100,10,10))
        if PyGine.KeyListener.getPressed(ord("s")) :
            PyGine.Game.game.setScene(1)
