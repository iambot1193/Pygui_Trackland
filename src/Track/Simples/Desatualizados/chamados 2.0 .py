import pyautogui as pa
import time
import keyboard
pa.FAILSAFE = False

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
        print("f2")
        close_progam()


        inicial_y = 220
        abax = 150
        wait=0

        
        for index in range(0, 200):
            close_progam()
            pa.moveTo(1060, 120)
            pa.leftClick()
            pa.moveTo(877, 228)

            
            currentColor = findcolor()
            while currentColor!=(77, 77, 77):
                close_progam()
                currentColor = findcolor()
                time.sleep(0.05)
                currentColor = findcolor()
                if currentColor == (77, 77, 77): break
                wait+=1
                if wait>=(10):
                    pa.moveTo(1060, 120)
                    pa.leftClick()
                    pa.moveTo(877, 228)
                    wait = 0
                currentColor = findcolor()
                
            for i in range (0, 2): 
                close_progam()
                pa.moveTo(880, inicial_y)
                pa.leftClick()
                inicial_y+=45
                
            
            inicial_y = 220
            time.sleep(1)
