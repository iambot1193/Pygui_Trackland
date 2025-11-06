import pyautogui as pa
from screeninfo import get_monitors
import keyboard
import time
#pa.useImageNotFoundException(False) usavel em casos que eu nao queira retonar imagemNotFoundExceptione e queira 
#retornar none no lugar     
pa.FAILSAFE = False
MONITOR = [1, 2]
keyboard.block_key("f2")
keyboard.block_key("esc")


def close_program():
    if keyboard.is_pressed("esc"):
        exit(1) 
    
def check_loading(reference_point):
    try:
        check = pa.locateCenterOnScreen(reference_point, confidence=0.7, grayscale=True)
    except pa.ImageNotFoundException:
        check = None
        
    while check is None:
        try:
            time.sleep(0.2)
            close_program()
            check = pa.locateCenterOnScreen(reference_point, confidence=0.7, grayscale=True)
        except pa.ImageNotFoundException:
            check = None
            
    return check

def page_ready(reference_point):
    try:
        check = pa.locateCenterOnScreen(reference_point, confidence=0.7, grayscale=True, )
    except pa.ImageNotFoundException:
        check = None
        
    while check is None:
        try:
            time.sleep(0.2)
            close_program()
            check = pa.locateCenterOnScreen(reference_point, confidence=0.7, grayscale=True)
        except pa.ImageNotFoundException:
            check = None
            
    return check

def click_image(reference):
    pa.click(pa.locateCenterOnScreen(reference, confidence=0.7, grayscale=True))


        

while(1):
    time.sleep(0.1)
    
    
    if keyboard.is_pressed("f2"):
        close_program()
        page_ready = r"C:\Users\jenni\Downloads\programs\Scripts\pygui_trackland\src\Track\Projeto_SSX\Nocord\assets\settings.png"
        page_ready2 = r"C:\Users\jenni\Downloads\programs\Scripts\pygui_trackland\src\Track\Projeto_SSX\Nocord\assets\settings.png"
        ssx = r"C:\Users\jenni\Downloads\programs\Scripts\pygui_trackland\src\Track\Projeto_SSX\Nocord\assets\ssx.png"
        ssx_pos = pa.locateCenterOnScreen(ssx, confidence= 0.7, grayscale=True)
        x, y = ssx_pos
        ssx_pos = x +50, y
                    
        n1 = 0
        n2 = 0
        n3 = 1
        veiculos = 9
        
        
        
        
        # if n1:
        #     placa = r"C:\Users\jenni\Downloads\programs\Scripts\pygui_trackland\src\Track\Projeto_SSX\Nocord\assets\placa.png"
        #     search = r"C:\Users\jenni\Downloads\programs\Scripts\pygui_trackland\src\Track\Projeto_SSX\Nocord\assets\search.png" 
        
        #     placa = pa.locateCenterOnScreen(placa, confidence=0.7, grayscale=True)
        #     placa_y = (placa.y+20)
        #     ssx = pa.locateCenterOnScreen(ssx, confidence=0.7, grayscale=True)
        #     pa.click(ssx)
        #     print("clickssx")
        #     pa.moveTo(placa.x ,placa_y)
        #     pa.click()
        #     print("clickplanilha")
        #     pa.hotkey("ctrl", "c")
        #     check_loading(page_ready)
        #     pa.click(search)
        #     print("clickssx")
        
        if n2:   
            open_hist1png = r"C:\Users\jenni\Downloads\programs\Scripts\pygui_trackland\src\Track\Projeto_SSX\Nocord\assets\openhistory1.png"
            open_hist2png = r"C:\Users\jenni\Downloads\programs\Scripts\pygui_trackland\src\Track\Projeto_SSX\Nocord\assets\openhistory2.png"    
            
            pa.click(ssx_pos)
            contador_veiculos = 0
            
            while contador_veiculos <= veiculos:
                close_program()
                
                pa.click(ssx_pos)
                check_loading(page_ready)
                
                
                check_loading(open_hist1png)
                hist1 = pa.locateCenterOnScreen(open_hist1png, confidence=0.7, grayscale=True)
                pa.click(hist1.x+12, hist1.y)
                check_loading(open_hist2png)
                click_image(open_hist2png)
                
                ssx_pos = (ssx_pos[0] + 110, y)
                contador_veiculos += 1
        
        if n3:
            filter = r"C:\Users\jenni\Downloads\programs\Scripts\pygui_trackland\src\Track\Projeto_SSX\Nocord\assets\filter.png"
            minus = r"C:\Users\jenni\Downloads\programs\Scripts\pygui_trackland\src\Track\Projeto_SSX\Nocord\assets\minus.png"
            
            pa.click(ssx_pos)
            check_loading(page_ready)
            
            check_loading(filter)
            click_image(filter)
            time.sleep(0.5)
            click_image(minus)
            pa.click(clicks=9)#valor -1 por conta do click image
            
            
            
            
            
            
            
            