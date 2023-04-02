import PyGine
from Cell import Cell
import random
class gridManager(PyGine.GameObject) :
    def __init__(self) :
        super().__init__()
        self.name = "GM"
        

    def start(self) :
        self.grid = [[PyGine.Game.game.instanciate(Cell(i * 50,j*50,getRandomState())) for i in range(20)] for j in range(12)]

    def initGame(self) :
        for i in range(20) :
            for j in range(12) :
                self.grid[j][i].destroy()
        self.grid = [[PyGine.Game.game.instanciate(Cell(i * 50,j*50,getRandomState())) for i in range(20)] for j in range(12)]
    

    def update(self,dt) :
        pass


def getRandomState() :
    choices = ["-1", "0"]
    return random.choices(choices, weights = [0.2,0.8])[0]