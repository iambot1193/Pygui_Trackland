import pyautogui as pa
import time
import keyboard
pa.FAILSAFE = False

keyboard.block_key('f2')
keyboard.block_key('f3')

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
     

while(1):
    if keyboard.is_pressed('f2'):
        print("f2")

        inicial_x = -1330
        inicial_y = 270
        aba_x = 75
        number_vehicles = 1
        

        pa.moveTo(90, 20)
        pa.leftClick()


        for i in range (0, number_vehicles): 
            close_program()#psedo threanding de fechamento
            check_loading()#pseudo threanding de check
            
            #copiando da planilha
            pa.moveTo(-1330, inicial_y)
            pa.leftClick()
            pa.hotkey('ctrl', 'c')
            pa.moveTo(1211, 118)
            pa.leftClick()
            pa.moveTo(1238, 173)
            pa.leftClick()
            pa.hotkey('ctrl', 'v')
            pa.moveTo(1325, 170)
            pa.leftClick()
            #copiado da planilha

            #pesquisando o veículo
            pa.moveTo(964, 287)
            currentColor = find_color()
            waiting = 1
            next = 0
            while currentColor!=(255,182,99):
                close_program()
                time.sleep(0.1)
                currentColor = find_color()
                waiting +=1
                if waiting>=10 :
                    pa.moveTo(1010, 174)
                    pa.leftClick()
                    pa.hotkey('ctrl', 'a')
                    pa.hotkey('ctrl', 'v')
                    pa.moveTo(1325, 170)
                    pa.leftClick()
                    pa.moveTo(964, 287)
                    waiting = 0 
                    break
            pa.leftClick()
            pa.leftClick()
            #pesquisando o veículo
            

            #indo pra próxima guia
            aba_x += 113
            inicial_y += 32
            pa.moveTo(aba_x, 20)
            pa.leftClick()
            check_loading()
            #indo pra próxima guia
        #FIM LOOP 1    


            #resetando variaveis para abrir histórico
        inicial_x = -1330
        inicial_y = 270
        aba_x = 90
        pa.moveTo(aba_x, 20)
        pa.leftClick()

            #abrindo histórico
        for i in range (0, number_vehicles):
            close_program()
            check_loading()

            pa.moveTo(48, 552)
            pa.leftClick()
            pa.moveTo(195, 233)
            pa.leftClick()

            aba_x += 113
            inicial_y += 32
            pa.moveTo(aba_x, 20)
            pa.leftClick()
            check_loading()
            #abrindo histórico
        #FECHANDO LOOP 2


                #resetando variaveis para aumentar amostragem
        inicial_x = -1330
        inicial_y = 270
        aba_x = 90
        pa.moveTo(aba_x, 20)
        pa.leftClick()

            #expandindo amostragem
        for i in range (0, number_vehicles):
            close_program()
            check_loading()

            
            pa.moveTo(573, 445)
            pa.leftClick()
            time.sleep(0.5)
            pa.moveTo(240, 488)
            for click in range (0, 6):
                pa.leftClick()
            time.sleep(0.1)
            pa.moveTo(281, 555)
            pa.mouseDown()
            pa.moveTo(20, 555, 0.2)
            pa.mouseUp()

            pa.moveTo(569, 488, 0.1)
            pa.leftClick()
            time.sleep(0.4)
            
            
            aba_x += 113
            inicial_y += 32
            pa.moveTo(aba_x, 20)
            pa.leftClick()
            time.sleep(0.3)
                #expandindo amostragem    