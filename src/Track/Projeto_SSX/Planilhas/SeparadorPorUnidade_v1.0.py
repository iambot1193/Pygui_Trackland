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
pd.set_option("display.width", 0)  # deixa quebrar linha conforme termina

COLS = [
    "PLACA",
    "UNIDADE_ORGANIZACIONAL_CLIENTE",
    "CLIENTE",
    "N_RASTREADOR",
    "SITUACAO",
    "INCIO_OBSERVACAO",
    "FIM_OBSERVACAO",
    "DATA_ULTIMA_POSICAO",
    "ACAO_TOMADA",
    "MOTIVO",
    "OBSERVACAO"
]

pasta_saida = r"C:\Users\jenni\Downloads\SSXSAIDA"
os.makedirs(pasta_saida, exist_ok=True)

dfs = []
for arquivo in os.listdir(Pasta_fonte):
    
    #ignorar os que nao sao excel     (mudar extenão dos arquivos caso não encontrar nada)
    if not arquivo.lower().endswith(("xlsx", "xls")):
        continue
    #configurando o caminho para cada arquivos excel que ele identificar
    caminho = os.path.join(Pasta_fonte, arquivo)
    

    
    #separador
    print(f"----------{arquivo}----------")
    df = pd.read_excel(caminho, dtype={"N° RASTREADOR": str})
    
    df.columns = (
    df.columns
        .str.strip()
        .str.upper()
        .str.normalize("NFKD").str.encode("ascii", "ignore").str.decode("ascii")
        .str.replace(" ", "_", regex=False)
        .str.replace("°", "", regex=False)
)
    
    df = df[COLS]
    
    #
for grupo, tabela in df.groupby("UNIDADE_ORGANIZACIONAL_CLIENTE"):
    caminho_arquivo = os.path.join(pasta_saida, f"{grupo}.xlsx")
    tabela.to_excel(caminho_arquivo, index=False)
    print(f"Arquivo criado: {caminho_arquivo}")

    print("\n")
    #
        
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


    

