from oled_screen import oled_screen
from oled_object import oled_object
from PIL import ImageFont

class text_box(oled_object):
    def __init__(self,init_x,init_y,text,display,draw,image,lock,show):
        self.text=text
        self.font = ImageFont.load_default()
        super().__init__(init_x,init_y,display,draw,image,lock,show)
    @classmethod
    def using_screen(cls,init_x,init_y,text,screen,lock,show):
        return cls(init_x,init_y,text,screen.disp,screen.draw,screen.image,lock,show)
    def drawObject(self):
            self.draw.text((self.current_x, self.current_y), self.text, font=self.font, fill=255)
            super().drawObject()
    def deleteObject(self):
            self.draw.text((self.current_x, self.current_y), self.text, font=self.font, fill=None)
            #super().drawObject()
    def setText(self,text):
            self.text=text
