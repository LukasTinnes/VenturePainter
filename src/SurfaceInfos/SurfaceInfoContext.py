from src.Texture import Texture
import json
from src.SurfaceInfos.SurfaceInfo import SurfaceInfo


class SurfaceInfoContext(SurfaceInfo):
    """
    SurfaceInfo is a class to store information about the surface of a FESS
    """

    def __init__(self, function_name, args):
        super().__init__(function_name, args)

    def paint(self, hierarchy, shapes, shape):
        if shape.context is None:
            shape.context = {}
        final_args = self.parse_args(shape)

        return getattr(Texture, self.function_name)((shape.shape.width, shape.shape.height), **final_args)

    def parse_args(self, shape):
        final_args = {}
        for key in self.args.keys():
            arg = self.args[key]
            final_args[key] = arg
            if type(arg) is str:
                if arg[0] == '$':
                    final_args[key] = shape.context[arg[1:]]
            elif type(arg) is list:
                final_args[key] = arg.copy()
                for i in range(len(arg)):
                    if type(arg[i]) is str:
                        if arg[i][0] == '$':
                            final_args[key][i] = shape.context[arg[i][1:]]
        print("Final args", final_args)
        return final_args

    def to_json(self):
        """
        Converts the SurfaceInfo to JSON for Storage
        :return:
        """
        return f'{{"kind":"Context", "name":\"{self.function_name}\", "args":{self.args}}}'

    def __str__(self):
        return f"SurfaceInfo - kind: Context, function_name: {self.function_name}, args: {self.args}"

    @staticmethod
    def from_json(args_dict):
        name = args_dict["name"]
        args = args_dict["args"]
        return SurfaceInfoContext(name, args)
