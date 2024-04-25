import time
import matplotlib.pyplot as plt
#####################################################
def ordenacao_merge_sort(lista):
  if len(lista) <= 1:
    return lista

  meio = len(lista) // 2
  esquerda = ordenacao_merge_sort(lista[:meio])
  direita = ordenacao_merge_sort(lista[meio:])

  return merge(esquerda, direita)

def merge(esquerda, direita):
  resultado = []
  i = 0
  j = 0
  while i < len(esquerda) and j < len(direita):
    if esquerda[i] <= direita[j]:
      resultado.append(esquerda[i])
      i += 1
    else:
      resultado.append(direita[j])
      j += 1

  resultado += esquerda[i:]
  resultado += direita[j:]
  return resultado
#####################################################
tmLista = []
tmExecu = []
lista = []

for i in range(150):
    tmLista.append(i*10)

for n in tmLista:
    for i in range(n):
        lista.append(1)
    
    inicio = time.perf_counter()
    ordenacao_merge_sort(lista)
    fim = time.perf_counter()

    tempo_execucao = fim - inicio
    tmExecu.append(tempo_execucao)
    #print("Tamanho:",n,"Tempo de execução:", tempo_execucao, "segundos")

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
