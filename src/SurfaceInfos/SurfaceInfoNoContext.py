from src.Texture import Texture
import json
from src.SurfaceInfos.SurfaceInfo import SurfaceInfo


class SurfaceInfoNoContext(SurfaceInfo):
    """
    SurfaceInfo is a class to store information about the surface of a FESS
    """

    def __init__(self, function_name, args):
        super().__init__(function_name, args)

    def paint(self, hierarchy, shapes, shape):
        getattr(Texture, self.function_name)(*self.args)

    def to_json(self):
        """
        Converts the SurfaceInfo to JSON for Storage
        :return:
        """
        return f'{{"kind":"NoContext", "name":\"{self.function_name}\", "args":{self.args}}}'

    def __str__(self):
        return f"SurfaceInfo - kind: NoContext, function_name: {self.function_name}, args: {self.args}"

    @staticmethod
    def from_json(args_dict):
        name = args_dict["name"]
        args = args_dict["args"]
        return SurfaceInfoNoContext(name, args)
