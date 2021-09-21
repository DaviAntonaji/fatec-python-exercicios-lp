"""

8. (Função com retorno sem parâmetro) Faça uma função/método retorne um vetor com os três primeiros números perfeitos. Sabe-se que um número é perfeito quando é igual a soma de seus divisores (exceto ele mesmo).
Exemplo: os divisores de 6 são 1, 2 e 3, e 1 + 2 + 3 = 6, logo 6 é perfeito. Não use função pronta.

1º número perfeito: 6

2º número perfeito: 28

3º número perfeito: 496

"""

def pegaPerfeitos():
  perfeitos = []
  Max = 497
  for Number in range(1, Max):
    Sum = 0
    for i in range(1,Number):
      if (Number%i==0):
        Sum +=i
   
    if Sum == Number:
      perfeitos.append(Number)

  return perfeitos


def main():
  perfeitos = pegaPerfeitos()
  print("Os 3 primeiros numeros perfeitos são:", perfeitos)

main()