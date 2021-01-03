import random
from typing import List

from PIL import Image, ImageDraw
from pygame import Rect

from src.Node import Node


def get_draw_coords(shape):
    # Todo png image coordinates from shape coordinates
    pass


class Painter:
    """
    Paints a picture/thing based on the given hierarchy, which was build in Interpreter.py
    Surfaces are used to represent interactions between adjacent surfaces
    """

    def __init__(self):
        pass

    def image_scale(self, window: Rect, shapes: List[Rect], scaling_factor):
        """
        Scales the viewing window and all other shapes, to obtain image bounds sth sth todo
        :param window:
        :param shapes:
        :param scaling_factor:
        :return:
        """
        window = window.fit(scaling_factor * window.width, scaling_factor * window.height)
        for shape in shapes:
            shape = shape.fit(scaling_factor * shape.width, scaling_factor * shape.height)
        return Image.new("RGB", (int(window.width), int(window.height)))

    def paint(self, hierarchy: List[Node], shapes: List[Rect], viewing_window: Rect):
        """
        Paints an image based on a relationship graph provided
        :param hierarchy: interpreted shape hierarchy
        :param shapes: list of shapes read by the Loader
        :param viewing_window: viewing window of the hierarchy shapes
        :return: png
        """
        img = self.image_scale(viewing_window, shapes, 2)

        draw = ImageDraw.ImageDraw(img)
        hs = list(zip(hierarchy, shapes))
        for i in range(len(hs)):
            node = hs[i][0]
            shape = hs[i][1]
            anchor = get_draw_coords(shape)
            draw.rectangle([(anchor[0], anchor[1]), (anchor[0] + shape.width, anchor[1] + shape.height)],
                           fill=(random.randint(0, 125), random.randint(0, 125), random.randint(0, 125)))
        # for i in range(len(hs)):
        #     shape = hs[i][1]
        #     node = hs[i][0]
        #     anchor = camera.world_to_cam([shape.left, shape.up])
        #     draw.text((anchor[0], anchor[1]), f"{hash(shape)}", fill=(255, 255, 255))
        return img
