class Shape:

    def __init__(self, shape, id, kind=None, context=None):
        self.shape = shape
        self.id = id
        self.kind = kind
        self.context = context

    def __str__(self):
        return f"id:{self.id} kind:{self.kind} Shape:{str(self.shape)}"

