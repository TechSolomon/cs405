# variables.py

import pygame

# BOARD & GRAPHICAL DISPLAY
ROWS, COLUMNS = 8, 8
WIDTH, HEIGHT = 600, 600
BOARD_SIZE = (WIDTH, HEIGHT)
MARKER_SIZE = int(WIDTH / ROWS / 2)
SEARCH_TIME = [1, 5, 10, 15, 30]  # (seconds)
RESOLUTION = pygame.display.set_mode(BOARD_SIZE)
FPS = 60  # Frames Per Second
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
