import pandas as pd
from IPython.display import display
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
import time
import urllib
import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Números de telefone',size=(10,0)), sg.Input(size=(60,0),key='numeros')],
            [sg.Text('Mensagem',size=(10,0)), sg.Input(size=(60,0),key='mensagem')],
            [sg.Button('Enviar')]
        ]

        janela = sg.Window("WEB Disparador").layout(layout)

        self.button, self.values = janela.read()

        contatos = pd.read_excel("Enviar.xlsx")
    display(contatos)

        navegador = webdriver.Edge()




    def Iniciar(self):
        numeros = self.values['numeros']
        mensagem = self.values['mensagem']



