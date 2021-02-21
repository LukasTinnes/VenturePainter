from .Theme import Theme
from src.Graph import Graph


class TransformationTheme(Theme):

    def __init__(self):
        super().__init__()
        self.size_max = 0
        self.size_min = 0

        self.width_min = 0
        self.width_max = 0

        self.height_min = 0
        self.height_max = 0

        self.x_min = 0
        self.x_max = 0

        self.y_min = 0
        self.y_max = 0

    def prepare(self, graph, shapes):
        self.prepare_size_ratio(shapes)
        self.prepare_width_ratio(shapes)
        self.prepare_height_ratio(shapes)
        self.prepare_x_ratio(shapes)
        self.prepare_y_ratio(shapes)

    def prepare_size_ratio(self, shapes):
        node_sizes = []
        for shape in shapes:
            size = shape.shape.width * shape.shape.height
            node_sizes.append((shape.id, size))
        node_sizes = sorted(node_sizes, key=lambda tup: tup[1])
        self.size_min = node_sizes[-1][1]
        self.size_max = node_sizes[0][1]

    def prepare_width_ratio(self, shapes):
        node_sizes = []
        for shape in shapes:
            node_sizes.append((shape.id, shape.shape.width))
        node_sizes = sorted(node_sizes, key=lambda tup: tup[1])
        self.width_min = node_sizes[-1][1]
        self.width_max = node_sizes[0][1]

    def prepare_height_ratio(self, shapes):
        node_sizes = []
        for shape in shapes:
            node_sizes.append((shape.id, shape.shape.height))
        node_sizes = sorted(node_sizes, key=lambda tup: tup[1])
        self.height_min = node_sizes[-1][1]
        self.height_max = node_sizes[0][1]

    def prepare_x_ratio(self, shapes):
        node_sizes = []
        for shape in shapes:
            node_sizes.append((shape.id, shape.shape.x))
        node_sizes = sorted(node_sizes, key=lambda tup: tup[1])
        self.x_min = node_sizes[-1][1]
        self.x_max = node_sizes[0][1]

    def prepare_y_ratio(self, shapes):
        node_sizes = []
        for shape in shapes:
            node_sizes.append((shape.id, shape.shape.y))
        node_sizes = sorted(node_sizes, key=lambda tup: tup[1])
        self.y_min = node_sizes[-1][1]
        self.y_max = node_sizes[0][1]

    def determine_kind(self, graph: Graph, shapes, shape):
        size_ratio = (shape.shape.width * shape.shape.height - self.size_min) / (self.size_max - self.size_min)
        width_ratio = (shape.shape.width * shape.shape.height - self.width_min) / (self.width_max - self.width_min)
        height_ratio = (shape.shape.width * shape.shape.height - self.height_min) / (self.height_max - self.height_min)
        x_ratio = (shape.shape.width * shape.shape.height - self.x_min) / (self.x_max - self.x_min)
        y_ratio = (shape.shape.width * shape.shape.height - self.y_min) / (self.y_max - self.y_min)

        shape.context = {'size_ratio': size_ratio,'width_ratio': width_ratio,
                         'height_ratio': height_ratio,
                         'x_ratio': x_ratio,
                         'y_ratio': y_ratio,
                         'squareness': self.get_squareness(shape)}
        return "transformation"

    def get_squareness(self, shape):
        squareness = min(shape.shape.width, shape.shape.height) / max(shape.shape.width, shape.shape.height)
        return squareness
