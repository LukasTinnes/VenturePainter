class Shape:

    def __init__(self, shape, id, kind=None):
        self.shape = shape
        self.id = id
        self.kind = kind

    def __str__(self):
        return f"id:{self.id} kind:{self.kind} Shape:{str(self.shape)}"

