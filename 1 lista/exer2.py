""" 2. (Função sem retorno sem parâmetro) Faça uma função/método que leia dois valores positivos e apresente a soma dos N números existentes entre eles (inclusive). 
    Exemplo: 
        a = 2
        b = 8
       soma = 35
"""
def funcao():
  numero1 = float(input("Digite o 1° número: "))
  numero2 = float(input("Digite o 2° número: "))
  soma = 0
  for i in range(numero1,numero2+1):
    soma+=i
  print(f"A soma destes números é: {soma}")

def main():
  funcao()
  
main()