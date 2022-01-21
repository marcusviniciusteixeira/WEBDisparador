import pandas as pd
from IPython.display import display
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
import time
import urllib
import pyautogui

contatos = pd.read_excel("Enviar.xlsx")
display(contatos)

navegador = webdriver.Edge()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(3)

for i, mensagem in enumerate(contatos['Mensagem']):
    pessoa = contatos.loc[i, "Pessoa"]
    numero = contatos.loc[i, "Número"]
    t1 = '''*A CLARO ESTÁ LIBERANDO PARA O SEU NÚMERO*

✅*10GB DE INTERNET*
✅*LIGAÇÕES ILIMITADAS PRA QUALQUER OPERADORA*
✅*WHATSAPP FACEBOOK INSTAGRAM TWITTER WAZE*
✅*DESCONTOS EM APARELHO CELULAR NAS LOJAS CLARO*

*PARA SABER MAIS*

*ENVIE SIM* PARA ESSE PERFIL QUE UM DE NOSSOS CONSULTORES ENTRARÁ EM CONTATO!'''
    texto = urllib.parse.quote(f"OLÁ, {pessoa}\n{t1}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)


    time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    #navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(3)


        

