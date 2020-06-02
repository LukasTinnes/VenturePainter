from src.Shapes.FESS import FESS
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.AAB import AAB


class Rectangle(AAB, FESS):

    def __init__(self, position, width, height, identifier=-1, surface_info=None):
        AAB.__init__(self, position, width, height, identifier)
        self.surface_info = surface_info

    def get_surface_info(self):
        return self.surface_info
