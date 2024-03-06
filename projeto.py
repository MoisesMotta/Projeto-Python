# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
import pandas
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.5

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa um pouco maior(3 segundos, só nesse lugar especifico)

time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=497, y=356)
# escrever o seu email
pyautogui.write("testededados@gmail.com")
pyautogui.press("tab")  # passando pro próximo campo
pyautogui.write("senhateste")
pyautogui.click(x=646, y=513)  # clique no botao de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar usar o pandas para base de dados

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # para cada linha, na mminha tabela ^^
    # clicar no campo de código
    pyautogui.click(x=424, y=240)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]  # tabela.loc = pega inf da tabela, loc = localizar
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"])) #str = string = texto, str(1) = "1"
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
    if not pandas.isna(obs): #if not é uma condição, se nao tiver vazia: isna = vef se ta vazio
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")  # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
