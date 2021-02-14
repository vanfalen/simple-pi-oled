# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import random


random.seed()
deltas=[-1,0,1]
# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width-1, height-1), outline=1, fill=0)
curr_x=3
curr_y=3
delta_x=1
delta_y=0
frame_skip=5
curr_frame=0
while True:
	#draw.point([curr_x,curr_y],fill=255)
	draw.arc([curr_x,curr_y,curr_x+10,curr_y+10],0,360,fill=None)#delete the old circle
	curr_x+=delta_x
	curr_y+=delta_y
	if curr_x+10>=width-2: 
	    delta_x=-1
	    delta_y=deltas[random.randint(0,2)]
	if curr_x<=2:
	    delta_x=1
	    delta_y=deltas[random.randint(0,2)]
	if curr_y+10>=height-2: 
	    delta_y=-1
	    delta_x=deltas[random.randint(0,2)]
	if curr_y<=2:
	    delta_y=1
	    delta_x=deltas[random.randint(0,2)]
	curr_frame+=1
	if curr_frame>=frame_skip:
		draw.arc([curr_x,curr_y,curr_x+10,curr_y+10],0,360,fill=255)
		disp.image(image)
		disp.show()
		curr_frame=0
	#time.sleep(0.001)
