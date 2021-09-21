"""
1. (Função sem retorno sem parâmetro) Faça um programa contendo uma função/método que apresente o valor 1 se o número digitado for positivo e 0 se for negativo.
"""

def funcao():
  numero = int(input("Digite um número: "))
  if numero >= 0:
    print(1)
  else:
    print(0)

def main():
  funcao()
  
main()