from typing import List
import numpy as np
from typing import List

import numpy as np
from PIL import ImageDraw
from pygame import Rect

from src.Node import Node
from src.Texture import Texture


def get_draw_coords(shape):
    # Todo png image coordinates from shape coordinates
    pass


def get_splices(viewing_window, shape):
    # Case 1 (Overlap top right corner
    if shape.left < viewing_window.left and shape.top < viewing_window.top:
        pass
    # Case 2 (Overlap top edge)
    if shape.top < viewing_window.top and not (shape.right > viewing_window.right or shape.left < viewing_window.left):
        pass
    # Case 3 (Overlap top right)
    if shape.top < viewing_window.top and shape.right > viewing_window.right:
        pass
    # Case 4 (Overlap left edge)
    if shape.left < viewing_window.left and not (
            shape.bottom > viewing_window.bottom or shape.top < viewing_window.top):
        pass
    # Case 5 (Overlap Right Edge)
    if shape.right > viewing_window.right and not (
            shape.bottom > viewing_window.bottom or shape.top < viewing_window.top):
        pass
    # Case 6 (Overlap bottom left)
    if shape.left < viewing_window.left and shape.bottom > viewing_window.bottom:
        pass
    # Case 7 (Overlap Bottom Edge)
    if shape.bottom > viewing_window.bottom and not (
            shape.left < viewing_window.left or shape.right > viewing_window.right):
        pass
    # Case 8 (Overlap bottom right)
    if shape.bottom > viewing_window.bottom and shape.right > viewing_window.right:
        pass
    # Case shape completely in viewing_window
    else:
        # Move slices to image slices
        row_splices = [shape.left - viewing_window.left, shape.right - viewing_window.left]
        column_splices = [shape.top - viewing_window.top, shape.bottom - viewing_window.top]
    return (row_splices, column_splices)


class Painter:
    """
    Paints a picture/thing based on the given hierarchy, which was build in Interpreter.py
    Surfaces are used to represent interactions between adjacent surfaces
    """

    def __init__(self):
        pass

    def paint(self, hierarchy: List[Node], shapes: List[Rect], viewing_window: Rect):
        """
        Paints an image based on a relationship graph provided
        :param hierarchy: interpreted shape hierarchy
        :param shapes: list of shapes read by the Loader
        :param viewing_window: viewing window of the hierarchy shapes
        :return: png
        """
        img = np.zeroes((int(viewing_window.width), int(viewing_window.height), 3))
        # Fun mode
        # img = np.empty((viewing_window.height, viewing_window.width, 3))
        drawn_shapes = [shape for shape in shapes if
                        viewing_window.contains(shape) or viewing_window.colliderect(shape)]
        draw = ImageDraw.ImageDraw(img)
        hs = list(zip(hierarchy, drawn_shapes))
        for i in range(len(hs)):
            node = hs[i][0]
            shape = hs[i][1]
            texture = Texture.condiments([shape.width, shape.height],
                                         [(255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 0), (0, 0, 255)])
            splices = get_splices(viewing_window, shape)
            img[splices] = texture
        # for i in range(len(hs)):
        #     shape = hs[i][1]
        #     node = hs[i][0]
        #     anchor = camera.world_to_cam([shape.left, shape.up])
        #     draw.text((anchor[0], anchor[1]), f"{hash(shape)}", fill=(255, 255, 255))
        return img
