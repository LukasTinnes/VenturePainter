from src.Shapes.FESS import FESS
from src import Shapes
AAB = Shapes.shape_factory.AAB


class Rectangle(AAB, FESS):

    def __init__(self, position, width, height, identifier=-1, surface_info=None):
        self.surface_info = surface_info
        AAB.__init__(self, position, width, height, identifier)
