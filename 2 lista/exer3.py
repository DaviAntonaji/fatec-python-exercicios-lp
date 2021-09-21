### 3. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em 9%.

def reajusta(preco):
  reajuste = preco + (preco * 9 / 100)
  reajuste = "{:.2f}".format(reajuste)
  print(f"O preço do produto reajustado é de: R$ {reajuste}")

def main():
  preco = float(input("Digite o preço do produto: R$ "))
  reajusta(preco)

main()