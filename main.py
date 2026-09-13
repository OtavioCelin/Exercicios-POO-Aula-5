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

    while True:


        print("\n===== Banco =====")
        print("1 - Visualizar Saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Cadastrar Conta")
        print("5 - Sair \n")


        escolha = input("Escolha uma opção:")

        if escolha == "1":
            conta = int(input("Digite o Numero da Sua Conta: "))
            cliente.conta.visualizar_saldo(conta)


        elif escolha == "2":
            conta = int(input("Digite o Numero da Sua Conta: "))
            valor = float(input("Digite o valor do Deposito: "))
            cliente.conta.depositar(conta, valor)

        elif escolha == "3":
            conta = int(input("Digite o Numero da Sua Conta: "))
            valor = float(input("Digite qual o valor do Saque: "))
            cliente.conta.sacar(conta, valor)

        elif escolha == "4":
            user_conta = input("Qual o Nome do Titular da Conta: ")
            cliente: PessoaBanco = PessoaBanco(user_conta)
            cliente.cadastrar_conta()

        elif escolha == "5":
            print("Programa Encerrado!")
            break

        else:
            print("Opção Invalida!")
            


            
            


if __name__ == '__main__':
    main()