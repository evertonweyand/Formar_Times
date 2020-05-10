import random
class Time():
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.lista1 = []
        self.lista2 = []
        self.lista3 = []
        self.time_a = []
        self.time_b = []


    def separar_jogadores_por_nivel(self):
        """
        Separar os jogadores por nível (equivalência)
        """
        for jogador in self.jogadores:
            if jogador.nivel == 1:           # Bola cheia
                self.lista1.append(jogador)
            elif jogador.nivel == 2:         # Bola murcha
                self.lista2.append(jogador)
            else:
                self.lista3.append(jogador)  # Goleiros


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
        self.embaralhar_jogadores(self.lista1)
        self.embaralhar_jogadores(self.lista2)
        self.embaralhar_jogadores(self.lista3)


    def imprimir_lista(self, lista):
        for jogador in lista:
            print('  ', jogador.nome, 'Nível: ', jogador.nivel)


    def imprimir_times(self):
        self.separar_jogadores_por_nivel()
        self.formar_times()

        # Imprimir TimeA
        print(12 * '*')
        print('Time A:')
        self.imprimir_lista(self.time_a)

        print(12 * '*')

        # Imprimir TimeB
        print('Time B')
        self.imprimir_lista(self.time_b)
        print(12 * '*')
