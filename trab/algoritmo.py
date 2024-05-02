# Iplementaçao do algorimo do Problema do turista de Manhattan

import numpy as np

'''
@param n: O número de linhas da grade.
@param m: O número de colunas da grade.
@param down: Uma matriz que representa os custos de mover para baixo em cada célula da grade.
@param right: Uma matriz que representa os custos de mover para a direita em cada célula da grade.

@return um valor que representa o menor custo total.
para percorrer o caminho do canto superior esquerdo ao canto inferior direito na grade.
'''
def ManhattanTour(n, m, down, right):

    '''
    cria uma matriz score de zeros com tamanho (n+1, m+1). 
    Essa matriz será utilizada para armazenar os custos acumulados para cada célula da grade.
    '''
    score = np.zeros([n+1, m+1])

    '''
    O loop percorre as linhas da grade (de 1 a n).
    e preenche a primeira coluna da matriz score. 
    Para cada linha i, o valor da célula (i, 0) é calculado como a soma do valor da célula acima ((i-1, 0))
    e do custo de mover para baixo na célula (i - 1, 0), armazenado em down[i - 1, 0].
    '''
    for i in range(1, n+1):
        score[i, 0] = score[i-1, 0] + down[i - 1, 0]

    '''
    O loop percorre as colunas da grade (de 1 a m).
    e preenche a primeira linha da matriz score. 
    Para cada coluna j, o valor da célula (0, j) é calculado como a soma do valor da célula à esquerda ((0, j-1))
    e do custo de mover para a direita na célula (0, j - 1), armazenado em right[0, j - 1].
    '''
    for j in range(1, m+1):
        score[0, j] = score[0, j-1] + right[0, j - 1]

    '''
    O loop percorre as linhas da grade (de 1 a n).
    O loop aninhado percorre as colunas da grade (de 1 a m).
    então preenche as células restantes da matriz score. 
    Para cada célula (i, j), o valor é calculado como o máximo entre:
    O valor da célula acima ((i - 1, j)) somado ao custo de mover para baixo na célula (i - 1, j), armazenado em `down[i - 1, j, e
    O valor da célula à esquerda ((i, j - 1)) somado ao custo de mover para a direita na célula (i, j - 1), armazenado em right[i, j - 1].
    '''
    for i in range(1, n+1):
        for j in range(1, m +1):
            score[i, j] = max(score[i - 1, j] + down[i - 1, j], score[i, j - 1] + right[i, j - 1])
    return score[n, m]

right = np.array([
    [3, 2, 4, 0],
    [3, 2, 4, 2],
    [0, 7, 3, 4],
    [3, 3, 0, 2],
    [1, 3, 2, 2]
])

down = np.array([
    [1, 0, 2, 4, 3],
    [4, 6, 5, 2, 1],  
    [4, 4, 5, 2, 1],
    [5, 6, 8, 5, 3]
])

# Esta entrada representa uma grade 5x5 

n = len(down)  # Tamanho da grade (linhas)
m = len(right[0])  # Tamanho da grade (colunas)

# Chamando a função ManhattanTour
score = ManhattanTour(n, m, down, right)

# O valor 'score' representa o menor custo total do caminho
print("Menor custo total:", score)