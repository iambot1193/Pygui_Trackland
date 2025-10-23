import pyautogui as pa
import keyboard
import time 

pa.FAILSAFE = False
keyboard.block_key("f1")
keyboard.block_key("f2")
keyboard.block_key("f3")
keyboard.block_key("f4")
keyboard.block_key("f6")

def close_program():
        if keyboard.is_pressed('esc'):
            exit()

def find_color():
            mouse_x, mouse_y = pa.position()
            pixel_image = pa.screenshot(region=(mouse_x, mouse_y, 1, 1))
            pixel_color = pixel_image.getpixel((0, 0))
            return pixel_color
        
def copiar():
    pa.hotkey('ctrl', 'c')

def colar():
    pa.hotkey('ctrl','v')
    
def mover(x, y):
    pa.moveTo(x, y)
    
def click_esquerdo():
    pa.leftClick()
        
y_planilha_inicial = 270
        
for i in range (0, 10):
    while(1):
        time.sleep(0.5)
        
        if keyboard.is_pressed('f6'):
            print("f6")
            
            mover(-1300, 20)
            click_esquerdo()    
            mover(-1350, y_planilha_inicial) # somar +30 para a proxima placa
            click_esquerdo()
            copiar()
        
            mover(-1050, 15)
            click_esquerdo()
            mover(-780, 110)
            click_esquerdo()
            colar()

            btn_click = 0
            
            while btn_click == 0:
                time.sleep(0.5)
                
                if keyboard.is_pressed('f1'):
                    mover(-800, 180)    #somar 40    
                    click_esquerdo() 
                    btn_click = 1
                if keyboard.is_pressed('f2'):
                    mover(-800, 220)    #somar 40
                    click_esquerdo()
                    btn_click = 1  
                if keyboard.is_pressed('f3'):
                    mover(-800, 260)    #somar 40
                    click_esquerdo()
                    btn_click = 1  
                if keyboard.is_pressed('f4'):
                    mover(-800, 300)    #somar 40
                    click_esquerdo()
                    btn_click = 1          

            btn_click = 0
            while btn_click == 0:
                time.sleep(0.5)
                
                if keyboard.is_pressed('f1'):
                    btn_click = 1  
                    
                    mover(-1300, 20)
                    click_esquerdo()   
                    mover(-300, y_planilha_inicial) 
                    click_esquerdo()
                    copiar()
                    mover(-1050, 20) 
                    click_esquerdo()
                    mover(-475, 325) 
                    click_esquerdo()
                    mover(-220, 390) 
                    click_esquerdo()
                    colar()
                    pa.hotkey(' ')
                    
                    mover(-1300, 20)
                    click_esquerdo()
                    mover(-900, y_planilha_inicial) 
                    click_esquerdo()
                    copiar()
                    mover(-1050, 20) 
                    click_esquerdo()
                    mover(-220, 390) 
                    click_esquerdo()
                    colar()
                    pa.hotkey(' ')
                    
                    mover(-1300, 20)
                    click_esquerdo()
                    mover(-445, y_planilha_inicial) 
                    click_esquerdo()
                    copiar()
                    mover(-1050, 20) 
                    click_esquerdo()
                    mover(-220, 390) 
                    click_esquerdo()
                    colar()
                    pa.hotkey(' ')
                    
                    mover(-250, 160) 
                    click_esquerdo()
                    mover(-250, 160) 
                    pa.leftClick(-200, 215)
                    y_planilha_inicial += 30
                    i+=1
                    