import pyautogui as pa
import time
import keyboard
pa.FAILSAFE = False

while(1):
    if keyboard.is_pressed('f2'):
        print("f2")
        inicialc = 240
        inicialv = -300

        def findcolor():
            mouse_x, mouse_y = pa.position()
            pixel_image = pa.screenshot(region=(mouse_x, mouse_y, 1, 1))
            pixel_color = pixel_image.getpixel((0, 0))
            return pixel_color
        


        for i in range (0, 1): 
            pa.moveTo(75, inicialc, duration=0.2)
            pa.leftClick()
            pa.hotkey('ctrl', 'c')
            time.sleep(0.3)
            pa.moveTo(inicialv, -180, duration=0.2)
            pa.leftClick()
            pa.moveTo(-150, -80, duration=0.2)
            pa.leftClick()
            pa.moveTo(-200, -30, duration=0.2)
            pa.leftClick()
            pa.hotkey('ctrl', 'v')
            pa.moveTo(-45, -30, duration=0.2)
            pa.leftClick()
            pa.moveTo(-400, 83, duration=0.2)
            #ocr ou na mudança de cor
            currentcolor = findcolor()
            samecolor = 1
            while samecolor :
                time.sleep(0.3)
                if currentcolor == (255, 255, 255):
                    samecolor = 1
                else: 
                    print("cor preta")
                    samecolor = 0
            time.sleep(0.1)
            pa.leftClick()
            inicialc+=26
            inicialv-=120
            


    if keyboard.is_pressed('f4'):
        break;        

            
                    #pa.moveTo(-1390, 415, duration=0.5)
            #pa.leftClick()        
            #pa.moveTo(-1317, 170, duration=0.2)
            #pa.leftClick()