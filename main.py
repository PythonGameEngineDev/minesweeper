import PyGine
from Scene1 import Scene1
from GameOverScene import GameOverScene
from startScene import startScene
class game(PyGine.Game) :
    def __init__(self) :
        super().__init__(1000, 600,self)
        self.addScene(Scene1())
        self.addScene(GameOverScene())
        self.addScene(startScene())

        self.setScene(3)
        self.setImageLibFolder("Images")
        self.fps = 60

game().run()