import xml.etree.ElementTree as ET
import re
from src.Shapes.Rectangle import Rectangle
from src.SurfaceInfo import SurfaceInfo
import numpy as np
from Engine.Camera import Camera


class Loader:
    """
    The Loader class loads an SVG file and translates it into Shape objects of the Engine
    """

    def __init__(self, path):
        """
        Initialises the loader for a given folder
        :param path: Path to the svg image that is to be painted
        """
        self.path = path
        self.id_count = 0
        # Action dict, to map different shapes to their respective loading functions
        self.action_dict = {"rect": self._load_rect}

    def load(self, filename):
        """
        Loads every child node of the root of a specific svg images' xml tree representation
        :param filename: filename of the svg image (in the resource folder)
        """
        tree = ET.parse(self.path + filename)
        root = tree.getroot()
        attrib = root.attrib
        background = Rectangle(np.array([float(attrib["width"])/2, float(attrib["height"])/2]),
                               float(attrib["width"]), float(attrib["height"]), -1)

        cam = Camera(np.array([float(attrib["width"])/2, float(attrib["height"])/2]),
                     int(attrib["width"]), int(attrib["height"]), anchor=(True, False))

        shapes = []
        for child in root:
            shapes.append(self._load_object(child, cam))
        return background, shapes, cam

    def _load_object(self, child, cam):
        """
        Loads a specific tree element depending on its tag
        :param child: tree element
        :return: Fuzzy shape object representing the given tree element
        """
        # Filtering tag from svg namespace, because xml sux
        tag = re.sub("{.*}", "", child.tag)
        attrib = child.attrib
        return self.action_dict[tag](attrib, cam)

    def _load_rect(self, attrib, cam: Camera):
        """
        Loads a rectangle (gets called in load_object)
        :param attrib: rectangle attributes
        :return: The Fuzzy shape representing this rectangle
        """
        width = float(attrib["width"])
        height = float(attrib["height"])
        cam_position = np.array([float(attrib["x"]) + width/2, float(attrib["y"]) + height/2])
        position = cam.cam_to_world(cam_position)
        rect = Rectangle(position, width, height, self.id_count, SurfaceInfo(color=attrib["fill"]))
        self.id_count += 1
        return rect
