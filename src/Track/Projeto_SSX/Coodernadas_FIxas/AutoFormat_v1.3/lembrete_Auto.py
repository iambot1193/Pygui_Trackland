import tkinter as tk

def executar(
    itens=None,
    largura=360,
    altura=260,
    opacidade=0.98,
    borda=False,
):
    """
    Abre uma janelinha fixa (somente leitura), sempre no topo, com linhas numeradas.
    - itens: lista de strings a exibir (uma por linha)
    - largura/altura: tamanho da janela
    - opacidade: 0.0 a 1.0
    - borda: False = janela sem moldura; True = janela com moldura do SO
    """

    # Lista padrão: os "seguintes textos" (curtos) que você enviou
    if itens is None:
        itens = [
            "S COMUNICAÇÃO.",
            "RESET.",
            "BUZZER VIOLADO.",
            "SALTOS.",
            "IGNIÇÃO VIOLADA.",
            "MAL CONTATO BACKUP.",
            "BACKUP NUNCA TEM CARGA.",
            "S DADOS O SUFICIENTE",
            "POSIÇÃO IG OFF.",
            "BATERIA VIOLADA PORTAL.",
            "SALTOS IG OFF.",
            "GPS TRAVADO.",
        ]

    class StickyNote(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("")
            if not borda:
                self.overrideredirect(True)   # sem borda
            self.attributes("-topmost", True)   # sempre no topo
            self.attributes("-alpha", opacidade)
            self.configure(bg="#101014")

            # posiciona no canto superior direito
            self.geometry(f"{largura}x{altura}+0+0")
            self.update_idletasks()
            sw = self.winfo_screenwidth()
            x = sw - largura - 12
            y = 12
            self.geometry(f"{largura}x{altura}+{x}+{y}")

            # título/legenda
            titulo = tk.Label(
                self, text="Lembretes (somente leitura) • ESC fecha",
                bg="#101014", fg="#cfd3ff", font=("Segoe UI", 9, "bold"), anchor="w"
            )
            titulo.pack(fill="x", padx=8, pady=(8, 0))

            # área de texto somente leitura com linhas numeradas
            self.txt = tk.Text(
                self,
                wrap="word",
                bg="#0f1117",
                fg="#e8e8ff",
                relief="flat",
                font=("Segoe UI", 10),
                height=10,
                padx=10,
                pady=8,
            )
            self.txt.pack(fill="both", expand=True, padx=8, pady=8)

            # insere linhas numeradas
            self._popular(itens)

            # bloqueia edição
            self.txt.config(state="disabled")

            # binds
            self.bind("<Escape>", lambda e: self.destroy())
            

            # mover janela clicando (se sem borda)
            if not borda:
                for w in (self, self.txt, titulo):
                    w.bind("<Button-1>", self._start_move)
                    w.bind("<B1-Motion>", self._on_move)

        def _popular(self, itens):
            linhas = [f"{i+1}. {t}" for i, t in enumerate(itens)]
            conteudo = "\n".join(linhas)
            self.txt.insert("1.0", conteudo)

        # mover a janela
        def _start_move(self, e):
            self._ox, self._oy = e.x, e.y
        def _on_move(self, e):
            try:
                self.geometry(f"+{self.winfo_x() + (e.x - self._ox)}+{self.winfo_y() + (e.y - self._oy)}")
            except Exception:
                pass

    StickyNote().mainloop()


# permitir rodar sozinho: python lembrete.py
if __name__ == "__main__":
    executar()
