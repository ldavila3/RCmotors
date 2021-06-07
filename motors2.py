import RPi.GPIO as gpio
import time
from Tkinter import *
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
# (11 OR 16) XOR 18
pins=[11,16,18,22]
for i in range(len(pins)):
    gpio.setup(pins[i],gpio.OUT)

def values():
    pins=[11,16,18,22]
    outputs=''
    for i in range(len(pins)):
        outputs+=str(gpio.input(pins[i]))
    return outputs
    return str(gpio.input(pins[0]))+str(gpio.input(pins[1]))
def resetpins(activate_0,activate_1):
    stop()
    if activate_0 < 0 or activate_1 >= len(pins):
        return
    for i in range(len(pins)):
        if i == activate_0 or i == activate_1:
            gpio.output(pins[i],1)
def resetpin(activate):
    resetpins(activate,activate)
def stop():
    for i in range(len(pins)):
        gpio.output(pins[i],0)
def stop_(event):
    stop()
def forward(event):
    resetpins(0,1)
    #gpio.output(pins[0],1)
    #gpio.output(pins[1],1)
    print(values())
def turn_right(event):
    resetpin(1)
    #gpio.output(pins[0],1)
    #gpio.output(pins[2],1)
    print(values())
def turn_left(event):
    resetpin(0)
    #gpio.output(pins[0],1)
    #gpio.output(pins[3],1)
    print(values())
def backward(event):
    current=values()
    resetpins(2,3)
    print(values())

root = Tk()
root.title("Motors GUI")
root.geometry("64x32")
app = Frame(root)
app.grid()
button0=Button(app,text="Stop")
button0.bind("<Button-1>",stop_)
button0.grid()
root.bind('w',forward)
root.bind('<KeyRelease-w>',stop_)
root.bind('a',turn_left)
root.bind('<KeyRelease-a>',stop_)
root.bind('d',turn_right)
root.bind('<KeyRelease-d>',stop_)
root.bind('s',backward)
root.bind('<KeyRelease-s>',stop_)
#root.bind('s',stop_s)
root.mainloop()