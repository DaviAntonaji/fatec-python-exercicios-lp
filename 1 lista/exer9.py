"""
9. (Função sem retorno sem parâmetro) Faça uma função/método que leia cinco valores inteiros, determine e mostre o maior e o menor deles. Não pode usar vetor e função pronta da linguagem Python.
"""
def pegaMaiorMenor():
  maior = None
  menor = None
  for i in range(0,5):
    numero = input(f"Digite o valor do {i+1}° número: ")
    if maior == None:
      maior = numero
    if menor == None:
      menor = numero
    if numero < menor:
      menor = numero
    elif numero > maior:
      maior = numero
  
  print("-"*20)
  print(f"O maior número é {maior}")
  print(f"O menor número é {menor}")
def main():
  pegaMaiorMenor()
main()
