### 9. (Função sem retorno com parâmetro) Faça uma função/método para verificar se um nome digitado é igual a ‘Ana’, mostre o valor True ou False como resposta.

def verificaAna(nome):
  if nome.lower() == "ana":
    print("True")
  else:
    print("False")

def main():
  nome = input("Digite o nome: ")
  verificaAna(nome)

main()