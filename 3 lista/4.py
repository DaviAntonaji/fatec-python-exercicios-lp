# 4. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia o lado de um quadrado e retorne sua área, area = lado².
def quadrado():
  lado = float(input("Digite o lado do quadrado: "))
  return lado * lado

def main():
  area = quadrado()
  print(f"O valor da área deste quadrado é de {area}")

main()