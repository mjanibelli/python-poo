import os

import PySimpleGUI as sg
from tkinter import Event
from typing import ValuesView

import janelas
import manipulador_modulo

sg.theme("DarkGrey8")

window1 = janelas.make_win1()
event, values = window1.read()

if event == "Inserir":
    arquivo_dir = values["Input_Arq"]

    if os.path.isfile(arquivo_dir):
        arquivo_manip = manipulador_modulo.ArquivoTexto(arquivo_dir)
        window1.close()

        window2 = janelas.make_win2()

        while True:
            event, values = window2.read()

            if event in (None, "Sair"):
                break
            
            elif values["Escolha"] == "Procurar palavra":
                window_palavra = janelas.make_win_palavra()
                event, values = window_palavra.read()

                if event in (None, "Cancelar"):
                    window_palavra.close()
                else:
                    palavra = values["Palavra"]
                    mensagem = arquivo_manip.procurar_palavra(palavra)
                    sg.popup(mensagem)
                    window_palavra.close()

            elif values["Escolha"] == "Proteger PDF":
                window_pdf_senha = janelas.make_win_senha_pdf()
                event, values = window_pdf_senha.read()

                if event in (None, "Cancelar"):
                    window_pdf_senha.close()
                else:
                    senha_pdf = values["Senha_pdf"]
                    mensagem = arquivo_manip.gerarsenha_pdf(senha_pdf)  # Usar threading para fazer uma loading screen.
                    sg.popup(mensagem)
                    window_pdf_senha.close()

            elif values["Escolha"] == "Realocar":
                window_realocar = janelas.make_win_realocar()
                event, values = window_realocar.read()

                if event in (None, "Cancelar"):
                    window_realocar.close()
                else:
                    caminho_novo = values["Caminho_novo"]
                    mensagem = arquivo_manip.realocar_arquivo(caminho_novo)
                    sg.popup(mensagem)
                    window_realocar.close()

            elif values["Escolha"] == "Renomear":
                window_renomear = janelas.make_win_renomear()
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