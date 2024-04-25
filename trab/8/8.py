import time
import matplotlib.pyplot as plt
#####################################################
def permutacoes(lista):
  if len(lista) == 0:
    return [[]]
  else:
    primeiro_elemento = lista[0]
    permutacoes_restantes = permutacoes(lista[1:])
    permutacoes_finais = []
    for permutacao in permutacoes_restantes:
      for i in range(len(permutacao) + 1):
        nova_permutacao = permutacao[:i] + [primeiro_elemento] + permutacao[i:]
        permutacoes_finais.append(nova_permutacao)
    return permutacoes_finais
#####################################################
tmLista = []
tmExecu = []
lista = []

for i in range(5):
    tmLista.append(i)

for n in tmLista:
    for i in range(n):
        lista.append(1)
    
    inicio = time.perf_counter()
    permutacoes(lista)
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
Tamanho: 0 Tempo de execução: 2.00001522898674e-06 segundos
Tamanho: 1 Tempo de execução: 8.499948307871819e-06 segundos
Tamanho: 2 Tempo de execução: 1.2200092896819115e-05 segundos
Tamanho: 3 Tempo de execução: 0.017168600112199783 segundos
Tamanho: 4 Tempo de execução: 4.384967900114134 segundos
'''