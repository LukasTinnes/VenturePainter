from PIL import Image, ImageDraw
from Engine.Camera import Camera
from src.Shapes.Rectangle import Rectangle
import random


class Painter:
    """
    Paints a picture/thing based on the given hierarchy, which was build in Interpreter.py
    Surfaces are used to represent interactions between adjacent surfaces
    """

    def __init__(self):
        pass

    def paint(self, hierarchy, background: Rectangle, shapes: list, camera: Camera):
        """
        Paints an image based on a relationship graph provided
        :return:
        """
        img = Image.new("RGB", (int(background.width), int(background.height)))
        draw = ImageDraw.ImageDraw(img)
        hs = list(zip(hierarchy, shapes))
        for i in range(len(hs)):
            shape = hs[i][1]
            node = hs[i][0]
            anchor = camera.world_to_cam([shape.left, shape.up])
            draw.rectangle([(anchor[0], anchor[1]), (anchor[0] + shape.width, anchor[1] + shape.height)], fill=(random.randint(0,125),random.randint(0,125),random.randint(0,125)))
        for i in range(len(hs)):
            shape = hs[i][1]
            node = hs[i][0]
            anchor = camera.world_to_cam([shape.left, shape.up])
            draw.text((anchor[0], anchor[1]), f"{hash(shape)}", fill=(255, 255, 255))
        return img

