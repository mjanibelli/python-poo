import os
import time

import conta_modulo

nome = input("Digite seu nome: ")
saldo_inicial = float(input("Digite seu saldo inicial (Se houver): "))
cliente_1 = conta_modulo.ContaBancaria(nome, saldo_inicial)
cliente_teste = conta_modulo.ContaBancaria("Teste", 100)
print("Entrando na sua conta...")

while True:
    time.sleep(1.5)
    os.system("cls")
    print("[1] -> Sacar\n[2] -> Depositar\n[3] -> Fazer transferência")
    print("[4] -> Abrir conta conjunta\n[5] -> Conta\n[0] -> Sair")

    escolha = input("\nEscolha: ")
    os.system("cls")

    if escolha == "1":
        quantia = float(input("Digite a quantia que deseja sacar: "))
        print(cliente_1.sacar(quantia))

    elif escolha == "2":
        quantia = float(input("Digite a quantia que deseja depositar: "))
        print(cliente_1.depositar(quantia))

    elif escolha == "3":
        quantia = float(input("Digite a quantia que deseja transferir: "))
        print(cliente_1.transferencia(cliente_teste, quantia))

    elif escolha == "4":
        nome_parc = input("Digite o nome do parceiro(a): ")
        saldo_inicial_parc = float(input("Digite o saldo inicial do parceiro(a): "))
        cliente_2 = conta_modulo.ContaBancaria(nome_parc, saldo_inicial_parc)
        cliente_conjunto = cliente_1 + cliente_2
        print(cliente_conjunto)

    elif escolha == "5":
        print(cliente_1)

    elif escolha == "0":
        break

    else:
        print("Opção inválida!")
