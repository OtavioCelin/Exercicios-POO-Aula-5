from Pessoa import Pessoa
from Retangulo import Retangulo
from ContaBancaria import ContaBancaria
from PessoaBanco import PessoaBanco

def main() -> None:
    # pessoa: Pessoa = Pessoa("Otavio", 20)
    # pessoa.apresentar()

    # retangulo: Retangulo = Retangulo(20,18)
    # retangulo.calcular_area()
    # retangulo.calcula_perimetro()

    

    cliente: PessoaBanco = PessoaBanco("Otavio")
    cliente.cadastrar_conta()

    contaBancaria: ContaBancaria = ContaBancaria(100)
    contaBancaria.visualizar_saldo()
    contaBancaria.depositar(1345, 2000)
    contaBancaria.sacar(123, 1000)

if __name__ == '__main__':
    main()