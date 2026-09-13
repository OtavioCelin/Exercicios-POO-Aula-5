import random

class ContaBancaria:
    num_conta: int
    __saldo: float


    def __init__(self, saldo_inicial: float = 0.0) -> None:
        self.num_conta = random.randint(1000, 9999)
        self.__saldo = saldo_inicial

    def visualizar_saldo(self) -> None:
        print(f"O seu Saldo é R${self.__saldo}")

    def depositar(self, senha: int, valor: float) -> None:
        if senha == self.num_conta:
            if valor > 0:
                self.__saldo = self.__saldo + valor
                print(f"O Depósito de R${valor: .2f} foi realizado com Sucesso!")
            else:
                print(f"O valor de Deposito é Invalido")
        else:
            print("Acesso Negado!")

    def sacar(self, senha: int, valor: float) -> None:
        if senha == self.num_conta:
            if valor < self.__saldo:
                self.__saldo = self.__saldo - valor
                print(f"O Saque de R${valor: .2f} foi realizado com Sucesso!") 
            else:
                print(f"Não é possivel realizar o Saque. Saldo Insuficiente!")
        else:
            print("Acesso Negado!")