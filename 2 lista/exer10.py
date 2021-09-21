### 10. (Função sem retorno com parâmetro) Faça uma função/método para verificar e contar quantas letras **a** tem numa frase. Não use NENHUMA função pronta da linguagem Python.

def verificaLetras(texto):
  totalA = 0
  for letra in texto:
    if letra in ["a", "A"]:
      totalA += 1
  print(f"O total de letras A é {totalA}")

def main():
  texto = input("Digite um texto: \n")
  verificaLetras(texto)

main()
