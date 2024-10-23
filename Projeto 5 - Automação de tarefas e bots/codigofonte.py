# Importando as bibliotecas
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1.0

# Abrir o navegador e entrar no link
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(4)

# Preencher o login
pyautogui.click(x=403, y=279)
pyautogui.write("rafael123@gmail.com")
pyautogui.press("tab")
pyautogui.write("rafaelcb123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4)  # Esperar para a página carregar

# Importar a tabela
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Preencher o formulário de acordo com a tabela
for linha in tabela.index:
    pyautogui.click(x=395, y=206)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)

pyautogui.hotkey("alt", "f4")

