#!/usr/bin/env python
# coding: utf-8

# # Automação de Sistemas e Processos com Python
# 
# ### Desafio:
# 
# Para controle de custos, todos os dias, seu chefe pede um relatório com todas as compras de mercadorias da empresa.
# O seu trabalho, como analista, é enviar um e-mail para ele, assim que começar a trabalhar, com o total gasto, a quantidade de produtos compradas e o preço médio dos produtos.
# 
# E-mail do seu chefe: para o nosso exercício, coloque um e-mail seu como sendo o e-mail do seu chefe<br>
# Link de acesso ao sistema da empresa: https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema
# 
# Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

# In[9]:


import pyautogui
import time


pyautogui.PAUSE= 1

#acessar o site da empresa
pyautogui.hotkey ("ctrl","t")
pyautogui.write ("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press ("enter")

#esperar o site carregar
time.sleep (2)

# a posição varia para cada tamanho de tela por isso podem ser necessários ajustes

#fazer login
pyautogui.click(x=828, y=390)

#user
pyautogui.write("1")

pyautogui.click(x=870, y=452)
#senha
pyautogui.write("2")

#acessar
pyautogui.click(x=872, y=518)
time.sleep (3)

#exportar base de dados
pyautogui.click(x=570, y=334)
pyautogui.click(x=658, y=863)
time.sleep (3)


# In[6]:


# para pegar pegar o posição do mouse usei: (espera 5s e printa a posição)
# time.sleep(5)
# print(pyautogui.position())


# In[11]:


#calcular indicadores
import pandas as pd

tabela = pd.read_csv(r"Compras.csv", sep=";")
display (tabela)

total_gasto= tabela["ValorFinal"].sum()
quantidade=  tabela["Quantidade"].sum()
preco_medio= total_gasto / quantidade
print ("Total Gasto:", total_gasto)
print ("Quantidade:", quantidade)
print ("Preço médio:", preco_medio)


# In[12]:


#enviar e mail, novamente talvez seja necessário ajustes na posição do mouse, e claro usar um e mail válido
import pyperclip

pyautogui.PAUSE= 1
pyautogui.hotkey("ctrl","t")

pyautogui.write("https://mail.google.com/mail/u/0/#inbox")

pyautogui.press("enter")

time.sleep(3)
        
pyautogui.click(x=87, y=200)

time.sleep(3)

pyautogui.write("exemplot@gmail.com")
pyautogui.press("tab")#seleciona o e e-mail

pyautogui.press("tab")#pula para o assunto do texto
pyperclip.copy("Relatório semanal")
pyautogui.hotkey("ctrl","v")

pyautogui.press("tab")#pula para o corpo do texto

texto=f"""
seguem os relatórios

Total gasto: R$ {total_gasto:,.2f}
Quantidade: R$ {quantidade:,.2f}
Preço médio: R$ {preco_medio:,.2f}

QUALQUER DÚVIDA ENTRE EM CONTATO
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("ctrl","enter")

