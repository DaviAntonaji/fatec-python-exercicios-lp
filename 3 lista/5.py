# 5. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que verifique se um número é par, retorne mostrando a str/string ‘É par’ ou se ‘É ímpar’.

def verifica():
  numero = int(input("Digite um número inteiro: "))
  if numero%2 == 0:
    return "par"
  else:
    return "ímpar"

def main():
  tipo = verifica()
  print(f"Este número é {tipo}")

main()