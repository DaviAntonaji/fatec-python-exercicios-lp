"""
7. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Função para construir um menu de opções para uma calculadora:

*** Minha Calculadora ***
Digite um número.....: 
Digite outro número..: 
    + Soma dois números
    - Subtrai dois números
    * Multiplica dois números
    / Divide dois números
Qual opção deseja? 
b) Desenvolva uma função para cada opção de cálculo, mas estas não terão retorno.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos caracteres do menu.

A função de desenho/construção do menu, chamará todas as outras passando a elas os valores digitados.

"""

def soma(n1,n2):
  print(f"A soma de {n1} e {n2} é {n1+n2}")

def subtrai(n1,n2):
  print(f"A subtração de {n1} e {n2} é {n1-n2}")

def multiplica(n1,n2):
  print(f"A multiplicação de {n1} e {n2} é {n1*n2}")

def divide(n1,n2):
  if n2 == 0:
    print(f"A divisão de {n1} e {n2} é invalida")
  else:
    print(f"A divisão de {n1} e {n2} é {n1/n2}")

def main():
  print("*** Minha Calculadora ***")
  
  n1 = float(input("Digite um número: "))
  n2 = float(input("Digite outro número: "))
  print("*"*25)
  print("+ Soma dois números")
  print("- Subtrai dois números")
  print("* Multiplica dois números")
  print("/ Divide dois números")
  print("*"*25)
  operacao = None
  possiveis = [None, "*", "-", "+", "/"]
  while operacao in possiveis:
    operacao = input("Digite a operação:")

    if operacao == "+":
      soma(n1,n2)
    elif operacao == "-":
      subtrai(n1,n2)
    elif operacao == "*":
      multiplica(n1,n2)
    elif operacao == "/":
      divide(n1,n2)
    else:
      print("Operação invalida.")

main()