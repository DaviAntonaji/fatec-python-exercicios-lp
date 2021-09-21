# 2. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba dois números via parâmetro, some os dois valores, retorne e apresente o resultado.

def somar(numero1,numero2):
  return numero1+numero2

def main():
  n1 = float(input("Digite um número: "))
  n2 = float(input("Digite outro número: "))
  soma = somar(n1,n2)
  print(f"A soma desses números é {soma}")

main()