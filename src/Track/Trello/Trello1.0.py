import pyautogui as pa
import time
import keyboard
pa.FAILSAFE = False

keyboard.block_key("f1")
keyboard.block_key("f2")
keyboard.block_key("f3")

def findcolor():    
    mouse_x, mouse_y = pa.position()
    pixel_image = pa.screenshot(region=(mouse_x, mouse_y, 1, 1))
    pixel_color = pixel_image.getpixel((0, 0))
    return pixel_color

def close_progam():
    if keyboard.is_pressed('esc'):
        exit()
    

while(1):
    if keyboard.is_pressed('f2'):
        close_progam()
        
        pa.moveTo(-1350, 270)
        pa.leftClick()
        pa.hotkey("ctrl", "c")
        pa.moveTo(600, 110)
        pa.leftClick()
        pa.hotkey("ctrl", "v")
        btn = 0
        keyboard.block_key("spacebar")
        while btn == 0:
            time.sleep(0.1)
            
            if keyboard.is_pressed("f1"):        
                pa.moveTo(600, 180)
            if keyboard.is_pressed("f2"):
                pa.moveTo(600, 220)
            if keyboard.is_pressed("f3"):
                pa.moveTo(600, 260)
            if keyboard.is_pressed("spacebar"):
                pa.leftClick()
                btn = 1
        keyboard.unblock_key("spacebar")
            
        
        