"""

6. Uma empresa prestadora de serviços armazena informações sobre os serviços prestados. Sabe-se que a empresa pode realizar no máximo três serviços diariamente. É de interesse de sua direção manter um histórico mensal (30 dias) sobre os serviços prestados.
A empresa realiza quatro tipos de serviços:

1) pintura;

2) jardinagem;

3) faxina e

4) reforma em geral.

Cada serviço realizado deve ser cadastrado com as seguintes informações: número do serviço, valor do serviço, código do serviço e código do cliente, numa matriz 30x3 referente a estrutura Servico_prestado.

Cadastre/digite os quatro tipos de serviços (código e descrição) que a empresa poderá realizar. Para isso, utilize um vetor de quatro posições referente a estrutura Tipo_servico. O programa deverá mostrar o seguinte menu de opções:

Cadastrar os tipos de serviços
Mostrar todos os tipos de serviço
Cadastrar os serviços prestados
Mostrar todos os serviços prestados
Mostrar os serviços prestados em determinado dia
Mostrar os serviços prestados dentro de um intervalo de valor
Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço
Sair
Para a opção 1: deve-se cadastrar os tipos de serviços oferecidos pela empresa, com código e descrição.

Para a opção 3: deve-se considerar que deverão ser cadastrados os serviços prestados ao logo do mês. Em cada dia podem ser cadastrados, no máximo, três serviços prestados.

Utilize uma matriz capaz de armazenar em cada posição todas as informações referentes a um serviço prestado (número, valor, código do serviço, código do cliente). Cada linha representa um dia do mês. Dessa maneira, considere a matriz com dimensão 30 × 3.

Solicite o dia em que o serviço foi prestado e as demais informações. Lembre-se de que a empresa só pode prestar os serviços que já tenham sido cadastrados no vetor de tipo de serviços.

Caso o usuário digite um código de tipo de serviço inválido, o programa deverá mostrar uma mensagem de erro.

Quando o usuário tentar cadastrar mais de três serviços prestados em um mesmo dia, também deverá mostrar uma mensagem de erro.

Para a opção 5: o programa deverá receber o dia que se deseja consultar e mostrar os respectivos serviços prestados.

Para a opção 6: o programa deverá receber o valor mínimo e o valor máximo e mostrar os serviços prestados que estiverem nesse intervalo.

Para a opção 7: o programa deverá mostrar todos os serviços prestados, conforme o exemplo a seguir.

              DIA 01
No do serviço	Valor do serviço R$	Código do serviço	Descrição	Código do cliente
100	200,00	1	Pintura	1
150	100,00	3	Faxina	5
201	640,00	4	Reforma em geral	2
              DIA 02
No do serviço	Valor do serviço R$	Código do serviço	Descrição	Código do cliente
301	600,00	4	Reforma em geral	3
280	352,00	1	Pintura	2
306	200,00	2	Jardinagem	1



"""
import time
from tabulate import tabulate

tipo_servico = []
servicos = []
for i in range(0,31):
    servicos.insert(i, [])
# --- #
# Estruturas
# --- #

class TipoServico:
    codigo:int
    nome:str

class Servico:
    numero_servico:int
    valor_servico:float
    codigo_servico:int
    codigo_cliente:int

# --- #
# Fim das Estruturas
# --- #

    
# --- #
# Funções de filtro
# --- #

def pegaTipo(codigo):
    return [tipo for tipo in tipo_servico if tipo.codigo == codigo][0].nome

def pegaServicosDia(dia):
    return servicos[dia-1]

# --- #
# Fim das Funções de filtro
# --- #

# --- #
# Operações
# --- #

def cadastrar_tipos():
    
    print("Começando a cadastrar\n")
    tipo = TipoServico()
    tipo.codigo = 1
    tipo.nome = "Pintura"
    tipo_servico.append(tipo)
    print("Pintura cadastrada...\n")
    
    tipo = TipoServico()
    tipo.codigo = 2
    tipo.nome = "Jardinagem"
    tipo_servico.append(tipo)
    print("Jardinagem cadastrada...\n")

    tipo = TipoServico()
    tipo.codigo = 3
    tipo.nome = "Faxina"
    tipo_servico.append(tipo)
    print("Faxina cadastrada...\n")

    tipo = TipoServico()
    tipo.codigo = 4
    tipo.nome = "Reforma em geral"
    tipo_servico.append(tipo)
    print("Reforma em geral cadastrada...\n")
    print("Concluindo... Aguarde")
    time.sleep(3)
    menu()

def consultar_tipos():
    if tipo_servico == []:
        print("Não há serviços cadastrados")
        
    else:
        for tipo in tipo_servico:
            print("."*30)
            print("Código: " + str(tipo.codigo))
            print("Nome: " + tipo.nome)
            print("."*30)
    time.sleep(2)
    menu()

def cadastra_servico():
    if tipo_servico == []:
        print("Não há tipos de serviço.")
        time.sleep(2)
        menu()
    else:
        desejaCadastrar = True
        while desejaCadastrar == True:

            dia = int(input("Digite o dia de serviço: "))

            if len(servicos[dia-1]) < 3:

                servico = Servico()
                servico.numero_servico = int(input("Digite o número do serviço: "))
                servico.valor_servico = float(input("Digite o valor do serviço: "))
                servico.codigo_servico = int(input("Digite o código do tipo de serviço: "))
                servico.codigo_cliente = int(input("Digite o código do cliente: "))
                servicos[dia-1].append(servico)
            
            else:
                print("Já á três serviços nesse dia.")

            resposta = input("Deseja cadastrar mais um serviço prestado? (S/N): ")
            if resposta.lower() == "s":
                desejaCadastrar = True
            else:
                desejaCadastrar = False
            
        time.sleep(2)
        menu()


def consultar_tudo():

    contador = 0
    dados = []
    for dia in servicos:
        print("*"*30)
        contador+=1
        
        if dia != []:
            
            
            for servico in dia:
              
       
                dados.append([contador, str(servico.numero_servico), str(servico.valor_servico), str(servico.codigo_servico), pegaTipo(servico.codigo_servico), str(servico.codigo_cliente)])
        

    print(tabulate(dados, headers=["Dia", "No de serviço", "Valor do serviço R$", "Código de serviço", "Descrição", "Código de cliente"]))
    menu()





def consultar_preco():

    valor_inicial = float(input("Digite o valor inicial: "))
    valor_final = float(input("Digite o valor final: "))
    contador = 0
    dados = []
    for dia in servicos:
        print("*"*30)
        contador+=1
        print("Dia:", contador)
        
        if dia != []:
            
            print("DIA: ", contador)
            for servico in dia:
              
                if servico.valor_servico >= valor_inicial and servico.valor_servico <= valor_final:
                    dados.append([contador, str(servico.numero_servico), str(servico.valor_servico), str(servico.codigo_servico), pegaTipo(servico.codigo_servico), str(servico.codigo_cliente)])
        

    print(tabulate(dados, headers=["Dia", "No de serviço", "Valor do serviço R$", "Código de serviço", "Descrição", "Código de cliente"]))
    menu()

def relatorio_geral():

    contador = 0
    for dia in servicos:
        print("*"*30)
        contador+=1
        print("Dia:", contador)

        if dia != []:
            dados = []
            print("DIA: ", contador)
            for servico in dia:
              
       
                dados.append([str(servico.numero_servico), str(servico.valor_servico), str(servico.codigo_servico), pegaTipo(servico.codigo_servico), str(servico.codigo_cliente)])
        

            print(tabulate(dados, headers=["No de serviço", "Valor do serviço R$", "Código de serviço", "Descrição", "Código de cliente"]))
        else:
            print("Neste dia não há serviços.")
         


        print("*"*30)
    if len(servicos) == 0:
        print("Não há serviços cadastrados...")
    time.sleep(2)
    menu()

def consulta_dia():
    data = int(input("Digite a dia que deseja consultar : "))
    vetor = pegaServicosDia(data)
    
    print()
    dados = []
    for servico in vetor:
   
     
        dados.append([str(servico.numero_servico), str(servico.valor_servico), str(servico.codigo_servico), pegaTipo(servico.codigo_servico), str(servico.codigo_cliente)])
        

    print(tabulate(dados, headers=["No de serviço", "Valor do serviço R$", "Código de serviço", "Descrição", "Código de cliente"]))
       



    if len(vetor) == 0:
        print("Não há serviços cadastrados nesse dia...")
    print("*"*30)
    time.sleep(2)
    menu()
        


# --- #
# Fim das Operações
# --- #

def menu():
    print("#" + "-"*30 + "#")
    print(" "*14 + "Menu" + " "*14)
    print("1. Cadastrar os tipos de serviços")
    print("2. Mostrar todos os tipos de serviço")
    print("3. Cadastrar os serviços prestados")
    print("4. Mostrar todos os serviços prestados")
    print("5. Mostrar os serviços prestados em determinado dia")
    print("6. Mostrar os serviços prestados dentro de um intervalo de valor")
    print("7. Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço")
    print("8. Sair")
    print("#" + "-"*30 + "#")
    operacao = input("Digite a operação: ")
    possiveis = ["1", "2", "3", "4", "5", "6", "7", "8"]
    if operacao in possiveis:
        if operacao == "1":
            cadastrar_tipos()
        elif operacao == "2":
            consultar_tipos()
        elif operacao == "3":
            cadastra_servico()
        elif operacao == "4":
            consultar_tudo()
        elif operacao == "5":
            consulta_dia()
        elif operacao == "6":
            consultar_preco()
        elif operacao == "7":
            relatorio_geral()
        elif operacao == "8":
            print("Saindo...")
            time.sleep(2)
            exit("Aplicação encerrada!")
    else:
        print("Operação invalida!")
        menu()

def main():
    menu()

main()
