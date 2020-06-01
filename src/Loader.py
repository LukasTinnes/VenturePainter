import xml.etree.ElementTree as ET
import re
from src.Shapes.Rectangle import Rectangle
import numpy as np


class Loader:
    """
    The Loader class loads an SVG file and translates it into Shape objects of the Engine
    """

    def __init__(self, path):
        self.path = path
        self.id_count = 0

        self.action_dict = {"rect": self._load_rect}

    def load(self, filename):
        tree = ET.parse(self.path + filename)
        root = tree.getroot()
        shapes = []
        for child in root:
            shapes.append(self._load_object(child))
        return shapes

    def _load_object(self, child):
        tag = re.sub(r"{http://www\.w3\.org/2000/svg}", "", child.tag)  # TODO this is not future proof!
        attrib = child.attrib
        return self.action_dict[tag](attrib)

    def _load_rect(self, attrib):
        width = float(attrib["width"])
        height = float(attrib["height"])
        position = np.array([float(attrib["x"]) + width/2, float(attrib["y"]) + height/2])
        rect = Rectangle(position, width, height, self.id_count, {"color": attrib["fill"]})
        self.id_count += 1
        return rect
