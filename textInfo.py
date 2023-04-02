import PyGine
class textInfo(PyGine.GameObject) :
    def __init__(self, text = "", pos = PyGine.Vector3(0,0,0), color = (255,255,255),size = 32) :
        super().__init__()
        self.fixed = True
        self.text = text
        self.transform.position = pos
        self.color = color
        self.size = size

    def start(self) :
        self.addComponent(PyGine.TextComponent(self,self.text, self.color, self.size))