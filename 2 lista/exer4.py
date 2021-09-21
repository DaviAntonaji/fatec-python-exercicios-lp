### 4. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em alguma porcentagem que deve ser informada (digitada) pelo usuário.

def reajusta(preco, porcentagem):
  reajuste = preco + (preco * porcentagem / 100)
  reajuste = "{:.2f}".format(reajuste)
  print(f"O preço do produto reajustado é de: R$ {reajuste}")

def main():
  preco = float(input("Digite o preço do produto: R$ "))
  porcentagem = float(input("Digite a porcentagem de reajuste: "))
  reajusta(preco, porcentagem)

main()