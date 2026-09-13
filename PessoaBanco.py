from ContaBancaria import ContaBancaria

class PessoaBanco:
    nome: str

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.conta = None

    def cadastrar_conta(self, saldo_inicial: float = 0.0) -> None:
        self.conta = ContaBancaria(saldo_inicial)
        print(f"Parabéns {self.nome}, Sua Conta foi Cadastrada com Sucesso")
        print(f"O numero da Conta é {self.conta.num_conta}")

    def acessar_conta(self) -> None:
        return self.conta.num_conta

