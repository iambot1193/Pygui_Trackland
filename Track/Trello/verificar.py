import pyautogui as pa
import time
import keyboard
pa.FAILSAFE = False

keyboard.block_key('f2')
keyboard.block_key('f1')

def close_program():
        if keyboard.is_pressed('esc'):
            exit()

def find_color():
            mouse_x, mouse_y = pa.position()
            pixel_image = pa.screenshot(region=(mouse_x, mouse_y, 1, 1))
            pixel_color = pixel_image.getpixel((0, 0))
            return pixel_color
        
planilha_y = 265 #+32
while(1):
    time.sleep(1)
    if keyboard.is_pressed('f2'):
        print("f2")
        
        pa.moveTo(-1350, planilha_y)
        pa.leftClick()
        pa.hotkey("ctrl","c")
        pa.moveTo(620, 111)
        pa.leftClick()
        btn = 0
        while btn == 0:
            time.sleep(0.1)
            
    