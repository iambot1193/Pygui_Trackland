import pyautogui as pa
import time
import keyboard
from playsound import playsound
import sonsperso
import pyperclip
import lembrete_Auto
import threading



#configs
pa.FAILSAFE = False
pa.PAUSE = 0.1
keyboard.block_key("f1")
keyboard.block_key("esc")
keyboard.block_key("f2")
keyboard.block_key("f3")
keyboard.block_key("f4")
keyboard.block_key("f6")
keyboard.block_key("f7")
#configs



                               #################funções##########################
def close_program():
        if keyboard.is_pressed('esc'):
            exit()
            
def find_color():
            mouse_x, mouse_y = pa.position()
            pixel_image = pa.screenshot(region=(mouse_x, mouse_y, 1, 1))
            pixel_color = pixel_image.getpixel((0, 0))
            return pixel_color

def check_loading():
        pa.moveTo(201, 94)################## MUDAR
        pa.moveTo(209, 113) ######### MUDAR
        currentColor = find_color()
        while(currentColor!=(51, 52, 62)): 
            close_program()

            time.sleep(0.1)
            currentColor = find_color() 
            
def mouse_info():
    time.sleep(0.01) 
    mouse_x, mouse_y = pa.position()
    pixel_image = pa.screenshot(region=(mouse_x, mouse_y, 1, 1))
    pixel_color = pixel_image.getpixel((0, 0))
    print(f"        Posição: ({mouse_x}, {mouse_y}) \n Cor: {pixel_color}")
    
def click():
    pa.leftClick()
    
def move(x ,y):
    pa.moveTo(x ,y)
    
def colar(texto):
    pyperclip.copy(texto)
    pa.hotkey("ctrl", "v")

def situ_substituir(numero):
    match numero:
        case 1: #S COMUNICAÇÃO
            colar("Sem comunicação.")
            for i in range (0, 4):
                pa.hotkey("tab")
            colar("Contatar cliente.")
            pa.hotkey("tab")
            colar("SEM COMUNICAÇÃO.")
            return
        case 2: #RESET
            colar("Veículo apresenta pequenos saltos e travamentos durante a rota.")
            for i in range (0, 4):
                pa.hotkey("tab")
            colar("Enviar reset.")
            pa.hotkey("tab")
            colar("PEQUENOS SALTOS E TRAVAMENTOS.")
            return
        case 3: #BUZZER VIOLADO
            colar("Veículo apresenta possível violação de buzzer, faz maior parte da rota sem identificação de motorista.")
            for i in range (0, 4):
                pa.hotkey("tab")
            colar("Agendar manutenção.")
            pa.hotkey("tab")
            colar("POSSÍVEL VIOLAÇÃO.")
            return
        case 4: #SALTOS
            colar("Veículo apresenta saltos e travamentos durante a rota.")
            for i in range (0, 4):
                pa.hotkey("tab")
            colar("Agendar manutenção.")
            pa.hotkey("tab")
            colar("SALTOS E TRAVAMENTOS.")
            return
        case 5: #IGNIÇÃO VIOLADA
            colar("Veículo apresenta sensor de ignição violado durante a rota.")
            for i in range (0, 4):
                pa.hotkey("tab")
            colar("Agendar manutenção.")
            pa.hotkey("tab")
            colar("POSSÍVEL VIOLAÇÃO.")
            return
        case 6: #MAL CONTATO BACKUP
            colar("Bateria backup apresenta mal contato durante a rota.")
            for i in range (0, 4):
                pa.hotkey("tab")
            colar("Agendar manutenção.")
            pa.hotkey("tab")
            colar("POSSÍVEL VIOLAÇÃO.")
            return
        case 7: #BACKUP NUNCA TEM CARGA
            colar("Bateria backup nunca tem carga, mesmo com ignição ligada.")
            for i in range (0, 4):
                pa.hotkey("tab")
            colar("Agendar manutenção.")
            pa.hotkey("tab")
            colar("POSSÍVEL VIOLAÇÃO.")
            return
        case 8: #S DADOS O SUFICIENTE
            colar("Veículo não apresentou dados o suficiente. Aguardar próxima análise.")
            for i in range (0, 4):
                pa.hotkey("tab")
            colar("Em observação.")
            pa.hotkey("tab")
            colar("")
            return
        case 9: #POSIÇÃO IG OFF
            colar("Veículo apresentou posição com a ignição desligada.")
            for i in range (0, 4):
                pa.hotkey("tab")
            colar("Agendar manutenção.")
            pa.hotkey("tab")
            colar("POSSÍVEL VIOLAÇÃO.")
            return
        case 10: #BATERIA VIOLADA PORTAL
            colar("Veículo apresentou violação de bateria indicado pelo portal SSX.")
            for i in range (0, 4):
                pa.hotkey("tab")
            colar("Agendar manutenção.")
            pa.hotkey("tab")
            colar("POSSÍVEL VIOLAÇÃO.")
            return
        case 11: #SALTOS IG OFF
            colar("Veículo apresentou saltos e travamentos com a ignição desligada durante a rota.")
            for i in range (0, 4):
                pa.hotkey("tab")
            colar("Agendar manutenção.")
            pa.hotkey("tab")
            colar("POSSÍVEL VIOLAÇÃO.")
            return
        case 12: #GPS TRAVADO
            colar("Veículo apresenta gps travado durante a rota.")
            for i in range (0, 4):
                pa.hotkey("tab")
            colar("Agendar manutenção.")
            pa.hotkey("tab")
            colar("GPS TRAVADO.")
            return
        case _:
            return
    



                               #################funções##########################
                               
while(True):
    time.sleep(0.1)
    close_program()
    
    if keyboard.is_pressed("f1"):
        mouse_info()
        time.sleep(0.3)
        
    if keyboard.is_pressed("f2"):
        
        sonsperso.tocar_som() #somrandom
        n1 = 1
        n2 = 1
        n3 = 1
        
        

        ##### variaveis padrão #########################
        number_vehicles = 10
        sheets_y = 270
        ssx_x = 95
        ##### variaveis padrão #############################
        
        if (n1):
            
            for numero in range (0, number_vehicles):
                close_program()

                move(ssx_x , 15)
                click()
                move(-1350, sheets_y) 
                click()
                pa.hotkey("ctrl", "c")
                check_loading()
                move(1212, 115)
                click()   
                
                #detecando abertura da pesquisa
                pa.moveTo(920, 147)
                current_color = find_color()
                contador = 0
                while current_color != (255, 182, 99):
                    time.sleep(0.1)
                    contador += 1
                    current_color = find_color()
                    if contador >= 5:
                        pa.moveTo(1212, 122)
                        pa.leftClick()
                        pa.moveTo(920, 147)
                        contador == 0
                #detectando abertura da pesquisa

                
                move(1135, 172)
                click()
                pa.hotkey("ctrl", "v")
                move(1324, 171)
                click()
                
                ########################## esperar carregmento
                move(965, 285)
                current_color = find_color()
                contador = 0
                while current_color != (255, 182, 99):

                    close_program()
                    
                    time.sleep(0.1)
                    current_color = find_color()
                    contador += 1
                    if contador >= 10:
                        move(1142, 174)
                        click()
                        pa.hotkey("ctrl", "a")
                        pa.hotkey("ctrl", "v")
                        move(1323, 172)
                        click()
                        move(965, 285)
                        current_color = find_color()
                        contador = 0
                        
                        
                ########verificar se tem mais de um rastreador
                
                move(980, 437)
                current_color = find_color()
                if current_color != (255, 255, 255):
                    btn = 0
                    while btn == 0:

                        close_program()
                        
                        playsound(r"C:\Users\jenni\Downloads\programs\Scripts\pygui_trackland\src\Track\Simples\sons\bonk_BEtiM8g.mp3")
                        time.sleep(0.3)
                        if keyboard.is_pressed("f1"):
                            btn = 1    
                            
                            
                else:
                    move(966, 285) 
                    click()   
                #################    ver0ificar se tem mais de um rastreador
                
                
                ### adicionando para ir para o proximo 
                sheets_y += 30
                ssx_x += 105
                numero +=1
            
        if (n2):     
                    
            ssx_x = 95
            
            for numero in range (0, number_vehicles):
                close_program()

                move(ssx_x, 20)
                click()
                check_loading()
                move(45, 548) 
                click()
                move(202, 232)
                click()
                
                ssx_x += 105
                numero +=1
        
        if (n3):    
                
            ssx_x = 95
            
            for numero in range (0, number_vehicles):
                close_program()

                move(ssx_x, 20)
                click()
                check_loading()
                move(575, 440)
                click()
                move(570, 473) 
                time.sleep(0.3)
                current_color = find_color()
                contador = 0
                btn = 0
                while current_color != (51, 52, 62) and btn == 0:
                    current_color = find_color()
                    close_program()
                    
                    if keyboard.is_pressed("f1"):
                        btn = 1
                    time.sleep(0.1)
                    current_color = find_color()
                    contador +=1
                    if contador >= 10:
                        contador = 0
                        move(575, 440)
                        click()
                        move(570, 473)
                move(237, 475) 
                if btn != 1:
                    pa.PAUSE = 0.05
                    for i in range (0 , 10):
                        close_program()

                        click()
                    pa.PAUSE = 0.1
                    time.sleep(0.2)
                    move(282, 550) 
                    pa.mouseDown()
                    move(2, 5530.3) 
                    pa.mouseUp()
                    move(570, 473) 
                    time.sleep(0.3)
                    click()
                
                ssx_x += 105
                numero +=1
            
            sonsperso.tocar_som()
            
            #playsound(r"C:\Users\jenni\Downloads\programs\SCIUTPS\Simples\sons\tafarco.mp3")
                
    if keyboard.is_pressed("f3"):
    
        pa.moveTo(269, 97)
        pa.click()
        pa.hotkey("left")
        pyperclip.copy("RELATÓRIO ")
        pa.hotkey("ctrl", "v")
        pa.hotkey("ctrl", "a")        
        pa.hotkey("right")
        for i in range (0, 5):
            pa.hotkey("left")
        pa.write(" 17-10-2025")
                    
    if keyboard.is_pressed("f4"):                
        threading.Thread(target= lembrete_Auto.executar, daemon=True).start()
        threading.Thread(target= close_program(), daemon=True).start()  
        
    if keyboard.is_pressed("f6"):
            pa.moveTo(-975, 160)
            pa.leftClick()
            pa.moveTo(-961, 341)
            pa.leftClick()
            
            pa.moveTo(-904, 164)
            pa.click()
            pa.hotkey("ctrl", "a")
            pa.write("12")
            pa.hotkey("enter")
            
            pa.leftClick()
            close_program()
            
            pa.moveTo(-609, 164)
            pa.leftClick()
            pa.moveTo(-579, 197)
            pa.leftClick()
            close_program()
            
            pa.moveTo(-577, 159)
            pa.leftClick()
            pa.moveTo(-543, 199)
            pa.leftClick()
            close_program()
            
            pa.moveTo(-534, 166)
            pa.leftClick()
            pa.moveTo(-505, 201)
            pa.leftClick()
            close_program()
            
            pa.moveTo(-845, 163)
            pa.leftClick()
            
            pa.moveTo(-688, 161)
            pa.leftClick()
            pa.moveTo(-524, 229)
            pa.leftClick()
            pa.moveTo(-498, 298)
            pa.leftClick()
            pa.moveTo(-675, 205)
            pa.leftClick()
            
        
    if keyboard.is_pressed("f7"):
        #40px de altura
        coodernada_situ = (-984, 313)
        pa.moveTo(coodernada_situ)
        pa.click()
        situ = 1
        while  1<= situ <= 12:  
            pa.hotkey("ctrl", "c")
            situ = int(pyperclip.paste())
            situ_substituir(situ)
            for i in range (0,5):
                pa.hotkey("left")
            pa.hotkey("down")
        
     
            

