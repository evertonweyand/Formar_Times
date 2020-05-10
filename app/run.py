from jogador import Jogador
from equipe import Equipe


"""
Cria uma lista vazia para adicionar os jogadores
"""
jogadores = []
"""
Criar a lista com todos os jogadores.
Depois esta lista virá do banco de dados.
"""
for x in range(10):
    if x > 7:
        nivel = 3 # Os jogadores 7 e 8 serão os 2 goleiros
    elif x % 2 == 0:
        nivel = 1 # Os jogadores pares serão de nível 1, bola cheia
    else:
        nivel = 2 # Os jogadores ímpares serão de nível 2, bola murcha

    jogadores.append(Jogador('Jogador {} '.format(x), nivel, 'S'))

equipes = Equipe(jogadores)
equipes.imprimir_times()
