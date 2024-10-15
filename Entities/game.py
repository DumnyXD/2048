# game.py
from Entities.board import Board

class Game:
    def __init__(self):
        self.board = Board()

    def move(self, direction):
        """Recebe o movimento ('left', 'right', 'up', 'down') e atualiza o tabuleiro"""
        valid_directions = ['left', 'right', 'up', 'down']

        if direction in valid_directions:
            self.board.move(direction)

    def get_board(self):
        """Retorna o estado atual do tabuleiro"""
        return self.board.get_tiles()

    def is_game_over(self):
        """Verifica se o jogo terminou"""
        return not self.board.can_move()
