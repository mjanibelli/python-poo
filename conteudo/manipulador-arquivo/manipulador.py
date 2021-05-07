# Fazer com mais de um arquivo
import os
import time

import manipulador_modulo

arquivo_dir = input("Digite o diretório do arquivo ou arraste-o até aqui: ")

if os.path.isfile(arquivo_dir):
    arquivo_manip = manipulador_modulo.ArquivoTexto(arquivo_dir)
    print("Carregando menu...")

    while True:
        time.sleep(1.5)
        os.system("cls")
        print(f"Trabalhando com o arquivo: '{arquivo_dir}'\n")
        print("[1] -> Procurar palavra\n[2] -> Realocar\n[3] -> Renomear")
        print("[4] -> Zipar\n[0] -> Sair")
        escolha = input("O que deseja fazer?: ")
        os.system("cls")

        if escolha == "1":
            palavra = input("Digite a palavra ou frase que deseja procurar: ")
            print(arquivo_manip.procurar_palavra(palavra))

        elif escolha == "2": 
            caminho_novo = input("Digite o novo caminho para o arquivo: ")
            print(arquivo_manip.realocar_arquivo(caminho_novo))

        elif escolha == "3":
            nome_novo = input("Digite o novo nome do arquivo: ")
            print(arquivo_manip.renomear_arquivo(nome_novo))

        elif escolha == "4":
            print(arquivo_manip.zipar())

        elif escolha == "0":
            break

        else:
            print("Essa opção não existe! Tente novamente.")

else:
    print("É preciso inserir um diretório para um arquivo válido.")
