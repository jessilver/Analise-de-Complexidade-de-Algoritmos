import time
import matplotlib.pyplot as plt
#####################################################
def encontrar_pares(lista):
  pares = []
  for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
      pares.append((lista[i], lista[j]))
  return pares
#####################################################
tmLista = []
tmExecu = []
lista = []

for i in range(25):
    tmLista.append(i*10)

for n in tmLista:
    for i in range(n):
        lista.append(1)
    
    inicio = time.perf_counter()
    encontrar_pares(lista)
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
