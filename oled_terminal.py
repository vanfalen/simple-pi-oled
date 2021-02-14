from demo_opts import get_device
from luma.core.virtual import terminal
from PIL import ImageFont

def make_font(name, size):                                                 
	font_path = '/home/pi/Downloads/luma.examples-master/examples/fonts/%s'%(name)
	return ImageFont.truetype(font_path, size)                             
class oled_term(object):
    def __init__(self):
        self.font=make_font("miscfs_.ttf", 12)
        self.device=get_device()
        self.term=terminal(self.device,self.font)
        #self.term=terminal(self.device,None)
    def print_line(self,line):
        self.term.println(line)
