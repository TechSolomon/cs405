# main.py
# Solomon Himelbloom
# 2022-01-18
#
# For CS 405 Spring 2022

"""
Basic checkers implementation.
[] Start with 8 x 8 --> 32 active spaces.
[] Bunch of if/then statements.
[] No bit mapping / packing?
[] For each x do y (loop).
[] 5 pieces (R, B, -, RK, BK).
"""

import math
import pygame
import random
from string import ascii_uppercase as key
import sys
import time

# TODO: Custom graphic art of Red & White King. 👑
from mechanics.variables import BOARD_SIZE, WIDTH, HEIGHT

# CONSTANTS
RP = "R"  # Red Pawn
BP = "B"  # Black Pawn
EM = "-"  # Empty Cell
RK = "RK"  # Red King
BK = "BK"  # Black King


class Match:
    def __init__(self, display):
        self.display = display


class Movement(object):
    def __init__(self, color, row, column, occupied=None):
        self.color = color
        self.row = row
        self.col = column
        self.occupied = occupied
        self.king = False
    # TODO:
    #  - Attributes for each piece & neighbor interactions.
    #  - Determine piece residing at given square.


# position = [
#     [EM, RP, EM, RP],
#     [EM, EM, EM, EM],
#     [BP, EM, BP, EM]
# ]


# position = [
#     [EM, RP, EM, RP],
#     [EM, EM, EM, EM],
#     [EM, EM, EM, EM],
#     [BP, EM, BP, EM]
# ]


position = [
    [EM, RP, EM, RP, EM, RP, EM, RP],
    [RP, EM, RP, EM, RP, EM, RP, EM],
    [EM, RP, EM, RP, EM, RP, EM, RP],
    [EM, EM, EM, EM, EM, EM, EM, EM],
    [EM, EM, EM, EM, EM, EM, EM, EM],
    [BP, EM, BP, EM, BP, EM, BP, EM],
    [EM, BP, EM, BP, EM, BP, EM, BP],
    [BP, EM, BP, EM, BP, EM, BP, EM]
]


def print_grid(board):
    for row in board:
        print(row)


def coordinates(board, number):
    number = int(number) - 1
    return number % len(board), number // len(board)


def jump(board, transition):
    (src_x, src_y), (dst_x, dst_y) \
        = (coordinates(board, x) for x in transition.split())
    x_diff = abs(src_x - dst_x)
    y_diff = abs(src_y - dst_y)

    # if sorted([x_diff, y_diff]) != [0, 2]:
    #     print('Invalid coordinates!')
    #     return

    mid_x = (src_x + dst_x) // 2
    mid_y = (src_y + dst_y) // 2

    if board[src_y][src_x] == EM:
        print('Source cell empty!')

    if board[dst_y][dst_x] != EM:
        print('Target cell occupied!')

    if board[mid_y][mid_x] == EM:
        print('Error: No piece to jump over!')

    if board[src_y][src_x] == board[mid_y][mid_x]:
        print('Error: Same color jump!')

    board[dst_y][dst_x] = board[src_y][src_x]
    board[mid_y][mid_x] = EM
    board[src_y][src_x] = EM


def ascii_display():
    """Default grid for a new game of checkers."""

    print("HW1 – Basic Checkers")
    print(">> Starting game...")

    # Grid Key
    heading = list(key[:BOARD_SIZE])
    index = iter(range(0, BOARD_SIZE))

    # Empty Initial Board
    board = [[EM for vertical in range(BOARD_SIZE)]
             for horizontal in range(BOARD_SIZE)]

    print("  " + " ".join(heading))
    for dimensions in board:
        print(next(index), end=" ")
        print(" ".join(dimensions))

    print()

    return position


def move_generation():
    """Generate all moves and jumps available to a player."""
    # print("Red & Black Table / Key")  # FIXME

    print(math.pi)
    print(random.randint(10, 100))
    print(time.time_ns())

    moves = []

    # for rows in range(BOARD_SIZE):
    #     for columns in range(BOARD_SIZE):
    #         print("START HERE!")  # FIXME


def human_playable():
    """Allow a human to play your move generator."""
    iteration = True
    while iteration:
        print_grid(position)
        move = input(">> Desired move (e.g. # [space] #): ")
        print('>> Executing move: {}'.format(move))
        jump(position, move)
        print_grid(position)
        print()


def gui_display():
    """Display the checkers board."""
    print("Hello, GUI display!")

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('🎲 CS 405 – Checkers')
    multimedia = pygame.image.load('assets/board.png')

    active = True

    while active:
        window.blit(multimedia, (0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()


# Main program
if __name__ == "__main__":
    gui_display()

    # ascii_display()
    # try:
    #     human_playable()
    # except KeyboardInterrupt:
    #     sys.exit(0)

    # move_generation()
