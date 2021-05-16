from tkinter import Event
from tkinter.constants import CENTER
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import POPOUT_WINDOW_FONT, Window

TITULO = "Manipulador de Arquivos"


def make_win1():
    layout1 = [
        [sg.Text("Escolha o arquivo que deseja manipular: ")], 
        [sg.Input(k="Input_Arq"), sg.FileBrowse("Pesquisar", k="Arquivo")], 
        [sg.Button("Inserir", k="Inserir"), sg.Exit("Sair", k="Sair")]]

    return sg.Window(TITULO, layout1)


def make_win2():
    layout2 = [
        [sg.Text("Menu de Opções", size=(40, 2), justification=CENTER)], 
        [sg.Text("Escolha o que fazer com o arquivo: ")], 
        [sg.InputCombo(("Procurar palavra", "Realocar", "Renomear", "Zipar"), size=(20, 10), k="Escolha")], 
        [sg.Button("Inserir"), sg.Exit("Sair")]]

    return sg.Window(TITULO, layout2)


def make_win_palavra():
    layout_esc_palavra = [
        [sg.Text("Digite a palavra ou frase que deseja procurar no arquivo: ")],
        [sg.Input(k="Palavra")], 
        [sg.Button("Inserir"), sg.Cancel("Cancelar")]]

    return sg.Window(TITULO, layout_esc_palavra)


def make_win_realocar():
    layout_realocar = [
        [sg.Text("Insira o novo caminho para o arquivo: ")],
        [sg.Input(k="Caminho_novo")], 
        [sg.Button("Inserir"), sg.Cancel("Cancelar")]]
    
    return sg.Window(TITULO, layout_realocar)


def make_win_renomear():
    layout_renomear = [
        [sg.Text("Digite o novo nome do arquivo: ")], 
        [sg.Input(k="Nome_novo")], 
        [sg.Button("Inserir"), sg.Cancel("Cancelar")]]

    return sg.Window(TITULO, layout_renomear)
