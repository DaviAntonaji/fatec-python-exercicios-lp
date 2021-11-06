"""
Elabore uma estrutura para representar e armazenar 10 produtos (código, nome, preço). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura.
"""


class Tipo_Produto:
    codigo = 0
    nome = ''
    preco = 0.0

arq_produto = open('produto1.txt','w')
for i in range(10):
    tp = Tipo_Produto()
    tp.codigo = int(input('Informe o código do produto: '))
    tp.nome = input('Informe o nome do produto: ')
    tp.preco = float(input('Informe o preço do produto: '))
    arq_produto.write(f'{tp.codigo},{tp.nome},{tp.preco:.2f}\n')
arq_produto.close()

arq_produto = open('produto1.txt','r')
for x in arq_produto.readlines():
    c,n,p = x.strip().split(',')
    print(c,'\t\t',n,'\t\t',p)
arq_produto.close()