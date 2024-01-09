import pyautogui
import time

pyautogui.PAUSE = 1 #Declaro que haverá um intervalo de 1s em todos os comandos

pyautogui.press("win") #Etapa 1 (Abrindo o menu)
pyautogui.write("chrome") #Etapa 2 (Abrindo o brownser)
pyautogui.press("enter") #Etapa 3 (Executando o navegador)

#Etapa 4 (Navegador)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(5) #Declara que nesse trecho de código haverá uma pausa de 5s

pyautogui.click(x=506, y=359) #Click na posição de login
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=651, y=519) # clique no botao de login
time.sleep(3) #Tempo de espera caso haja algum problema na aplicação

#Importando o csv com o Pandas
import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Etapa 5 (Cadastrar um produto)
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=499, y=245)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
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
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim


