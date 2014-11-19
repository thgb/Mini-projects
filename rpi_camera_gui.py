import picamera
from time import sleep
from Tkinter import *


camera = picamera.PiCamera()

frame = 1

def onclick():
    pass

def close_window():
    root.destroy()

def take_pic():
    global frame
    camera.start_preview()
    sleep(2)
    camera.capture("/home/pi/Desktop/Photos/frame %d.jpg" % frame)
    frame += 1
    camera.stop_preview()


root = Tk()
root.wm_title("Camera App")
root.geometry('300x300')
a = Button(root, background='green', text="Take Pic", height=5, command=take_pic, font=(30))
b = Button(root, text="Done", height=5, command=close_window)
a.pack()
b.pack()

root.mainloop()
