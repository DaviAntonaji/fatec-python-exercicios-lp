### 2. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método para subtrair dois números e apresentar o resultado.

def subtrai(a,b):
  print(f"O valor de {a} - {b} é {a-b}")

def main():
  a =  int(input("Digite o valor de A: "))
  b =  int(input("Digite o valor de B: "))
  subtrai(a,b)

main()