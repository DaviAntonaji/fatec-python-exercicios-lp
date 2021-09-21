"""

9. (Função com retorno sem parâmetro) Foi realizada uma pesquisa sobre algumas características físicas de cinco habitantes de uma região. Foram coletados os seguintes dados de cada habitante: idade, sexo (M - masculino ou F - feminino), cor dos olhos (A - azuis ou C - castanhos), cor dos cabelos (L - louros, P - pretos ou C - castanhos).
Faça uma função/método que leia esses dados, armazenando-os em vetores (listas);
Faça uma função/método que determine e devolva a função principal a média de idades das pessoas com olhos castanhos e cabelos pretos;
Faça uma função/método que determine e devolva a função principal a maior idade entre os habitantes;
Faça uma função/método que determine e devolva a função principal a quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos(inclusive) e que tenham olhos azuis e cabelos louros.

"""


idade = []
sexo = []
olho = []
cabelo = []

def cadastrar():
    for i in range(1, 6):
        idade.append(int(input(f"Digite a idade do {i}º participante: ")))
        sexo.append(input(f"Digite o sexo do {i}º participante [M - masculino / F - feminino]: ").upper().strip()[0])
        olho.append(input(f"Digite a cor dos olhos do {i}º participante [A - azuis / C - castanhos]: ").upper().strip()[0])
        cabelo.append(input(f"Digite a cor dos cabelos do {i}º participante [L - louros / P - pretos / C - castanhos]: ").upper().strip()[0])
        print()

def media():
    idade_pc = [idade[i] for i in range(len(idade)) if cabelo[i] == "P" and olho[i] == "C"]
    return sum(idade_pc) / len(idade_pc)

def maior():
    maior_idade = [idade[i] for i in range(len(idade)) if idade[i] > i]
    return max(maior_idade)

def criterio():
    feminino = [i for i in range(len(idade)) if idade[i] >= 18 if idade[i] <= 35 if cabelo[i] == "L" if olho[i] == "A"]
    return len(feminino)

def main():
    cadastrar()
    print(f'A média de idade de pessoas com olhos castanhos e cabelos pretos é de {media()} anos')
    print(f'A maior idade entre os habitantes é de {maior()} anos')
    print(f'A quantidade de mulheres loiras de olhos azuis, entre 18 e 35 anos de idade, é de {criterio()} mulheres.')

main()