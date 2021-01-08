from abc import abstractmethod


class SurfaceInfo:
    """
    SurfaceInfo is a class to store information about the surface of a FESS
    """

    def __init__(self, function_name, args):
        self.function_name = function_name
        self.args = args

    @abstractmethod
    def paint(self, hierarchy, shapes, shape):
        raise NotImplementedError("This function has yet to be implemented")

    @abstractmethod
    def to_json(self):
        """
        Converts the SurfaceInfo to JSON for Storage
        :return:
        """
        raise NotImplementedError("This function has yet to be implemented")

    @staticmethod
    @abstractmethod
    def from_json(string):
        raise NotImplementedError("This function has yet to be implemented")
