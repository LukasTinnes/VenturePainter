from Engine import shape_factory
Simple = shape_factory.Simple
from abc import abstractmethod


class FESS(Simple):
    """This class implements Fuzzy Elevated Surface Shapes"""

    @abstractmethod
    def get_fuzziness(self):
        pass

    @abstractmethod
    def get_surface_info(self):
        pass
