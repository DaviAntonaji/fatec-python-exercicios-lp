# 1. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba por parâmetro um número e o multiplique por 2, retorne e apresente o resultado da função.

def multiplica(numero1):
  return numero1*2

def main():
  n1 = float(input("Digite um número: "))
  multiplicacao = multiplica(n1,n2)
  print(f"A multiplicação desses números é {multiplicacao}")

main()