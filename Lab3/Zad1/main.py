import time

import pygame

from source import config, utils


def main():
    pygame.init()
    win = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption("Lab3 - Oskar Stasiak")

    buttons = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8,
               pygame.K_9]
    pressed = {button: {'pressed': False, 'at': None} for button in buttons}

    septagon_surface = pygame.Surface((config.SURFACE_WIDTH, config.SURFACE_HEIGHT),
                                      pygame.SRCALPHA)

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

        septagon_center = (config.WINDOW_WIDTH // 2,
                           config.WINDOW_HEIGHT // 2)

        septagon = None
        if pressed[pygame.K_1]['pressed']:
            septagon = utils.create_septagon(septagon_center, config.SEPTAGON_SIZE)

        if pressed[pygame.K_2]['pressed']:
            septagon = utils.create_septagon(septagon_center, 1.75 * config.SEPTAGON_SIZE,
                                             angle=-90)

        if pressed[pygame.K_3]['pressed']:
            septagon = utils.create_septagon(septagon_center, config.SEPTAGON_SIZE,
                                             angle=180, vertical_stretch=2)

        if pressed[pygame.K_4]['pressed']:
            septagon = utils.create_septagon(septagon_center, 1.75 * config.SEPTAGON_SIZE,
                                             x_skew=0.5)

        if pressed[pygame.K_5]['pressed']:
            septagon = utils.create_septagon(septagon_center, config.SEPTAGON_SIZE,
                                             horizontal_stretch=2.0)
            top_y = min(septagon, key=lambda point: point[1])[1]
            top_difference = - top_y + 45  # TODO: Calculate this properly

            septagon = [(x, y + top_difference) for x, y in septagon]

        if pressed[pygame.K_6]['pressed']:
            septagon = utils.create_septagon(septagon_center, 1.75 * config.SEPTAGON_SIZE,
                                             x_skew=0.5, angle=90)

        if pressed[pygame.K_7]['pressed']:
            septagon = utils.create_septagon(septagon_center, config.SEPTAGON_SIZE,
                                             angle=180, vertical_stretch=2, horizontal_flip=True)

        if pressed[pygame.K_8]['pressed']:
            septagon_center = (config.WINDOW_WIDTH // 2, (config.WINDOW_HEIGHT // 2) + 100)
            septagon = utils.create_septagon(septagon_center, config.SEPTAGON_SIZE,
                                             angle=45, horizontal_stretch=2.0)

        if pressed[pygame.K_9]['pressed']:
            septagon = utils.create_septagon(septagon_center, 1.75 * config.SEPTAGON_SIZE,
                                             angle=180, x_skew=0.5)

            top_x = max(septagon, key=lambda point: point[0])[0]

            top_difference = 590 - top_x  # TODO: Calculate this properly
            septagon = [(x + top_difference, y) for x, y in septagon]

        if septagon:
            pygame.draw.polygon(win, config.COLOR_OF_USE, septagon, 2)

        pygame.display.update()


if __name__ == "__main__":
    main()
