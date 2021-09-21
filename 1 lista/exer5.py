"""
5. (Função sem retorno sem parâmetro) Faça uma função/método que receba o preço antigo e atual de um produto, determine o percentual de acréscimo entre esses valores e apresente-o.
"""
def calcula():
  preco_antigo = float(input("Digite o preço antigo: "))
  preco_novo  = float(input("Digite o preço novo: "))
  r = "{:.2f}".format(((100 * preco_novo - 100 * preco_antigo) / preco_antigo))
  print(f"O porcentual de aumento é: {r}%")
def main():
  calcula()

main()