import os

import PySimpleGUI as sg
from tkinter import Event
from typing import ValuesView

import layouts
import manipulador_modulo

window1 = layouts.make_win1()
event, values = window1.read()

if event == "Inserir":
    arquivo_dir = values["Arquivo"]

    if os.path.isfile(arquivo_dir):
        arquivo_manip = manipulador_modulo.ArquivoTexto(arquivo_dir)
        window1.close()

        window2 = layouts.make_win2()

        while True:
            event, values = window2.read()

            if event in (None, "Sair"):
                break
            
            elif values["Escolha"] == "Procurar palavra":
                window_palavra = layouts.make_win_palavra()
                event, values = window_palavra.read()

                if event in (None, "Cancelar"):
                    window_palavra.close()
                else:
                    palavra = values["Palavra"]
                    mensagem = arquivo_manip.procurar_palavra(palavra)
                    sg.popup(mensagem)
                    window_palavra.close()

            elif values["Escolha"] == "Realocar":
                window_realocar = layouts.make_win_realocar()
                event, values = window_realocar.read()

                if event in (None, "Cancelar"):
                    window_realocar.close()
                else:
                    caminho_novo = values["Caminho_novo"]
                    mensagem = arquivo_manip.realocar_arquivo(caminho_novo)
                    sg.popup(mensagem)
                    window_realocar.close()

            elif values["Escolha"] == "Renomear":
                window_renomear = layouts.make_win_renomear()
                event, values = window_renomear.read()

                if event in (None, "Cancelar"):
                    window_realocar.close()
                else:
                    nome_novo = values["Nome_novo"]
                    mensagem = arquivo_manip.renomear_arquivo(nome_novo)
                    sg.popup(mensagem)
                    window_renomear.close()

            elif values["Escolha"] == "Zipar":
                mensagem = arquivo_manip.zipar()
                sg.popup(mensagem)

        window2.close()

    else:
        sg.popup("Não foi inserido um diretório válido!")
