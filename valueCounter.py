import PyGine
class valueCounter(PyGine.GameObject) :
    def __init__(self,cell) :
        super().__init__()
        self.parent = cell
        self.transform.position = PyGine.Vector3(20,20,0)
        self.transform.scale = PyGine.Vector3(1,2,0)
        self.txt = self.addComponent(PyGine.TextComponent(self,str(cell.value)))

    def update(self, dt):
        self.txt.setText(str(self.parent.value))
