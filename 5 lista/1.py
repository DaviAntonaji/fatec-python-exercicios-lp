# 1. Elabore uma estrutura para representar um produto (código, nome, preço). Aplique 10% de aumento no preço do produto e apresente.


class Produto:
    codigo = 0
    nome = ''
    preco = 0.0

def main():
    produto = Produto()
    produto.codigo = int(input("Digite o código do produto: "))
    produto.nome = input("Digite o nome do produto: ")
    produto.preco = float(input("Digite o preço do produto: R$"))
    
    
    print("."*20)
    print(f"Produto: {produto.nome}")
    print(f"Código: {produto.codigo}")
    print(f"Preço: {produto.preco:.2f}")
    produto.preco += (produto.preco * 10/100)
    print(f"Preço reajustado: {produto.preco:.2f}")
    print("."*20)

main()