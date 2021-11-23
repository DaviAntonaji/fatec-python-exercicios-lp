from tabulate import tabulate


class Tipo_Cliente:
    cliente_id: int
    nome: str


class Tipo_Venda:
    cod_venda: int
    dia: int
    total: float
    cliente: int


clientes = []
vendas = []


def cadastra_clientes():
    continuar = "s"
    while continuar == "s":
        cliente = Tipo_Cliente()
        cliente.cliente_id = int(input("Digite o código do cliente: "))
        cliente.nome = input("Digite o nome do cliente: ")

        clientes.append(cliente)

        continuar = input("Deseja continuar? (S/N): ").lower()

    menu()


def listar_clientes():
    matriz = []
    for cliente in clientes:
        matriz.append([cliente.cliente_id, cliente.nome])
    print(tabulate(matriz, headers=["Código do cliente", "Nome"]))

    menu()


def cadastrar_vendas():
    cadastro = "s"
    while cadastro == "s":
        if len(vendas) != 5:
            venda = Tipo_Venda()
            venda.cod_venda = int(input("Digite o código da venda: "))
            venda.dia = int(input("Digite o dia de venda: "))
            venda.total = float(input("Digite o valor da venda: "))
            venda.cliente = int(input("Digite o código do cliente: "))
            vendas.append(venda)

            cadastro = input("Deseja continuar? (S/N): ").lower()
        else:
            print("Limite de vendas atingido!")
            cadastro = "n"

    menu()


def listar_vendas():
    matriz = []
    for venda in vendas:
        matriz.append([venda.cod_venda, venda.dia, venda.total, venda.cliente])
    print(tabulate(matriz, headers=[
          "Código da venda", "Dia da venda", "Valor", "Código do cliente"]))

    menu()


def listar_vendas_dia():

    dia = int(input("Digite o dia: "))
    if dia > 0 and dia < 32:
        matriz = []
        for venda in vendas:
            if venda.dia == dia:
                matriz.append([venda.cod_venda, venda.dia,
                              venda.total, venda.cliente])
        print(tabulate(matriz, headers=[
              "Código da venda", "Dia da venda", "Valor", "Código do cliente"]))
    else:
        print("Dia invalido!")
    menu()


def armazenar():
    with open("vendas.txt", "a+", encoding="utf-8") as file:
        for venda in vendas:
            file.write(str(venda.cod_venda) + "," + str(venda.dia) +
                       "," + str(venda.total) + "," + str(venda.cliente) + "\n")
    menu()


def apresentar():
    with open("vendas.txt", "r", encoding="utf-8") as file:
        tabela = []
        for line in file.readlines():
            venda = line.split(",")
            tabela.append([venda[0], venda[1], venda[2], venda[3]])
        print(tabulate(tabela, headers=[
              "Código da venda", "Dia da venda", "Valor", "Código do cliente"]))
    menu()


def menu():
    print("."*50)
    print("1 Cadastrar clientes")
    print("2 Mostrar todos os clientes")
    print("3 Cadastrar vendas")
    print("4 Mostrar todas as vendas")
    print("5 Mostrar o total de vendas de um determinado dia")
    print("6 Armazenar todos os campos da venda em um arquivo")
    print("7 Apresentar o conteúdo do arquivo")
    print("8 Sair")
    print("."*50)

    operacao = input("Digite a operação: ")
    operacoes_validas = ["1", "2", "3", "4", "5", "6", "7", "8"]
    if operacao in operacoes_validas:
        if operacao == "1":
            cadastra_clientes()
        elif operacao == "2":
            listar_clientes()
        elif operacao == "3":
            cadastrar_vendas()
        elif operacao == "4":
            listar_vendas()
        elif operacao == "5":
            listar_vendas_dia()
        elif operacao == "6":
            armazenar()
        elif operacao == "7":
            apresentar()
        elif operacao == "8":
            exit("Aplicação encerrada.")
    else:
        menu()


def main():
    menu()


main()
