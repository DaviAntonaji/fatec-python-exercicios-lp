"""
8. (Função sem retorno sem parâmetro) Faça uma função/método que leia uma hora de início e de término de um jogo, ambas divididas em dois valores distintos: hora e minuto. Deverá ser apresentado a duração expressa em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que ele pode começar em um dia e terminar no outro.
    se m_f < m_i
        m_f = m_f + 60
        h_f = h_f - 1
    se h_f < h_i
        h_f = h_f + 24
    tot_m = m_f - m_i
    tot_h = h_f - h_i
    total = tot_h * 60 + tot_m 
"""

def calcula():
  h_i = int(input("Digite a hora inicial: "))
  m_i = int(input("Digite o minuto inicial: "))
  h_f = int(input("Digite a hora inicial: "))
  m_f = int(input("Digite o minuto final: "))
  if m_f < m_i:
    m_f = m_f + 60
    h_f = h_f - 1
  if h_f < h_i:
      h_f = h_f + 24
  tot_m = m_f - m_i
  tot_h = h_f - h_i
  total = tot_h * 60 + tot_m
  if total >= 60:
    horas = int(total/60)
    minutos = int(total%60)
    if minutos == 0:
      print(f"O periodo jogado é de {horas} horas")
    else:
      print(f"O periodo jogado é de {horas} horas e {minutos} minutos")
  else:
    print(f"O periodo jogado é de {total} minutos")

def main():
  calcula()
main()