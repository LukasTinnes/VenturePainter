from src.Shapes.FESS import FESS
from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.AAB import AAB


class Rectangle(AAB, FESS):

    def get_fuzziness(self):
        # Todo implement
        pass

    def __init__(self, position, width, height, identifier=-1, surface_info=None):
        AAB.__init__(self, position, width, height, identifier)
        FESS.__init__(self, surface_info)
