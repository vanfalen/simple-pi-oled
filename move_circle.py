import time
import subprocess

import random
from oled_screen import oled_screen
from oled_circle_2 import circle
import threading
from oled_text_box import text_box
from threading import Condition
from queue import Queue


random.seed()
deltas=[-1,0,1]


lock=threading.Lock()
myScreen=oled_screen()
width=myScreen.disp.width
height=myScreen.disp.height
width//=2
cv=Condition()
q=Queue(1)
q.put(None)
def timer(cv,q):
    max_threads=4
    curr_thread=0
    while True:
        with cv:
            print("adding %d\n"%(curr_thread))
            q.get(False)
            q.put(curr_thread,False)
            print("added %d\n"%(curr_thread))
            cv.notifyAll()
            curr_thread+=1
            if curr_thread >= max_threads:
                curr_thread=0
        time.sleep(1)
        


myScreen.draw.rectangle((0, 0, width-1, height-1), outline=1, fill=0)
def showCPU(lock):
    curr_x=width+2
    curr_y=2
    myTextBox=text_box.using_screen(curr_x,curr_y,"",myScreen,lock,False)
    import subprocess
    while True:
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load:\\n%.2f %%\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
        with myTextBox.lock:
           myTextBox.deleteObject()
           myTextBox.setText(CPU)
           myTextBox.drawObject()
        time.sleep(2)


def animateCircle(lock,cv,q,turn):
    curr_x=3
    curr_y=3
    delta_x=1
    delta_y=0
    frame_skip=4
    curr_frame=0
    myTurn=turn
    current_turn=-1
    myCircle=circle.using_screen(curr_x,curr_y,5,myScreen,lock,False)
    while True:
            while current_turn != myTurn:
                    with cv:
                        cv.wait()
                        current_turn=q.get(False)
                        q.put(current_turn,False)
            #its our turn to draw
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
                    myCircle.teleportObject(curr_x,curr_y)
                    curr_frame=0
timerThread=threading.Thread(target=timer,args=(cv,q))
t1=threading.Thread(target=animateCircle,args=(lock,cv,q,0))
t2=threading.Thread(target=animateCircle,args=(lock,cv,q,1))
t4=threading.Thread(target=showCPU,args=(lock,))
t3=threading.Thread(target=animateCircle,args=(lock,cv,q,2))
t5=threading.Thread(target=animateCircle,args=(lock,cv,q,3))
t1.start()
t2.start()
t4.start()
t3.start()
t5.start()
timerThread.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
timerThread.join()

while False:
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
