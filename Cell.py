import PyGine
from valueCounter import valueCounter
from flag import flag
import sys
sys.setrecursionlimit(10000)

class Cell(PyGine.GameObject) :
    def __init__(self, x, y,value) :

        super().__init__()

        self.transform.position = PyGine.Vector3(x, y, 0)
        self.transform.scale = PyGine.Vector3(49,49,0)

        self.dr = self.addComponent(PyGine.DrawRectComponent(self,(100,100,100)))
        self.revealed = False
        self.value = value

        self.flagged = False
        self.flag = None


    def verify(self) :
        grid =PyGine.Game.game.getCurrentScene().getGameObject("GM").grid
        x = int(self.transform.position.x // 50)
        y = int(self.transform.position.y // 50)

        if self.value == "-1" :
            PyGine.Game.game.getCurrentScene().getGameObject("GM").initGame()
            PyGine.Game.game.setScene(2)
            return

        for px in [x-1 , x , x+1] :
            for py in [y-1 , y , y+1] :
                if px >= 0 and px < 20 and py >= 0 and py < 12 and not (px == x and py == y):
                    if grid[py][px].value == "-1" :
                        self.value = str(int(self.value) + 1)
        
        if self.value == "0" :
            for px in [x-1 , x , x+1] :
                for py in [y-1 , y , y+1] :
                    if px >= 0 and px < 20 and py >= 0 and py < 12 and not (px == x and py == y):
                        if not grid[py][px].revealed :
                            self.revealed = True
                            grid[py][px].verify()
                            grid[py][px].reveal()


    def reveal(self) :
        self.revealed = True
        self.addComponent(PyGine.DrawRectComponent(self,(0,0,0)))
        self.addComponent(valueCounter(self))
        if self.flag :
            self.flag.destroy()


    def update(self,dt) :

        self.dr.color = (100,100,100)
        if self.transform.isPointInside(PyGine.MouseListener.getPos()) :
            self.dr.color = (120,120,150)

        if PyGine.MouseListener.getPressed(0) and self.transform.isPointInside(PyGine.MouseListener.getPos()) and not self.revealed :
            self.verify()
            self.reveal()



        if PyGine.KeyListener.getPressed(ord("f")) and self.transform.isPointInside(PyGine.MouseListener.getPos()) and not self.flagged :
            self.flagged = True
            self.flag = PyGine.Game.game.instanciate(flag(self.transform.position.x, self.transform.position.y))

        if PyGine.KeyListener.getPressed(ord("d"))  and self.transform.isPointInside(PyGine.MouseListener.getPos()) and self.flagged:

            self.flagged = False
            self.flag.destroy()

