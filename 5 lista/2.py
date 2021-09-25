# 1. Elabore uma estrutura para representar um produto (código, nome, preço). Aplique 10% de aumento no preço do produto e apresente.


class Produto:
    codigo = 0
    nome = ''
    preco = 0.0

def main():
    produtos = []
    for i in range(3):
        produto = Produto()
        produto.codigo = int(input(f"Digite o código do {i+1}° produto: "))
        produto.nome = input(f"Digite o nome do {i+1}° produto: ")
        produto.preco = float(input(f"Digite o preço do {i+1}° produto: R$"))
        produtos.append(produto)
        print("."*20)
    
    for produto in produtos:
        preco_reajustado = produto.preco + (produto.preco * 10/100)
        print("."*20)
        print(f"Produto: {produto.nome}")
        print(f"Código: {produto.codigo}")
        print(f"Preço: {produto.preco:.2f}")
        print(f"Preço reajustado: {preco_reajustado:.2f}")
        print("."*20)
        print()

main()