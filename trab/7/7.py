import time
import matplotlib.pyplot as plt
#####################################################
def particao_de_conjunto(conjunto, tamanho_subconjunto):
  if len(conjunto) < tamanho_subconjunto:
    return []
  if len(conjunto) == tamanho_subconjunto:
    return [[conjunto]]
  else:
    particoes_restantes = particao_de_conjunto(conjunto[1:], tamanho_subconjunto)
    particoes_com_primeiro_elemento = []
    for particao in particoes_restantes:
      for elemento in conjunto[:1]:
        nova_particao = [[elemento]] + particao
        particoes_com_primeiro_elemento.append(nova_particao)
    return particoes_restantes + particoes_com_primeiro_elemento

#####################################################
tmLista = []
tmExecu = []
lista = []

for i in range(8):
    tmLista.append(i)

for n in tmLista:
    for i in range(n):
        lista.append(i)
    
    inicio = time.perf_counter()
    particao_de_conjunto(lista,n)
    fim = time.perf_counter()

    tempo_execucao = fim - inicio
    tmExecu.append(tempo_execucao)
    print("Tamanho:",n,"Tempo de execução:", tempo_execucao, "segundos")

# Dados
x = tmLista
y = tmExecu

# Criar o gráfico
plt.plot(x, y)

# Personalizar o gráfico
plt.xlabel("Tamanho")
plt.ylabel("Tempo")
plt.title("Meu Gráfico")

# Exibir o gráfico
plt.show()
'''

'''