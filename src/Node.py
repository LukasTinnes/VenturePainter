class Node:
    """
    A node in a graph
    """

    def __init__(self, identifier):
        """
        :param identifier: Identifier is the object id given to a Object in Loader.py
        """
        self.identifier = identifier
        self.pointer = []

    def point_to(self, identifier):
        self.pointer.append(identifier)

    def search_for(self, identifier):
        return self.__search_for(identifier, [])

    def __search_for(self, identifier, exclude):
        if self.identifier == identifier:
            return self
        else:
            for node in self.pointer:
                if not hash(node) in exclude:
                    exclude.append(hash(node))
                    ret = node.__search_for(identifier, exclude)
                    if ret is not None:
                        return ret

    def __hash__(self):
        return self.identifier
