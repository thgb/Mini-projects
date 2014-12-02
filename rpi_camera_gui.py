import picamera
from time import sleep
from Tkinter import *
import RPi.GPIO as GPIO


camera = picamera.PiCamera()
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
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


def detect_button():
    while True:
        input_state = GPIO.input(18)
        if input_state is False:
            take_pic()
            break

root = Tk()
root.wm_title("Camera App")
root.geometry('300x300')
a = Button(root, text="Take Pic", height=5, command=take_pic, font=(30))
b = Button(root, text="Use Button", height=5, command=detect_button, font=(30))
c = Button(root, text="Done", height=5, command=close_window)
a.pack()
b.pack()
c.pack()


root.mainloop()
