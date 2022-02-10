import PySimpleGUI as sg
import os
import time
import pyautogui

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Números de telefone',size=(10,0)), sg.Input(size=(60,0),key='numeros')],
            [sg.Text('Mensagem',size=(10,0)), sg.Input(size=(60,0),key='mensagem')],
            [sg.Button('Enviar')]
        ]

        janela = sg.Window("WEB Disparador").layout(layout)

        self.button, self.values = janela.read()

    def Iniciar(self):
        numeros = self.values['numeros']
        mensagem = self.values['mensagem']
       

tela = TelaPython()
tela.Iniciar()