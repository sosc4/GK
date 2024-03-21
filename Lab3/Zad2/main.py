import pygame

pygame.init()

BLUE = (0, 0, 255)

size = [400, 400]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Lab 3 - Oskar Stasiak")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
