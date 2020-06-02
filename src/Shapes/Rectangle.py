from src.Shapes.FESS import FESS
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.AAB import AAB


class Rectangle(AAB, FESS):

    def __init__(self, position, width, height, identifier=-1, surface_info=None):
        self.surface_info = surface_info
        AAB.__init__(self, position, width, height, identifier)
