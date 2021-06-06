import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import No, Tree

import conta_modulo
import janelas

sg.theme("DarkGrey8")

win_login = janelas.make_win_login()
event, values = win_login.read()

if event == "Inserir":
    cliente_1 = conta_modulo.ContaBancaria(values["Nome"], values["SaldoIni"])
    cliente_teste = conta_modulo.ContaBancaria("Teste", 100)
    win_menu = janelas.make_win_menu()
    win_login.close()

    while True:
        event, values = win_menu.read()

        if event in (None, "Sair"):
            break
        
        elif event == "Sacar":
            win_menu.Hide()
            win_sacar = janelas.make_win_sacar()
            event, values = win_sacar.read()

            if event in (None, "Cancelar"):
                win_sacar.close()
            else:
                quantia = float(values["SacaQnt"])
                sg.popup(cliente_1.sacar(quantia))
                win_sacar.close()

            win_menu.UnHide()

        elif event == "Depositar":
            win_menu.Hide()
            win_depositar = janelas.make_win_depositar()
            event, values = win_depositar.read()

            if event in (None, "Cancelar"):
                win_depositar.close()
            else:
                quantia = float(values["DeposQnt"])
                sg.popup(cliente_1.depositar(quantia))
                win_depositar.close()

            win_menu.UnHide()

        elif event == "Transferência":
            win_menu.Hide()
            win_transf = janelas.make_win_transf()
            event, values = win_transf.read()

            if event in (None, "Cancelar"):
                win_transf.close()
            else:
                quantia = float(values["TransfQnt"])
                sg.popup(cliente_1.transferencia(cliente_teste, quantia))
                win_transf.close()

            win_menu.UnHide()

        elif event == "Abrir conta conjunta":
            win_menu.Hide()
            win_contaconj = janelas.make_win_contaconj()
            event, values = win_contaconj.read()

            if event in (None, "Cancelar"):
                win_contaconj.close()
            else:
                nome_parc = values["NomeParc"]
                saldo_inicial_parc = float(values["SaldoParc"])
                cliente_2 = conta_modulo.ContaBancaria(nome_parc, saldo_inicial_parc)
                cliente_conjunto = cliente_1 + cliente_2
                sg.popup(cliente_conjunto)
                win_contaconj.close()
            
            win_menu.UnHide()

        elif event == "Minha conta":
            sg.popup(cliente_1)
    
    win_menu.close()