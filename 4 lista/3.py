# 3. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento via parâmetro, aplique este aumento a um salário de um funcionário, retorne e apresente o novo salário.

def novoSalario(salario, porcentagem):
  return salario + (salario*porcentagem/100)

def main():
  salario = float(input("Digite o salario: "))
  porcentagem = float(input("Digite a porcentagem adicional: "))
  new_salario = novoSalario(salario,porcentagem)
  print("O novo salario é R$", new_salario)

main()