import math
from typing import Optional

import numpy as np
import pygame


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


def skew_matrix(x_skew: float, y_skew: float) -> np.ndarray:
    return np.array([
        [1, x_skew, 0],
        [y_skew, 1, 0],
        [0, 0, 1]
    ])


def affine_transform(point: tuple[float, float], matrix: np.ndarray) -> tuple[float, float]:
    point = np.array([*point, 1.0])
    transformed_point = matrix @ point

    return transformed_point[0], transformed_point[1]


def find_centroid(coordinates):
    x_list = [vertex[0] for vertex in coordinates]
    y_list = [vertex[1] for vertex in coordinates]
    len_coords = len(coordinates)
    x = sum(x_list) / len_coords
    y = sum(y_list) / len_coords
    return x, y


def draw_septagon(surface: pygame.Surface,
                  color: tuple[int, int, int],
                  center: tuple[float | int, float | int],
                  size: int | float,
                  *,
                  angle: Optional[int | float] = 0,
                  vertical_stretch: Optional[float] = 1.0,
                  x_skew: Optional[float] = 0.0,
                  y_skew: Optional[float] = 0.0):
    skew_mat = skew_matrix(x_skew, y_skew)  # Create skew matrix

    temp_coordinates = []

    for i in range(7):
        original_x = center[0] + size * math.cos(math.radians(i * (360 / 7) - 90))
        original_y = center[1] + size * math.sin(math.radians(i * (360 / 7) - 90))

        original_y = center[1] + (original_y - center[1]) * vertical_stretch

        skewed_x, skewed_y = affine_transform((original_x, original_y), skew_mat)

        rotated_point = rotate_point(center, (skewed_x, skewed_y), math.radians(angle))
        temp_coordinates.append(rotated_point)

    skewed_centroid = find_centroid(temp_coordinates)

    translation_x = center[0] - skewed_centroid[0]
    translation_y = center[1] - skewed_centroid[1]

    coordinates = [(x + translation_x, y + translation_y) for x, y in temp_coordinates]

    pygame.draw.polygon(surface, color, coordinates, 2)  # Draw septagon with transformed and
