from .Theme import Theme
from src.Graph import Graph


class SizeRatioTheme(Theme):

    def __init__(self):
        super().__init__()
        self.node_sizes = []
        self.max = 0
        self.min = 0

    def prepare(self, graph, shapes):
        node_sizes = []
        for shape in shapes:
            size = shape.shape.width * shape.shape.height
            node_sizes.append((shape.id, size))
        self.node_sizes = sorted(node_sizes, key=lambda tup: tup[1])
        print(self.node_sizes)
        self.min = self.node_sizes[-1][1]
        self.max = self.node_sizes[0][1]

    def determine_kind(self, graph: Graph, shapes, shape):
        ratio = (shape.shape.width * shape.shape.height - self.min) / (self.max - self.min)
        shape.context = {'size_ratio': ratio}
        return "size_ratio"
