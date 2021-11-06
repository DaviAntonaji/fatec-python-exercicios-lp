"""
 Baixe o arquivo futebol.txt que esta na pasta Material do aula do Teams. Leia este arquivo e o apresente. Com os dados lidos, armazene na estrutura Futebol (posicao_jogo, altura, peso, imc), calcule o IMC (Índice de Massa Corporal), armazene na estrutura e também em outro arquivo, mas agora chamado futebol_imc.txt. Apresente este novo arquivo.
Observação: esse exercício deve ser testado fora do Colab, no Idle ou qualquer outra IDE, porque usará um arquivo que estará na pasta material de aula do Teams.
"""

from tabulate import tabulate

def consulta():
    with open("futebol.txt", "r", encoding="utf-8") as file:
        tabela = []
        i = 0
        for line in file.readlines():
            i+=1
            dados = line.split(",")

            posicao = dados[0]
            altura = float(dados[1])
            peso = float(dados[2])
            imc = peso / (altura ** 2)
            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif imc >= 18.5 and imc <= 24.9:
                classificacao = "Peso normal"
            elif imc >= 25 and imc <= 29.9:
                classificacao = "Sobrepeso"
            elif imc >= 30:
                classificacao = "Obesidade"
            
            with open("futebol4.txt", "a+", encoding="utf-8") as newfile:
                newfile.write(str(posicao) + ","+ str(altura) + "," + str(peso) + "," + str(imc) + "," + classificacao + "\n")

            tabela.append([i, posicao,altura,peso,imc, classificacao])
        print(tabulate(tabela, headers=["Jogador", "Posição", "Altura", "Peso", "IMC", "Classificação"]))


def main():
    consulta()

main()