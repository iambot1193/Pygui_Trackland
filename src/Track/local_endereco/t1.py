import pandas as pd
import os
import glob
import keyboard
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

# Configurações iniciais
geolocator = Nominatim(user_agent="meu_app")
pastafonte = r"C:\Users\jenni\Downloads\pegarendereco"
cache = {}  # Cache de coordenadas já convertidas

pd.set_option('display.max_rows', None)
keyboard.block_key('f2')

print("Pressione ENTER para iniciar o processo...")

while True:
    input("\nPressione ENTER para iniciar o processo...")

    arquivos_xlsx = glob.glob(os.path.join(pastafonte, "*.xlsx"))

    for arquivo in arquivos_xlsx:
        print(f"\nLendo {arquivo}...")
        try:
            df = pd.read_excel(arquivo, usecols=["lst_localizacao"])
        except Exception as e:
            print(f"Erro ao ler {arquivo}: {e}")
            continue

        enderecos = []
        for linha in df.itertuples(index=False):
            coord_raw = str(linha.lst_localizacao)

            try:
                # 🔧 Limpa colchetes, espaços e divide em latitude e longitude
                coord_limpa = coord_raw.strip("[]() ").replace(" ", "")
                lat_str, lon_str = coord_limpa.split(",")
                lat, lon = float(lat_str), float(lon_str)

                chave = (lat, lon)

                if chave in cache:
                    endereco = cache[chave]
                else:
                    location = geolocator.reverse(chave, language='pt')
                    endereco = location.address if location else "Não encontrado"
                    cache[chave] = endereco

                enderecos.append(endereco)
                print(f"✔ {coord_raw} → {endereco.split(',')[0]}")
                time.sleep(1)  # respeita limite da API

            except GeocoderTimedOut:
                print(f"⏳ Timeout para {coord_raw}, tentando novamente...")
                time.sleep(2)
                continue
            except Exception as e:
                print(f"❌ Erro com coordenada {coord_raw}: {e}")
                enderecos.append("Erro")
                continue

        # Adiciona resultado e salva novo arquivo
        df["endereco"] = enderecos
        novo_nome = arquivo.replace(".xlsx", "_enderecos.xlsx")
        df.to_excel(novo_nome, index=False)
        print(f"💾 Arquivo salvo: {novo_nome}\n")

    print("✅ Processo finalizado. Pressione ENTER novamente para repetir.\n")
