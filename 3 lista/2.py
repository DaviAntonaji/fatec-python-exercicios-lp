# 2. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método para subtrair dois números, retornar o resultado e o apresentando.

def subtrai():
  numero1 = int(input("Digite um número inteiro: "))
  numero2 = int(input("Digite outro número inteiro: "))
  return numero1-numero2

def main():
  
  subtracao = subtrai()
  print(f"O primeiro número menos o segundo é {subtracao}")

main()