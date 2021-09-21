# 4. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba duas notas (P1, P2) calcule a média, chame outra função na main que avalie se este aluno esta aprovado ou reprovado retornando a str/string 'Aprovado' ou 'Reprovado'.

def verificaAprovado(media):
  if media < 6:
    return "Reprovado"
  else:
    return "Aprovado"

def calculaMedia(n1, n2):
  return (n1+n2)/2

def main():
  nota1 = float(input("Digite a nota da P1: "))
  nota2 = float(input("Digite a nota da P2: "))
  media = calculaMedia(nota1,nota2)
  aprovado = verificaAprovado(media)  
  print(f"Com a media {media} o aluno foi {aprovado}")

main()