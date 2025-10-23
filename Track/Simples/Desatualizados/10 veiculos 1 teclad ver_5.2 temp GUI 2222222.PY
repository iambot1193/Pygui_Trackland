import pyautogui as pa
import time
import keyboard
from playsound import playsound
pa.FAILSAFE = False
pa.PAUSE = 0.1

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
        pa.moveTo(214, 131)
        pa.moveTo(233, 149)
        currentColor = find_color()
        while(currentColor!=(51, 52, 62)):
            time.sleep(0.2)
            currentColor = find_color() 
            
def mouse_info():
    time.sleep(0.1) 
    mouse_x, mouse_y = pa.position()
    pixel_image = pa.screenshot(region=(mouse_x, mouse_y, 1, 1))
    pixel_color = pixel_image.getpixel((0, 0))
    print(f"Posição: ({mouse_x}, {mouse_y})  |||  Cor: {pixel_color}")
    
     

while(1):
    time.sleep(0.1)
    close_program()
    
    if keyboard.is_pressed("f1"):
        mouse_info() #mostra informações sobre a posição do mouse e etc.
    
    if keyboard.is_pressed('f2'):
        print("f2")

        inicial_y = 335 #ok
        aba_x = 75
        number_vehicles = 5
        

        pa.moveTo(163, 19)
        pa.leftClick()


        for i in range (0, number_vehicles): 
            close_program()#psedo threanding de fechamento
            check_loading()#pseudo threanding de check
            
            #copiando da planilha
            pa.moveTo(-1157, inicial_y)
            pa.leftClick()
            pa.hotkey('ctrl', 'c')
            pa.moveTo(1191, 162)
            pa.leftClick()
            time.sleep(0.2)
            pa.moveTo(1061, 245)
            currentColor = find_color()
            contador = 0
            while currentColor != (255, 182, 99):
                close_program()
                currentColor = find_color()
                contador += 0.1
                if contador >= 2:
                    contador = 0
                    pa.moveTo(1191, 162)
                    pa.leftClick()
                    pa.moveTo(1061, 245)
                    currentColor = find_color()
            pa.moveTo(1118, 216)
            pa.leftClick()
            pa.hotkey('ctrl', 'v')
            pa.moveTo(1318, 214)
            pa.leftClick()
            #copiado da planilha

            #pesquisando o veículo
            pa.moveTo(921, 342)
            currentColor = find_color()
            waiting = 1
            btn = 0
            while currentColor!=(255,182,99): #espera um veículo aparecer disponível para a busca
                close_program()
                time.sleep(0.2)
                currentColor = find_color()
                waiting +=1
                if waiting>=10 : #se (tempo passar) então procurar de novo
                    close_program()
                    pa.moveTo(1130, 214)
                    pa.leftClick()
                    pa.hotkey('ctrl', 'a')
                    pa.hotkey('ctrl', 'v')
                    pa.moveTo(1311, 207)
                    pa.leftClick()
                    pa.moveTo(921, 342)
                    waiting = 1            
            #tratando 2 rastreadores ou mais    
            pa.moveTo(934, 504)
            currentColor = find_color()
            if currentColor != (255, 255,255): # se (tem mais de um veículo) tocar som
                for i in range (0, 2):
                    playsound(r"C:\Users\fetec\Downloads\SCRIPTS\not.mp3")
                    time.sleep(0.3)
                btn = 0
                while btn == 0:
                    if keyboard.is_pressed("f1"): #esperar pelo usuario clicar f1 para continuar o script
                        btn = 1 
            else:
                pa.moveTo(920, 340)
                pa.leftClick() 
                # se não achar uma segunda placa, então buscar pela primeira.

            #indo pra próxima guia
        
            aba_x += 220
            inicial_y += 30
            pa.moveTo(aba_x, 20)
            pa.leftClick()
            check_loading()
            #indo pra próxima guia
        #FIM LOOP 1    


        #resetando variaveis para abrir histórico  
        inicial_y = 270
        aba_x = 75
        pa.moveTo(aba_x, 20)
        pa.leftClick()

    #abrindo histórico
        for i in range (0, number_vehicles):    
                close_program()
                check_loading()

                pa.moveTo(51, 585)
                pa.leftClick()
                time.sleep(0.1)
                pa.moveTo(183, 174)
                pa.leftClick()

                aba_x += 220
                inicial_y += 40
                pa.moveTo(aba_x, 20)
                pa.leftClick()
                check_loading()
                close_program()
        #abrindo histórico
    
        #FECHANDO LOOP 2
        #resetando variaveis para aumentar amostragem das datas
        
        inicial_y = 270
        aba_x = 75
        pa.moveTo(aba_x, 20)
        pa.leftClick()

            #expandindo amostragem
        for i in range (0, number_vehicles):
            close_program()
            check_loading()

            
            pa.moveTo(642, 464)
            pa.leftClick()
            pa.moveTo(630, 504)
            currentColor = find_color()
            contador = 0
            while currentColor!= (51,52,62):
                contador +=1
                if contador >= 15:
                    playsound(r"C:\Users\fetec\Downloads\SCRIPTS\not.mp3")
                    contador = 0
                if keyboard.is_pressed('f1'):
                    break
                currentColor = find_color()
                time.sleep(0.01)
                close_program()
            time.sleep(0.3)
                
            pa.moveTo(264, 506)
            for i in range (0, 14):
                pa.leftClick()
            time.sleep(0.3)
            pa.moveTo(323, 587)
            pa.mouseDown()
            pa.moveTo(16, 587, 0.2)
            pa.mouseUp()
            close_program()

            pa.moveTo(633, 500, 0.1)
            pa.leftClick()
            time.sleep(0.4)
            close_program()
        
            aba_x += 220
            inicial_y += 40
            pa.moveTo(aba_x, 20)
            pa.leftClick()
            check_loading()
                #expandindo amostragem   
                
    #tocar som para notificar o fim da pesquisa 
        for i in range (0, 2):
            playsound(r"C:\Users\fetec\Downloads\SCRIPTS\not.mp3")