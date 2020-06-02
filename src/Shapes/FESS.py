from Engine.Shapes.FinitelyBounded.ShapeCollections.Std.Shape import Shape
from abc import abstractmethod


class FESS(Shape):
    """This class implements Fuzzy Elevated Surface Shapes"""

    @abstractmethod
    def get_fuzziness(self):
        pass

    @abstractmethod
    def get_surface_info(self):
        pass
