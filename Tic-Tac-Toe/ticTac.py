import numpy as np
import pygame

pygame.init()

# COLORS

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
GRAY = (180,180,180)

# CONSTANT

WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH//BOARD_COLS
CERCLE_RADIUIS = SQUARE_SIZE // 3
CERCLE_SIZE = 15
CROSS_SIZE = 25
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC - TAC- TOE')

screen.fill(BLACK)
board = np.zeros((BOARD_ROWS,BOARD_COLS))

def draw_line(color=WHITE):
    for i in  range(1,BOARD_ROWS):
        pygame.draw.line(screen,color,(0,SQUARE_SIZE*i),(WIDTH,SQUARE_SIZE*i),LINE_WIDTH)
        pygame.draw.line(screen,color,(SQUARE_SIZE*i,0),(SQUARE_SIZE*i,HEIGHT),LINE_WIDTH)


def draw_figures(color=WHITE):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen,color,(int(col*SQUARE_SIZE*SQUARE_SIZE //2),int(row*SQUARE_SIZE*SQUARE_SIZE // 2)),CERCLE_RADIUIS,CERCLE_SIZE)
            elif board[row][col] == 2_
            pygame.draw.line(screen,color,(col*SQUARE_SIZE+SQUARE_SIZE // 4,row*SQUARE_SIZE+SQUARE_SIZE // 4))
            pygame.draw.line(screen,color,(col*SQUARE_SIZE+SQUARE_SIZE // 4,row*SQUARE_SIZE+ 3 * SQUARE_SIZE // 4))



def mark_square(row,col,player):
    board[row][col] = player



def avalaible_square



running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    board = np.zeros((BOARD_ROWS, BOARD_COLS))


    pygame.display.flip()




pygame.quit()