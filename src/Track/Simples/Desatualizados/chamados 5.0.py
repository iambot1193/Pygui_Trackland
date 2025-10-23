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
        close_progam()
        print("f2")
        
        pa.moveTo(1071, 118) # chamados, laranja
        call = findcolor()
        while call == (217, 123, 76):
            close_progam()
            
            time.sleep(0.1)
            pa.leftClick()
            pa.moveTo(837, 227) #verificando se chamados foi aberto
            time_try = 0
            checkload = findcolor()
            while checkload != (51, 51, 51):
                close_progam()
                
                time.sleep(0.1)
                checkload = findcolor()
                time_try +=1
                if time_try >= 20:
                    pa.moveTo(1071, 118) # re abrindo chamados
                    pa.leftClick()
                    pa.moveTo(837, 227)
                    time_try = 0
                checkload = findcolor()
                
            pa.moveTo(880, 230) #chamado 1
            pa.leftClick()
            pa.moveTo(880, 270) #chamado 2
            pa.leftClick()
            pa.moveTo(880, 310) #chamado 3
            pa.leftClick()
            pa.moveTo(880, 350) #chamado 3
            pa.leftClick()
            
            pa.moveTo(837, 227) #verificando se chamados está aberto
            checkload = findcolor()
            while checkload == (51, 51, 51):
                close_progam()
                
                time.sleep(0.1)
                checkload = findcolor()
                
                
            pa.moveTo(1071, 118)
        
        