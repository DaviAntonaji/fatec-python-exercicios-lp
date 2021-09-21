"""
5. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento e um salário via parâmetro, aplique este aumento ao salário do funcionário. Na parte principal do programa, na chamada da função, utilize um laço de repetição para ler 10 salários, chame a função para aplicar o aumento e gerar o novo salário, ainda dentro da estrutura de repetição acumule os novos salários e ao final apresente quanto será gasto no novo salário. Também apresente qual será a diferença entre o que se pagava para todos os funcionário e o que será pago após o aumento.
"""



def novoSalario(salario, porcentagem):
  return salario + (salario*porcentagem/100)

def main():
  salariosAntigos = []
  salariosNovos = []
  totalDiferenca = 0
  porcentagem = float(input("Digite a porcentagem adicional: "))
  for i in range(0,10):
    salario = float(input(f"Digite o salario do {i+1}° funcionario: "))
    salariosAntigos.append(salario)
    
    new_salario = novoSalario(salario,porcentagem)
    salariosNovos.append(new_salario)
    totalDiferenca += new_salario - salario
  print("*"*25)
  print("Os salarios antigos eram:", salariosAntigos)
  print("Os salarios novos são: ", salariosNovos)
  print("Foi acrescentado o custo total de R$",totalDiferenca)
  

main()