from playwright.sync_api import sync_playwright, expect

urldb = "https://docs.google.com/spreadsheets/d/1dn6tvlR3XRqHpuBEe71D6yjF0Ad-h7fz/edit?gid=2122038294#gid=2122038294"
urltrello = "https://trello.com/b/L9MtrvAH/suporte-i-op-e-cnt-track-land"

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False)            # ou p.firefox / p.webkit
    context = browser.new_context()                        # nova sessão (cookies, cache)
    page = context.new_page()   
    page.goto(urldb)# nova aba
    page = context.new_page()   
    page.goto(urltrello)# nova aba
    page.pause()

    
