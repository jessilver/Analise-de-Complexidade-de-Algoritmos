import time
import matplotlib.pyplot as plt
#####################################################
def todas_sublistas_soma_3(lista):
  sublistas = []
  for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
      for k in range(j + 1, len(lista)):
        if lista[i] + lista[j] + lista[k] == 3:
          sublistas.append([lista[i], lista[j], lista[k]])
  return sublistas
#####################################################
tmLista = []
tmExecu = []
lista = []

for i in range(25):
    tmLista.append(i)

for n in tmLista:
    for i in range(n):
        lista.append(1)
    
    inicio = time.perf_counter()
    todas_sublistas_soma_3(lista)
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
