import pyautogui as pa
import time
import keyboard
pa.FAILSAFE = False

while(1):
    if keyboard.is_pressed('f2'):
        print("f2")

        inicialx = -1330
        inicialy = 270
        abax = 150

        def findcolor():
            mouse_x, mouse_y = pa.position()
            pixel_image = pa.screenshot(region=(mouse_x, mouse_y, 1, 1))
            pixel_color = pixel_image.getpixel((0, 0))
            return pixel_color


        for i in range (0, 4): 
            

            pa.moveTo(-1330, inicialy, duration=0.1)
            pa.leftClick()
            pa.hotkey('ctrl', 'c')
            pa.moveTo(1211, 118)
            pa.leftClick()
            time.sleep(0.4)
            pa.hotkey('ctrl', 'v')
            pa.moveTo(1325, 170)
            pa.leftClick()

            pa.moveTo(964, 287)
            currentColor = findcolor()
            while currentColor!=(255,182,99):
                time.sleep(0.1)
                currentColor = findcolor()
            pa.leftClick()

            
            abax += 225
            inicialy += 35
            pa.moveTo(abax, 20)
            pa.leftClick()


        
        pa.moveTo(-1330, inicialy, duration=0.1)
        pa.leftClick()
        pa.hotkey('ctrl', 'c')
        pa.moveTo(1211, 118)
        pa.leftClick()
        time.sleep(0.4)
        pa.hotkey('ctrl', 'v')
        pa.moveTo(1325, 170)
        pa.leftClick()

        pa.moveTo(964, 287)
        currentColor = findcolor()
        while currentColor!=(255,182,99):
            time.sleep(0.1)
            currentColor = findcolor()
        pa.leftClick()



