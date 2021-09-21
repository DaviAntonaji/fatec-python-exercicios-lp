"""
7. (Função sem retorno sem parâmetro) Faça uma função/método que leia três notas de um aluno e uma letra, se a letra for igual a *A*, deverá calcular a média aritimética das notas dos alunos, se for *P*, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média deve ser mostrada ao final.
N1, N2 e N3 são notas.
P1, P2 e P3 são pesos.

 Média ponderada = (N1 * P1 + N2 * P2 + N3 * P3 ) / (P1 + P2 + P3)
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