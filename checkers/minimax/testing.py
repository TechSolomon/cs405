# Testing GitHub Copilot -- Checkers Minimax (2022-02-10)

class Board(object):
    """Board class."""
    def __init__(self):
        """Initialize board."""

class Piece(object):
    """Piece class."""
    def __init__(self, color, row, col):
        """Initialize piece."""
        self.color = color
        self.row = row
        self.col = col

class Game(object):
    """Game class."""
    def __init__(self, board, player):
        """Initialize game."""
        self.board = board
        self.player = player

    def get_score(self):
        """Return score of game."""
        return self.board.get_score()

class Player(object):
    """Player class."""
    def __init__(self, color):
        """Initialize player."""
        self.color = color

class Minimax(object):
    """Minimax class."""
    def __init__(self, board, player):
        """Initialize minimax."""
        self.board = board
        self.player = player

    def get_score(self):
        """Return score of board."""
        return self.board.get_score()

    def get_children(self):
        """Return list of children of board."""
        return self.board.get_children()

    def is_game_over(self):
        """Return True if game is over."""
        return self.board.is_game_over()

    def get_player(self):
        """Return player."""
        return self.player

    def get_board(self):
        """Return board."""
        return self.board

    def __str__(self):
        """Return string representation of board."""
        return str(self.board)

class MinimaxAI(object):
    """Minimax AI class."""
    def __init__(self, player):
        """Initialize minimax AI."""
        self.player = player

    def get_move(self, board):
        """Return move of minimax AI."""

# TODO: Build GUI Checkers Board
# 1. Create a class for the board.
# 2. Create a class for the pieces.
# 3. Create a class for the game.
# 4. Create a class for the player.
# 5. Create a class for the AI.
# 6. Create a class for the GUI.

# def minimax(board, depth, maximizing_player):
#     """Return best move for player."""
#     if depth == 0 or board.is_game_over():
#         return board.get_score()
#     if maximizing_player:
#         value = -float('inf')
#         for child in board.get_children():
#             value = max(value, minimax(child, depth - 1, False))
#         return value
#     else:
#         value = float('inf')
#         for child in board.get_children():
#             value = min(value, minimax(child, depth - 1, True))
#         return value
    
# def evaluate(board, maximizing_player):
#     """Board evaluation function."""
#     if board.is_game_over():
#         return board.get_score()
#     if maximizing_player:
#         value = -float('inf')
#         for child in board.get_children():
#             value = max(value, evaluate(child, False))
#         return value
#     else:
#         value = float('inf')
#         for child in board.get_children():
#             value = min(value, evaluate(child, True))
#         return value

def main():
    """Main function."""
    print("Testing Checkers Minimax.")

main()

# def pieces(self, player):
    #     pieces = []
    #     return pieces
    #
    # def moves(self, player):
    #     moves = []
    #     return moves

# def evaluation(match, player):
#     MYP = match.pieces[player]
#     NMYP = match.pieces[(player + 1) % 2]
#     MYK = match.kings[player]
#     NMYK = match.kings[(player + 1) % 2]
#     return MYP - NMYP + 0.5 * (MYK - NMYK)
#
#
# def minimax(match, depth, board, alpha=float('-inf'), beta=float('+inf')):
#     index = match.turn % 2
#     winner = match.check_winner()
#     if winner is not None:
#         if winner == match.players[board]:
#             return float('+inf'), None, []
#         elif winner == match.players[(board + 1) % 2]:
#             return float('-inf'), None, []
#         else:
#             return evaluation(match, board), None, []
#     elif depth == 0:
#         attempt = evaluation(match, board)
#         return attempt, None
#
#     elif board == index:
#         max_eval = float('-inf')
#         best_move = None
#         moves = match.get_valid_moves(match.players[index])
#         for move in moves:
#             new_game = copy.deepcopy(match)
#             new_game.play(match.players[index], move[0], move[1], move[2], True)
#             attempt = minimax(new_game, depth - 1, board, alpha, beta)[0]
#             max_eval = max(max_eval, attempt)
#             alpha = max(alpha, attempt)
#             if beta <= alpha:
#                 break
#             if max_eval == attempt:
#                 best_move = move
#         return max_eval, best_move
#
#     else:
#         min_eval = float('+inf')
#         best_move = None
#         moves = match.get_valid_moves(match.players[index])
#         for move in moves:
#             new_game = copy.deepcopy(match)
#             new_game.play(match.players[index], move[0], move[1], move[2], True)
#             attempt = minimax(new_game, depth - 1, board, alpha, beta)[0]
#             min_eval = min(min_eval, attempt)
#             beta = min(beta, attempt)
#             if beta <= alpha:
#                 break
#             if min_eval == attempt:
#                 best_move = move
#         return min_eval, best_move
