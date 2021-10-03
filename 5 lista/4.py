"""

Uma escola precisa montar o cadastro geral de seus alunos. Este cadastro deverá conter as seguintes informações por aluno: nome completo, data de nascimento, telefone, endereço e série atual. Levando em conta que esta escola possui no máximo 500 alunos, como você faria para estruturar estas informações num sistema de gerenciamento para a escola? Implemente utilizando estrutura. Também use a criação de funções para cada operação. Use o menu a seguir:
Menu de opções:

1; Cadastrar alunos
2. Consulta por nome
3. Visualizar todos os dados
4. Sair


"""

alunos = []


class Aluno:
    nome = ""
    telefone = ""
    endereco = ""
    serie = ""


def menu():
    print()
    print("."*30)
    print("1. Cadastrar alunos")
    print("2. Consulta por nome")
    print("3. Visualizar todos os dados")
    print("4. Sair")
    print("."*30)
    return int(input("Digite sua operação: "))


def sair():
    print("Adeus")


def buscaAluno():
    nome = input("Digite o nome do aluno que deseja buscar:")
    achei = False
    for aluno in alunos:

        if achei == False:
            if aluno.nome.lower() == nome.lower():
                print("."*30)
                print("Achei o aluno:")
                print("O nome dele é: ", aluno.nome)
                print("O telefone dele é: ", aluno.telefone)
                print("O endereço dele é: ", aluno.endereco)
                print("A série dele é: ", aluno.serie)
                print("."*30)
                achei = True

    if achei == False:
        print("Não encontrei esse aluno...")
    main()


def cadastraAlunos():
    qtdeAlunos = int(input("Digite quantos alunos deseja cadastrar: "))
    if len(alunos) + qtdeAlunos > 500:
        print("O limite de alunos dessa escola é 500, você ainda pode cadastrar: ", 500-len(alunos), "alunos")
    else:

        for i in range(qtdeAlunos):
            aluno = Aluno()
            aluno.nome = input(f"Digite o nome do {i+1}° aluno: ")
            aluno.telefone = input(f"Digite o telefone do {i+1}° aluno: ")
            aluno.endereco = input(f"Digite o endereço do {i+1}° aluno: ")
            aluno.serie = input(f"Digite a série do {i+1}° aluno: ")
            alunos.append(aluno)
        main()


    def listaAlunos():
        for aluno in alunos:
            print("."*30)
            print("Aluno: ", aluno.nome)
            print("O telefone dele é: ", aluno.telefone)
            print("O endereço dele é: ", aluno.endereco)
            print("A série dele é: ", aluno.serie)
            print("."*30)
        main()


def main():

    operacao = menu()
    print()
    if operacao == 1:
        cadastraAlunos()

    elif operacao == 2:
        buscaAluno()

    elif operacao == 3:
        listaAlunos()

    elif operacao == 4:
        sair()


main()
