from PIL import Image

class Painter:
    """
    Paints a picture/thing based on the given hierarchy, which was build in Interpreter.py
    Surfaces are used to represent interactions between adjacent surfaces
    """

    def __init__(self):
        pass

    def paint(self, hierarchy, dimensions):
        """
        Paints an image based on a relationship graph provided
        :return:
        """
        img = Image.new("RGB", dimensions)
        #TODO MAGIC
        return img

