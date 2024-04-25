def acesso_constante(indice, lista):
  return lista[indice]
######################################################
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
######################################################
def soma_elementos(lista):
  soma = 0
  for elemento in lista:
    soma += elemento
  return soma
######################################################
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
def encontrar_pares(lista):
  pares = []
  for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
      pares.append((lista[i], lista[j]))
  return pares
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
def potencia_recursiva(base, expoente):
  if expoente == 0:
    return 1
  else:
    return base * potencia_recursiva(base, expoente - 1)
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
