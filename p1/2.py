"""

2. Não use nenhum método/função pronto da linguagem Python.
Desenvolva todas as funções a seguir:
a) Faça uma função com retorno (um valor no INSS calculado) e com parâmetro (um salario e alíquota de 9% do INSS) para calcular o imposto do INSS que é descontado de um funcionário.
b) Faça uma função com retorno (um salário líquido) e com parâmetro (um salario, um valor do INSS) que calcule o salário líquido de cada funionário.
c) Na função main() num laço de repetição, preencha um vetor de 10 funcionários. Em outro laço chame as outras funções (a e b) e apresente os salários orginais um por um, o valor que será desconto do INSS e salário líquido gerado.

"""


funcionarios = 10

# Esse percent = 9 indica que 
# Caso não seja passado ele como parametro ele receberá o valor padrão de 9%.
def calculaINSS(salario,percent=9):
  return  (salario*percent/100)

def calculaLiquido(salario, inss):
  return salario - inss

def main():
  salarios = []
  lista_inss = []
  salarios_liquidos = []
  for i in range(0, funcionarios):
    salario = float(input(f"Digite o salário do {i+1}° funcionario: "))
    valor_inss = calculaINSS(salario)
    liquido = calculaLiquido(salario,valor_inss)

    salarios.append(salario)
    lista_inss.append(valor_inss)
    salarios_liquidos.append(liquido)
    
  for i in range(0,funcionarios):
    print("."*15)
    print("Salário: ", salarios[i])
    print("Desconto INSS: ", lista_inss[i])
    print("Salário liquido: ", salarios_liquidos[i])
    print("."*15)
    print("")


main()