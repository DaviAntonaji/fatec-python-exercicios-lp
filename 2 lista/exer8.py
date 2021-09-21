### 8. (Função sem retorno com parâmetro) Faça uma função/método sem parâmetro, para ler um valor e chamar/criar OUTRA função (com parâmetro) que mostre se o valor é par ou ímpar.

def verificaPar(numero):
  if numero % 2 == 0:
    print("Este número é par.")
  else:
    print("Este número é impar.")

def main():
  numero = int(input("Digite um número: "))
  verificaPar(numero)

main()