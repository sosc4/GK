import math
import time
from typing import Optional

import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Lab3 - Oskar Stasiak")

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
LIGHT_BLUE = (0, 255, 255)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

COLOR_OF_USE = RED


def rotate_point(center: tuple[float | int, float | int],
                 point: tuple[float | int, float | int],
                 angle: float | int) -> tuple[float | int, float | int]:
    """
    Rotate a point counterclockwise by a given angle around a given origin.
    The angle should be given in radians.
    """
    ox, oy = center
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


def draw_septagon(surface: pygame.Surface,
                  color: tuple[int, int, int],
                  center: tuple[float | int, float | int],
                  size: int | float,
                  *,
                  angle: Optional[int | float] = 0,
                  vertical_stretch: Optional[float] = 1.0):
    """
    Draw a septagon on a given surface, with an option to rotate and vertically stretch.
    """
    coordinates = []
    for i in range(7):
        original_x = center[0] + size * math.cos(math.radians(i * (360 / 7) - 90))
        original_y = center[1] + size * math.sin(math.radians(i * (360 / 7) - 90))

        original_y = center[1] + (original_y - center[1]) * vertical_stretch

        rotated_point = rotate_point(center, (original_x, original_y), math.radians(angle))
        coordinates.append(rotated_point)

    pygame.draw.polygon(surface, color, coordinates, 2)


buttons = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
pressed = {button: {'pressed': False, 'at': None} for button in buttons}

font = pygame.font.SysFont('bitstreamverasans', 30)
septagon_surface = pygame.Surface((400, 400), pygame.SRCALPHA)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill("white")
    pygame.draw.rect(win, YELLOW, (10, 45, 580, 545))

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
        draw_septagon(win, COLOR_OF_USE, septagon_center, septagon_size)

    if pressed[pygame.K_2]['pressed']:
        draw_septagon(win, COLOR_OF_USE, septagon_center, septagon_size,
                      angle=-90)

    if pressed[pygame.K_3]['pressed']:
        draw_septagon(win, COLOR_OF_USE, septagon_center, septagon_size,
                      angle=180, vertical_stretch=1.5)

    pygame.display.update()
