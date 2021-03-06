import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import POPOUT_WINDOW_FONT, TimerStart, Window
from tkinter import Event
from tkinter.constants import CENTER

TITULO = "Manipulador de Arquivos"


def make_win_esc_arq() -> sg.Window:
    layout1 = [
        [sg.Text("Escolha o arquivo que deseja manipular: ")], 
        [sg.Input(k="Input_Arq"), sg.FileBrowse("Pesquisar", k="Arquivo")], 
        [sg.Button("Inserir", bind_return_key=True), sg.Exit("Sair")]]

    return sg.Window(TITULO, layout1)


def make_win_menu() -> sg.Window:

    layout_menu = [
        [sg.Text("Menu de Opções", s=(26, 2), justification=CENTER, font=("Courier New", 15, "bold"))], 
        [sg.Text("Escolha o que fazer com o arquivo: ")],
        [sg.Button("Procurar palavra", s=(12, 2)), sg.Button("Realocar", s=(12, 2)), sg.Button("Renomear", s=(12, 2))],
        [sg.Button("Zipar", s=(12, 2)), sg.Button("Proteger PDF", s=(12, 2)), sg.Exit("Sair", s=(12, 2))]]

    return sg.Window(TITULO, layout_menu)


def make_win_palavra() -> sg.Window:
    layout_esc_palavra = [
        [sg.Text("Digite a palavra ou frase que deseja procurar no arquivo: ")],
        [sg.Input(k="Palavra")], 
        [sg.Button("Inserir", bind_return_key=True), sg.Cancel("Cancelar")]]

    return sg.Window(TITULO, layout_esc_palavra)


def make_win_realocar() -> sg.Window:
    layout_realocar = [
        [sg.Text("Insira o novo caminho para o arquivo: ")],
        [sg.Input(k="Caminho_novo")], 
        [sg.Button("Inserir", bind_return_key=True), sg.Cancel("Cancelar")]]
    
    return sg.Window(TITULO, layout_realocar)


def make_win_renomear() -> sg.Window:
    layout_renomear = [
        [sg.Text("Digite o novo nome do arquivo: ")], 
        [sg.Input(k="Nome_novo")], 
        [sg.Button("Inserir", bind_return_key=True), sg.Cancel("Cancelar")]]

    return sg.Window(TITULO, layout_renomear)


def make_win_senha_pdf() -> sg.Window:
    layout_senha_pdf = [
        [sg.Text("Digite a senha que deseja inserir no PDF: ")],
        [sg.Input(k="Senha_pdf")],
        [sg.Button("Inserir", bind_return_key=True), sg.Cancel("Cancelar")]]

    return sg.Window(TITULO, layout_senha_pdf)
