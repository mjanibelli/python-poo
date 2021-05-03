import os
import time
import datetime

import tamagotchi_modulo

while True:
    print("Menu Inicial\n[1] -> Jogar\n[0] -> Sair")
    esc = input("Escolha: ")
    os.system("cls")

    if esc == "1":
        if tamagotchi_modulo.carregar_tamagotchi():
            tamagotchi = tamagotchi_modulo.carregar_tamagotchi()
            tamagotchi.perder_status()

        else:
            nome = input("Digite o nome do seu Tamagotchi: ")
            tamagotchi = tamagotchi_modulo.Tamagotchi(nome)

            print(f"{tamagotchi.nome} nasceu!\n")
            time.sleep(1)
            os.system("cls")

        while True:  
            dias_vida = (datetime.date.today() - tamagotchi.nascimento).days
            tamagotchi.mostrar_tela(dias_vida)
            acao = input("O que fazer agora?: ")

            if acao == "0":
                os.system("cls")
                tamagotchi.salvar_tamagotchi()
                print("Seu tamagotchi foi salvo!\n")
                break

            elif acao == "1":
                os.system("cls")

                if tamagotchi.fome == 10:
                    print(f"{tamagotchi.nome} já está cheio!")
                else:
                    tamagotchi.alimentar()
            
            elif acao == "2":
                os.system("cls")
                tamagotchi.carinho()

            elif acao == "3":
                os.system("cls")

                if tamagotchi.limpeza == 10:
                    print(f"{tamagotchi.nome} já está limpo!")
                else:
                    tamagotchi.banho()       

    elif esc == "0":
        break

print("Até a próxima!")