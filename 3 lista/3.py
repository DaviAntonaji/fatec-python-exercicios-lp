# 3. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia a base e a altura de um triângulo e retorne/apresente sua área A = (base x altura)/2.

def calcula():
  altura = float(input("Digite a altura do triangulo: "))
  base = float(input("Digite a base do triangulo: "))

  return (base*altura)/2

def main():
  calculo = calcula()
  print(f"O valor da área deste triangulo é de: {calculo}")

main()