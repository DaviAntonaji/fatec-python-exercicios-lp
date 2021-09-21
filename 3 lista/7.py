"""
7. (Função com retorno sem parâmetro) Faça uma função/método que leia e armazene 5 elementos inteiros no vetor A, deverá ser gerado um vetor B, de mesmo tamanho, que armazenará o fatorial de cada elemento de A. Não use função pronta de cálculo de fatorial. Retorne/apresente o vetor B.
"""
def armazena():
  vetorA = []
  vetorB = []
  for i in range(0,5):
    numero = int(input(f"Digite o {i+1}° número inteiro: "))
    vetorA.append(numero)
    fatorial = 1
    for j in range(1,numero+1):
      fatorial*=j
    vetorB.append(fatorial)
  return vetorB

def main():
  vetorB = armazena()
  print("O vetor B é igual a: ", vetorB)

main()