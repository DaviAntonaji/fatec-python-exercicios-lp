""" 
3. (Função sem retorno sem parâmetro) Faça uma função/método que receba três números inteiros a, b, c que sejam divisíveis por a. O valores b e c representam o intervalo da estrutura de repetição. Apresente a quantidade e os números divisíveis. Não pode usar vetor e função pronta da linguagem Python.

"""        
def funcao():
  print("-"*20)
  a = int(input("Digite o valor de A: "))
  if a == 0:
    print("O valor de A não pode ser 0.")
    funcao()
  else:
    b = int(input("Digite o valor de B: "))
    if b%a == 0:
      c = int(input("Digite o valor de C: "))
      if c%a == 0:
        print("-"*20)
        divisiveis = 0
        ndivisiveis = 0
        total = 0
        for i in range(b,c+1):
          total+=1
          if i % a == 0:
            print(f"O número {i} é divisivel por {a}")
            divisiveis += 1
          else:
            print(f"O número {i} não é divisivel por {a}")
            ndivisiveis +=1
        print()
        print(f"O total de números testados é: {total}")
        print(f"O total de números divisiveis é: {divisiveis}")
        print(f"O total de números não divisiveis é: {ndivisiveis}")
      else:
        print("C não é divisivel por A.")
        funcao()
    else:
      print("B não é divisivel por A.")
      funcao()

def main():
  funcao()
  
main()