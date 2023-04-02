import PyGine
from gridManager import gridManager
from HUD import HUD

class GameScene(PyGine.Scene) :

    def start(self) :
        self.addGameObject(gridManager())
        self.addGameObject(HUD())
        print("GameScene started")
        PyGine.Game.game.setBgColor((0,0,0))