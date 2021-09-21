### 7. (Função sem retorno com parâmetro) Faça uma função/método que calcule a média de um aluno que realizou duas provas (P1 e P2), a partir desta média, chame/crie OUTRA função que verifique se esta média aprova ou reprova o aluno.

def verificaAprovado(media):
  if media < 6:
    print("Com esta média o aluno está reprovado")
  else:
    print("Com esta média o aluno está aprovado")
  print("-"*40)
def calculaMedia(p1,p2):
  media = (p1 + p2) / 2
  print("-"*40)
  print(f"A média deste aluno é {media}")
  verificaAprovado(media)

def main():
  print("-"*40)
  print("Calculo de média de aluno:")
  print()
  p1 = float(input("Digite a nota da P1: "))
  p2 = float(input("Digite a nota da P2: "))
  calculaMedia(p1,p2)

main()

