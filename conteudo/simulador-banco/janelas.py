from math import ceil
from tkinter.constants import CENTER
import PySimpleGUI as sg

TITULO = "Conta Bancária"

def make_win_login() -> sg.Window:
    layout_login = [
        [sg.Text("Nome: "), sg.Input(k="Nome", s=(30, 30))],
        [sg.Text("Saldo Inicial: "), sg.Input(k="SaldoIni", s=(8, 10))],
        [sg.Button("Inserir", bind_return_key=True), sg.Exit("Sair")]]

    return sg.Window(TITULO, layout_login)


def make_win_menu() -> sg.Window:
    layout_menu = [
        [sg.Text("Escolha uma opção:", justification=CENTER)], 
        [sg.Button("Sacar"), sg.Button("Depositar"), sg.Button("Transferência")], 
        [sg.Button("Abrir conta conjunta"), sg.Button("Minha conta")], 
        [sg.Exit("Sair")]]

    return sg.Window(TITULO, layout_menu)


def make_win_sacar():
    layout_sacar = [
        [sg.Text("Digite a quantia que deseja sacar: "), sg.Input(k="SacaQnt", s=(8, 10))],
        [sg.Button("Inserir", bind_return_key=True), sg.Cancel("Cancelar")]]

    return sg.Window(TITULO, layout_sacar)


def make_win_depositar():
    layout_depositar = [
        [sg.Text("Digite a quantia que deseja depositar: "), sg.Input(k="DeposQnt", s=(8, 10))],
        [sg.Button("Inserir", bind_return_key=True), sg.Cancel("Cancelar")]]

    return sg.Window(TITULO, layout_depositar)


def make_win_transf():
    layout_transf = [
        [sg.Text("Digite a quantia que deseja transferir: "), sg.Input(k="TransfQnt", s=(8, 10))],
        [sg.Button("Inserir", bind_return_key=True), sg.Cancel("Cancelar")]]

    return sg.Window(TITULO, layout_transf)


def make_win_contaconj():
    layout_contaconj = [
        [sg.Text("Digite o nome do seu parceiro: "), sg.Input(k="NomeParc", s=(30, 30))], 
        [sg.Text("Digite o saldo inicial do seu parceiro: "), sg.Input(k="SaldoParc", s=(8, 10))],
        [sg.Button("Inserir", bind_return_key=True), sg.Cancel("Cancelar")]]

    return sg.Window(TITULO, layout_contaconj)