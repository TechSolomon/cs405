import random

# Implement Monte Carlo Tree Search
from mcts.node import Node


def mcts(state, player, n_iterations=1000, n_simulations=100, verbose=False):
    """
    Monte Carlo Tree Search
    :param state: current state
    :param player: current player
    :param n_iterations: number of iterations
    :param n_simulations: number of simulations per iteration
    :param verbose: whether to print the tree
    :return: the best move
    """
    # Initialize root node
    root = Node(state, player)

    # Run MCTS
    # for i in range(n_iterations):
    #     # Select
    #     node = select(root)
    #
    #     # Expand
    #     node = expand(node)
    #
    #     # Simulate
    #     node = simulate(node, n_simulations)
    #
    #     # Backpropagate
    #     backpropagate(node)

    # Return the best move
    # return best_move(root)


# Select
def select(node):
    """
    Select
    :param node: current node
    :return: the selected node
    """
    # While the node is not a leaf
    while not node.is_leaf():
        # If the node is not fully expanded
        if not node.is_fully_expanded():
            # Return the unexpanded node
            return node

        # Else, select the best child
        # node = best_child(node)

    # Return the node
    return node


# Rollout step of the MCTS
def rollout(state, player):
    """
    Rollout step of the MCTS
    :param state: current state
    :param player: current player
    :return: the result of the rollout
    """
    # While the game is not over
    while not state.is_terminal():
        # Get the legal actions
        actions = state.legal_actions(player)

        # If there is no legal action
        if len(actions) == 0:
            # Return the current state
            return state

        # Else, get a random action
        action = random.choice(actions)

        # Apply the action
        state = state.apply_action(action)

    # Return the state
    return state


print(">> CS 405 - HW 3: Monte Carlo Tree Search")
