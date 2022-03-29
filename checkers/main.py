# main.py
# Solomon Himelbloom
# 2022-01-18
#
# For CS 405 Spring 2022

import copy
import pygame
import time

from mechanics.match import Match
# from mcts.search import MCTS
from mechanics.variables import BOARD_SIZE, FPS, GRAY, SEARCH_TIME


# TODO:
# - Log game output to file
# - Require piece capture on relevant moves
# - Step through each move in the game
# - Continue working on MiniMax & MCTS (Alpha-Beta pruning)

def evaluate(game, maximizing_player):
    """Board evaluation function for the AI player."""

    # FIXME: If a piece is available, take it.
    if game.piece_selection is None:
        return 0

    return game.pieces[maximizing_player] - game.pieces[(maximizing_player + 1) % 2] + 0.5 * (
            game.kings[maximizing_player] - game.kings[(maximizing_player + 1) % 2])


def minimax(match, depth, maximizing_player_index, alpha=float('-inf'), beta=float('inf')):
    """Minimax algorithm with alpha-beta pruning."""
    player_index = match.turn % 2
    winner = match.winning_heuristic()
    if winner is not None:
        if winner == match.players[maximizing_player_index]:
            return float('+inf'), None, []
        elif winner == match.players[(maximizing_player_index + 1) % 2]:
            return float('-inf'), None, []
        else:
            return evaluate(match, maximizing_player_index), None, []
    elif depth == 0:
        assessment = evaluate(match, maximizing_player_index)
        return assessment, None

    elif maximizing_player_index == player_index:
        max_eval = float('-inf')
        best_move = None
        moves = match.move_collection(match.players[player_index])
        for move in moves:
            new_game = copy.deepcopy(match)
            new_game.mechanics(match.players[player_index], move[0], move[1], move[2], True)
            assessment = minimax(new_game, depth - 1, maximizing_player_index, alpha, beta)[0]
            max_eval = max(max_eval, assessment)
            alpha = max(alpha, assessment)
            if beta <= alpha:
                break
            if max_eval == assessment:
                best_move = move
        return max_eval, best_move

    else:
        min_eval = float('+inf')
        best_move = None
        moves = match.move_collection(match.players[player_index])
        for move in moves:
            new_game = copy.deepcopy(match)
            new_game.mechanics(match.players[player_index], move[0], move[1], move[2], True)
            assessment = minimax(new_game, depth - 1, maximizing_player_index, alpha, beta)[0]
            min_eval = min(min_eval, assessment)
            beta = min(beta, assessment)
            if beta <= alpha:
                break
            if min_eval == assessment:
                best_move = move
        return min_eval, best_move


# Implement MCTS
def monte_carlo(match, param, maximizing_player_index, search_time):
    """Monte Carlo tree search algorithm."""

    # Pause for the allotted time
    time.sleep(SEARCH_TIME[1])

    # FIXME: Initialize root node (from external class)

    player_index = match.turn % 2
    winner = match.winning_heuristic()

    if winner is not None:
        if winner == match.players[maximizing_player_index]:
            return float('+inf'), None, []
        elif winner == match.players[(maximizing_player_index + 1) % 2]:
            return float('-inf'), None, []
        else:
            return evaluate(match, maximizing_player_index), None, []
    elif param == 0:
        assessment = evaluate(match, maximizing_player_index)
        return assessment, None

    # TODO: Implement MCTS algorithm from search.py class (MCTS)
    # 1. Selection
    # 2. Expansion
    # 3. Simulation
    # 4. Backpropagation


# Save the final game state to a text file
def output_log(match):
    """Output the final game state to a text file."""
    moves = []

    # Get the moves of the game
    for player in match.players:
        moves.append(player.moves)
    with open('final_state.txt', 'a') as f:
        f.write(str(moves) + '\n')
        f.write(str(match.winner) + '\n')
        f.write(str(match.winning_heuristic()) + '\n')
        # Output the final board position to a text file
        f.write(str(match.board) + '\n')
    f.close()

    print("🎮 Game State [Moves]: " + str(moves))
    print("🏆 Winner: " + str(match.winner))
    print("🧠 Winning Heuristic: " + str(match.winning_heuristic()))
    print("✅ Final Board State: " + str(match.board))

    return moves + [match.winner] + [match.winning_heuristic()] + [match.board]


def gui_display():
    """Display the checkers board."""
    print("🚀 Launched Checkers [GUI]")

    # Match Properties
    pygame.init()
    window = pygame.display.set_mode(BOARD_SIZE)
    pygame.display.set_caption('🎲 CS 405: Checkers')

    # Match Beginning
    match = Match()
    completed = False
    clock = pygame.time.Clock()

    # Player 1 - MiniMax
    minimax_active = False
    minimax_depth = 8
    alternate_player = 0

    # Player 2 - MCTS
    mcts_active = False
    mcts_simulations = FPS
    mcts_time_limit = SEARCH_TIME[4]

    while not completed:
        if match.turn % 2 == alternate_player and minimax_active:
            assess, best = minimax(match, minimax_depth, alternate_player)
            print(f'⏳ Attempt Evaluation: {assess}')
            print(f'🧠 Ideal Move: {best}')

            winner = match.winning_heuristic()
            if winner is not None:
                print(f'🏆 Winner: {winner}')
                # FIXME: Save the final board position to a text file
                with open('log.txt', 'a') as f:
                    f.write(str(match.grid()) + '\n')
                f.close()

                completed = True
            else:
                match.mechanics(match.players[match.turn % 2], best[0], best[1], best[2], True)
                print('Score', match.pieces, "\tKings", match.kings, '\n')

        if mcts_active:
            # assess, best = monte_carlo(match, mcts_simulations, alternate_player, mcts_time_limit)
            # print(f'⏳ Attempt Evaluation: {assess}')
            # print(f'🧠 Ideal Move: {best}')

            winner = match.winning_heuristic()
            if winner is not None:
                print(f'🏆 Winner: {winner}')
                # FIXME: Save the final board position to a text file
                with open('log.txt', 'a') as f:
                    f.write(str(match.grid()) + '\n')
                f.close()

                completed = True
            else:
                # match.mechanics(match.players[match.turn % 2], best[0], best[1], best[2], True)
                print('Score', match.pieces, "\tKings", match.kings, '\n')

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    completed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y, = pygame.mouse.get_pos()

                    # FIXME: Debug Information
                    print("🖱 Mouse (x, y): " + str(mouse_x) + ", " + str(mouse_y))

                    match.click_evaluation(pygame.mouse.get_pos())

            # Grid Creation
            window.fill(GRAY)
            match.grid()
            pygame.display.flip()
            clock.tick(FPS)

            # EMOJI / TERMINAL STATUS KEY:
            # - ✅ Completed
            # - ⚠️ Warning
            # - ❌ Quit
            # - 🚀 Launch

    pygame.quit()
    print("❌ Quit Checkers [GUI]")


# def test_minimax():
#     match = Match()
#     minimax_depth = 8
#     alternate_player = 0
#     assess, best = minimax(match, minimax_depth, alternate_player)
#     print(f'⏳ Attempt Evaluation: {assess}')
#     print(f'🧠 Ideal Move: {best}')
#     assert best == (0, 0, 0)

# Pytest Example
# Source: https://docs.pytest.org/en/6.2.x/getting-started.html
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def solution():
    assert fibonacci(10) == 55


# Main program
if __name__ == '__main__':
    gui_display()

    # TODO: Save the finished board position to a text file.

    # Monte Carlo Tree Search
    # - Node traversal
    # - Result of the simulation
    # - Selection of the node to expand
    # - Randomly selecting a child node
    # - Backpropagation
    # - Selecting the best child node
