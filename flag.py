import PyGine
class flag(PyGine.GameObject) :

    def __init__(self,x,y) :
        super().__init__()
        self.transform.position = PyGine.Vector3(x,y,0) 
        self.transform.scale = PyGine.Vector3(20,20,0)

    def start(self) :
        self.addComponent(PyGine.SpriteComponent(self,"Carrot.jpg"))
