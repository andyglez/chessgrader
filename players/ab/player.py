import chess

AUTHOR = ['Andy']
NAME = 'ab'

class Player:
    def __init__(self, color):
        self.color = color
    def play(self, board: chess.Board, result, local_timeout, global_timeout):
        move = select_best_move_ever(board)
        result.value = str(move)

def select_best_move_ever(board):
    value = float("-inf")
    chess_move = list(board.legal_moves)[0]
    for move in list(board.legal_moves):
        aux = board.copy()
        aux.push(move)
        v = minmax(aux, 2, False, 1, 0)
        if v > value:
            value = v
            chess_move = move
    return chess_move


def minmax(board, depth, is_maximizing, alpha, beta):
    if depth == 0:
        return evaluate(board)
    
    possibles = get_possible_boards(board)
    value = float("-inf") if is_maximizing else float("inf")
    for valid_board in possibles:
        if is_maximizing:
            value = max(value, minmax(valid_board, depth - 1, False, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        else:
            value = min(value, minmax(valid_board, depth - 1, True, alpha, beta))
            if value <= alpha:
                return value
            beta = min(beta, value)
    return value

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
    #return 0

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