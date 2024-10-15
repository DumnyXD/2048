# board.py
import random

class Board:
    def __init__(self):
        self.size = 4
        self.tiles = [[0] * self.size for _ in range(self.size)]
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        """Adiciona um novo número (2 ou 4) em uma posição vazia aleatória"""
        empty_tiles = [(i, j) for i in range(self.size) for j in range(self.size) if self.tiles[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            self.tiles[i][j] = 2 if random.random() < 0.9 else 4

    def compress(self):
        """Move todos os blocos para a esquerda, mantendo a ordem"""
        new_tiles = [[0] * self.size for _ in range(self.size)]
        moved = False
        for i in range(self.size):
            position = 0
            for j in range(self.size):
                if self.tiles[i][j] != 0:
                    new_tiles[i][position] = self.tiles[i][j]
                    if j != position:
                        moved = True
                    position += 1
        self.tiles = new_tiles
        return moved

    def merge(self):
        """Combina blocos adjacentes iguais e move para a esquerda"""
        moved = False
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.tiles[i][j] == self.tiles[i][j + 1] and self.tiles[i][j] != 0:
                    self.tiles[i][j] *= 2
                    self.tiles[i][j + 1] = 0
                    moved = True
        return moved

    def reverse(self):
        """Inverte as linhas do tabuleiro (para suportar movimentação à direita)"""
        for i in range(self.size):
            self.tiles[i].reverse()

    def transpose(self):
        """Transpõe a matriz do tabuleiro (para suportar movimentação para cima e para baixo)"""
        self.tiles = [list(row) for row in zip(*self.tiles)]

    def move(self, direction):
        """Realiza o movimento no tabuleiro e adiciona um novo bloco"""
        moved = False

        if direction == 'left':
            moved = self.compress()
            merged = self.merge()
            self.compress()
            if merged or moved:
                self.add_random_tile()

        elif direction == 'right':
            self.reverse()
            moved = self.compress()
            merged = self.merge()
            self.compress()
            self.reverse()
            if merged or moved:
                self.add_random_tile()

        elif direction == 'up':
            self.transpose()
            moved = self.compress()
            merged = self.merge()
            self.compress()
            self.transpose()
            if merged or moved:
                self.add_random_tile()

        elif direction == 'down':
            self.transpose()
            self.reverse()
            moved = self.compress()
            merged = self.merge()
            self.compress()
            self.reverse()
            self.transpose()
            if merged or moved:
                self.add_random_tile()

    def get_tiles(self):
        return self.tiles

    def can_move(self):
        """Verifica se há movimentos disponíveis"""
        # Verificar se há blocos vazios
        for row in self.tiles:
            if 0 in row:
                return True

        # Verificar se há blocos adjacentes iguais (horizontalmente)
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.tiles[i][j] == self.tiles[i][j + 1]:
                    return True

        # Verificar se há blocos adjacentes iguais (verticalmente)
        for i in range(self.size - 1):
            for j in range(self.size):
                if self.tiles[i][j] == self.tiles[i + 1][j]:
                    return True

        return False
