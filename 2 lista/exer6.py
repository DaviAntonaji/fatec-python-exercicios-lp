### 6. (Função sem retorno com parâmetro) Faça uma função/método para calcular a tabuada de um número informado pelo usuário.

def tabuada(numero):
  for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")

def main():
  numero = int(input("Digite o número que deseja ver a tabuada: "))
  tabuada(numero)

main()
