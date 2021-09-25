# Elabore uma estrutura para representar um produto (código, nome, preço). Crie uma função para cadastrar 5 produtos. Crie outra função para aplicar 10% de aumento no preço do produto e apresente, po

class Produto:
    codigo = 0
    nome = ''
    preco = 0.0


produtos = []

def popular(total):
    for i in range(total):
        produto = Produto()
        produto.codigo = int(input(f"Digite o código do {i+1}° produto: "))
        produto.nome = input(f"Digite o nome do {i+1}° produto: ")
        produto.preco = int(input(f"Digite o preço do {i+1}° produto: R$"))
        print("."*20)
        produtos.append(produto)
    
    calculaReajuste()

def calculaReajuste():
    for produto in produtos:
        preco_reajustado = produto.preco + (produto.preco*10/100)
        printaProduto(produto,preco_reajustado)

def printaProduto(produto, preco_reajustado):
    print()
    print("."*20)
    print(f"Produto: {produto.nome}")
    print(f"Código: {produto.codigo}")
    print(f"Preço: {produto.preco:.2f}")
    print(f"Preço reajustado: {preco_reajustado:.2f}")
    print("."*20)

def main():
    popular(2)

main()