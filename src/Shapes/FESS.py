from abc import abstractmethod
from src.SurfaceInfo import SurfaceInfo


class FESS:
    """This class implements Fuzzy Elevated Surface Shapes"""

    def __init__(self, surface_info):
        self.surface_info = surface_info

    @abstractmethod
    def get_fuzziness(self):
        pass

    def get_surface_info(self) -> SurfaceInfo:
        return self.surface_info
