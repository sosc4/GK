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

    :param center: The center of rotation.
    :param point: The point to rotate.
    :param angle: The angle of rotation in radians.
    :return: The rotated point.
    """
    ox, oy = center
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


def skew_matrix(x_skew: float, y_skew: float) -> np.ndarray:
    """
    Create a skew matrix.

    :param x_skew: The skew factor for the x-axis.
    :param y_skew: The skew factor for the y-axis.
    :return: The skew matrix.
    """
    return np.array([
        [1, x_skew, 0],
        [y_skew, 1, 0],
        [0, 0, 1]
    ])


def affine_transform(point: tuple[float, float], matrix: np.ndarray) -> tuple[float, float]:
    """
    Apply an affine transformation to a point.

    :param point: The point to transform.
    :param matrix: The transformation matrix.
    :return: The transformed point.
    """
    point = np.array([*point, 1.0])
    transformed_point = matrix @ point

    return transformed_point[0], transformed_point[1]


def find_centroid(coordinates: list[tuple[float | int, float | int]]) -> tuple[float | int, float | int]:
    """
    Find the centroid of a polygon.

    :param coordinates: The coordinates of the polygon.
    :return: The centroid of the polygon.
    """
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
                  y_skew: Optional[float] = 0.0) -> None:
    """
    Draw a septagon on a surface.

    :param surface: The surface to draw on.
    :param color: The color of the septagon.
    :param center: The center of the septagon.
    :param size: The size of the septagon.
    :param angle: The rotation of the septagon.
    :param vertical_stretch: The vertical stretch of the septagon.
    :param x_skew: The skew factor for the x-axis.
    :param y_skew: The skew factor for the y-axis.
    :return: None
    """
    skew_mat = skew_matrix(x_skew, y_skew)
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

    pygame.draw.polygon(surface, color, coordinates, 2)
