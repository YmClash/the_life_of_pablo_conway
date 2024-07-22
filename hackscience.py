import pygame
import random
import time

pygame.init()

BLACK = [0, 0, 0]
WHITE = [15, 256, 256]
COLOR_RAM = [random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)]
COLOR_RAM_2 = [random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)]

COLOR_RAM_3 = [random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)]

Haut = 250
Larg = 250
FPS = 60

screen = pygame.display.set_mode((Haut, Larg))
clock = pygame.time.Clock()

carre = pygame.Rect(100, 150, 20, 20)

cercle = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

running = True

while running :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

    if event.type == pygame.KEYDOWN :
        if event.key == pygame.K_DOWN :
            carre.y += 10
        if event.key == pygame.K_UP :
            carre.y -= 10
        if event.key == pygame.K_LEFT :
            carre.x -= 10
        if event.key == pygame.K_RIGHT :
            carre.x += 10

    screen.fill(COLOR_RAM)
    pygame.draw.circle(screen, COLOR_RAM_2, cercle, 40)
    pygame.draw.rect(screen, COLOR_RAM_3, carre)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()

"""
numb = 1.01
halo = "hallo"
co = 5
ic(type(numb), type(halo), type(co))
"""
