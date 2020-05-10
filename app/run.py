import random
from app.jogador import Jogador
from app.time import Time

jogadores = []
"""
Criar a lista com todos os jogadores, depois esta lista virá do banco de dados.
"""
for x in range(10):
    if x > 7:
        nivel = 3
    elif x % 2 == 0:
        nivel = 1
    else:
        nivel = 2

    jogadores.append(Jogador('Everton {} '.format(x), nivel, 'S'))

times = Time(jogadores)
times.imprimir_times()
