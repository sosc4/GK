import time

import pygame

from source import config, utils

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Lab3 - Oskar Stasiak")

buttons = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
pressed = {button: {'pressed': False, 'at': None} for button in buttons}

septagon_surface = pygame.Surface((400, 400), pygame.SRCALPHA)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill("white")
    pygame.draw.rect(win, config.YELLOW, (10, 45, 580, 545))

    keys = pygame.key.get_pressed()
    for button in buttons:
        if not keys[button]:
            continue

        at = pressed[button]['at']
        if at is None or time.time() - at > 0.5:
            pressed[button]['at'] = time.time()
            pressed[button]['pressed'] = not pressed[button]['pressed']

            for other_button in buttons:
                if other_button != button:
                    pressed[other_button]['pressed'] = False

    septagon_center = (300, 300)
    septagon_size = 100
    if pressed[pygame.K_1]['pressed']:
        utils.draw_septagon(win, config.COLOR_OF_USE, septagon_center, septagon_size)

    if pressed[pygame.K_2]['pressed']:
        utils.draw_septagon(win, config.COLOR_OF_USE, septagon_center, 2 * septagon_size,
                            angle=-90)

    if pressed[pygame.K_3]['pressed']:
        utils.draw_septagon(win, config.COLOR_OF_USE, septagon_center, septagon_size,
                            angle=180, vertical_stretch=1.5)

    if pressed[pygame.K_4]['pressed']:
        utils.draw_septagon(win, config.COLOR_OF_USE, septagon_center, 2 * septagon_size,
                            x_skew=0.5)

    pygame.display.update()
