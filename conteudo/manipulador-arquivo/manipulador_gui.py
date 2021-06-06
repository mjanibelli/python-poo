import os

import PySimpleGUI as sg
from tkinter import Event
from typing import ValuesView

import janelas
import manipulador_modulo

sg.theme("DarkGrey8")

win_esc_arq = janelas.make_win_esc_arq()
event, values = win_esc_arq.read()

if event == "Inserir":
    arquivo_dir = values["Input_Arq"]

    if os.path.isfile(arquivo_dir):
        arquivo_manip = manipulador_modulo.ArquivoTexto(arquivo_dir)
        win_esc_arq.close()

        win_menu = janelas.make_win_menu()

        while True:
            event, values = win_menu.read()

            if event in (None, "Sair"):
                break
            
            elif values["Escolha"] == "Procurar palavra":
                win_menu.Hide()
                win_palavra = janelas.make_win_palavra()
                event, values = win_palavra.read()

                if event in (None, "Cancelar"):
                    win_palavra.close()
                else:
                    palavra = values["Palavra"]
                    mensagem = arquivo_manip.procurar_palavra(palavra)
                    sg.popup(mensagem)
                    win_palavra.close()
                
                win_menu.UnHide()

            elif values["Escolha"] == "Proteger PDF":
                win_menu.Hide()
                win_pdf_senha = janelas.make_win_senha_pdf()
                event, values = win_pdf_senha.read()

                if event in (None, "Cancelar"):
                    win_pdf_senha.close()
                else:
                    senha_pdf = values["Senha_pdf"]
                    mensagem = arquivo_manip.gerarsenha_pdf(senha_pdf)  # Usar threading para fazer uma loading screen.
                    sg.popup(mensagem)
                    win_pdf_senha.close()

                win_menu.UnHide()

            elif values["Escolha"] == "Realocar":
                win_menu.Hide()
                win_realocar = janelas.make_win_realocar()
                event, values = win_realocar.read()

                if event in (None, "Cancelar"):
                    win_realocar.close()
                else:
                    caminho_novo = values["Caminho_novo"]
                    mensagem = arquivo_manip.realocar_arquivo(caminho_novo)
                    sg.popup(mensagem)
                    win_realocar.close()

                win_menu.UnHide()

            elif values["Escolha"] == "Renomear":
                win_menu.Hide()
                win_renomear = janelas.make_win_renomear()
                event, values = win_renomear.read()

                if event in (None, "Cancelar"):
                    win_realocar.close()
                else:
                    nome_novo = values["Nome_novo"]
                    mensagem = arquivo_manip.renomear_arquivo(nome_novo)
                    sg.popup(mensagem)
                    win_renomear.close()

                win_menu.UnHide()

            elif values["Escolha"] == "Zipar":
                mensagem = arquivo_manip.zipar()
                sg.popup(mensagem)

        win_menu.close()

    else:
        sg.popup("Não foi inserido um diretório válido!")
