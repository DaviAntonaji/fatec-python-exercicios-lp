"""
6. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que verifique se um número é par, retorne/mostre o valor bool True para par e False para ímpar.
"""

def verifica():
  numero = int(input("Digite um número inteiro: "))
  if numero%2 == 0:
    return True
  else:
    return False

def main():
  par = verifica()
  print(f"Este número é par? {par}")

main()