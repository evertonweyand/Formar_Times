import random
from model.equipe import Equipe

class EquipeController():
    def __init__(self, jogadores):
        self.equipe_model = Equipe(jogadores)
        self.bola_cheia  = []
        self.bola_murcha = []
        self.goleiros    = []
        self.time_a      = []
        self.time_b      = []        


    def separar_jogadores_por_nivel(self):
        """
        Separar os jogadores por nível (equivalência)
        """
        for jogador in self.equipe_model.jogadores:
            if jogador.nivel == 1:           # Bola cheia
                self.bola_cheia.append(jogador)
            elif jogador.nivel == 2:         # Bola murcha
                self.bola_murcha.append(jogador)
            else:
                self.goleiros.append(jogador)  # Goleiros


    def embaralhar_jogadores(self, lista):
        """
        Embaralhar as lista de jogadores e dividir no Time_A e Time_B
        """
        random.shuffle(lista)
        x = 0
        for jogador in lista:
            x += 1
            if x % 2 == 0:
                self.time_a.append(jogador)
            else:
                self.time_b.append(jogador)


    def formar_times(self):
        """
        Embaralhar as lista de jogadores e dividir no Time_A e Time_B
        """
        self.embaralhar_jogadores(self.bola_cheia)
        self.embaralhar_jogadores(self.bola_murcha)
        self.embaralhar_jogadores(self.goleiros)


    def imprimir_lista(self, lista):
        for jogador in lista:
            qtdeEspacos = 20 - len(jogador.nome)
            espacos = qtdeEspacos * ' ';
            print('*   ', jogador.nome, espacos, 'Nível: ', jogador.nivel, ' *')


    def imprimir_times(self):
        self.separar_jogadores_por_nivel()
        self.formar_times()

        # Imprimir TimeA
        print(39 * '*')
        print('* Time A:                             *')
        self.imprimir_lista(self.time_a)

        print(39 * '*')

        # Imprimir TimeB
        print('* Time B:                             *')
        self.imprimir_lista(self.time_b)
        print(39 * '*')
