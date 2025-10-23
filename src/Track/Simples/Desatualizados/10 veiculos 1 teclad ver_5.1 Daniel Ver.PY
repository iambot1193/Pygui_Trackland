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

def check_loading():
        pa.moveTo(203, 101)
        pa.moveTo(206, 99)
        currentColor = find_color()
        while(currentColor!=(51, 52, 62)):
            time.sleep(0.1)
            currentColor = find_color() 

def moverpara(x ,y):
    pa.moveTo(x ,y)

def clicar():
    pa.leftClick()
    
def esperar(tempo):
    time.sleep(tempo)
    
def copiar():
    pa.hotkey('ctrl', 'c')

def colar():
    pa.hotkey('ctrl', 'v')
     

while(1):
    esperar(0.1)
    
    if keyboard.is_pressed('f1'):
        time.sleep(0.1) 
        mouse_x, mouse_y = pa.position()
        print(f"Posição: ({mouse_x}, {mouse_y})")
        

    
    if keyboard.is_pressed('f2'):
        print("f2")
        
        y_incial = 100
        
        
        for repetisão in range (0, 10):
            
            moverpara(674, y_incial)
            
            y_incial+=70
        
        





