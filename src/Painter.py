from PIL import Image, ImageDraw
from Engine.Camera import Camera

class Painter:
    """
    Paints a picture/thing based on the given hierarchy, which was build in Interpreter.py
    Surfaces are used to represent interactions between adjacent surfaces
    """

    def __init__(self):
        pass

    def paint(self, hierarchy, background, shapes, dimensions):
        """
        Paints an image based on a relationship graph provided
        :return:
        """
        cam = Camera()
        img = Image.new("RGB", dimensions)
        draw = ImageDraw.ImageDraw(img)
        hs = list(zip(hierarchy, shapes))
        for i in range(len(hs)):
            shape = hs[i][1]
            node = hs[i][0]
            draw.rectangle([(shape.left, dimensions[1]-shape.up), (shape.width, shape.height)], fill="#ffff33")
        return img

