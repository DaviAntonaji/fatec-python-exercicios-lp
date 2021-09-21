# 1. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia um número e o multiplique por 2 retornando o resultado e o apresente.

def multiplica():
  numero = int(input("Digite um número inteiro: "))
  return numero*2

def main():
  
  multiplicacao = multiplica()
  print(f"Este número multiplicado por 2 é {multiplicacao}")

main()