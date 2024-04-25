def particao_de_conjunto(conjunto, tamanho_subconjunto):
  """
  Calcula todas as partições do conjunto 'conjunto' em subconjuntos de tamanho 'tamanho_subconjunto'.

  Args:
      conjunto: Conjunto de elementos.
      tamanho_subconjunto: Tamanho do subconjunto desejado.

  Returns:
      Lista de todas as partições.
  """
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

# Exemplo de uso
conjunto = [1, 2, 3]
particoes_de_2 = particao_de_conjunto(conjunto, 2)
print(particoes_de_2)