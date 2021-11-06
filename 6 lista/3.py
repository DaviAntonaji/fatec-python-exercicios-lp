"""
3. Elabore uma estrutura para representar e armazenar 10 alunos (matricula, nome, telefone). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura. Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.
Menu de opções:

Cadastrar alunos
Visualizar todos os dados
Sair

"""


from tabulate import tabulate

class Aluno:
    matricula:int
    nome:str
    telefone:str


def cadastrarAlunos():
    try:
        # Tente abrir o arquivo e contar o tanto de produtos já cadastrados
        with open("alunos3.txt", "r", encoding="utf-8") as file:
            totalAlunosCadastrados =  len(file.readlines())
    except:
        # Se não existir, defina como 0
        totalAlunosCadastrados = 0

    desejaCadastrar = True
    while desejaCadastrar:


        if totalAlunosCadastrados == 10:
            print("Você chegou ao limite de cadastros.")
            desejaCadastrar = False

        with open("alunos3.txt", "a+", encoding="utf-8") as file:
            aluno =  Aluno()
            aluno.matricula = int(input("Digite a matricula do aluno: "))
            aluno.nome = input("Digite o nome do aluno: ")
            aluno.telefone = input("Digite o telefone do aluno:  ")

            file.write(str(aluno.matricula) + "|" + aluno.nome + "|" + str(aluno.telefone) + "\n")

        totalAlunosCadastrados += 1

            

        resposta = input("Deseja cadastrar mais um aluno? (S/N)").lower()
        if resposta != "s":
            desejaCadastrar = False
    menu()


def visualizarAlunos():
    try:
        with open("alunos3.txt", "r", encoding="utf-8") as file:
        
            # Tenta abrir o arquivo:
            tabela = []
            for line in file.readlines():
                dados = line.split("|")
                aluno = Aluno()
                aluno.matricula = dados[0]
                aluno.nome = dados[1]
                aluno.telefone = dados[2]
                tabela.append([aluno.matricula,aluno.nome,aluno.telefone])

            print(tabulate(tabela, headers=["Matricula", "Nome", "Telefone"]))
            menu()
                
               
    except:
        # Se o arquivo não existir
     
        menu()

def menu():
    print("#"*30)
    print("1. Cadastrar alunos")
    print("2. Visualizar todos os dados")
    print("3. Sair")
    print("#"*30)
    operacao = input("Digite a operação: ")
    if operacao in ["1", "2", "3"]:
        operacao = int(operacao)
        if operacao ==  1:
            cadastrarAlunos()
        elif operacao == 2:
            visualizarAlunos()
        elif operacao == 3:
            exit("Aplicação encerrada")
    else:
        print("Operação invalida!")
        menu()


def main():
    
        
    menu()

main()