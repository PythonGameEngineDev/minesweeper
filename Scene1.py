import PyGine
from gridManager import gridManager
from HUD import HUD

class Scene1(PyGine.Scene) :

    def start(self) :
        self.addGameObject(gridManager())
        self.addGameObject(HUD())
        print("Scene1 started")
        PyGine.Game.game.setBgColor((0,0,0))