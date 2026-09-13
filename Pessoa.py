class Pessoa: 
    nome: str
    idade: int

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def apresentar(self) -> None:
        print(f"""
            Nome: {self.nome}
            idade: {self.idade}
            """)
