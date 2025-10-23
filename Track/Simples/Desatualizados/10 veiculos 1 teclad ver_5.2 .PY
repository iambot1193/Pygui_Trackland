import pyautogui as pa
import time
import keyboard
from playsound import playsound
#configs
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
        pa.moveTo(203, 101)
        pa.moveTo(206, 99)
        currentColor = find_color()
        while(currentColor!=(51, 52, 62)):
            time.sleep(0.1)
            currentColor = find_color() 
            
def mouse_info():
    time.sleep(0.1) 
    mouse_x, mouse_y = pa.position()
    pixel_image = pa.screenshot(region=(mouse_x, mouse_y, 1, 1))
    pixel_color = pixel_image.getpixel((0, 0))
    print(f"Posição: ({mouse_x}, {mouse_y})  |||  Cor: {pixel_color}")
    
def ck():
    pa.leftClick()
    
     

while(1):
    time.sleep(0.1)
    close_program()
    
    if keyboard.is_pressed("f1"):
        mouse_info() #mostra informações sobre a posição do mouse e etc.
    
    if keyboard.is_pressed('f2'):
        print("f2")

        inicial_y = 270 #pla nilha soma 1-2 + 2-3 / 2 = y 
        aba_x = 75 #aba ssx soma, 1-2 + 2-3 / 2 = x
        number_vehicles = 1 #soma veiculos
        

        pa.moveTo(90, 20) #primeira aba ssx
        ck()


        for i in range (0, number_vehicles): 
            close_program()#psedo threanding de fechamento
            check_loading()#pseudo threanding de check
            
            #copiando da planilha
            pa.moveTo(-1330, inicial_y) #coodernada fixa da linha das placas + altura das planilhas média
            ck()
            pa.hotkey('ctrl', 'c')
            pa.moveTo(1211, 118) # botao de busca1
            ck()
            pa.moveTo(1238, 173) #botao de busca1
            ck()
            pa.hotkey('ctrl', 'v')
            pa.moveTo(1325, 170) #clica no botao da pesqisa 2 
            ck()
            #copiado da planilha

            #pesquisando o veículo
            pa.moveTo(964, 287)
            currentColor = find_color()
            waiting = 1
            btn = 0
            while currentColor!=(255,182,99): #espera um veículo aparecer disponível para a busca
                close_program()
                time.sleep(0.1)
                currentColor = find_color()
                waiting +=1
                if waiting>=10 : #se (tempo passar) então procurar de novo
                    close_program()
                    pa.moveTo(1010, 174)
                    ck()
                    pa.hotkey('ctrl', 'a')
                    pa.hotkey('ctrl', 'v')
                    pa.moveTo(1325, 170)
                    ck()
                    pa.moveTo(964, 287)
                    waiting = 1        
            pa.moveTo(965, 286)
            currentColor = find_color() 
            while currentColor != (255, 182, 99):
                time.sleep(0.01)
                currentColor = find_color()
                pa.moveTo(965, 590, 0.5)
            pa.moveTo(980, 440)
            currentColor = find_color()
            if currentColor != (255, 255,255): # se (tem mais de um veículo) tocar som
                for i in range (0, 2):
                    playsound(r"C:\Users\jenni\Downloads\programs\SCIUTPS\Simples\not.mp3")
                btn = 0
                while btn == 0:
                    if keyboard.is_pressed("f1"): #esperar pelo usuario clicar f1 para continuar o script
                        btn = 1 
            else:
                pa.moveTo(965, 286)
                ck() 
                # se não achar uma segunda placa, então buscar pela primeira.

            #indo pra próxima guia
            aba_x += 113
            inicial_y += 32
            pa.moveTo(aba_x, 20)
            ck()
            check_loading()
            #indo pra próxima guia
        #FIM LOOP 1     ###############################################################################


        #resetando variaveis para abrir histórico
        inicial_y = 270
        aba_x = 90
        pa.moveTo(aba_x, 20)
        ck()

    #abrindo histórico
        for i in range (0, number_vehicles):
            close_program()
            check_loading()

            pa.moveTo(48, 552)
            ck()
            pa.moveTo(195, 233)
            ck()

            aba_x += 113
            inicial_y += 32
            pa.moveTo(aba_x, 20)
            ck()
            check_loading()
            close_program()
    #abrindo histórico
    
        #FECHANDO LOOP 2 ####################################################################
        
        
        #resetando variaveis para aumentar amostragem das datas
        inicial_x = -1330
        inicial_y = 270
        aba_x = 90
        pa.moveTo(aba_x, 20)
        ck()

            #expandindo amostragem
        for i in range (0, number_vehicles):
            close_program()
            check_loading()

            
            pa.moveTo(573, 445)
            ck()
            pa.moveTo(574, 474)
            currentColor = find_color()
            contador = 0
            while currentColor!= (51,52,62):
                contador +=1
                if contador >= 30:
                    playsound(r"C:\Users\jenni\Downloads\programs\SCIUTPS\Simples\not.mp3")
                    contador = 0
                if keyboard.is_pressed('f1'):
                    break
                currentColor = find_color()
                time.sleep(0.01)
                close_program()
                
            pa.moveTo(240, 488)
            for click in range (0, 9):
                ck()
            time.sleep(0.3)
            pa.moveTo(281, 555)
            pa.mouseDown()
            pa.moveTo(20, 555, 0.1)
            pa.mouseUp()
            close_program()

            pa.moveTo(569, 488, 0.1)
            ck()
            time.sleep(0.4)
            close_program()
            
            
            aba_x += 113
            inicial_y += 32
            pa.moveTo(aba_x, 20)
            ck()
            time.sleep(0.3)
                #expandindo amostragem   
                
    #tocar som para notificar o fim da pesquisa 
        for i in range (0, 2):
            playsound(r"C:\Users\jenni\Downloads\programs\SCIUTPS\Simples\not.mp3")