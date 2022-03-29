# search.py

import random
import copy
import time


class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.children = []
        self.visits = 0
        self.reward = 0
        self.untried_actions = state.get_actions()


def traverse(node):
    while node.parent is not None:
        yield node
        node = node.parent
    yield node


def expand(node, state):
    action = random.choice(node.untried_actions)
    state.apply_action(action)
    node.untried_actions.remove(action)
    new_node = Node(state, node, action)
    node.children.append(new_node)
    return action


def rollout(state):
    while state.get_actions():
        action = random.choice(state.get_actions())
        state.apply_action(action)
    return state.get_reward()


def backpropagation(node, reward):
    for n in traverse(node):
        n.visits += 1
        n.reward += reward


def best_child(node):
    best_score = -1
    optimal_generation = None
    # FIXME: New Best Child?
    for child in node.children:
        score = child.reward / child.visits
        if score > best_score:
            best_score = score
            optimal_generation = child
    return optimal_generation


# Implement the MCTS algorithm
# Source: https://en.wikipedia.org/wiki/Monte_Carlo_tree_search
class MCTS:
    def __init__(self, state, player, seconds):
        self.root = Node(state)
        self.time = seconds
        self.player = player

    # FIXME: Search
    # - one iteration of MCTS
    # - recursively called a leaf node is found
    # - action chosen = maximum upper confidence bound

    def search(self):
        start = time.time()
        while time.time() - start <= self.time:
            node = self.root
            state = copy.deepcopy(self.root.state)
            while node.untried_actions == [] and node.children != []:
                # node = self.select_child(node)
                state.apply_action(node.action)
            # action = expand(node, state)
            reward = state.get_reward()
            backpropagation(node, reward)
        return best_child(self.root)

    # def select_child(self, node):
    #     s = 0
    #     for child in node.children:
    #         s += child.visits
    #     best_score = -1
    #     optimal_generation = None
    #     for child in node.children:
    #         score = child.reward / child.visits + self.c * math.sqrt(2 * math.log(s) / child.visits)
    #         if score > best_score:
    #             best_score = score
    #             optimal_generation = child
    #     return optimal_generation
