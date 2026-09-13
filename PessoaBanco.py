from ContaBancaria import ContaBancaria

class PessoaBanco:
    nome: str

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.conta = None

    def cadastrar_conta(self, saldo_inicial: float = 0.0) -> None:
        self.conta = ContaBancaria(saldo_inicial)
        print(f"Conta {self.conta.num_conta} foi cadastrado com Sucesso para {self.nome}!")
        print(self.conta)

    def acessar_conta(self) -> None:
        return self.conta.num_conta

