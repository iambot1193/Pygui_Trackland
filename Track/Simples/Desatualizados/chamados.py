import pyautogui as pa
import time
import keyboard
pa.FAILSAFE = False

while(1):
    if keyboard.is_pressed('f2'):
        print("f2")
        if keyboard.is_pressed('esc'):
                break


        inicialx = 880
        inicialy = 220
        abax = 150

        def findcolor():
            mouse_x, mouse_y = pa.position()
            pixel_image = pa.screenshot(region=(mouse_x, mouse_y, 1, 1))
            pixel_color = pixel_image.getpixel((0, 0))
            return pixel_color

        for index in range(0, 20):
            pa.moveTo(1060, 120)
            pa.leftClick()
            pa.moveTo(1060, 140)
            if keyboard.is_pressed('esc'):
                break


            currentColor = findcolor()
            while currentColor==(251, 106, 106):
                pa.moveTo(1060, 120)
                pa.leftClick()
                pa.moveTo(1060, 140)
                time.sleep(1.5)
                currentColor = findcolor()
            inicialy = 220

            for i in range (0, 3): 
                    
                pa.moveTo(inicialx, inicialy)
                pa.leftClick()
                inicialy+=45
            time.sleep(1)
