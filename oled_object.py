class oled_object(object):
    def __init__(self,init_x,init_y,display,draw,image,lock,show=False):
        self.current_x=init_x
        self.current_y=init_y
        self.display=display
        self.draw=draw
        self.image=image
        self.lock=lock
        if show:
            with self.lock:
                self.drawObject()
    def drawObject(self):
            self.display.image(self.image)
            self.display.show()
    def moveShape(self,delta_x,delta_y):
        with self.lock:
            self.deleteObject()
            self.current_x+=delta_x
            self.current_y+=delta_y
            self.drawShape()
    def deleteObject(self):
        pass
    def teleportObject(self,new_x,new_y):
        with self.lock:
            self.deleteObject()
            self.current_x=new_x
            self.current_y=new_y
            self.drawObject()

