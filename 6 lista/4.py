"""
 Baixe o arquivo futebol.txt que esta na pasta Material do aula do Teams. Leia este arquivo e o apresente. Com os dados lidos, armazene na estrutura Futebol (posicao_jogo, altura, peso, imc), calcule o IMC (Índice de Massa Corporal), armazene na estrutura e também em outro arquivo, mas agora chamado futebol_imc.txt. Apresente este novo arquivo.
Observação: esse exercício deve ser testado fora do Colab, no Idle ou qualquer outra IDE, porque usará um arquivo que estará na pasta material de aula do Teams.
"""

from tabulate import tabulate

class Futebol:
    posicao:str
    altura:float
    peso:float
    imc:float
    classificacao:str

def consulta():
    with open("futebol.txt", "r", encoding="utf-8") as file:
        tabela = []
        i = 0
        for line in file.readlines():
            i+=1
            dados = line.split(",")
            futebol = Futebol

            futebol.posicao = dados[0]
            futebol.altura = float(dados[1])
            futebol.peso = float(dados[2])
            futebol.imc = futebol.peso / (futebol.altura ** 2)
            if futebol.imc < 18.5:
                futebol.classificacao = "Abaixo do peso"
            elif futebol.imc >= 18.5 and futebol.imc <= 24.9:
                futebol.classificacao = "Peso normal"
            elif futebol.imc >= 25 and futebol.imc <= 29.9:
                futebol.classificacao = "Sobrepeso"
            elif futebol.imc >= 30:
                futebol.classificacao = "Obesidade"
            
            with open("futebol4.txt", "a+", encoding="utf-8") as newfile:
                newfile.write(str(futebol.posicao) + ","+ str(futebol.altura) + "," + str(futebol.peso) + "," + str(futebol.imc) + "," + futebol.classificacao + "\n")

            tabela.append([i, futebol.posicao,futebol.altura,futebol.peso,futebol.imc, futebol.classificacao])
        print(tabulate(tabela, headers=["Jogador", "Posição", "Altura", "Peso", "IMC", "Classificação"]))


def main():
    consulta()

main()