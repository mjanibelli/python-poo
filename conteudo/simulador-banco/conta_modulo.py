import decorator


class ContaBancaria:

    def __init__(self, nome: str, saldo: float=0.0) -> None:
        self.nome = nome.title()
        self.saldo = float(saldo)

    def __add__(self, outro):
        if isinstance(outro, self.__class__):
            novo_nome = self.nome + ", " + outro.nome
            novo_saldo = self.saldo + outro.saldo
            return self.__class__(novo_nome, novo_saldo)

        raise TypeError("Só é possível somar duas instâncias de ContaBancaria.")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.nome}, {self.saldo})"

    def __str__(self):
        return f"Nome do cliente: {self.nome} | Saldo: R$ {self.saldo}"

    @decorator.recibo
    @decorator.logger
    def depositar(self, quantia: float) -> str:
        if quantia > 0:
            self.saldo += quantia
            return f"Foram depositados R$ {quantia} em sua conta!"

        return "Não foi possível realizar o depósito."

    @decorator.recibo
    @decorator.logger
    def sacar(self, quantia: float) -> str:
        if self.saldo >= quantia > 0:
            self.saldo -= quantia
            return f"Foram sacados R$ {quantia} de sua conta!"

        return "Não foi possível realizar o saque."

    @decorator.recibo
    @decorator.logger
    def transferencia(self, destinatario, quantia: float) -> str:
        if isinstance(destinatario, self.__class__):
            if self.saldo > quantia > 0:
                destinatario.saldo += quantia
                return f"Transferência para {destinatario.nome} efetuada."

        return "Não foi possível realizar essa transferência."
