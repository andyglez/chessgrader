""" Plantilla para crear un nuevo jugador.
"""
import chess

AUTHOR = ['Autor 0', 'Autor 1']
NAME = 'Plantilla'


class Player:
    def __init__(self, color):
        self.color = color

    def play(self, board: chess.Board, result, local_timeout, global_timeout):
        # Este jugador siempre juega la primera jugada válida que encuentre
        result.value = str(next(iter(board.legal_moves)))