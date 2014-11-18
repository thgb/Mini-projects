import picamera
from time import sleep
from Tkinter import *


camera = picamera.PiCamera()

frame = 1

def onclick():
    pass

def onKeyPress(event):
    global frame
    camera.start_preview()
    sleep(2)
    camera.capture("/home/pi/Desktop/Photos/frame %d.jpg" % frame)
    frame += 1
    camera.stop_preview()

root = Tk()
root.wm_title("Camera App")
root.geometry('300x300')

text = Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.insert(INSERT, "Press any key to take a photograph\n")
text.pack()

root.bind('<KeyPress>', onKeyPress)


root.mainloop()