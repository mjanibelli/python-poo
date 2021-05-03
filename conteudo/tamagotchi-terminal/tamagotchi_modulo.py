import datetime
import pickle
import random

import tamagotchi_sprite


class Tamagotchi:

    def __init__(self, nome):
        self.nome = nome.title()
        self.nascimento = datetime.date.today()
        self.fome = 5  # MAX = 10
        self.felicidade = 5  # MAX = 10
        self.limpeza = 5 # MAX = 10
        self.arquivo = "Tamagotchi.pkl"

    def alimentar(self):
        self.fome += 2
        if self.fome > 10:
            self.fome = 10

        print(f"{self.nome} foi alimentado!")

    def banho(self):
        self.limpeza += 5
        if self.limpeza > 10:
            self.limpeza = 10

        print(f"{self.nome} se sente mais limpo!")

    def carinho(self):
        self.felicidade += 3
        if self.felicidade > 10:
            self.felicidade = 10

        print(f"{self.nome} fica muito feliz com seu carinho!")

    def mostrar_tela(self, dias_vida):
        print(f"Fome: {self.fome} Felicidade: {self.felicidade} Limpeza: {self.limpeza}")
        print(f"Dias de vida: {dias_vida}")
        print(f"\t{tamagotchi_sprite.mostrar_sprite(dias_vida)}")
        print("[1] -> Alimentar", "[2] -> Fazer carinho", sep=" ")
        print("[3] -> Banho", "    [0] -> Salvar e sair\n", sep=" ")
    
    def perder_status(self):
        self.fome -= random.randint(1, 8)
        if self.fome < 0:
            self.fome = 0

        self.felicidade -= random.randint(1, 6)
        if self.felicidade < 0:
            self.felicidade = 0

        self.limpeza -= random.randint(1, 10)
        if self.limpeza < 0:
            self.limpeza = 0

        print(f"Enquanto você esteve fora, {self.nome} perdeu alguns status!")

    def salvar_tamagotchi(self):
        with open(self.arquivo, "wb") as arquivo:
            pickle.dump(self, arquivo, pickle.HIGHEST_PROTOCOL)




def carregar_tamagotchi():
    try:
        with open("Tamagotchi.pkl", "rb") as arquivo:
            tamagotchi = pickle.load(arquivo)
    except FileNotFoundError:
        return None
    else:
        return tamagotchi

