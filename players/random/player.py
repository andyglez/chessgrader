"""
    Jugador Aleatorio

    Su estrategia es elemental, en cada paso escoge de forma aleatoria una jugada en el conjunto de jugadas válidas.

    Nota: La implementación del agente debe poderse acceder de la forma

        players.module_name.player.Player

    Donde `module_name` es el nombre designado por los desarrolladores.
    En el caso de este agente `module_name = random`
"""
import random

#
# python-chess library
#
# Esta es la biblioteca empleada para manejar la lógica del juego
# Pueden acceder a ella en: https://github.com/niklasf/python-chess
# Se recomienda que exploren todas las funcionalidades que ofrece,
# dado que facilita enormemente el diseño de estrategias.
#
import chess

AUTHOR = ['Singularity']  # Nombre de los autores
NAME = 'Random'  # Nombre del jugador (cada autor puede presentar más de un jugador)


class Player:
    def __init__(self, color):
        """
        color -> Denota el color de las piezas del jugador.

        >>> color in (chess.WHITE, chess.BLACK)
        ... True
        """
        self.color = color

    def play(self, board: chess.Board, result, local_timeout, global_tiemout):
        """
        Esta función será invocada cada vez que el jugador deba realizar una acción.
        La respuesta debe ser guardada en `result.value` como un string.
        Para más información leer la implementación debajo.

        El valor almacenado en `result.value` será interpretada como la solución.
        Si ocurre algún error durante la ejecución de esta función se da por terminado el juego
        con una derrota para el jugador actual.

        Tiempo: El jugador tiene `global_timeout` segundos para todo el juego más `local_timeout`
        segundos de bono por cada jugada. Por tanto la jugada actual puede tomarse a lo sumo
        `local_timeout + global_timeout` segundos, en caso de que se tome más tiempo se da por
        terminado el juego con una derrota para el jugador actual.

        board: Estado actual del tablero.

        >>> type(board)
        ... chess.Board
        """
        legal_moves = list(board.legal_moves)
        move = random.choice(legal_moves)
        result.value = str(move)
