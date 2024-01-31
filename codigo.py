import pyautogui 
import time

pyautogui.PAUSE = 1 

pyautogui.press("win") 
pyautogui.write("chrome") 
pyautogui.press("enter") 

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.click(x=484, y=73)
pyautogui.write(link)
pyautogui.press("enter")

#time.sleep(5)      25.95   6.5     


pyautogui.click(x=925, y=515) 
pyautogui.write("rafael@gmail.com")
pyautogui.press("tab") 
pyautogui.write("sua senha")
pyautogui.click(x=974, y=721) 
time.sleep(3) 


import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:
    pyautogui.click(x=952, y=358)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
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
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    pyautogui.scroll(5000)



