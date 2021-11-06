"""

2. Elabore uma estrutura para representar e armazenar 10 produtos (código, nome, preço). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura.Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.
Menu de opções:

Cadastrar produtos
Visualizar todos os dados
Sair


"""


from tabulate import tabulate

class Produto:
    codigo:int
    nome:str
    preco:float


def cadastrarProdutos():
    try:
        # Tente abrir o arquivo e contar o tanto de produtos já cadastrados
        with open("produtos2.txt", "r", encoding="utf-8") as file:
            totalProdutosCadastrados =  len(file.readlines())
    except:
        # Se não existir, defina como 0
        totalProdutosCadastrados = 0

    desejaCadastrar = True
    while desejaCadastrar:


        if totalProdutosCadastrados == 10:
            print("Você chegou ao limite de cadastros.")
            desejaCadastrar = False

        with open("produtos2.txt", "a+", encoding="utf-8") as file:
            produto =  Produto()
            produto.codigo = int(input("Digite o código do produto: "))
            produto.nome = input("Digite o nome do produto: ")
            produto.preco = float(input("Digite o preço do produto: R$ "))

            file.write(str(produto.codigo) + "|" + produto.nome + "|" + str(produto.preco) + "\n")

        totalProdutosCadastrados += 1

            

        resposta = input("Deseja cadastrar mais um produto? (S/N)").lower()
        if resposta != "s":
            desejaCadastrar = False
    menu()


def visualizarProdutos():

    
    try:
        # Tenta abrir o arquivo:
        with open("produtos2.txt", "r", encoding="utf-8") as file:
            
            tabela = []
            for line in file.readlines():
                dados = line.split("|")
                produto = Produto()
                produto.codigo = dados[0]
                produto.nome = dados[1]
                produto.preco = dados[2]
                tabela.append([produto.codigo,produto.nome,"R$" + "{:.2f}".format(float(produto.preco))])
            print(tabulate(tabela, headers=["Código", "Nome", "Preço"]))
            menu()
                
               
    except:
        # Se o arquivo não existir
        menu()

def menu():
    print("#"*30)
    print("1. Cadastrar produtos")
    print("2. Visualizar todos os dados")
    print("3. Sair")
    print("#"*30)
    operacao = input("Digite a operação: ")
    if operacao in ["1", "2", "3"]:
        operacao = int(operacao)
        if operacao ==  1:
            cadastrarProdutos()
        elif operacao == 2:
            visualizarProdutos()
        elif operacao == 3:
            exit("Aplicação encerrada")
    else:
        print("Operação invalida!")
        menu()


def main():
    
        
    menu()

main()