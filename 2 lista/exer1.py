# 1. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método que leia um número e o multiplique por 2, apresente o resultado.

def multiplica(a):
    print(f"O valor de {a} x 2 é {a*2}")


def main():
    a = int(input("Digite o valor de A: "))
    multiplica(a)


main()
