from oled_object import oled_object
class circle(oled_object):
    def __init__(self,init_x,init_y,radius,display,draw,image,lock,show=False):
        self.radius=radius
        super().__init__(init_x,init_y,display,draw,image,lock,show)
    @classmethod
    def using_screen(cls,init_x,init_y,radius,screen,lock,show):
        return cls(init_x,init_y,radius,screen.disp,screen.draw,screen.image,lock,show)

    def drawObject(self):
            self.draw.arc([self.current_x,self.current_y,self.current_x+(2*self.radius),self.current_y+(2*self.radius)],0,360,fill=255)
            super().drawObject()
    def deleteObject(self):
            self.draw.arc([self.current_x,self.current_y,self.current_x+(2*self.radius),self.current_y+(2*self.radius)],0,360,fill=None)
            #super().drawObject()

# _____
#|     |
#|     |
#|     |
#|     |
#|_____|

