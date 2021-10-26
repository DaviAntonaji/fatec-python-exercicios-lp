import time

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

            if len(servicos[dia]) < 3:

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


def consulta_todos():

    contador = 0
    for dia in servicos:
        print("*"*30)
        contador+=1
        print("Dia:", contador)

        if dia != []:
        
            for servico in dia:
                
                print("-"*10)
                print("Número de serviço: ", servico.numero_servico)
                print("Valor de serviço: R$", "{:.2f}".format(servico.valor_servico))
                print("Código de serviço: ", servico.codigo_servico)
                print("Tipo de serviço: ", pegaTipo(servico.codigo_servico))
                print("Código de cliente: ", servico.codigo_cliente)
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
    
    
    for servico in vetor:

        print("*"*30)
        print("Número de serviço: ", servico.numero_servico)
        print("Valor de serviço: R$", "{:.2f}".format(servico.valor_servico))
        print("Código de serviço: ", servico.codigo_servico)
        print("Tipo de serviço: ", pegaTipo(servico.codigo_servico))
        print("Código de cliente: ", servico.codigo_cliente)



        print("*"*30)



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
            consulta_todos()
        elif operacao == "5":
            consulta_dia()
  
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
