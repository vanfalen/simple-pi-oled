from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
class oled_screen(object):
    def __init__(self):
        i2c = busio.I2C(SCL, SDA)
        self.disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
        self.disp.fill(0)
        self.disp.show()
        height = self.disp.height
        width = self.disp.width
        self.image = Image.new("1", (width, height))
        self.draw = ImageDraw.Draw(self.image)


