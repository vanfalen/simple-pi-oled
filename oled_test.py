#!/usr/bin/python3
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from time import sleep
import subprocess
from time import sleep
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

def getIP():
	c=subprocess.Popen("ifconfig wlan0",shell=True,stdout=subprocess.PIPE)
	c.wait()
	for line in c.stdout:
		if "broadcast 192.168.1.255" in str(line):
			try:
				return line.split()[1]
			except:
				return ""
while True:
	ip=getIP()
	if ip is not None and ip != "":
		with canvas(device) as draw:
		    #draw.rectangle(device.bounding_box, outline="white", fill="black")
		    draw.text((20, 20), ip, fill="white")
		    #wait here forever
		sleep(10)
		break
	else:
		sleep(5)


