import chess
import multiprocessing as mp
import threading
import ctypes

AUTHOR = ['Andy']
NAME = 'mt'


class Player:
    def __init__(self, color):
        self.color = color

    def play(self, board: chess.Board, result, local_timeout, global_timeout):
        move = select_best_move_ever(board)
        result.value = str(move)


def select_best_move_ever(board):
    value = float("-inf")
    chess_move = list(board.legal_moves)[0]
    pool = []
    for move in list(board.legal_moves):
        aux = board.copy()
        aux.push(move)
        result = [float("-inf")]#mp.Manager().Value(ctypes.c_void_p, float("-inf"))
        thread = threading.Thread(target=minmax, args=(aux, 1, False, result))
        pool.append((thread, result, move))
        thread.start()

    while pool.__len__() > 0:
        (thread, result, move) = pool.pop()
        if result[0] > value:
            thread.join(0.1)
            value = result[0]
            chess_move = move
        elif thread.is_alive():
            pool.append((thread, result, move))


    return chess_move


def minmax(board, depth, is_maximizing, result):
    if board.is_checkmate() or board.is_check():
        result[0] = 1000
    elif depth == 0:
        result[0] = evaluate(board)
    else:
        possibles = get_possible_boards(board)
        for valid_board in possibles:
            if is_maximizing:
                sub_res = [float("-inf")]#mp.Manager().Value(ctypes.c_void_p, float("-inf"))
                minmax(valid_board, depth - 1, False, sub_res)
                if sub_res[0] < result[0]:
                    result[0] = sub_res[0]
            else:
                sub_res = [float("inf")]#mp.Manager().Value(ctypes.c_void_p, float("inf"))
                minmax(valid_board, depth - 1, True, sub_res)
                if sub_res[0] > result[0]:
                    result[0] = sub_res[0]


def get_possible_boards(board):
    possibles = []
    for move in list(board.legal_moves):
        aux = board.copy()
        aux.push(move)
        possibles.append(aux)
    return possibles


def evaluate(board):
    text = board.fen().split()[0]
    return sum_pieces(text) + frontier(text)
    # return 0


def frontier(board):
    text = board.split('/')
    last_white = 1
    first_black = 7
    index = 0
    for row in text:
        if row.count("p") == 1:
            last_white = index
        if row.count("P") == 1:
            first_black = index
        index += 1
    return last_white / first_black


def sum_pieces(board):
    pawns = board.count("P") - board.count("p")
    rooks = board.count("R") - board.count("r")
    knights = board.count("N") - board.count("n")
    bishops = board.count("B") - board.count("b")
    queens = board.count("Q") - board.count("q")
    return pawns + 3 * (bishops + knights) + 5 * rooks + 9 * queens
