"""

8. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Função para construir um menu de opções para uma calculadora:

*** Minha Calculadora ***
Digite um número.....: 
Digite outro número..: 
    + Soma dois números
    - Subtrai dois números
    * Multiplica dois números
    / Divide dois números
Qual opção deseja? 
b) Desenvolva uma função para cada opção de cálculo.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos caracteres do menu.

A função de desenho/construção do menu, chamará todas as outras passando a elas os valores digitados.

"""


def soma(n1,n2):
  return n1+n2

def subtrai(n1,n2):
  return n1-n2

def multiplica(n1,n2):
  return n1*n2

def divide(n1,n2):
  if n2 == 0:
    return "invalida"
  else:
    return n1/n2

def main():
  print("*** Minha Calculadora ***")
  operacao = None
  possiveis = [None, "*", "-", "+", "/"]
  while operacao in possiveis:
    print("*"*25)
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    print("*"*25)
    print("+ Soma dois números")
    print("- Subtrai dois números")
    print("* Multiplica dois números")
    print("/ Divide dois números")
    print("*"*25)
    operacao = input("Digite a operação:")

    if operacao == "+":
      print(f"A soma destes 2 números é {soma(n1,n2)}")
    elif operacao == "-":
      print(f"A subtração destes 2 números é {subtrai(n1,n2)}")
    elif operacao == "*":
      print(f"A multiplicação destes 2 números é {multiplica(n1,n2)}")
    elif operacao == "/":
      print(f"A divisão destes 2 números é {divide(n1,n2)}")
    else:
      print("Operação invalida. Encerrando programa")

main()