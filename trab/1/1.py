import time
import matplotlib.pyplot as plt
#####################################################
def acesso_constante(indice, lista):
  return lista[indice]
#####################################################
tmLista = []
tmExecu = []
lista = []

for i in range(1000):
    tmLista.append(i*10)

for n in tmLista:
    if n == 0:n=1
    for i in range(n):
        lista.append(1)

    indice = n // 2
    inicio = time.perf_counter()
    acesso_constante(indice, lista)
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
