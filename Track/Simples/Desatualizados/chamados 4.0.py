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
        repeat = 500
        
        
        for repeat in range (0, repeat):
            close_progam()
            
            var_y = 224
                
            pa.moveTo(1059, 117)
            pa.leftClick()
            
            vartime = 0
            pa.moveTo(838, 224)
            currentcolor = findcolor()
            close_progam()
            while currentcolor!= (51,51,51):
                close_progam()
                time.sleep(0.05)
                currentcolor = findcolor()
                vartime += 1
                
                if (vartime>=10):
                    close_progam()
                    pa.moveTo(1059, 117)
                    pa.leftClick()
                    pa.moveTo(838, 224)
                    vartime = 0
                    currentcolor = findcolor()
                    close_progam()
                
            for i in range (0, 2):
                close_progam()
                print("click")
                pa.moveTo(881, var_y)
                pa.leftClick()
                var_y += 45
            time.sleep(0.2)
            close_progam()