import pandas as pd
import os
import pyautogui as pa
import keyboard
import time
import pyperclip as clip

Pasta_fonte = r"C:\Users\jenni\Downloads\SEDOBTER"

keyboard.block_key("f2")
keyboard.block_key("esc")
keyboard.block_key("f3")

def close_program():
        if keyboard.is_pressed('esc'):
            exit()

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 0)  # deixa quebrar linha conforme terminal


COLS = ["Placa", "Unidade organizacional cliente", "Rastreador"]

dfs = []
for arquivo in os.listdir(Pasta_fonte):
    caminho = os.path.join(Pasta_fonte, arquivo)
    print(f"----------{arquivo}----------")
    df = pd.read_excel(caminho, usecols=COLS)
    df["Unidade organizacional cliente"] = ("SED " + df["Unidade organizacional cliente"].astype(str).str.strip())
    print(df[COLS].to_csv(sep=";", index=False, header=False), end="")
    
while 1:
    time.sleep(1)
    close_program()
    if keyboard.is_pressed("f2"):
        pa.moveTo(-975, 160)
        pa.leftClick()
        pa.moveTo(-961, 341)
        pa.leftClick()
        pa.moveTo(-870, 165)
        pa.leftClick()
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
        
    if keyboard.is_pressed("f3"):
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
        clip.copy(" (24-10-2025)")
        pa.hotkey("ctrl", "v")
        time.sleep(0.2)


    

