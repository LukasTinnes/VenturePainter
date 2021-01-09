from .Theme import Theme


class UniformTheme(Theme):

    def __init__(self):
        super().__init__()

    def determine_kind(self, graph, shapes, shape):
        return "uniform"
