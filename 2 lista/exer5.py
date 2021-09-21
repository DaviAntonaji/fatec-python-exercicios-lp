"""
5. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um valor inicial e um valor final realizar o acumulo desse valores e apresentar o resultado. Não use vetor.
    Exemplo:
        a = 2
        b = 8
        2 + 3 + 4 + 5 + 6 + 7 + 8 = 35
        r = 35
"""

def acumulo(inicio,fim):
  r = 0
  string = ""
  for i in range(inicio, fim + 1):
    string += str(i) + " +"
    r += i
  string = string[:-1]
  string = string + "= " + str(r)
  print()
  print(string)

def main():
  inicio = int(input("Digite o valor inicial: "))
  fim = int(input("Digite o valor final: "))
  acumulo(inicio,fim)

main()
