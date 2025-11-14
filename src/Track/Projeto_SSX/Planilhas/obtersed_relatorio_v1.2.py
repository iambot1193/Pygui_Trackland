import pandas as pd
import os
import pyautogui as pa
import keyboard
import time
import pyperclip as clip
from datetime import datetime

Pasta_fonte = r"C:\Users\jenni\Downloads\SEDOBTER"

keyboard.block_key("f2")
keyboard.block_key("esc")

def close_program():
        if keyboard.is_pressed('esc'):
            exit()

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 0)  # deixa quebrar linha conforme terminal


COLS = ["Placa", "Unidade organizacional cliente", "Rastreador"]

dfs = []
for arquivo in os.listdir(Pasta_fonte):
    
    #ignorar os que nao sao excel     (mudar extenão dos arquivos caso não encontrar nada)
    if not arquivo.lower().endswith(("xlsx", "xls")):
        continue
    #configurando o caminho para cada arquivos excel que ele identificar
    caminho = os.path.join(Pasta_fonte, arquivo)
    ####################################################################
    unidade = 3
    ###################################################################
    match unidade: 
        case 1: 
            unidade = "SED"
        case 2: 
            unidade = "AGEMS"
        case 3: 
            unidade = "FUNDEPAR"
        case _:
            pass
            #olho magico e sanesul não precisam do complemento
    
    
    
    #separador
    print(f"----------{arquivo}----------")
    df = pd.read_excel(caminho, usecols=COLS, dtype={"Rastreador": str})#lendo e forçando str no rastrador
    df["Unidade organizacional cliente"] = (f"{unidade} " + df["Unidade organizacional cliente"].str.strip())
    print(df[COLS].to_csv(sep=";", index=False, header=False), end="")#configurando separador
        
while 1: 
    time.sleep(0.1)
    close_program()
        
    if keyboard.is_pressed("f2"):
        close_program()
        pa.moveTo(-1171, 100)
        pa.leftClick()
        pa.hotkey("left")
        clip.copy("RELATÓRIO ")
        pa.hotkey("ctrl", "v")
        pa.hotkey("ctrl", "a")
        pa.hotkey("right")
        for i in range (0, 5):
            close_program()
            pa.hotkey("left")
        data_atual = datetime.now().strftime("%d-%m-%Y")
        clip.copy(f" ({data_atual}) ")
        pa.hotkey("ctrl", "v")
        time.sleep(0.2)


    

