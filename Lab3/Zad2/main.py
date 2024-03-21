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

    # rectangle
    pygame.draw.rect(screen, BLUE, [100, 150, 200, 100], 0)

    # triangles
    pygame.draw.polygon(screen, BLUE, [[200, 150], [150, 50], [250, 50]], 0)
    pygame.draw.polygon(screen, BLUE, [[200, 250], [150, 350], [250, 350]], 0)

    pygame.display.flip()
