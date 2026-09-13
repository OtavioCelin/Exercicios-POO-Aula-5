class Retangulo:
    largura: float
    altura: float

    def __init__(self, largura: float, altura: float) -> None:
        self.largura = largura
        self.altura = altura

    def calcular_area(self) -> None:
        area = self.largura * self.altura
        print(f"A Área do Retangulo é {area}")

    def calcula_perimetro(self) -> None:
        perimetro = (self.largura + self.altura) * 2
        print(f"O Perimetro do Retangulo é {perimetro}")
        