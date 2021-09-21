"""
6. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Função para construir um menu de opções para uma calculadora:

Menu de cálculos
1.   Número ao quadrado
2.   Número ao cubo
3.   Raiz do número
4.   Raiz cúbica do número
Qual é a opção desejada?
b) Desenvolva uma função para cada opção de cálculo.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos números do menu.

A função de desenho/construção do menu, esta chamará todas as outras passando a elas o valor digitado.
"""


def quadrado(n1):
  return n1**2

def cubo(n1):
  return n1**3

def rquadrada(n1):
  return n1 ** (1/2)

def rcubica(n1):
  return n1 ** (1/3)

def main():
  print("*** Minha Calculadora ***")
  operacao = None
  possiveis = [None, "1", "2", "3", "4"]
  while operacao in possiveis:
    print("*"*25)
    n1 = float(input("Digite um número: "))
    print("*"*25)
    print("1.   Número ao quadrado")
    print("2.   Número ao cubo")
    print("3.   Raiz do número")
    print("4.   Raiz cúbica do número")
    print("*"*25)
    operacao = input("Digite a operação:")

    if operacao == "1":
      print(f"Este número ao quadrado é: {quadrado(n1)}")
    elif operacao == "2":
      print(f"Este número ao cubo é: {cubo(n1)}")
    elif operacao == "3":
      print(f"A raiz quadradada do número é: {rquadrada(n1)}")
    elif operacao == "4":
      print(f"A raiz cubica do número é: {rcubica(n1)}")
    else:
      print("Operação invalida. Encerrando programa")

main()