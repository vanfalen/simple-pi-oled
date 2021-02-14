class circle(object):
    def __init__(self,init_x,init_y,radius,display,draw,image,lock,show=False):
        self.current_x=init_x
        self.current_y=init_y
        self.display=display
        self.draw=draw
        self.image=image
        self.radius=radius
        self.lock=lock
        if show:
            self.drawShape()
    def drawShape(self):
            self.draw.arc([self.current_x,self.current_y,self.current_x+(2*self.radius),self.current_y+(2*self.radius)],0,360,fill=255)
            self.display.image(self.image)
            self.display.show()
    def moveShape(self,delta_x,delta_y):
        self.draw.arc([self.current_x,self.current_y,self.current_x+(2*self.radius),self.current_y+(2*self.radius)],0,360,fill=None)
        self.current_x+=delta_x
        self.current_y+=delta_y
        self.drawShape()
    def teleportShape(self,new_x,new_y):
        with self.lock:
            self.draw.arc([self.current_x,self.current_y,self.current_x+(2*self.radius),self.current_y+(2*self.radius)],0,360,fill=None)
            self.current_x=new_x
            self.current_y=new_y
            self.drawShape()

# _____
#|     |
#|     |
#|     |
#|     |
#|_____|

