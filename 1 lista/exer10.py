"""

10. (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro e positivo N e mostre o valor de S, obtido pelo seguinte cálculo:
S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
Observação: Não pode usar vetor e função pronta da linguagem Python.

"""


def pegaMedia():
  print("-"*20)
  notas = []
  for i in range(0,3):
    notas.append(float(input(f"Digite a {i+1}° nota: ")))

  print("-"*20)
  print("A = Aritimetica | P = Ponderada")
  tipoMedia = input("Digite o tipo da média que deseja:")
  if tipoMedia == "A" or tipoMedia == "a":
    media = "{:.2f}".format(sum(notas) / len(notas))
    print("-"*20)
    print(f"A média aritimética dessas notas são: {media}")
  elif tipoMedia == "P" or tipoMedia == "p":
    pesos = []
    for i in range(0,3):
      pesos.append(float(input(f"Digite o {i+1}° peso: ")))
    media = 0
    for i in range(0,3):
      media += notas[i] * pesos[i]

    media /= sum(pesos)
    media = "{:.2f}".format(media)
    print("-"*20)
    print(f"A média ponderada dessas notas são: {media}")
  else:
    print("Tipo de média invalida...")
    pegaMedia()
def main():
  pegaMedia()

main()