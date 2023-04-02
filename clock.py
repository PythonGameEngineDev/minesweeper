import PyGine
class clock(PyGine.GameObject) :

    def __init__(self, parent) :
        super().__init__()
        self.parent = parent
        self.transform.position = PyGine.Vector3(0,0,0)
        self.transform.scale = PyGine.Vector3(100,100,0)
        self.txt = self.addComponent(PyGine.TextComponent(self,"0",(200,200,200),20))
        self.fixed = True
        self.time = 0
        self.txt.setText(str(self.time//60))

    def update(self, dt):
        self.time += 1
        self.txt.setText("Time played : " + str(self.time//60))