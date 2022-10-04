### 1. Para fazer o cadastro em uma rede social, o usuário deve preencher vários dados, inclusive um e-mail válido, ou seja, um e-mail deve conter UM caracter arroba '@' e UM ou MAIS caracteres ponto '.'
### Crie uma função que retorne como resposta, se um e-mail é 'válido' ou 'inválido'. Não use nenhum método/função pronto ou o operador in no if, da linguagem Python. Avalie caracter por caracter. Deve ser criada a função main para chamar a da verificação.


def verificaEmail(email):
  totalArroba = 0
  totalPonto = 0
  for i in range(0,len(email)):
    letra = email[i]
    if letra == ".":
      totalPonto+=1
    elif letra == "@":
      totalArroba+=1
  if totalArroba == 1 and totalPonto >= 1:
    return True
  else:
    return False

def main():
  email = input("Digite seu e-mail: ")
  if verificaEmail(email):
    print("Esse e-mail é VALIDO")
  else:
    print("Esse e-mail é INVALIDO")
main()