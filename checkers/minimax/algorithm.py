# algorithm.py
# Solomon Himelbloom
# 2022-02-10
# Testing Minimax for CS 405.

class Board:
    """Example board class."""

    def __init__(self, board, player):
        """Initialize board."""
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


# TODO: Add Minimax [eventually with alpha-beta pruning].
# 1. Generate ony moves (no jumps).
# 2. More testing with several patterns (correct output).
# 3. Add single jumps.
# 4. Try minimax again (with single jumps).
# 5. Full minimax from B-0.
# 6. Add kings + piece count 1.5 testing.
# 7. Play game with minimax (depth = 8).
# 8. Multiple jumps (2+ pieces); update piece count.
# 9. Iterative deepening search (IDS) --> depth = 1.

def minimax(board, player, depth):
    """Inplementation of minimax algorithm."""
    if depth == 0 or Board.is_game_over():
        return Board.get_score()
    if player:
        value = -1
        for child in Board.get_children():
            value = max(value, minimax(child, False, depth - 1))
        return value
    else:
        value = 1
        for child in Board.get_children():
            value = min(value, minimax(child, True, depth - 1))
        return value


def evaluate(node, maximizing_player):
    """Board evaluation function."""
    if node.is_game_over():
        return node.get_score()
    if maximizing_player:
        value = -1
        for child in node.get_children():
            value = max(value, evaluate(child, False))
        return value
    else:
        value = 1
        for child in node.get_children():
            value = min(value, evaluate(child, True))
        return value


# Main function
def main():
    print("UAF CS 405 - HW2 (Searching)")

    ply = 1  # FIXME: Starting depth of search tree.

    board = Board(156, True)

    # move = minimax(board, True, ply)

    print(">> Evaluating Minimax with depth = {}.".format(ply))


main()


# function  minimax(node, depth, maximizingPlayer) is
#     if depth = 0 or node is a terminal node then
#         return the heuristic value of node
#     if maximizingPlayer then
#         value := −∞
#         for each child of node do
#             value := max(value, minimax(child, depth − 1, FALSE))
#         return value
#     else (* minimizing player *)
#         value := +∞
#         for each child of node do
#             value := min(value, minimax(child, depth − 1, TRUE))
#         return value

