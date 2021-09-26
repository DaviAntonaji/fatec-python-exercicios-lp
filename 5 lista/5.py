"""

5. Faça um programa que realize o cadastro de contas bancarias com as seguintes informações: numero da conta, nome do titular e saldo. O banco permitirá o cadastramento de 15 contas. **Crie uma função para cada opção do menu** a seguir. Utilize a estrutura na passagem de parâmetro:
Menu de opções:
1. Cadastrar contas
2. Visualizar todas as contas
3. Consultar por nome
4. Alterar nome e/ou saldo de um número de conta
5. Excluir a conta com menor saldo
6. Sair

Observação: 

* No item de menu 4. Alterar nome e/ou saldo de um número de conta, entenda que apenas pode ser alterado o nome e o saldo depois que você pesquisar pelo número da conta.
* No item 5 do menu, encontre o menor saldo dentre todos cadastrados, **depois exclua esta ÚNICA conta.**. O assunto de excluir algo de um vetor foi dado na disciplina de Algoritmo.



"""

import time

contas = []
numeros_existentes = []

class ContaBancaria:
    numero = 0
    titular = ""
    saldo = 0.0

def cadastrarContas(qtde):
    if len(contas) + qtde > 15:
        print("O limite de contas desse banco é 15, você ainda pode cadastrar: ", 15-len(contas), "contas")
    else:
        for i in range(qtde):
            conta = ContaBancaria()
            print("."*30)
            numero = int(input(f"Digite o n° da {i+1}° conta: "))
            if numero in numeros_existentes:
                print("O número dessa conta já existe.")
                i = i-1
            else:
                conta.numero = numero
                conta.titular = input(f"Digite o titular da  {i+1}° conta:  ")
                conta.saldo = float(input(f"Digite o saldo da  {i+1}° conta:  "))
                print("."*30)
                contas.append(conta)
                numeros_existentes.append(numero)
    main()
def consultarContas():
    if len(contas) == 0:
        print("Não há contas cadastradas")
    else:
        for conta in contas:
            print("."*30)
            print("Conta: ", conta.numero)
            print("Titular: ", conta.titular)
            print("Saldo: ", conta.saldo)
            print("."*30)
    time.sleep(3)
    main()

def consultarTitular(nome):
    achei = False
    i = 0
    
    for conta in contas:
        if achei == False:
            if conta.titular.lower() == nome.lower():
                print("."*30)
                print("Achei a conta.")
                print("Número: ", conta.numero)
                print("Titular: ", conta.titular)
                print(f"Número: {conta.saldo:.2f}")
                print("."*30)
                achei = True
    if achei == False:
        print("Não encontrei uma conta com esse titular")

    time.sleep(3)
    main()
    

def alterarConta():
    codigo = int(input("Digite o código da conta que deseja alterar: "))
    posicao = None
    if codigo in numeros_existentes:
        for i in range(len(contas)):
            if posicao == None:
                conta = contas[i]
                if conta.numero == codigo:
                    posicao = i
        conta = ContaBancaria()
        conta.numero = codigo
        conta.titular = input("Digite o novo nome do titular da conta: ")
        conta.saldo = float(input("Digite o novo saldo titular da conta: "))
        contas[posicao] = conta
        print("...")
        time.sleep(1)
        print("Conta atualizada com sucesso!")



    else:
        print("Essa conta não existe.")
    
    time.sleep(3)
    main()

def excluirMenorSaldo():
    if len(contas) == 0:
        print("Não há contas cadastradas")
    else:
        posicaoMenorSaldo = 0
        menorSaldo = None
        for i in range(len(contas)):
            conta = contas[i]
            if menorSaldo == None:
                posicaoMenorSaldo = i
                menorSaldo = conta.saldo
            elif conta.saldo < menorSaldo:
                posicaoMenorSaldo = i
                menorSaldo = conta.saldo
        
        contaRemover = contas[posicaoMenorSaldo]
        print("."*30)
        print("Removendo a conta:")
        print("Número: ", contaRemover.numero)
        print("Titular: ", contaRemover.titular)
        print("Saldo: ", contaRemover.saldo)
        print("."*30)
        contas.remove(contaRemover)
    time.sleep(3)
    main()

def sair():
    print("Até mais")

def menu():
    print("."*30)
    print("1. Cadastrar contas")
    print("2. Visualizar todas as contas")
    print("3. Consultar por nome")
    print("4. Alterar nome e/ou saldo de um número de conta")
    print("5. Excluir a conta com menor saldo")
    print("6. Sair")
    print("."*30)
    return int(input("Digite a operação: "))

def main():
    operacao = menu()
    if operacao == 1:
        qtde = int(input("Digite a quantidade de contas que deseja cadastrar: "))
        cadastrarContas(qtde)
    elif operacao == 2:
        consultarContas()
    elif operacao == 3:
        if len(contas) != 0:
            titular = input("Digite o nome do titular da conta: ")
            consultarTitular(titular)
        else:
            print("Não há contas cadastradas")
            main()
    elif operacao == 4:
        alterarConta()
    elif operacao == 5:
        excluirMenorSaldo()
    elif operacao == 6:
        sair()

main()