import logging
import random
from typing import List

import cv2
import numpy as np
from pygame import Rect

from src.Node import Node
from src.Shape import Shape


def get_splices(viewing_window, shape):
    # x1 is either 0 (overlap left side), or shape left minus vw left
    x1_index = np.maximum(0, shape.left - viewing_window.left)
    # x2 is either vw.width (overlap right side), or x_1_index + shape.width
    x2_index = np.minimum(viewing_window.width, shape.width + x1_index)
    # y1 is either 0 (overlap top) or shape.top-vw.top
    y1_index = np.maximum(0, shape.top - viewing_window.top)
    # y2 is either vw.height (overlap bottom side) or y1+shape.height
    y2_index = np.minimum(viewing_window.height, y1_index + shape.height)
    return x1_index, x2_index, y1_index, y2_index
    # # Case 1 (Overlap top right corner
    # if shape.left < viewing_window.left and shape.top < viewing_window.top:
    #     pass
    # # Case 2 (Overlap top edge)
    # if shape.top < viewing_window.top and not (shape.right > viewing_window.right or shape.left < viewing_window.left):
    #     pass
    # # Case 3 (Overlap top right)
    # if shape.top < viewing_window.top and shape.right > viewing_window.right:
    #     pass
    # # Case 4 (Overlap left edge)
    # if shape.left < viewing_window.left and not (
    #         shape.bottom > viewing_window.bottom or shape.top < viewing_window.top):
    #     pass
    # # Case 5 (Overlap Right Edge)
    # if shape.right > viewing_window.right and not (
    #         shape.bottom > viewing_window.bottom or shape.top < viewing_window.top):
    #     pass
    # # Case 6 (Overlap bottom left)
    # if shape.left < viewing_window.left and shape.bottom > viewing_window.bottom:
    #     pass
    # # Case 7 (Overlap Bottom Edge)
    # if shape.bottom > viewing_window.bottom and not (
    #         shape.left < viewing_window.left or shape.right > viewing_window.right):
    #     pass
    # # Case 8 (Overlap bottom right)
    # if shape.bottom > viewing_window.bottom and shape.right > viewing_window.right:
    #     pass
    # # Case shape completely in viewing_window
    # else:
    #     # Move slices to image slices
    #     row_splices = [shape.left - viewing_window.left, shape.right - viewing_window.left]
    #     column_splices = [shape.top - viewing_window.top, shape.bottom - viewing_window.top]


def random_colors():
    colors = [(0, 0, 1), (0, 1, 0)]
    samples = random.sample(colors, 2)
    return samples


class Painter:
    """
    Paints a picture/thing based on the given hierarchy, which was build in Interpreter.py
    Surfaces are used to represent interactions between adjacent surfaces
    """

    def __init__(self):
        pass

    def paint(self, hierarchy: List[Node], shapes: List[Shape], viewing_window: Rect, action_dict):
        """
        Paints an image based on a relationship graph provided
        :param action_dict: dict of kind -> texture function each texture function gets (hierarchy, shapes and shape)
        :param hierarchy: interpreted shape hierarchy
        :param shapes: list of shapes read by the Loader
        :param viewing_window: viewing window of the hierarchy shapes
        :return: png
        """
        img = np.zeros((int(viewing_window.width), int(viewing_window.height), 3))
        # Fun mode
        # img = np.empty((viewing_window.height, viewing_window.width, 3))
        drawn_shapes = [shape for shape in shapes if
                        viewing_window.contains(shape.shape) or viewing_window.colliderect(shape.shape)]
        hs = list(zip(hierarchy, drawn_shapes))
        for i in range(len(hs)):
            node = hs[i][0]
            shape = hs[i][1]
            logging.info(f"Generating texture for shape {shape.id} with kind {shape.kind}")
            texture = action_dict[shape.kind](hierarchy, shapes, shape)
            # Get indices
            logging.info(f"Getting indices for shape {shape} and viewing window {viewing_window}")
            x1, x2, y1, y2 = get_splices(viewing_window, shape.shape)
            # Reshape the texture to fit (hopefully)
            logging.info(f"Indices are {x1}, {x2}, {y1}, {y2}")
            resize = np.resize(texture, (x2 - x1, y2 - y1, 3))
            img[x1:x2, y1:y2] = resize
        # for i in range(len(hs)):
        #     shape = hs[i][1]
        #     node = hs[i][0]
        #     anchor = camera.world_to_cam([shape.left, shape.up])
        #     draw.text((anchor[0], anchor[1]), f"{hash(shape)}", fill=(255, 255, 255))
        return cv2.flip(cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE), 1)
