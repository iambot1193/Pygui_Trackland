import pynput as nput
from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed: 
        print("X:{} Y:{}".format(x , y))


with mouse.Listener(on_click=on_click) as listener:
    listener.join()  # Keeps the program running and listening