import PyGine
from GameScene import GameScene
from startScene import startScene
class game(PyGine.Game) :
    def __init__(self) :
        super().__init__(1000, 600,self)
        self.addScene(GameScene())
        self.addScene(startScene())

        self.setScene(2)
        self.setImageLibFolder("Images")
        self.fps = 60

game().run()