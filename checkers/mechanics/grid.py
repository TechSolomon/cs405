# grid.py

import pygame
from .variables import ROWS, COLUMNS, RED, BLACK, SQUARE_SIZE


def squares(display):
    display.fill(BLACK)
    for row in range(ROWS):
        for column in range(row % 2, ROWS, 2):
            pygame.draw.rect(display, RED, (row * SQUARE_SIZE,
                                            column * SQUARE_SIZE,
                                            SQUARE_SIZE, SQUARE_SIZE))


# Testing Additional Classes
class Grid:
    def __init__(self):
        self.grid = []

        # Board Starting Position
        self.RP_remaining = 12
        self.WP_remaining = 12
        self.RK_remaining = 0
        self.WK_remaining = 0

    def draw(self, display):
        squares(display)
        for row in range(ROWS):
            for column in range(COLUMNS):
                piece = self.grid[row][column]
                if piece != 0:
                    piece.draw(display)
