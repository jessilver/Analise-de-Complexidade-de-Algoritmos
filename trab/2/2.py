import time
import matplotlib.pyplot as plt
#####################################################
def busca_binaria(elemento, lista_ordenada):
  inicio = 0
  fim = len(lista_ordenada) - 1

  while inicio <= fim:
    meio = (inicio + fim) // 2
    valor_meio = lista_ordenada[meio]

    if valor_meio == elemento:
      return meio
    elif valor_meio < elemento:
      inicio = meio + 1
    else:
      fim = meio - 1

  return -1  # Elemento não encontrado
#####################################################
tmLista = []
tmExecu = []
lista = []

for i in range(500):
    tmLista.append(i*10)

for n in tmLista:
    for i in range(n):
        lista.append(1)
    indice = n // 2
    inicio = time.perf_counter()
    busca_binaria(indice, lista)
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
