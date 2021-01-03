import logging
import xml.etree.ElementTree as ET
from src.Shape import Shape

import planar


class Loader(object):
    """
    The Loader class loads an SVG file and translates it into Shape objects of the Engine
    """

    def __init__(self):
        """
        Initialises the loader for a given folder
        """
        self.id_count = 0

    def load(self, filename):
        """
        Loads every child node of the root of a specific svg images' xml tree representation
        :param filename: filename of the svg image (in the resource folder)
        """
        #TODO fileending descrimination
        return self._load_svg(filename)

    def _load_svg(self, filename):
        """
        Loads Objects from SVG file
        :param filename:
        :return:
        """
        tree = ET.parse(filename)
        root = tree.getroot()

        # Load information on background size
        root_attrib = root.attrib
        root_width = float(root_attrib["width"])
        root_height = float(root_attrib["height"])

        """Load shapes"""
        shapes = []

        # Create bounding boxes from children
        logging.info(f"Detected {len(root)} children. Loading")
        for child in root:
            # TODO other shapes
            # Extract parameters
            child_attrib = child.attrib
            child_x = float(child_attrib["x"])
            child_y = float(child_attrib["y"])
            child_width = float(child_attrib["width"])
            child_height = float(child_attrib["height"])
            child_color = int(child_attrib["fill"][1:], 16)

            # Build BBox
            maximum = planar.Vec2(child_x + child_width, child_y + child_height)
            minimum = planar.Vec2(child_x, child_y)
            box = planar.BoundingBox([minimum, maximum])

            # Build Shape

            shape = Shape(box, self.id_count, child_color)
            self.id_count += 1

            # Append to shappe list
            shapes.append(shape)
            logging.info(f"Loaded child {shape}")
        logging.info(f"loaded all children")
        return shapes
